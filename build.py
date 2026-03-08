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


# ── 0. Iconen genereren (avocado + V) via Pillow met 4× supersampling ──────────

def _draw_avocado_icon(size):
    """
    Tekent het Vocado avocado-icoon — flat cartoon stijl.
    Gebruikt 4× supersampling voor vloeiende randen (anti-aliasing).
    Kleuren & vormen gebaseerd op het officiële Vocado-icoon.
    """
    from PIL import Image, ImageDraw

    SUPER = 4                  # supersampling factor
    SS    = size * SUPER       # tekeningresolutie (b.v. 2048 voor 512-icoon)
    s     = SS / 512           # schaalfactor (referentie: 512 px coördinatenstelsel)

    img = Image.new('RGBA', (SS, SS), (0, 0, 0, 0))
    d   = ImageDraw.Draw(img)

    # ── Hulpfuncties ──────────────────────────────────────────────────────────

    def p(x, y):
        """Coördinaat in 512-ruimte → schermcoördinaat."""
        return (x * s, y * s)

    def cubic_bezier(p0, p1, p2, p3, n=100):
        """Bereken n+1 punten langs een kubische bezier-curve (512-ruimte → scherm)."""
        pts = []
        for i in range(n + 1):
            t  = i / n
            mt = 1 - t
            x = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
            y = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
            pts.append((x * s, y * s))
        return pts

    def avocado_poly(top_y, right_x, wide_y, bot_y, n=100):
        """
        Genereert polygoonpunten voor de avocado-peervorm.
        Symmetrisch rond x=256 in 512-coördinatenruimte.
        Kubische bezier, G1-continue joins aan top en bodem.
        """
        cx = 256
        # Rechts boven (top → breedste punt)
        r1 = cubic_bezier(
            (cx, top_y),
            (cx + (right_x - cx) * 0.82, top_y),   # tangent horizontaal aan top
            (right_x, (top_y + wide_y) * 0.56),
            (right_x, wide_y), n=n)
        # Rechts onder (breedste → bodem)
        r2 = cubic_bezier(
            (right_x, wide_y),
            (right_x, wide_y + (bot_y - wide_y) * 0.74),
            (cx + (right_x - cx) * 0.49, bot_y - 4),
            (cx, bot_y), n=n)
        # Links (gespiegeld)
        left_bot = [(2 * cx * s - x, y) for x, y in reversed(r2[:-1])]
        left_top = [(2 * cx * s - x, y) for x, y in reversed(r1)]
        return r1 + r2[1:] + left_bot + left_top[1:]

    # ── Witte iOS-stijl achtergrond ───────────────────────────────────────────
    r_bg = int(113 * s)
    d.rounded_rectangle([0, 0, SS - 1, SS - 1],
                        radius=r_bg, fill=(255, 255, 255, 255))

    # ── Avocado schil (donker bosgroen) ───────────────────────────────────────
    d.polygon(avocado_poly(top_y=40,  right_x=447, wide_y=308, bot_y=476),
              fill=(23, 73, 44, 255))   # #17492C

    # ── Avocado mid-laag (olijfgroen) ─────────────────────────────────────────
    d.polygon(avocado_poly(top_y=58,  right_x=426, wide_y=310, bot_y=459),
              fill=(136, 191, 66, 255))  # #88BF42

    # ── Avocado vruchtvlees (licht geelgroen) ─────────────────────────────────
    d.polygon(avocado_poly(top_y=76,  right_x=406, wide_y=311, bot_y=443),
              fill=(204, 218, 110, 255)) # #CCDA6E

    # ── Pit buitenrand (zeer donkerbruin) ─────────────────────────────────────
    cx_p, cy_p = int(256 * s), int(314 * s)
    r_out = int(95 * s)
    d.ellipse([cx_p - r_out, cy_p - r_out, cx_p + r_out, cy_p + r_out],
              fill=(94, 44, 6, 255))     # #5E2C06

    # ── Pit hoofdvlak (zadelbruin) ────────────────────────────────────────────
    r_in = int(86 * s)
    d.ellipse([cx_p - r_in, cy_p - r_in, cx_p + r_in, cy_p + r_in],
              fill=(136, 66, 19, 255))   # #884213

    # ── Pit glans (warm halftransparant highlight) ────────────────────────────
    hx, hy = int(228 * s), int(284 * s)
    hrx, hry = int(28 * s), int(19 * s)
    # Teken glans als halfransparant overlay (blend via alpha)
    glow = Image.new('RGBA', (SS, SS), (0, 0, 0, 0))
    gd   = ImageDraw.Draw(glow)
    gd.ellipse([hx - hrx, hy - hry, hx + hrx, hy + hry],
               fill=(165, 94, 42, 140))  # #A55E2A @ ~55%
    img = Image.alpha_composite(img, glow)
    d   = ImageDraw.Draw(img)             # reset draw handle

    # ── Witte V ──────────────────────────────────────────────────────────────
    v_pts = [
        p(203, 264), p(228, 264),
        p(256, 334),
        p(284, 264), p(309, 264),
        p(256, 353),
    ]
    d.polygon(v_pts, fill=(255, 255, 255, 255))

    # ── Schaal naar doelgrootte (LANCZOS = beste kwaliteit) ───────────────────
    return img.resize((size, size), Image.LANCZOS)

print('🖼️   Iconen genereren...')
try:
    for size, name in [(192, 'icon-192.png'), (512, 'icon-512.png')]:
        _draw_avocado_icon(size).save(os.path.join(WWW, name), 'PNG')
        print(f'    ✓ {name} ({size}×{size})')
except Exception as e:
    print(f'    ⚠️  Pillow niet beschikbaar ({e}) — installeer met: pip install pillow')


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
