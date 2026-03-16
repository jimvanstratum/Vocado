#!/usr/bin/env python3
"""
cleanup_dupes.py — Verwijder duplicate Italiaanse woorden uit vocabulary.json
en update curriculum.json dienovereenkomstig.

Strategie: bewaar de copy met de LAAGSTE les-nummer; verwijder alle latere copies.
"""
import json
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent.parent / 'www' / 'data'
VOCAB_FILE = BASE / 'vocabulary.json'
CURR_FILE  = BASE / 'curriculum.json'

with open(VOCAB_FILE, encoding='utf-8') as f:
    vocab = json.load(f)
with open(CURR_FILE, encoding='utf-8') as f:
    lessons = json.load(f)

# Bouw lesson-nr lookup per word-id
lesson_of_word = {}
for lesson in lessons:
    for wid in lesson.get('words', []):
        lesson_of_word[wid] = lesson['id']

# Groepeer word-IDs per Italiaans woord (lowercase)
by_it = defaultdict(list)
for w in vocab:
    by_it[w['it'].lower()].append(w['id'])

# Bepaal welke IDs bewaard worden (vroegste les) en welke verwijderd
keep_ids = set()
remove_ids = set()
replace_map = {}  # removed_id -> keep_id (voor eventuele referentie)

for it_lower, ids in by_it.items():
    if len(ids) == 1:
        keep_ids.add(ids[0])
        continue
    # Sorteer op les-nummer (woorden zonder les-veld krijgen 999)
    ids_sorted = sorted(ids, key=lambda wid: lesson_of_word.get(wid, 999))
    keep_ids.add(ids_sorted[0])
    for dup_id in ids_sorted[1:]:
        remove_ids.add(dup_id)
        replace_map[dup_id] = ids_sorted[0]

print(f'Te verwijderen duplicaten: {len(remove_ids)}')
print(f'Bewaard (uniek): {len(keep_ids)}')

# Verwijder uit vocabulary
vocab_clean = [w for w in vocab if w['id'] not in remove_ids]
print(f'Vocabulary na cleanup: {len(vocab_clean)} woorden (was {len(vocab)})')

# Verwijder uit curriculum lesson.words
lessons_affected = 0
for lesson in lessons:
    original = lesson.get('words', [])
    cleaned = [wid for wid in original if wid not in remove_ids]
    if len(cleaned) < len(original):
        lesson['words'] = cleaned
        lessons_affected += 1

print(f'Lessen aangepast: {lessons_affected}')

# Overzicht lessen met tekort na cleanup
print('\nLessen met <8 woorden na cleanup:')
short_lessons = []
for lesson in lessons:
    wc = len(lesson.get('words', []))
    if wc < 8 and lesson['id'] != 3:  # les 3 (Cijfers) mag 10 hebben
        short_lessons.append((lesson['id'], wc, 8 - wc, lesson['title']))

short_lessons.sort(key=lambda x: x[0])
for lid, wc, missing, title in short_lessons:
    print(f'  Les {lid:3d}: {wc} woorden ({missing} tekort) — {title}')
print(f'Totaal lessen met tekort: {len(short_lessons)}')
print(f'Totaal ontbrekende woorden: {sum(x[2] for x in short_lessons)}')

# Verificeer alle word-IDs in lesson.words nog bestaan
valid_ids = {w['id'] for w in vocab_clean}
for lesson in lessons:
    for wid in lesson.get('words', []):
        if wid not in valid_ids:
            print(f'⚠️  ONGELDIG ID: {wid} in les {lesson["id"]}')

# Sla op
with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
    json.dump(vocab_clean, f, ensure_ascii=False, indent=2)
with open(CURR_FILE, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print('\n✓ vocabulary.json en curriculum.json opgeslagen')
