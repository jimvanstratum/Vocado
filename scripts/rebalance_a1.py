#!/usr/bin/env python3
"""
rebalance_a1.py — Sprint 8b (v1.44): A1/A2-herbalancering.

De frequentie-analyse van v1.44 liet zien dat kernwoorden (uomo, donna, libro, dire, ...)
alleen in B1-lessen zaten. Dit script ruilt 99 paren: het kernwoord verhuist naar een
A1/A2-les met passend thema en krijgt een eenvoudige voorbeeldzin; het zeldzaamste
woord uit die les neemt zijn plek in de B1-les in. Woord-IDs blijven gelijk (geen SRS-
migratie nodig). Al uitgevoerd; opnieuw draaien geeft een foutmelding.

Formaat SWAPS: (kernwoord_it, doel_les, nieuwe_ex, nieuwe_exNl, partner_it)
"""
import json, re, sys
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent / 'www' / 'data'
VOCAB_FILE, CURR_FILE = BASE / 'vocabulary.json', BASE / 'curriculum.json'

SWAPS = [
    ('dire', 37, "Come si dice 'kaas' in italiano?", "Hoe zeg je 'kaas' in het Italiaans?", 'non capisco'),
    ('pensare', 61, 'Penso di sì.', 'Ik denk van wel.', 'penso che'),
    ('così', 61, 'Non è così.', 'Zo is het niet.', 'in effetti'),
    ('credere', 66, 'Credo di sì.', 'Ik geloof van wel.', 'infatti'),
    ('solo', 66, 'Ho solo dieci euro.', 'Ik heb maar tien euro.', 'fortunatamente'),
    ('allora', 63, "Allora non c'era internet.", 'Toen was er geen internet.', 'si usava'),
    ('ancora', 64, 'Non ho ancora deciso.', 'Ik heb nog niet besloten.', 'sicuramente'),
    ('lavorare', 67, 'Lavoro in un ufficio.', 'Ik werk op een kantoor.', 'scadenza'),
    ('tornare', 92, 'Torno a casa alle sei.', 'Ik kom om zes uur thuis.', 'addormentarsi'),
    ('finire', 92, 'Finisco di lavorare alle cinque.', 'Ik ben om vijf uur klaar met werken.', 'lavarsi'),
    ('il pranzo', 92, 'A pranzo mangio un panino.', 'Bij de lunch eet ik een broodje.', 'riposarsi'),
    ('studiare', 49, "Studio l'italiano ogni giorno.", 'Ik studeer elke dag Italiaans.', 'sciare'),
    ('spesso', 49, 'Vado spesso in piscina.', 'Ik ga vaak naar het zwembad.', 'giocare a calcio'),
    ('mai', 49, 'Non vado mai in palestra.', 'Ik ga nooit naar de sportschool.', 'andare in bicicletta'),
    ('aspettare', 13, 'Aspetto il treno.', 'Ik wacht op de trein.', 'la bicicletta'),
    ('restare', 44, 'Resto tre notti.', 'Ik blijf drie nachten.', 'singola'),
    ('cominciare', 50, 'Il corso comincia lunedì.', 'De cursus begint maandag.', 'dopodomani'),
    ("l'idea", 50, "Ho un'idea!", 'Ik heb een idee!', 'pianificare'),
    ('sentire', 24, 'Non sento bene.', 'Ik hoor niet goed.', 'la gola'),
    ('la faccia', 24, 'Mi lavo la faccia.', 'Ik was mijn gezicht.', 'il ginocchio'),
    ('la gamba', 7, 'Mi fa male la gamba.', 'Mijn been doet pijn.', "l'orecchio"),
    ('entrare', 14, 'Entriamo nel museo?', 'Gaan we het museum binnen?', 'il supermercato'),
    ('la gente', 14, "In piazza c'è molta gente.", 'Op het plein zijn veel mensen.', 'centro storico'),
    ('usare', 55, 'Uso il computer ogni giorno.', 'Ik gebruik elke dag de computer.', 'la batteria'),
    ('il telefono', 55, "Dov'è il mio telefono?", 'Waar is mijn telefoon?', "l'applicazione"),
    ('il numero', 55, 'Qual è il tuo numero?', 'Wat is jouw nummer?', 'scaricare'),
    ('conoscere', 98, 'Conosco Marco da dieci anni.', 'Ik ken Marco al tien jaar.', 'il/la migliore amico/a'),
    ("l'amico", 98, 'Esco con un amico.', 'Ik ga uit met een vriend.', 'il ritrovo'),
    ("l'uomo", 104, "L'uomo con la barba è mio zio.", 'De man met de baard is mijn oom.', 'robusto'),
    ('la donna', 104, 'La donna alta è la mia insegnante.', 'De lange vrouw is mijn lerares.', 'la carnagione'),
    ('il ragazzo', 104, 'Il ragazzo ha i capelli neri.', 'De jongen heeft zwart haar.', 'somigliare a'),
    ('la ragazza', 104, 'La ragazza ha gli occhi verdi.', 'Het meisje heeft groene ogen.', 'di media altezza'),
    ('il signore', 53, 'Il signor Rossi è il mio medico.', 'Meneer Rossi is mijn dokter.', 'il commerciante'),
    ('il bambino', 88, 'I bambini vanno a scuola a sei anni.', 'Kinderen gaan op hun zesde naar school.', 'la formazione continua'),
    ('il genitore', 88, "I genitori parlano con l'insegnante.", 'De ouders praten met de leraar.', 'la materia'),
    ('amare', 75, 'Ti amo.', 'Ik hou van je.', 'commosso'),
    ('mancare', 75, 'Mi manchi.', 'Ik mis je.', 'rispettare'),
    ('ridere', 30, 'Rido sempre con te.', 'Ik lach altijd met jou.', 'entusiasta'),
    ('piangere', 30, 'Il bambino piange.', 'Het kind huilt.', 'emozionato'),
    ('la paura', 35, 'Ho paura del buio.', 'Ik ben bang in het donker.', 'annoiato'),
    ('preoccuparsi', 35, 'Non ti preoccupare!', 'Maak je geen zorgen!', 'deluso'),
    ('ora', 16, 'Ora vado a casa.', 'Nu ga ik naar huis.', 'mezzogiorno'),
    ('il libro', 19, 'Leggo un libro.', 'Ik lees een boek.', 'la fotografia'),
    ('la palla', 57, 'Passami la palla!', 'Geef me de bal!', "l'arbitro"),
    ('il gioco', 57, 'Il calcio è un gioco di squadra.', 'Voetbal is een teamspel.', "l'allenamento"),
    ('forte', 20, 'Sei molto forte!', 'Je bent heel sterk!', 'la palestra'),
    ('la cena', 42, 'La cena è alle otto.', 'Het avondeten is om acht uur.', 'il contorno'),
    ('il cibo', 108, 'Il cibo italiano è famoso.', 'Het Italiaanse eten is beroemd.', 'la tradizione culinaria'),
    ('il latte', 21, 'Un litro di latte, per favore.', 'Een liter melk, alstublieft.', 'la banana'),
    ("l'uovo", 71, 'Mangio due uova a colazione.', 'Ik eet twee eieren bij het ontbijt.', 'cremoso'),
    ('la patata', 71, 'Le patate al forno sono pronte.', 'De aardappels uit de oven zijn klaar.', 'ingredienti'),
    ('il cane', 54, 'Il cane corre nel parco.', 'De hond rent in het park.', 'il parco nazionale'),
    ('il cavallo', 39, "Il cavallo mangia l'erba.", 'Het paard eet gras.', 'collina'),
    ('la stanza', 8, 'La mia stanza è piccola.', 'Mijn kamer is klein.', 'il salotto'),
    ('il corpo', 74, 'Il corpo ha bisogno di riposo.', 'Het lichaam heeft rust nodig.', 'prevenzione'),
    ('la voce', 77, 'Ha una bella voce.', 'Zij heeft een mooie stem.', 'melodia'),
    ('la vita', 80, 'La vita è bella.', 'Het leven is mooi.', 'pisolino'),
    ("l'amore", 80, "L'amore è importante.", 'Liefde is belangrijk.', 'passeggiata'),
    ('il mondo', 90, 'Voglio vedere il mondo.', 'Ik wil de wereld zien.', 'realizzare'),
    ('qualcosa', 11, 'Cerco qualcosa per mia madre.', 'Ik zoek iets voor mijn moeder.', 'economico'),
    ('qualcuno', 32, 'Qualcuno chiami un medico!', 'Iemand moet een dokter bellen!', 'passaporto'),
    ('la fortuna', 40, 'Buona fortuna!', 'Veel succes!', 'figurati!'),
    ('il minuto', 43, 'Il treno parte tra cinque minuti.', 'De trein vertrekt over vijf minuten.', 'partenza'),
    ('guidare', 43, 'Non so guidare.', 'Ik kan niet autorijden.', "l'arrivo"),
    ('il momento', 93, 'Un momento, per favore.', 'Een ogenblik, alstublieft.', 'disdire'),
    ('incontrare', 93, 'Ci incontriamo alle tre?', 'Zullen we om drie uur afspreken?', 'rimandare'),
    ('la giornata', 47, 'Che bella giornata!', 'Wat een mooie dag!', 'nevicare'),
    ('il nome', 120, 'Come si scrive il tuo nome?', 'Hoe schrijf je je naam?', 'la fluidità'),
    ('la parola', 120, 'Imparo dieci parole al giorno.', 'Ik leer tien woorden per dag.', 'conversare'),
    ('il paese', 58, 'Quale paese vuoi visitare?', 'Welk land wil je bezoeken?', 'la destinazione'),
    ('il giro', 58, 'Facciamo un giro in barca?', 'Zullen we een boottochtje maken?', 'esplorare'),
    ('la mappa', 70, 'Ho una mappa della città.', 'Ik heb een plattegrond van de stad.', 'la cartina'),
    ('avanti', 46, 'Vai avanti fino alla piazza.', 'Ga rechtdoor tot het plein.', 'semaforo'),
    ('fermare', 46, 'Può fermare qui, per favore?', 'Kunt u hier stoppen, alstublieft?', 'incrocio'),
    ('il dottore', 33, 'Devo andare dal dottore.', 'Ik moet naar de dokter.', 'allergico'),
    ('alto', 34, 'Mio fratello è molto alto.', 'Mijn broer is heel lang.', 'corto'),
    ('serio', 68, 'È una persona seria.', 'Het is een serieus persoon.', 'simpatico'),
    ('cattivo', 68, 'Non è cattivo, è solo timido.', 'Hij is niet gemeen, alleen verlegen.', 'curioso'),
    ('carino', 68, 'Sei molto carino.', 'Je bent heel aardig.', 'coraggioso'),
    ('la persona', 69, 'È una persona interessante.', 'Het is een interessant persoon.', 'affollato'),
    ('vero', 69, 'È vero!', 'Het is waar!', 'sorprendente'),
    ('sicuro', 69, 'Sei sicuro?', 'Weet je het zeker?', 'entusiasmante'),
    ('il problema', 103, "C'è un problema con la camera.", 'Er is een probleem met de kamer.', 'insoddisfatto'),
    ('il posto', 60, 'È un posto bellissimo.', 'Het is een prachtige plek.', 'il monumento'),
    ('i soldi', 101, 'Non ho abbastanza soldi.', 'Ik heb niet genoeg geld.', 'lo sportello'),
    ('la lista', 95, 'Ho fatto la lista della spesa.', 'Ik heb een boodschappenlijst gemaakt.', 'un etto'),
    ('il programma', 97, "Che programma c'è stasera?", 'Welk programma is er vanavond?', 'doppiato'),
    ("l'aria", 73, "L'aria in città è sporca.", 'De lucht in de stad is vuil.', 'spreco'),
    ('la terra', 113, 'La terra è secca.', 'De grond is droog.', 'grandine'),
    ('divertente', 26, 'Il film è molto divertente.', 'De film is heel grappig.', 'fotografare'),
    ('interessante', 26, 'Il libro è interessante.', 'Het boek is interessant.', 'la lettura'),
    ('la prova', 117, 'La prova è domani.', 'De toets is morgen.', 'bilingue'),
    ("l'incidente", 106, "C'è stato un incidente.", 'Er is een ongeluk gebeurd.', 'il pedaggio'),
    ('vendere', 59, 'Vendono frutta fresca.', 'Ze verkopen vers fruit.', 'rimborsare'),
    ('dimenticare', 107, 'Ho dimenticato il tuo compleanno.', 'Ik ben je verjaardag vergeten.', 'il rimpianto'),
    ('fuori', 15, 'Fuori piove.', 'Buiten regent het.', 'nuvoloso'),
    ('dentro', 28, 'Dentro casa fa caldo.', 'Binnen in huis is het warm.', 'il divano'),
    ('funzionare', 72, 'Il telefono non funziona.', 'De telefoon werkt niet.', 'la tastiera'),
    ('controllare', 72, 'Controllo le e-mail.', 'Ik controleer mijn e-mail.', 'caricatore'),
]

vocab = json.load(open(VOCAB_FILE, encoding='utf-8'))
lessons = json.load(open(CURR_FILE, encoding='utf-8'))
by_it = {}
for w in vocab:
    by_it.setdefault(w['it'].lower(), w)
by_lesson = {l['id']: l for l in lessons}
lesson_membership = Counter(wid for l in lessons for wid in l['words'])

NOUNS_NO_ART = {'scadenza', 'melodia', 'prevenzione', 'spreco', 'collina', 'passaporto', 'partenza',
                'semaforo', 'incrocio', 'grandine', 'pisolino', 'passeggiata', 'caricatore', 'ingredienti', 'un etto'}
def b1_cat(w):
    it, nl = w['it'].strip(), w['nl'].strip().lower()
    if re.search(r'(are|ere|ire|rsi)$', it) and ' ' not in it: return 'verbo'
    if it.lower() in NOUNS_NO_ART or re.match(r"^(il|lo|la|i|gli|le|l'|un|una|uno)\s", it) or "'" in it[:3] \
            or re.match(r'^(de|het|een)\s', nl): return 'sostantivo'
    if '!' in it or (' ' in it and not re.search(r'(are|ere|ire|rsi)$', it)): return 'espressione'
    if re.search(r'(are|ere|ire|rsi)$', it): return 'verbo'
    return 'aggettivo'

done = 0
for core_it, target, ex, exNl, partner_it in SWAPS:
    core, partner = by_it[core_it.lower()], by_it[partner_it.lower()]
    tl = by_lesson[target]
    assert core['level'] == 'B1' and int(core['id'][1:]) >= 2711, f'{core_it}: geen v1.44-kernwoord (al geruild?)'
    assert partner['id'] in tl['words'], f'{partner_it} staat niet in les {target}'
    assert lesson_membership[partner['id']] == 1, f'{partner_it} staat in meerdere lessen'
    src = by_lesson[core['lesson']]
    assert core['id'] in src['words'], f'{core_it} niet in les {core["lesson"]}'
    # les-woordenlijsten ruilen (zelfde positie)
    src['words'][src['words'].index(core['id'])] = partner['id']
    tl['words'][tl['words'].index(partner['id'])] = core['id']
    # partner -> B1
    partner['lesson'], partner['level'], partner['cat'] = src['id'], 'B1', b1_cat(partner)
    # kernwoord -> A1/A2 met eenvoudige zin en de dominante categorie van de doelles
    dom_cat = Counter(by_it_id['cat'] for by_it_id in vocab if by_it_id['id'] in tl['words'] and by_it_id['id'] != core['id']).most_common(1)[0][0]
    core['lesson'], core['level'], core['cat'], core['ex'], core['exNl'] = target, tl['level'], dom_cat, ex, exNl
    done += 1

assert all(len(l['words']) == 8 or l['id'] == 3 for l in lessons)
assert not [k for k, n in Counter(w['it'].lower() for w in vocab).items() if n > 1]
json.dump(vocab, open(VOCAB_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2); open(VOCAB_FILE, 'a').write('\n')
json.dump(lessons, open(CURR_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2); open(CURR_FILE, 'a').write('\n')
print(f'geruild: {done} paren | niveaus: {Counter(w["level"] for w in vocab)}')
