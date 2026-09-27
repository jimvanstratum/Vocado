#!/usr/bin/env python3
"""
add_b1_extra.py — Vult B1 aan met 60 extra woorden tot het CEFR-doel van 1500 (Sprint 7, v1.43).
Al uitgevoerd; opnieuw draaien geeft een foutmelding omdat de woorden dan al bestaan.

De woorden staan niet in de 'words'-lijst van een les (die blijft 8), maar krijgen wel een
lesson-nummer zodat ze meedraaien in de toetsles van het blok (app.js kiest quizwoorden op
w.lesson) en in het woordenboek. Zelfde patroon als de A1/A2-aanvulling in v1.38.
IDs: w2651–w2710.
"""
import json, re, sys
from pathlib import Path

BASE = Path(__file__).parent.parent / 'www' / 'data'
VOCAB_FILE = BASE / 'vocabulary.json'
CURR_FILE  = BASE / 'curriculum.json'
START_ID = 2651

with open(VOCAB_FILE, encoding='utf-8') as f: vocab = json.load(f)
with open(CURR_FILE, encoding='utf-8') as f: lessons = json.load(f)

ART = re.compile(r"^(il|lo|la|i|gli|le|l'|un|una|uno|un')\s*", re.I)
def norm(it): return ART.sub('', it.lower()).strip()
existing = {norm(w['it']) for w in vocab}
lesson_ids = {l['id'] for l in lessons if l['level'] == 'B1'}
if any(int(w['id'][1:]) >= START_ID for w in vocab):
    sys.exit('Script is al uitgevoerd (IDs vanaf w2651 bestaan al).')

# (it, nl, ph, ex, exNl, lesson, cat)
WORDS = [
    # Blok 7 — geschiedenis, kunst, tradities
    ('il Medioevo', 'de middeleeuwen', 'me-djo-E-vo', 'Nel Medioevo le città erano fortificate.', 'In de middeleeuwen waren de steden versterkt.', 183, 'sostantivo'),
    ('il mosaico', 'het mozaïek', 'mo-ZA-i-ko', 'I mosaici di Ravenna sono famosi.', 'De mozaïeken van Ravenna zijn beroemd.', 184, 'sostantivo'),
    ('lo scultore', 'de beeldhouwer', 'skul-TO-re', 'Michelangelo era anche uno scultore.', 'Michelangelo was ook beeldhouwer.', 184, 'sostantivo'),
    ('il cenone', 'het feestmaal (kerstavond, oudjaar)', 'tsje-NO-ne', 'Il cenone di Capodanno dura ore.', 'Het oudejaarsdiner duurt uren.', 188, 'cultura'),
    ('la Befana', 'de Befana (heks van 6 januari)', 'be-FA-na', 'La Befana porta i dolci ai bambini.', 'De Befana brengt snoep voor de kinderen.', 188, 'cultura'),
    # Blok 8 — financiën, wonen
    ('il padrone di casa', 'de huisbaas', 'pa-DRO-ne di KA-za', "Il padrone di casa vuole l'affitto.", 'De huisbaas wil de huur.', 197, 'sostantivo'),
    ("il contratto d'affitto", 'het huurcontract', 'kon-TRAT-to daf-FIT-to', "Ho firmato il contratto d'affitto.", 'Ik heb het huurcontract getekend.', 197, 'sostantivo'),
    # Blok 9 — onderwijs
    ('la facoltà', 'de faculteit', 'fa-kol-TA', 'Studio alla facoltà di lettere.', 'Ik studeer aan de faculteit letteren.', 206, 'sostantivo'),
    ('promosso', 'geslaagd', 'pro-MOS-so', "Sono stato promosso all'esame.", 'Ik ben geslaagd voor het examen.', 208, 'aggettivo'),
    ('la calligrafia', 'het handschrift', 'kal-li-gra-FI-a', 'Ha una calligrafia molto chiara.', 'Hij heeft een heel duidelijk handschrift.', 207, 'sostantivo'),
    ('il riassunto', 'de samenvatting', 'ri-as-SUN-to', 'Scrivi un riassunto del capitolo.', 'Schrijf een samenvatting van het hoofdstuk.', 207, 'sostantivo'),
    ('la punteggiatura', 'de interpunctie', 'pun-ted-dja-TU-ra', 'Attento alla punteggiatura!', 'Let op de interpunctie!', 209, 'sostantivo'),
    # Blok 10 — relaties, gevoelens
    ('il fidanzamento', 'de verloving', 'fi-dan-tsa-MEN-to', 'Hanno annunciato il fidanzamento.', 'Ze hebben hun verloving aangekondigd.', 212, 'sostantivo'),
    ('il tradimento', 'het verraad, het bedrog', 'tra-di-MEN-to', "Il tradimento ha rovinato l'amicizia.", 'Het verraad heeft de vriendschap verwoest.', 213, 'sostantivo'),
    ('il perdono', 'de vergiffenis', 'per-DO-no', 'Ti chiedo perdono.', 'Ik vraag je om vergiffenis.', 213, 'sostantivo'),
    ('permaloso', 'lichtgeraakt', 'per-ma-LO-zo', 'Non essere così permaloso!', 'Wees niet zo lichtgeraakt!', 214, 'aggettivo'),
    ('il sollievo', 'de opluchting', 'sol-LJE-vo', 'Che sollievo, è finita!', 'Wat een opluchting, het is voorbij!', 219, 'emozione'),
    # Blok 11 — natuur, milieu
    ('la cuccia', 'de hondenmand', 'KUT-tsja', 'Il cane dorme nella cuccia.', 'De hond slaapt in zijn mand.', 221, 'sostantivo'),
    ('la preda', 'de prooi', 'PRE-da', 'Il leone insegue la preda.', 'De leeuw achtervolgt de prooi.', 222, 'sostantivo'),
    ('il nido', 'het nest', 'NI-do', 'Gli uccelli fanno il nido in primavera.', 'Vogels bouwen hun nest in de lente.', 222, 'sostantivo'),
    ('la marea', 'het getij', 'ma-RE-a', 'La marea sale la sera.', "Het tij komt 's avonds op.", 225, 'sostantivo'),
    ('il faro', 'de vuurtoren', 'FA-ro', 'Il faro illumina la costa.', 'De vuurtoren verlicht de kust.', 225, 'sostantivo'),
    ('la bussola', 'het kompas', 'BUS-so-la', 'Senza bussola ci perdiamo.', 'Zonder kompas verdwalen we.', 226, 'sostantivo'),
    ('la pala eolica', 'de windturbine', 'PA-la e-O-li-ka', 'Le pale eoliche producono energia pulita.', 'Windturbines produceren schone energie.', 229, 'sostantivo'),
    # Blok 12 — media, cultuur
    ('il doppiaggio', 'de nasynchronisatie', 'dop-PJA-djo', 'In Italia il doppiaggio è molto comune.', 'In Italië is nasynchronisatie heel gebruikelijk.', 231, 'sostantivo'),
    ('il pennello', 'het penseel', 'pen-NEL-lo', 'Il pittore lava i pennelli.', 'De schilder wast zijn penselen.', 233, 'sostantivo'),
    ('lo scatto', 'de foto, het kiekje', 'SKAT-to', 'Ho fatto uno scatto bellissimo.', 'Ik heb een prachtige foto gemaakt.', 234, 'sostantivo'),
    ('la didascalia', 'het bijschrift', 'di-das-ka-LI-a', 'Leggi la didascalia sotto la foto.', 'Lees het bijschrift onder de foto.', 234, 'sostantivo'),
    ('la testata', 'de krant (als uitgave)', 'tes-TA-ta', 'È una testata molto seria.', 'Het is een heel serieuze krant.', 235, 'sostantivo'),
    ('il telecomando', 'de afstandsbediening', 'te-le-ko-MAN-do', "Dov'è il telecomando?", 'Waar is de afstandsbediening?', 236, 'sostantivo'),
    # Blok 13 — politiek, maatschappij
    ('il deputato', 'het parlementslid', 'de-pu-TA-to', 'Il deputato ha parlato in aula.', 'Het parlementslid heeft in de zaal gesproken.', 241, 'sostantivo'),
    ('la scheda elettorale', 'het stembiljet', 'SKE-da e-let-to-RA-le', 'Ho compilato la scheda elettorale.', 'Ik heb het stembiljet ingevuld.', 242, 'sostantivo'),
    ('il testimone', 'de getuige', 'tes-TI-mo-ne', 'Il testimone ha detto la verità.', 'De getuige heeft de waarheid gezegd.', 244, 'sostantivo'),
    ('la cittadinanza', 'het staatsburgerschap', 'tsjit-ta-di-NAN-tsa', 'Ha chiesto la cittadinanza italiana.', 'Hij heeft het Italiaanse staatsburgerschap aangevraagd.', 245, 'sostantivo'),
    ('la raccolta fondi', 'de inzamelingsactie', 'rak-KOL-ta FON-di', 'Organizziamo una raccolta fondi.', 'We organiseren een inzamelingsactie.', 246, 'sostantivo'),
    ('la donazione', 'de donatie', 'do-na-TSJO-ne', "Ho fatto una donazione all'ospedale.", 'Ik heb een donatie aan het ziekenhuis gedaan.', 246, 'sostantivo'),
    # Blok 14 — werk
    ('il tirocinio', 'de stage', 'ti-ro-TSJI-njo', 'Faccio un tirocinio in banca.', 'Ik loop stage bij een bank.', 251, 'sostantivo'),
    ('la scaletta', 'de opzet (van een presentatie)', 'ska-LET-ta', 'Prepara una scaletta per la presentazione.', 'Maak een opzet voor de presentatie.', 254, 'sostantivo'),
    ('in allegato', 'als bijlage', 'in al-le-GA-to', 'Trova il documento in allegato.', 'U vindt het document als bijlage.', 255, 'espressione'),
    ('lo sciopero', 'de staking', 'SJO-pe-ro', "Domani c'è lo sciopero dei treni.", 'Morgen is er een treinstaking.', 257, 'sostantivo'),
    # Blok 15 — gezondheid, wetenschap
    ('il ricovero', 'de ziekenhuisopname', 'ri-KO-ve-ro', 'Il ricovero è durato tre giorni.', 'De opname duurde drie dagen.', 261, 'sostantivo'),
    ('gli effetti collaterali', 'de bijwerkingen', 'ef-FET-ti kol-la-te-RA-li', 'Questo farmaco ha pochi effetti collaterali.', 'Dit medicijn heeft weinig bijwerkingen.', 262, 'sostantivo'),
    ('il cerotto', 'de pleister', 'tsje-ROT-to', 'Metti un cerotto sulla ferita.', 'Doe een pleister op de wond.', 264, 'sostantivo'),
    ('il razzo', 'de raket', 'RAT-tso', 'Il razzo parte domani.', 'De raket vertrekt morgen.', 269, 'sostantivo'),
    # Blok 16 — dagelijks leven
    ('il tagliando', 'de onderhoudsbeurt', 'ta-LJAN-do', 'La macchina ha bisogno del tagliando.', 'De auto moet een onderhoudsbeurt hebben.', 272, 'sostantivo'),
    ('il pneumatico', 'de band (van een auto)', 'pneu-MA-ti-ko', 'Devo cambiare i pneumatici.', 'Ik moet de banden vervangen.', 272, 'sostantivo'),
    ('la raccomandata', 'de aangetekende brief', 'rak-ko-man-DA-ta', 'Ho ricevuto una raccomandata.', 'Ik heb een aangetekende brief ontvangen.', 273, 'sostantivo'),
    ('il mestolo', 'de pollepel', 'MES-to-lo', 'Mescola la zuppa con il mestolo.', 'Roer de soep met de pollepel.', 275, 'sostantivo'),
    ('la teglia', 'de bakvorm, de ovenschaal', 'TE-lja', 'Ungi la teglia con il burro.', 'Vet de bakvorm in met boter.', 275, 'sostantivo'),
    ('il trapano', 'de boormachine', 'TRA-pa-no', 'Uso il trapano per fare un buco.', 'Ik gebruik de boormachine om een gat te maken.', 277, 'sostantivo'),
    ("l'annaffiatoio", 'de gieter', 'an-naf-fja-TO-jo', "Riempi l'annaffiatoio.", 'Vul de gieter.', 278, 'sostantivo'),
    # Blok 17 — uitdrukkingen, communicatie
    ("non vedo l'ora", 'ik kan niet wachten', 'non VE-do LO-ra', "Non vedo l'ora di partire!", 'Ik kan niet wachten om te vertrekken!', 281, 'espressione'),
    ('fare il ponte', 'een brugdag nemen', 'FA-re il PON-te', 'Venerdì facciamo il ponte.', 'Vrijdag nemen we een brugdag.', 282, 'espressione'),
    ('chi dorme non piglia pesci', 'wie slaapt, vangt geen vis', 'ki DOR-me non PI-lja PE-sji', 'Alzati presto: chi dorme non piglia pesci.', 'Sta vroeg op: wie slaapt, vangt geen vis.', 283, 'espressione'),
    ('riuscire a', 'erin slagen om', 'rju-SJI-re a', 'Sono riuscito a finire in tempo.', 'Ik ben erin geslaagd op tijd klaar te zijn.', 284, 'espressione'),
    ('smettere di', 'ophouden met', 'SMET-te-re di', 'Ha smesso di fumare.', 'Hij is gestopt met roken.', 284, 'espressione'),
    ('andare a trovare', 'opzoeken, bezoeken (iemand)', 'an-DA-re a tro-VA-re', 'Domenica vado a trovare i nonni.', 'Zondag ga ik mijn grootouders opzoeken.', 284, 'espressione'),
    ('lo squillo', 'het belsignaal', 'SKWIL-lo', 'Fammi uno squillo quando arrivi.', 'Bel me even als je aankomt.', 287, 'sostantivo'),
    ('la linea', 'de (telefoon)verbinding', 'LI-ne-a', 'La linea è disturbata.', 'De verbinding is slecht.', 287, 'sostantivo'),
    ('di cuore', 'van harte', 'di KWO-re', 'Grazie di cuore per tutto.', 'Van harte bedankt voor alles.', 289, 'espressione'),
]

assert len(WORDS) == 60, f'{len(WORDS)} woorden, 60 verwacht'
seen = set()
for it, *_, lesson, cat in WORDS:
    assert lesson in lesson_ids, f'{it}: les {lesson} is geen B1-les'
    assert norm(it) not in existing, f'{it} bestaat al'
    assert norm(it) not in seen, f'{it} dubbel in lijst'
    seen.add(norm(it))

added = [{'id': f'w{START_ID + i}', 'it': it, 'nl': nl, 'ph': ph, 'ex': ex, 'exNl': exNl,
          'lesson': lesson, 'level': 'B1', 'cat': cat}
         for i, (it, nl, ph, ex, exNl, lesson, cat) in enumerate(WORDS)]
vocab.extend(added)
with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2); f.write('\n')
print(f'toegevoegd: {len(added)} ({added[0]["id"]}–{added[-1]["id"]}), totaal nu {len(vocab)}')
