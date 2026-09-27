#!/usr/bin/env python3
"""
dedupe_b1.py — Sprint 8 (v1.44): dubbele Italiaanse woorden verwijderen en gaten opvullen.

1. Groepeert vocabulary.json op `it` (hoofdletterongevoelig). Per groep blijft één entry:
   laagste niveau (A1 < A2 < B1), daarna in-les vóór extra, daarna laagste ID.
2. Verwijderde entries die in een les-woordenlijst stonden, worden op dezelfde positie
   vervangen door een nieuw woord uit dedupe_b1_data.GAP_WORDS (thematisch per les).
3. Eén verwijderde A2-extra ('il carnevale') krijgt een A2-vervanger zodat A2 op 500 blijft.
4. Schrijft www/js/idmap.js: {verwijderd-ID: behouden-ID} voor de SRS-migratie in de app.

Al uitgevoerd; opnieuw draaien geeft een foutmelding.
"""
import json, re, sys
from pathlib import Path
from collections import defaultdict, Counter
sys.path.insert(0, str(Path(__file__).parent))
from dedupe_b1_data import GAP_WORDS

BASE = Path(__file__).parent.parent / 'www'
VOCAB_FILE, CURR_FILE, IDMAP_FILE = BASE/'data'/'vocabulary.json', BASE/'data'/'curriculum.json', BASE/'js'/'idmap.js'
START_ID = 2711
LV = {'A1': 0, 'A2': 1, 'B1': 2}
ART = re.compile(r"^(?:(?:il|lo|la|i|gli|le|un|una|uno)\s+|(?:l'|un')\s*)", re.I)
norm = lambda s: ART.sub('', s.lower()).strip()

vocab = json.load(open(VOCAB_FILE, encoding='utf-8'))
lessons = json.load(open(CURR_FILE, encoding='utf-8'))
if any(int(w['id'][1:]) >= START_ID for w in vocab):
    sys.exit('Script is al uitgevoerd (IDs vanaf w2711 bestaan al).')

lesson_of = {wid: l['id'] for l in lessons for wid in l['words']}
by_lesson = {l['id']: l for l in lessons}

# ── 1. Dubbels bepalen ────────────────────────────────────────────────────────
groups = defaultdict(list)
for w in vocab:
    groups[w['it'].lower()].append(w)
idmap = {}                      # verwijderd -> behouden
for ws in groups.values():
    if len(ws) < 2: continue
    ws.sort(key=lambda w: (LV[w['level']], lesson_of.get(w['id'], 999), int(w['id'][1:])))
    for w in ws[1:]:
        idmap[w['id']] = ws[0]['id']
removed = set(idmap)
print(f'dubbele entries verwijderd: {len(removed)}')

# ── 2. Gaten opvullen ─────────────────────────────────────────────────────────
existing = {norm(w['it']) for w in vocab if w['id'] not in removed}
queue = defaultdict(list)       # les -> nieuwe woorden (in volgorde)
for x in GAP_WORDS:
    queue[x[0]].append(x)
next_id = START_ID
new_words = []
for l in lessons:
    for i, wid in enumerate(l['words']):
        if wid not in removed: continue
        les, it, nl, ph, ex, exNl, cat = queue[l['id']].pop(0)
        assert norm(it) not in existing, f'{it} bestaat al'
        existing.add(norm(it))
        nw = {'id': f'w{next_id}', 'it': it, 'nl': nl, 'ph': ph, 'ex': ex, 'exNl': exNl,
              'lesson': l['id'], 'level': l['level'], 'cat': cat}
        next_id += 1
        new_words.append(nw)
        l['words'][i] = nw['id']
assert not any(queue.values()), f'ongebruikte gap-woorden: {[q for q in queue.values() if q]}'

# ── 3. A2-extra vervanger ─────────────────────────────────────────────────────
a2_lost = [w for w in vocab if w['id'] in removed and w['level'] == 'A2' and w['id'] not in lesson_of]
assert len(a2_lost) == 1, a2_lost
a2 = {'id': f'w{next_id}', 'it': 'la processione', 'nl': 'de processie', 'ph': 'pro-tsjes-SJO-ne',
      'ex': 'La processione attraversa il paese.', 'exNl': 'De processie trekt door het dorp.',
      'lesson': a2_lost[0]['lesson'], 'level': 'A2', 'cat': a2_lost[0].get('cat', 'tradizioni')}
assert norm(a2['it']) not in existing
new_words.append(a2); next_id += 1

# ── 4. Schrijven ──────────────────────────────────────────────────────────────
vocab = [w for w in vocab if w['id'] not in removed] + new_words
its = Counter(w['it'].lower() for w in vocab)
assert not [k for k, n in its.items() if n > 1], 'nog steeds dubbels'
json.dump(vocab, open(VOCAB_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2); open(VOCAB_FILE, 'a').write('\n')
json.dump(lessons, open(CURR_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2); open(CURR_FILE, 'a').write('\n')
js = ("// Gegenereerd door scripts/dedupe_b1.py (v1.44) — niet handmatig bewerken.\n"
      "// Verwijderd woord-ID → behouden woord-ID, voor de eenmalige SRS-migratie.\n"
      "export const ID_MAP = " + json.dumps(idmap, separators=(',', ':')) + ";\n")
IDMAP_FILE.write_text(js, encoding='utf-8')
print(f'nieuwe woorden: {len(new_words)} ({new_words[0]["id"]}–{new_words[-1]["id"]}) | totaal {len(vocab)} | '
      f'{Counter(w["level"] for w in vocab)} | idmap {len(idmap)} entries')
