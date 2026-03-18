#!/usr/bin/env python3
"""
Sprint 2 – stap 2: verwijder 37 duplicaten en voeg 60 unieke vervangers toe.
Na afloop: A1 ≥ 500, A2 ≥ 500.
"""
import json
from collections import Counter

VOCAB_PATH = 'www/data/vocabulary.json'

with open(VOCAB_PATH) as f:
    words = json.load(f)

# ── 1. Verwijder de 37 nieuwe duplicaten ──────────────────────────────────────
dup_ids = {
    # A1 duplicaten
    'w1041','w1046','w1049','w1056','w1057','w1058','w1059','w1067',
    'w1073','w1080','w1081','w1082','w1083','w1086','w1088','w1091',
    'w1092','w1093','w1098',
    # A2 duplicaten
    'w1102','w1106','w1107','w1108','w1111','w1113','w1114','w1116',
    'w1120','w1123','w1125','w1131','w1137','w1138','w1139','w1143',
    'w1146','w1148',
}
words = [w for w in words if w['id'] not in dup_ids]

existing_it = {w['it'] for w in words}
lvl = Counter(w['level'] for w in words)
print(f"Na verwijdering: A1={lvl['A1']}, A2={lvl['A2']}, totaal={len(words)}")
# Should be: A1=473, A2=467, totaal=940

# ── 2. Unieke vervangende woorden ─────────────────────────────────────────────
# 27 A1 + 33 A2 = 60 woorden; allemaal gecontroleerd uniek

new_a1 = [
    # huis / kamer
    ('il cielo',            'de lucht / de hemel',          'A1'),
    ('la luna',             'de maan',                      'A1'),
    ('la scala',            'de trap',                      'A1'),
    ('il muro',             'de muur',                      'A1'),
    ('il tetto',            'het dak',                      'A1'),
    ('la camera da letto',  'de slaapkamer',                'A1'),
    ('il forno a microonde','de magnetron',                  'A1'),
    ('il bicchiere',        'het glas',                     'A1'),
    ('il coltello',         'het mes',                      'A1'),
    ('il cucchiaio',        'de lepel',                     'A1'),
    ('il portafoglio',      'de portemonnee',               'A1'),
    # reizen / bagage
    ('la strada',           'de straat / de weg',           'A1'),
    ('lo zaino',            'de rugzak',                    'A1'),
    # lichaam
    ('il braccio',          'de arm',                       'A1'),
    ('il collo',            'de nek / de hals',             'A1'),
    ('lo stomaco',          'de maag',                      'A1'),
    # eten / keuken
    ('lo zucchero',         'de suiker',                    'A1'),
    ('il sale',             'het zout',                     'A1'),
    ('il pepe',             'de peper',                     'A1'),
    ('il burro',            'de boter',                     'A1'),
    ('il pollo',            'de kip',                       'A1'),
    ('la carne',            'het vlees',                    'A1'),
    ('il pesce',            'de vis',                       'A1'),
    ('le uova',             'de eieren',                    'A1'),
    ('il riso',             'de rijst',                     'A1'),
    # interieur
    ('la lampada',          'de lamp',                      'A1'),
    ('lo specchio',         'de spiegel',                   'A1'),
]

new_a2 = [
    # werk & loopbaan
    ("l'impiegato",         'de kantoormedewerker',         'A2'),
    ('la ditta',            'het bedrijf / de zaak',        'A2'),
    ("l'impresa",           'de onderneming',               'A2'),
    ('il capo',             'de baas / de chef',            'A2'),
    ('il collega di lavoro','de werkcollega',               'A2'),
    ('la candidatura',      'de sollicitatie',              'A2'),
    # stad & verkeer
    ('il marciapiede',      'het trottoir / de stoep',      'A2'),
    ('la rotonda',          'de rotonde',                   'A2'),
    ('il distributore',     'het benzinestation',           'A2'),
    # natuur
    ('il prato',            'de weide / het grasland',      'A2'),
    ('la collina',          'de heuvel',                    'A2'),
    ('il canale',           'het kanaal',                   'A2'),
    ('la cascata',          'de waterval',                  'A2'),
    ('la pianura',          'de vlakte',                    'A2'),
    ('il vulcano',          'de vulkaan',                   'A2'),
    ('la scogliera',        'de klif / de rotskust',        'A2'),
    # media
    ('la rivista',          'het tijdschrift',              'A2'),
    ('il podcast',          'de podcast',                   'A2'),
    ('la serie tv',         'de tv-serie',                  'A2'),
    ('il documentario',     'de documentaire',              'A2'),
    # gezondheid
    ('il medicinale',       'het geneesmiddel',             'A2'),
    ('la visita medica',    'het medisch onderzoek',        'A2'),
    ('il chirurgo',         'de chirurg',                   'A2'),
    ("l'infermiere",        'de verpleger / de verpleger',  'A2'),
    ('il reparto',          'de afdeling (ziekenhuis)',     'A2'),
    ('la diagnosi',         'de diagnose',                  'A2'),
    # cultuur & entertainment
    ('il dipinto',          'het schilderij',               'A2'),
    ('il concorso',         'de wedstrijd / de competitie', 'A2'),
    ('il premio',           'de prijs / de award',          'A2'),
    ("l'attore",            'de acteur',                    'A2'),
    ("l'attrice",           'de actrice',                   'A2'),
    ('il personaggio',      'het personage',                'A2'),
    # eten
    ('la zuppa',            'de soep',                      'A2'),
]

# ── 3. Dubbelen-check binnen nieuwe lijsten ───────────────────────────────────
all_new = new_a1 + new_a2
assert len(all_new) == 60, f"Verwacht 60, got {len(all_new)}"
new_its = [w[0] for w in all_new]
dups_internal = [it for it in new_its if new_its.count(it) > 1]
if dups_internal:
    print(f"⚠️  Interne duplicaten: {set(dups_internal)}")
    raise SystemExit(1)

conflicts = [(it,nl) for it,nl,_ in all_new if it in existing_it]
if conflicts:
    print(f"⚠️  Conflicten met bestaand vocabulaire ({len(conflicts)}):")
    for it,nl in conflicts:
        print(f"    {it}")
    raise SystemExit(1)

print("✓ Geen interne duplicaten, geen conflicten met bestaand vocabulaire")

# ── 4. Toevoegen met oplopende IDs ────────────────────────────────────────────
max_num = max(int(w['id'][1:]) for w in words)
print(f"Hoogste huidige ID: w{max_num}")

for it, nl, level in all_new:
    max_num += 1
    words.append({
        'id':     f"w{max_num:04d}",
        'it':     it,
        'nl':     nl,
        'level':  level,
        'lesson': 0
    })

# ── 5. Sla op ────────────────────────────────────────────────────────────────
with open(VOCAB_PATH, 'w') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

# ── 6. Eindstand ─────────────────────────────────────────────────────────────
lvl2 = Counter(w['level'] for w in words)
print(f"\n=== Eindstand ===")
print(f"A1: {lvl2['A1']} woorden (doel ≥500) {'✓' if lvl2['A1'] >= 500 else '⚠️'}")
print(f"A2: {lvl2['A2']} woorden (doel ≥500) {'✓' if lvl2['A2'] >= 500 else '⚠️'}")
print(f"Totaal: {len(words)}")
