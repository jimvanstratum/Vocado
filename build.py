#!/usr/bin/env python3
"""
Build script — Vocado
====================================
Genereert één zelfstandig HTML-bestand met alle data en code ingebakken.
Geen server nodig. Deelbaar via AirDrop, WhatsApp, iMessage, e-mail.

Gebruik:
    python3 build.py

Uitvoer:
    vocado.html  (~100 KB, werkt offline)
"""

import json
import re
import os
import struct
import sys
import zlib
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
WWW  = os.path.join(BASE, 'www')
OUT  = os.path.join(BASE, 'vocado.html')


# ── Helpers ────────────────────────────────────────────────────────────────────

def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


# ── 0. Iconen controleren ──────────────────────────────────────────────────────
# De PNG-iconen (icon-192.png, icon-512.png) zijn vooraf gegenereerd via de
# SVG-canvas pipeline en staan al in www/. Dit script overschrijft ze NIET.

print('🖼️   Iconen controleren...')
for name in ['icon-192.png', 'icon-512.png']:
    path = os.path.join(WWW, name)
    if os.path.exists(path):
        size_bytes = os.path.getsize(path)
        print(f'    ✓ {name} aanwezig ({size_bytes // 1024} KB)')
    else:
        print(f'    ⚠️  {name} ontbreekt — genereer via www/index.html canvas export')


# ── 1. Data inladen ────────────────────────────────────────────────────────────

print('📂  Data laden...')
vocab      = load_json(os.path.join(WWW, 'data', 'vocabulary.json'))
curriculum = load_json(os.path.join(WWW, 'data', 'curriculum.json'))

vocab_js      = json.dumps(vocab,      ensure_ascii=False, separators=(',', ':'))
curriculum_js = json.dumps(curriculum, ensure_ascii=False, separators=(',', ':'))

print(f'    → {len(vocab)} woorden, {len(curriculum)} lessen')


# ── 2. JS modules bundelen ─────────────────────────────────────────────────────

print('📦  JavaScript bundelen...')

# Volgorde is belangrijk: afhankelijkheden eerst
MODULE_ORDER = ['srs.js', 'progress.js', 'settings.js', 'audio.js', 'exercises.js', 'app.js']
parts = []

for fname in MODULE_ORDER:
    path = os.path.join(WWW, 'js', fname)
    if not os.path.exists(path):
        print(f'⚠️   {fname} niet gevonden, overgeslagen')
        continue

    code = read(path)

    # Verwijder import-regels (import ... from '...')
    code = re.sub(r'^import\s[^\n]*\n?', '', code, flags=re.MULTILINE)

    # Verwijder 'export' voor functie/const/class declaraties
    code = re.sub(
        r'\bexport\s+((?:async\s+)?(?:function|const|let|var|class)\b)',
        r'\1',
        code
    )

    # Verwijder losse export { ... } blokken
    code = re.sub(r'^export\s*\{[^}]*\}\s*;?\s*\n?', '', code, flags=re.MULTILINE)

    parts.append(f'\n// ════════════ {fname} ════════════\n{code.strip()}')
    print(f'    ✓ {fname}')

bundle = '\n'.join(parts)


# ── 3. loadData() vervangen door inline data ───────────────────────────────────

print('💉  Data inlinen...')

inline_load = (
    'async function loadData() {\n'
    f'  VOCAB = {vocab_js};\n'
    f'  CURRICULUM = {curriculum_js};\n'
    '}'
)

# Vervang de hele loadData functie (geen geneste accolades in origineel)
bundle, n = re.subn(
    r'async function loadData\(\)\s*\{[^}]*\}',
    lambda _: inline_load,
    bundle
)

if n == 0:
    print('⚠️   loadData() niet gevonden — controleer app.js')
else:
    print(f'    → loadData() vervangen door {(len(vocab_js)+len(curriculum_js))//1024} KB inline data')


# ── 4. HTML laden en aanpassen ─────────────────────────────────────────────────

print('🏗️   HTML samenstellen...')

html = read(os.path.join(WWW, 'index.html'))

# Manifest-link verwijderen (vereist HTTP/HTTPS server, niet nodig voor standalone)
html = re.sub(r'\s*<link rel="manifest"[^>]*>', '', html)

# Bouw de nieuwe inline script-tag
# Voeg laadscherm-verberger toe (service worker wordt overgeslagen)
new_script = (
    '<script type="module">\n'
    + bundle
    + '\n\n'
    + '// Laadscherm verbergen na initialisatie\n'
    + "window.addEventListener('load', () => {\n"
    + "  setTimeout(() => document.getElementById('loading').classList.add('hidden'), 600);\n"
    + '});\n'
    + '</script>'
)

# Vervang de originele module script-tag
# Gebruik lambda om te voorkomen dat \u / \n in de JS als regex-escape worden behandeld
html, replaced = re.subn(
    r'<script type="module">.*?</script>',
    lambda _: new_script,
    html,
    flags=re.DOTALL
)

if replaced == 0:
    print('⚠️   Script-tag niet gevonden in index.html')
    sys.exit(1)


# ── 5. Meta-info toevoegen ─────────────────────────────────────────────────────

build_date = datetime.now().strftime('%Y-%m-%d %H:%M')
meta_comment = f'<!-- Vocado — standalone build {build_date} -->\n'
html = meta_comment + html


# ── 5b. Service worker cache-versie bumpen ─────────────────────────────────────
# De browser vergelijkt sw.js byte-voor-byte. Als CACHE_NAME nooit verandert,
# detecteert de browser geen nieuwe versie en blijft de oude cache actief.
# Door de datum in CACHE_NAME op te nemen verandert sw.js bij elke dagelijkse
# build, waardoor de PWA op het startscherm automatisch updatet na een git push.

sw_path = os.path.join(WWW, 'sw.js')
sw_old  = read(sw_path)
cache_version = datetime.now().strftime('%Y%m%d-%H%M')
new_cache_name = f'vocado-{cache_version}'
sw_new, sw_n = re.subn(r"const CACHE_NAME = '[^']*'",
                        f"const CACHE_NAME = '{new_cache_name}'",
                        sw_old)
if sw_n and sw_new != sw_old:
    with open(sw_path, 'w', encoding='utf-8') as f:
        f.write(sw_new)
    print(f'🔄  Service worker: CACHE_NAME → {new_cache_name}')


# ── 6. Uitvoerbestand schrijven ────────────────────────────────────────────────

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(OUT) / 1024

print()
print(f'✅  Klaar! → vocado.html')
print(f'📏  Bestandsgrootte: {size_kb:.0f} KB')
print()
print('📤  Distributiemethoden:')
print('    • AirDrop     → stuur naar iPhone, open in Safari')
print('    • iMessage    → stuur als bijlage, tik om te openen')
print('    • WhatsApp    → stuur als bestand (<16 MB)')
print('    • E-mail      → bijlage, download & open in Safari')
print('    • iCloud Drive → sla op, open altijd & overal')
print()
print('💡  Op iPhone: open in Safari → werkt direct als app in browser')
