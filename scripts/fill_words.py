#!/usr/bin/env python3
"""
fill_words.py — Vul lessen aan tot 8 woorden met thematisch passende, unieke woorden.
IDs beginnen bij w961. Slaat op in vocabulary.json en curriculum.json.
"""
import json
from pathlib import Path

BASE = Path(__file__).parent.parent / 'www' / 'data'
VOCAB_FILE = BASE / 'vocabulary.json'
CURR_FILE  = BASE / 'curriculum.json'

with open(VOCAB_FILE, encoding='utf-8') as f:
    vocab = json.load(f)
with open(CURR_FILE, encoding='utf-8') as f:
    lessons = json.load(f)

existing_it = {w['it'].lower() for w in vocab}
lesson_map = {l['id']: l for l in lessons}

# Nieuwe woorden per les — thematisch passend, A1/A2-niveau
# Formaat: (it, nl, ph, ex, exNl, cat)
new_words_per_lesson = {

    # Les 16 — Tijdsaanduidingen (1 tekort)
    16: [
        ('mezzogiorno', 'middag (twaalf uur)', 'met-tso-djor-no',
         'A mezzogiorno mangiamo insieme.', 'Om twaalf uur eten we samen.', 'tijd'),
    ],

    # Les 22 — Meer kleuren (2 tekort)
    22: [
        ('a pois', 'gestippeld', 'a po-i',
         'Ho una gonna a pois.', 'Ik heb een gestippelde rok.', 'kleuren'),
        ('brillante', 'helder / schitterend', 'bril-lan-te',
         'Questo colore è molto brillante.', 'Deze kleur is heel helder.', 'kleuren'),
    ],

    # Les 29 — Kalender & afspraken (2 tekort)
    29: [
        ('il fine settimana', 'het weekend', 'il fi-ne set-ti-ma-na',
         'Il fine settimana vado al mare.', 'In het weekend ga ik naar zee.', 'tijd'),
        ("l'appuntamento", 'de afspraak', 'lap-pun-ta-men-to',
         "Ho un appuntamento alle tre.", 'Ik heb om drie uur een afspraak.', 'tijd'),
    ],

    # Les 35 — Gevoelens (6 tekort)
    35: [
        ('felice', 'blij', 'fe-li-tsje',
         'Sono molto felice oggi.', 'Ik ben vandaag erg blij.', 'gevoelens'),
        ('triste', 'verdrietig', 'tris-te',
         'Mi sento triste senza di te.', 'Ik voel me verdrietig zonder jou.', 'gevoelens'),
        ('arrabbiato', 'boos', 'ar-rab-bja-to',
         'Perché sei arrabbiato?', 'Waarom ben je boos?', 'gevoelens'),
        ('stanco', 'moe', 'stan-ko',
         'Sono stanco dopo il lavoro.', 'Ik ben moe na het werk.', 'gevoelens'),
        ('preoccupato', 'bezorgd', 'pre-ok-ku-pa-to',
         'Sei preoccupato per l\'esame?', 'Ben je bezorgd voor het examen?', 'gevoelens'),
        ('emozionato', 'opgewonden / emotioneel', 'e-mo-tsjo-na-to',
         'Sono emozionato per le vacanze!', 'Ik ben opgewonden voor de vakantie!', 'gevoelens'),
    ],

    # Les 40 — Klaar voor vertrek! (2 tekort)
    40: [
        ('a presto!', 'tot gauw!', 'a pres-to',
         'Ciao, a presto!', 'Dag, tot gauw!', 'uitdrukkingen'),
        ('figurati!', 'geen dank! / doe niet zo moeilijk!', 'fi-gou-ra-ti',
         '— Grazie mille! — Figurati!', '— Hartelijk dank! — Geen dank!', 'uitdrukkingen'),
    ],

    # Les 41 — In het café (5 tekort)
    41: [
        ('il cappuccino', 'de cappuccino', 'il kap-put-tsji-no',
         'Vorrei un cappuccino, per favore.', 'Ik wil graag een cappuccino, alstublieft.', 'eten & drinken'),
        ('il cornetto', 'het croissant', 'il kor-net-to',
         'Prendo un cornetto alla crema.', 'Ik neem een croissant met crème.', 'eten & drinken'),
        ("l'acqua minerale", 'het mineraalwater', 'lak-kwa mi-ne-ra-le',
         "Vorrei un'acqua minerale fresca.", 'Ik wil graag koud mineraalwater.', 'eten & drinken'),
        ('il conto', 'de rekening', 'il kon-to',
         'Posso avere il conto?', 'Kan ik de rekening krijgen?', 'café & restaurant'),
        ('il cameriere', 'de ober', 'il ka-me-rje-re',
         'Il cameriere è molto gentile.', 'De ober is erg vriendelijk.', 'café & restaurant'),
    ],

    # Les 42 — Al ristorante (6 tekort)
    42: [
        ('il secondo', 'het hoofdgerecht', 'il se-kon-do',
         'Come secondo prendo il pollo.', 'Als hoofdgerecht neem ik de kip.', 'eten & drinken'),
        ("l'antipasto", 'het voorgerecht', 'lan-ti-pas-to',
         "L'antipasto è una bruschetta.", 'Het voorgerecht is een bruschetta.', 'eten & drinken'),
        ('il menù', 'het menu', 'il me-nù',
         'Posso vedere il menù?', 'Mag ik het menu zien?', 'café & restaurant'),
        ('la forchetta', 'de vork', 'la for-ket-ta',
         'Dove è la forchetta?', 'Waar is de vork?', 'huishouden'),
        ('il piatto', 'het bord', 'il pjat-to',
         'Il piatto è molto grande.', 'Het bord is erg groot.', 'huishouden'),
        ('il contorno', 'het bijgerecht', 'il kon-tor-no',
         'Come contorno prendo le verdure.', 'Als bijgerecht neem ik de groenten.', 'eten & drinken'),
    ],

    # Les 43 — Vervoer (6 tekort)
    43: [
        ('il treno', 'de trein', 'il tre-no',
         'Il treno parte alle otto.', 'De trein vertrekt om acht uur.', 'vervoer'),
        ("l'aereo", 'het vliegtuig', 'la-e-re-o',
         "L'aereo arriva in ritardo.", 'Het vliegtuig komt te laat aan.', 'vervoer'),
        ('la stazione', 'het station', 'la sta-tsjo-ne',
         'La stazione è vicino al centro.', 'Het station is vlakbij het centrum.', 'vervoer'),
        ("l'autobus", 'de bus', 'lau-to-bus',
         "Prendo l'autobus ogni giorno.", 'Ik neem elke dag de bus.', 'vervoer'),
        ("l'arrivo", 'de aankomst', 'lar-ri-vo',
         "L'arrivo è previsto per le undici.", 'De aankomst is voorzien voor elf uur.', 'vervoer'),
        ('il binario', 'het perron', 'il bi-na-rjo',
         'Il treno parte dal binario tre.', 'De trein vertrekt van perron drie.', 'vervoer'),
    ],

    # Les 44 — Hotel & verblijf (7 tekort)
    44: [
        ('la camera', 'de kamer', 'la ka-me-ra',
         'Vorrei una camera per due notti.', 'Ik wil graag een kamer voor twee nachten.', 'reizen'),
        ('il letto', 'het bed', 'il let-to',
         'Il letto è molto comodo.', 'Het bed is erg comfortabel.', 'huishouden'),
        ('la chiave', 'de sleutel', 'la kjа-ve',
         'Ho dimenticato la chiave in camera.', 'Ik heb de sleutel op de kamer vergeten.', 'reizen'),
        ('la colazione', 'het ontbijt', 'la ko-la-tsjo-ne',
         'La colazione è inclusa nel prezzo.', 'Het ontbijt is inbegrepen in de prijs.', 'eten & drinken'),
        ('il bagno', 'de badkamer', 'il ban-jo',
         'Il bagno è in fondo al corridoio.', 'De badkamer is aan het einde van de gang.', 'huishouden'),
        ('singola', 'eenpersoons', 'sin-go-la',
         'Vorrei una camera singola.', 'Ik wil graag een eenpersoonskamer.', 'reizen'),
        ("l'ascensore", 'de lift', 'la-sjen-so-re',
         "L'ascensore è a destra.", 'De lift is rechts.', 'gebouwen'),
    ],

    # Les 45 — Familie (6 tekort)
    45: [
        ('la mamma', 'de mama', 'la mam-ma',
         'La mia mamma cucina benissimo.', 'Mijn mama kookt geweldig.', 'familie'),
        ('il papà', 'de papa', 'il pa-pà',
         'Il mio papà lavora in banca.', 'Mijn papa werkt bij de bank.', 'familie'),
        ('il fratello', 'de broer', 'il fra-tel-lo',
         'Ho un fratello più giovane.', 'Ik heb een jongere broer.', 'familie'),
        ('la sorella', 'de zus', 'la so-rel-la',
         'Mia sorella abita a Milano.', 'Mijn zus woont in Milaan.', 'familie'),
        ('il figlio', 'de zoon', 'il fil-jo',
         'Il loro figlio ha cinque anni.', 'Hun zoon is vijf jaar oud.', 'familie'),
        ('lo zio', 'de oom', 'lo dzjo',
         'Mio zio mi porta sempre un regalo.', 'Mijn oom brengt me altijd een cadeau.', 'familie'),
    ],

    # Les 46 — De weg vragen (1 tekort)
    46: [
        ('dritto', 'rechtdoor', 'drit-to',
         'Vada dritto per duecento metri.', 'Ga tweehonderd meter rechtdoor.', 'navigatie'),
    ],

    # Les 47 — Het weer (6 tekort)
    47: [
        ('il sole', 'de zon', 'il so-le',
         'Oggi c\'è il sole.', 'Vandaag schijnt de zon.', 'weer'),
        ('la pioggia', 'de regen', 'la pjod-dja',
         'La pioggia mi piace.', 'Ik hou van de regen.', 'weer'),
        ('il vento', 'de wind', 'il ven-to',
         'Oggi c\'è molto vento.', 'Vandaag is het erg winderig.', 'weer'),
        ('la neve', 'de sneeuw', 'la ne-ve',
         'D\'inverno cade la neve.', "'s Winters valt er sneeuw.", 'weer'),
        ('freddo', 'koud', 'fred-do',
         'Fa molto freddo in dicembre.', 'Het is erg koud in december.', 'weer'),
        ('caldo', 'warm / heet', 'kal-do',
         'In estate fa molto caldo.', 'In de zomer is het erg warm.', 'weer'),
    ],

    # Les 48 — Gezondheid (6 tekort)
    48: [
        ('la febbre', 'de koorts', 'la feb-bre',
         'Ho la febbre a 38 gradi.', 'Ik heb koorts van 38 graden.', 'gezondheid'),
        ('il mal di testa', 'de hoofdpijn', 'il mal di tes-ta',
         'Ho un forte mal di testa.', 'Ik heb erge hoofdpijn.', 'gezondheid'),
        ('la tosse', 'de hoest', 'la tos-se',
         'Ho la tosse da tre giorni.', 'Ik heb al drie dagen hoest.', 'gezondheid'),
        ('il raffreddore', 'de verkoudheid', 'il raf-fred-do-re',
         'Ho preso un raffreddore.', 'Ik heb een verkoudheid opgelopen.', 'gezondheid'),
        ('la farmacia', 'de apotheek', 'la far-ma-tsji-a',
         'Devo andare in farmacia.', 'Ik moet naar de apotheek.', 'gezondheid'),
        ('il dolore', 'de pijn', 'il do-lo-re',
         'Ho un dolore al ginocchio.', 'Ik heb pijn aan mijn knie.', 'gezondheid'),
    ],

    # Les 49 — Activiteiten & hobby's (5 tekort)
    49: [
        ('leggere', 'lezen', 'led-dje-re',
         'Mi piace leggere romanzi.', 'Ik lees graag romans.', 'activiteiten'),
        ('cucinare', 'koken', 'ku-tsji-na-re',
         'Nel tempo libero cucino.', 'In mijn vrije tijd kook ik.', 'activiteiten'),
        ('disegnare', 'tekenen', 'di-sen-ja-re',
         'Da bambino amavo disegnare.', 'Als kind hield ik van tekenen.', 'activiteiten'),
        ('viaggiare', 'reizen', 'vjad-dja-re',
         'Mi piace molto viaggiare.', 'Ik reis erg graag.', 'activiteiten'),
        ('nuotare', 'zwemmen', 'nuo-ta-re',
         'Ogni estate nuoto in mare.', 'Elke zomer zwem ik in zee.', 'activiteiten'),
    ],

    # Les 50 — Plannen maken (1 tekort)
    50: [
        ('finalmente', 'eindelijk', 'fi-nal-men-te',
         'Finalmente siamo in vacanza!', 'Eindelijk zijn we op vakantie!', 'uitdrukkingen'),
    ],

    # Les 56 — Muziek & cultuur (1 tekort)
    56: [
        ('il ritmo', 'het ritme', 'il rit-mo',
         'Questo brano ha un ritmo fantastico.', 'Dit nummer heeft een fantastisch ritme.', 'kunst & cultuur'),
    ],

    # Les 69 — Beschrijvingen (1 tekort)
    69: [
        ('entusiasmante', 'opwindend / enthousiasmerend', 'en-tu-zjaz-man-te',
         'Il viaggio è stato entusiasmante.', 'De reis was opwindend.', 'beschrijvingen'),
    ],

    # Les 70 — Reizen gevorderd (1 tekort)
    70: [
        ('la guida turistica', 'de reisgids', 'la gwi-da tu-ris-ti-ka',
         'Ho comprato una guida turistica di Roma.', 'Ik heb een reisgids van Rome gekocht.', 'reizen'),
    ],

    # Les 71 — Koken gevorderd (1 tekort)
    71: [
        ('cremoso', 'romig', 'kre-mo-zo',
         'Questa salsa è cremosa e deliziosa.', 'Deze saus is romig en heerlijk.', 'eten & drinken'),
    ],

    # Les 72 — Technologie (1 tekort)
    72: [
        ('la tastiera', 'het toetsenbord', 'la tas-tje-ra',
         'Ho bisogno di una nuova tastiera.', 'Ik heb een nieuw toetsenbord nodig.', 'technologie'),
    ],

    # Les 73 — Natuur & milieu (2 tekort)
    73: [
        ('la foresta', 'het bos / de jungle', 'la fo-res-ta',
         'Le foreste tropicali sono in pericolo.', 'De tropische bossen zijn in gevaar.', 'natuur'),
        ('il paesaggio', 'het landschap', 'il pa-e-zad-djo',
         'Il paesaggio toscano è bellissimo.', 'Het Toscaanse landschap is prachtig.', 'natuur'),
    ],

    # Les 74 — Gezondheid & welzijn (2 tekort)
    74: [
        ('il riposo', 'de rust', 'il ri-po-zo',
         'Il corpo ha bisogno di riposo.', 'Het lichaam heeft rust nodig.', 'gezondheid'),
        ("l'attività fisica", 'de lichamelijke activiteit', 'lat-ti-vi-tà fi-zi-ka',
         "L'attività fisica migliora l'umore.", 'Lichaamsbeweging verbetert de stemming.', 'gezondheid'),
    ],

    # Les 76 — Sport & competitie (2 tekort)
    76: [
        ('il gol', 'het doelpunt', 'il gol',
         'Ha segnato un gol al novantesimo.', 'Hij scoorde een doelpunt in de negentigste minuut.', 'sport'),
        ('la vittoria', 'de overwinning', 'la vit-to-rja',
         'La vittoria è stata sorprendente.', 'De overwinning was verrassend.', 'sport'),
    ],

    # Les 79 — Kunst & cultuur (1 tekort)
    79: [
        ("l'affresco", 'de fresco (muurschildering)', 'laf-fres-ko',
         "L'affresco nella cappella è del Rinascimento.", 'De fresco in de kapel is uit de Renaissance.', 'kunst & cultuur'),
    ],

    # Les 91 — Tijdsuitdrukkingen verleden (1 tekort)
    91: [
        ('di recente', 'recentelijk / onlangs', 'di re-tsjen-te',
         'Ho visitato Roma di recente.', 'Ik heb Rome onlangs bezocht.', 'tijd'),
    ],

    # Les 110 — Sport & outdoor (2 tekort)
    110: [
        ('il podio', 'het podium', 'il po-djo',
         'È salito sul podio tra gli applausi.', 'Hij besteeg het podium onder applaus.', 'sport'),
        ('la medaglia', 'de medaille', 'la me-dal-ja',
         'Ha vinto una medaglia d\'oro.', 'Hij won een gouden medaille.', 'sport'),
    ],

    # Les 112 — Technologie & internet (1 tekort)
    112: [
        ('la notifica', 'de melding / de notificatie', 'la no-ti-fi-ka',
         'Ho ricevuto una notifica dal telefono.', 'Ik heb een melding van de telefoon ontvangen.', 'technologie'),
    ],

    # Les 119 — Duurzaamheid & milieu (2 tekort)
    119: [
        ('il compost', 'het compost', 'il kom-post',
         'Facciamo il compost con gli scarti di cibo.', 'We maken compost van etensresten.', 'milieu'),
        ('la mobilità sostenibile', 'de duurzame mobiliteit', 'la mo-bi-li-tà sos-te-ni-bi-le',
         'Usiamo la mobilità sostenibile ogni giorno.', 'We gebruiken dagelijks duurzame mobiliteit.', 'milieu'),
    ],
}

# Bereken start-ID
max_id = max(int(w['id'].replace('w', '')) for w in vocab)
next_id = max_id + 1

added_words = []
skipped = []

for lesson_id in sorted(new_words_per_lesson.keys()):
    lesson = lesson_map[lesson_id]
    word_entries = new_words_per_lesson[lesson_id]
    level = lesson.get('level', 'A1')
    needed = 8 - len(lesson.get('words', []))

    added_for_lesson = 0
    for it, nl, ph, ex, exNl, cat in word_entries:
        if added_for_lesson >= needed:
            break
        if it.lower() in existing_it:
            skipped.append((lesson_id, it))
            continue
        wid = f'w{next_id}'
        next_id += 1
        word = {
            'id': wid, 'it': it, 'nl': nl, 'ph': ph,
            'ex': ex, 'exNl': exNl,
            'lesson': lesson_id, 'level': level, 'cat': cat
        }
        vocab.append(word)
        existing_it.add(it.lower())
        lesson.setdefault('words', []).append(wid)
        added_words.append((lesson_id, wid, it))
        added_for_lesson += 1

print(f'✓ {len(added_words)} nieuwe woorden toegevoegd')
if skipped:
    print(f'⚠️  {len(skipped)} woorden overgeslagen (al aanwezig): {[s[1] for s in skipped]}')

# Verificatie
print('\nWord counts na aanvulling:')
problems = []
for lesson in lessons:
    wc = len(lesson.get('words', []))
    if wc < 8 and lesson['id'] != 3:
        problems.append((lesson['id'], wc, lesson['title']))
if problems:
    print('  ⚠️  Lessen nog steeds te kort:')
    for lid, wc, title in problems:
        print(f'    Les {lid}: {wc} woorden — {title}')
else:
    print('  ✓ Alle lessen hebben ≥8 woorden (les 3 uitgezonderd)')

# Uniekheid check
all_it = [w['it'].lower() for w in vocab]
if len(set(all_it)) == len(all_it):
    print('  ✓ Alle Italiaanse woorden zijn uniek')
else:
    print('  ⚠️  Nog steeds duplicaten aanwezig!')

print(f'\nTotaal woorden: {len(vocab)}')

# Sla op
with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)
with open(CURR_FILE, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)
print('✓ Opgeslagen')
