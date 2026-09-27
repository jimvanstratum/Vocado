#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_readings.py — Genereert www/data/readings.json (v1.45): één leestekst per blok van 10 lessen,
getoond als eerste oefening van de toetsles (milestone). Vragen en opties in het Nederlands,
zodat de oefening tekstbegrip toetst. Richtlengte: A1 40–60, A2 90–120, B1 150–200 woorden.
Draai opnieuw na het bewerken van dit bestand: python3 scripts/build_readings.py
"""
import json
from pathlib import Path

OUT = Path(__file__).parent.parent / 'www' / 'data' / 'readings.json'

def R(milestone, level, title, text, *qs):
    return {'id': f'r{milestone}', 'milestone': milestone, 'level': level, 'title': title, 'text': text.strip(),
            'questions': [{'q': q, 'options': list(opts), 'answer': ans} for q, opts, ans in qs]}

READINGS = [
# ── A1 ────────────────────────────────────────────────────────────────────────
R(10, 'A1', 'Mi chiamo Marco', """
Ciao! Mi chiamo Marco e ho trent'anni. Sono italiano, di Bologna. Abito in una casa piccola con mia moglie Laura e nostro figlio Luca. Luca ha quattro anni.
La mattina bevo un caffè e mangio pane con marmellata. A pranzo mangiamo spesso la pasta. La sera andiamo al ristorante con gli amici. Buonasera e buon appetito!
""",
  ('Waar woont Marco?', ['In Rome', 'In Bologna', 'In Milaan', 'In Napels'], 1),
  ('Hoe oud is Luca?', ['Drie jaar', 'Vier jaar', 'Dertig jaar', 'Veertien jaar'], 1),
  ('Wat eet Marco bij het ontbijt?', ['Pasta', 'Pizza', 'Brood met jam', 'Fruit'], 2)),

R(20, 'A1', 'Una giornata a Roma', """
Oggi è sabato. Fa bel tempo: c'è il sole e non piove. Prendo l'autobus e vado in centro.
Al mercato compro una camicia blu e un paio di scarpe. Costano quaranta euro. Poi visito il museo con mia sorella. Alle sei torniamo a casa in treno. Domenica giochiamo a calcio nel parco.
""",
  ('Hoe is het weer?', ['Het regent', 'Het sneeuwt', 'Het is zonnig', 'Het is bewolkt'], 2),
  ('Wat koopt de schrijver op de markt?', ['Een rok en een hoed', 'Een blauw overhemd en schoenen', 'Een jas', 'Een fiets'], 1),
  ('Wat doen ze zondag?', ['Naar het museum', 'Naar de markt', 'Voetballen in het park', 'Zwemmen in zee'], 2)),

R(30, 'A1', 'La casa di Anna', """
Anna abita in un appartamento a Firenze. La casa ha una cucina, un bagno, un salotto e due camere. Il salotto è grande e ha un divano verde e una finestra sul giardino.
Anna è felice: il suo compleanno è venerdì. Invita gli amici a cena. Compra frutta, verdura e un dolce al mercato. Il weekend è sempre tranquillo.
""",
  ('Hoeveel slaapkamers heeft het appartement?', ['Eén', 'Twee', 'Drie', 'Vier'], 1),
  ('Welke kleur heeft de bank?', ['Rood', 'Blauw', 'Groen', 'Wit'], 2),
  ('Wanneer is de verjaardag van Anna?', ['Maandag', 'Woensdag', 'Vrijdag', 'Zondag'], 2)),

R(40, 'A1', 'In albergo', """
Buongiorno! Ho una prenotazione per due notti. La camera è al terzo piano, vicino all'ascensore. È piccola ma bella, con vista sul mare.
Purtroppo ho mal di testa. Chiedo alla reception: "Dov'è la farmacia?" "Sempre dritto, poi a sinistra, vicino alla chiesa." Grazie mille! Domani partiamo presto: ho fame e ho sete, ma sono contento.
""",
  ('Hoeveel nachten blijft de gast?', ['Eén nacht', 'Twee nachten', 'Drie nachten', 'Een week'], 1),
  ('Wat is het probleem van de gast?', ['Hoofdpijn', 'Koorts', 'Buikpijn', 'Een verkoudheid'], 0),
  ('Waar is de apotheek?', ['Rechts, naast het station', 'Rechtdoor en dan links, bij de kerk', 'In het hotel', 'Aan zee'], 1)),

R(50, 'A1', 'Al bar con Luca', """
Ogni mattina vado al bar con il mio amico Luca. Io prendo un cappuccino e un cornetto, lui prende un tè. Il barista è simpatico e parla sempre del tempo: oggi è nuvoloso.
Dopo il bar Luca va al lavoro in bicicletta. Io prendo il treno alle otto e mezzo. Sabato facciamo una passeggiata in montagna con la famiglia. Finalmente un po' di sport!
""",
  ('Wat drinkt Luca?', ['Een cappuccino', 'Een espresso', 'Thee', 'Water'], 2),
  ('Hoe gaat Luca naar zijn werk?', ['Met de trein', 'Met de auto', 'Op de fiets', 'Te voet'], 2),
  ('Wat doen ze zaterdag?', ['Een wandeling in de bergen', 'Naar de bioscoop', 'Voetballen', 'Zwemmen'], 0)),

R(60, 'A1', 'Il viaggio di Sofia', """
Sofia è un'insegnante di Torino. Domani parte per la Sicilia. All'aeroporto controlla il passaporto e il biglietto sul telefono. L'aereo decolla alle dieci.
In Sicilia vuole vedere il mare, la natura e un festival di musica. Compra anche un souvenir per il nonno: un piccolo vulcano di ceramica. "Che bello!" dice il nonno.
""",
  ('Wat is het beroep van Sofia?', ['Dokter', 'Lerares', 'Kok', 'Ingenieur'], 1),
  ('Hoe laat vertrekt het vliegtuig?', ['Om acht uur', 'Om tien uur', 'Om twaalf uur', 'Om zes uur'], 1),
  ('Wat koopt Sofia voor haar opa?', ['Een boek', 'Een keramische vulkaan', 'Een fles wijn', 'Een T-shirt'], 1)),

# ── A2 ────────────────────────────────────────────────────────────────────────
R(70, 'A2', 'Il primo giorno di lavoro', """
Ieri è stato il mio primo giorno di lavoro in un ufficio a Milano. Ero nervosa, ma i colleghi sono stati gentili. La mia collega Giulia mi ha spiegato il progetto: dobbiamo finire tutto prima della scadenza di venerdì.
Secondo me il lavoro è interessante, però la riunione era troppo lunga. Il capo è simpatico e molto paziente. Quando ero studentessa, lavoravo in un bar: era più stancante ma meno complicato.
Domani sarà una giornata piena. Probabilmente comincerò presto e finirò tardi. Comunque sono contenta: penso che questo lavoro sia meglio del vecchio.
""",
  ('Waar werkt de schrijfster?', ['In een bar in Rome', 'Op een kantoor in Milaan', 'Op een school', 'In een ziekenhuis'], 1),
  ('Wanneer is de deadline van het project?', ['Maandag', 'Woensdag', 'Vrijdag', 'Volgende maand'], 2),
  ('Hoe vergelijkt ze het oude werk met het nieuwe?', ['Het oude was vermoeiender maar minder ingewikkeld', 'Het oude was makkelijker en leuker', 'Het nieuwe is saaier', 'Er is geen verschil'], 0)),

R(80, 'A2', 'Una domenica italiana', """
La domenica in Italia è il giorno della famiglia. Da noi si cucina insieme: mia madre prepara il ragù con gli ingredienti freschi del mercato, mio padre apre una bottiglia di vino. Dopo pranzo tutti fanno un pisolino.
Nel pomeriggio facciamo una passeggiata in centro e prendiamo un aperitivo in piazza. I miei fratelli parlano di calcio: la loro squadra ha vinto la partita.
La sera guardo un film sul divano. Amo queste giornate lente: niente stress, solo la dolce vita.
""",
  ('Wie maakt de ragù?', ['De vader', 'De moeder', 'De broers', 'De schrijver'], 1),
  ('Wat doet de familie na de lunch?', ['Voetballen', 'Winkelen', 'Een dutje doen', 'Naar de bioscoop gaan'], 2),
  ('Waarover praten de broers?', ['Over politiek', 'Over voetbal', 'Over werk', 'Over muziek'], 1)),

R(90, 'A2', 'Il futuro di Giulia', """
Giulia ha diciotto anni e deve scegliere l'università. Le piacciono le scienze e vorrebbe studiare biologia a Padova. Suo padre, però, pensa che l'economia sia più utile.
"Il mondo cambia," dice Giulia. "Il clima, l'inquinamento, le energie rinnovabili: abbiamo bisogno di scienziati." Legge ogni giorno le notizie online e non crede alle fake news.
Il suo obiettivo è chiaro: una laurea, poi un lavoro in un laboratorio. Forse un giorno farà una scoperta importante. Suo padre alla fine sorride: "Realizza il tuo sogno."
""",
  ('Wat wil Giulia studeren?', ['Economie', 'Biologie', 'Rechten', 'Geschiedenis'], 1),
  ('Wat vindt haar vader nuttiger?', ['Biologie', 'Geneeskunde', 'Economie', 'Kunst'], 2),
  ('Wat is het doel van Giulia?', ['Een eigen bedrijf', 'Een baan in een laboratorium', 'Journalist worden', 'Politica worden'], 1)),

R(100, 'A2', 'Un appartamento nuovo', """
Il mese scorso ho cercato un appartamento in affitto a Bologna. Non era facile: le spese erano alte e il canone spesso troppo caro. Finalmente ho trovato un bilocale ammobiliato vicino al centro.
La mia routine è cambiata. Mi sveglio alle sette, faccio colazione e vado al lavoro a piedi. La sera cucino: ieri ho fatto un risotto con le verdure del mercato.
Sabato ho invitato i miei amici per vedere un film. Purtroppo Marco ha dovuto disdire all'ultimo momento, ma ci siamo divertiti lo stesso.
""",
  ('Wat voor woning heeft de schrijver gevonden?', ['Een groot huis met tuin', 'Een gemeubileerde tweekamerwoning', 'Een kamer bij een familie', 'Een villa buiten de stad'], 1),
  ('Hoe gaat de schrijver naar het werk?', ['Met de bus', 'Op de fiets', 'Te voet', 'Met de auto'], 2),
  ('Waarom was Marco er zaterdag niet?', ['Hij was ziek', 'Hij moest op het laatste moment afzeggen', 'Hij was op reis', 'Hij was het vergeten'], 1)),

R(110, 'A2', 'La festa di compleanno', """
Sabato scorso abbiamo festeggiato il compleanno di mia nonna: ottant'anni! Abbiamo organizzato tutto in segreto. Mio zio ha prenotato un ristorante con la cucina piccante della Calabria, la sua regione.
Alla banca ho prelevato i soldi per il regalo: un viaggio a Venezia. Quando è arrivata, la nonna aveva i capelli appena fatti e gli occhiali nuovi. "Auguri!" abbiamo gridato tutti insieme.
C'era un solo problema: il forno del ristorante era guasto e la torta è arrivata in ritardo. Ma la nonna ha riso e ha detto: "Cin cin, alla salute!"
""",
  ('Hoe oud wordt de oma?', ['Zeventig', 'Vijfenzeventig', 'Tachtig', 'Negentig'], 2),
  ('Wat is het cadeau?', ['Een bril', 'Een reis naar Venetië', 'Een taart', 'Een boek'], 1),
  ('Wat was het probleem in het restaurant?', ['Het eten was koud', 'De oven was kapot', 'Er was geen tafel', 'De ober was onbeleefd'], 1)),

R(120, 'A2', 'Il Carnevale di Venezia', """
Ogni anno a febbraio Venezia si trasforma. Il Carnevale è una tradizione antica: le persone indossano maschere e costumi eleganti e sfilano in Piazza San Marco. I saldi di gennaio sono finiti, ma i negozi vendono maschere di ogni colore.
Quest'anno ho scattato molte foto con il telefono e le ho condivise sui social network. Un giornalista ha scritto un articolo sul festival: dice che il turismo è importante per l'economia, ma che bisogna proteggere la città dall'acqua alta.
Ho imparato una cosa: per capire l'Italia bisogna vivere le sue tradizioni. Ora sono bilingue... quasi!
""",
  ('Wanneer is het Carnaval van Venetië?', ['In augustus', 'In februari', 'In december', 'In mei'], 1),
  ('Wat heeft de schrijver gedeeld op sociale media?', ["Foto's", 'Een artikel', 'Een video', 'Een recept'], 0),
  ('Waarvoor moet de stad volgens de journalist beschermd worden?', ['Toeristen', 'Vervuiling', 'Hoogwater', 'Verkeer'], 2)),
# ── B1 ────────────────────────────────────────────────────────────────────────
R(130, 'B1', 'Quando ero bambino', """
Quando ero bambino passavo tutte le estati dai nonni, in un piccolo paese sulle colline toscane. La casa era vecchia e aveva un giardino enorme dove giocavo con mio cugino dalla mattina alla sera.
Mi ricordo bene il profumo del pane che la nonna faceva ogni domenica. Il nonno, invece, raccontava sempre le stesse storie della guerra, ma noi le ascoltavamo come se fossero nuove. Quando pioveva, restavamo in casa e leggevamo i fumetti sul divano.
Un'estate, avevo forse nove anni, è arrivato un temporale terribile. Il vento ha rotto una finestra e la luce è andata via. Avevo paura, ma la nonna ha acceso una candela e ha cominciato a cantare. In quel momento la paura è sparita.
Oggi il paese è cambiato: ci sono più turisti e meno bambini. Eppure, ogni volta che torno, sento ancora quel profumo di pane.
""",
  ('Waar bracht de schrijver de zomers door?', ['Aan zee bij zijn ouders', 'Bij zijn grootouders in Toscane', 'In een stad in het noorden', 'Op een camping'], 1),
  ('Wat deed de opa altijd?', ['Brood bakken', 'Verhalen over de oorlog vertellen', 'Stripboeken lezen', 'Zingen bij onweer'], 1),
  ('Hoe verdween de angst tijdens het onweer?', ['De stroom kwam terug', 'De oma stak een kaars aan en begon te zingen', 'De neef maakte grapjes', 'Het onweer stopte meteen'], 1)),

R(140, 'B1', 'Un viaggio da sogno', """
Se avessi più tempo, farei un viaggio lungo la costa amalfitana. Partirei da Napoli in treno e poi prenderei l'autobus che segue la strada sul mare. Dicono che la vista sia spettacolare, anche se le curve fanno paura a chi soffre il mal d'auto.
Vorrei dormire in un piccolo albergo a Positano, con una terrazza sul mare. La sera cenerei in una trattoria di pesce: potrei ordinare gli spaghetti alle vongole e un bicchiere di vino bianco locale. Il giorno dopo andrei in barca a Capri.
Un consiglio? Sarebbe meglio prenotare in anticipo, perché in estate tutto è pieno. Inoltre, converrebbe evitare la macchina: parcheggiare è quasi impossibile e i traghetti sono più comodi.
Per ora resta un sogno, ma l'anno prossimo potrei finalmente realizzarlo.
""",
  ('Hoe zou de schrijver langs de kust reizen?', ['Met een huurauto', 'Met de bus langs de kustweg', 'Te voet', 'Met een fiets'], 1),
  ('Wat zou de schrijver in de trattoria bestellen?', ['Pizza', 'Spaghetti met vongole en witte wijn', 'Risotto', 'Een salade'], 1),
  ('Welk advies geeft de tekst?', ['Ga in de winter', 'Neem altijd de auto', 'Boek van tevoren en vermijd de auto', 'Slaap in Napels'], 2)),

R(150, 'B1', 'Il colloquio', """
Lunedì Chiara ha avuto un colloquio per un posto di assistente di marketing. Pensava che fosse difficile, ma la responsabile è stata gentile e ha fatto domande chiare sulle sue competenze.
"Credo che lei abbia il profilo giusto," ha detto la responsabile, "ma è importante che sappia lavorare in gruppo e che parli bene l'inglese." Chiara ha spiegato che aveva vissuto un anno a Londra e che aveva gestito i social media di un piccolo negozio.
Alla fine del colloquio le hanno mostrato l'ufficio: una scrivania vicino alla finestra, una stampante che non funziona mai e colleghi che discutevano animatamente di un progetto. Chiara ha pensato: "Spero che mi assumano."
Due giorni dopo è arrivata la telefonata. Il contratto comincia il primo del mese. Chiara è convinta che sia l'inizio di una nuova carriera.
""",
  ('Voor welke functie solliciteerde Chiara?', ['Boekhouder', 'Assistent marketing', 'Lerares Engels', 'Verkoopster'], 1),
  ('Wat vond de verantwoordelijke belangrijk?', ['Een rijbewijs', 'Samenwerken en goed Engels spreken', 'Ervaring in Londen', 'Kennis van printers'], 1),
  ('Hoe eindigt het verhaal?', ['Chiara wordt afgewezen', 'Chiara krijgt de baan', 'Chiara weigert het aanbod', 'Chiara wacht nog op antwoord'], 1)),

R(160, 'B1', 'Una vita sana', """
Da quando lavoro da casa, mi muovo meno e mangio peggio. Il medico me lo ha detto chiaramente: "Il suo corpo ha bisogno di esercizio, non di pillole." Così ho deciso di cambiare abitudini.
Ogni mattina faccio una corsa di mezz'ora nel parco. All'inizio le gambe mi facevano male e il fiato era corto, ma dopo tre settimane mi sento più forte. A pranzo preparo qualcosa di semplice: verdure, un uovo, un pezzo di pane integrale. Il cioccolato lo mangio solo la domenica.
Anche l'ambiente ne guadagna: vado al lavoro in bicicletta invece che in macchina e compro frutta e verdura al mercato, senza plastica. Lo spreco di cibo è diminuito perché faccio la lista della spesa.
Non sono ancora un atleta, ma dormo meglio e ho più energia. Il peso? È sceso di quattro chili.
""",
  ('Wat zei de dokter?', ['Neem meer medicijnen', 'Het lichaam heeft beweging nodig', 'Stop met werken', 'Eet meer chocolade'], 1),
  ('Wat doet de schrijver elke ochtend?', ['Zwemmen', 'Een half uur hardlopen in het park', 'Fietsen naar de markt', 'Yoga'], 1),
  ('Waarom is de voedselverspilling afgenomen?', ['Hij eet minder', 'Hij maakt een boodschappenlijst', 'Hij koopt geen fruit meer', 'Hij eet in restaurants'], 1)),

R(170, 'B1', 'Troppo tempo online', """
Mia figlia Elena ha quindici anni e sta sempre guardando lo schermo del cellulare. Quando le chiedo cosa stia facendo, risponde che sta parlando con le amiche, anche se sono nella stessa stanza.
Ieri sera le ho detto che, secondo un articolo, i ragazzi passano in media cinque ore al giorno sui social. Lei mi ha risposto che l'articolo esagerava e che io non capivo la sua generazione. Ha aggiunto che i video le servono anche per studiare.
Benché io sia preoccupato, so che vietare tutto non funziona. Perciò abbiamo fatto un accordo: niente telefono a tavola e nessuna notifica dopo le dieci di sera. In cambio, il sabato guardiamo insieme un film che sceglie lei.
Mentre scrivo queste righe, Elena sta leggendo un libro. Di carta. Non so quanto durerà, ma è un inizio.
""",
  ('Hoe oud is Elena?', ['Twaalf', 'Vijftien', 'Achttien', 'Twintig'], 1),
  ('Wat zegt Elena over het artikel?', ['Dat het klopt', 'Dat het overdrijft', 'Dat ze het geschreven heeft', 'Dat ze het niet gelezen heeft'], 1),
  ('Wat hebben vader en dochter afgesproken?', ['Geen telefoon meer', 'Geen telefoon aan tafel en geen meldingen na tien uur', 'Elke dag samen een film', 'Alleen video\'s voor school'], 1)),

R(180, 'B1', 'Nord e Sud', """
Si dice spesso che l'Italia sia un paese, ma in realtà sono almeno due. Il Nord è più industriale e più ricco; il Sud è più caldo, più lento e, secondo molti, più ospitale. Milano è la città più efficiente del paese, mentre Napoli è la più vivace.
Anche la cucina cambia. Al Nord si mangia più burro e riso: il risotto alla milanese è il piatto più famoso. Al Sud regnano l'olio d'oliva, il pomodoro e la pasta. Un napoletano vi dirà che la sua pizza è la migliore del mondo, e probabilmente avrà ragione.
Se aveste una settimana sola, che cosa scegliereste? Dipende da ciò che cercate: arte e design al Nord, mare e tradizioni al Sud. Se fossi in voi, farei entrambi, magari in due viaggi diversi.
Un consiglio formale: rispettate i ritmi locali. Al Sud i negozi chiudono nel pomeriggio, e non è pigrizia: è cultura.
""",
  ('Welke stad wordt de meest efficiënte genoemd?', ['Rome', 'Napels', 'Milaan', 'Turijn'], 2),
  ('Wat is typisch voor de keuken van het noorden?', ['Olijfolie en tomaat', 'Boter en rijst', 'Pizza', 'Vis'], 1),
  ('Wat betekent het volgens de tekst dat winkels in het zuiden \'s middags sluiten?', ['Luiheid', 'Economische crisis', 'Cultuur', 'Slechte organisatie'], 2)),

R(190, 'B1', 'Leonardo da Vinci', """
Leonardo nacque nel 1452 a Vinci, un piccolo paese vicino a Firenze. Era figlio di un notaio e di una contadina, e non ricevette un'istruzione classica. Eppure diventò il genio più famoso del Rinascimento.
A quattordici anni entrò nella bottega del Verrocchio, dove imparò a dipingere e a scolpire. Nel 1482 si trasferì a Milano, alla corte di Ludovico Sforza. Lì dipinse l'Ultima Cena, un affresco che ancora oggi attira milioni di visitatori.
Leonardo non fu solo un pittore. Riempì migliaia di pagine di disegni: macchine volanti, ponti, studi sul corpo umano. Scriveva da destra a sinistra, forse per proteggere i suoi segreti.
Negli ultimi anni visse in Francia, ospite del re Francesco I, e morì nel 1519. La Gioconda, il suo capolavoro, si trova ancora oggi a Parigi. Lasciò un'eredità che nessun altro artista ha mai eguagliato.
""",
  ('Wat was het beroep van de vader van Leonardo?', ['Schilder', 'Notaris', 'Boer', 'Koning'], 1),
  ('Wat schilderde Leonardo in Milaan?', ['De Mona Lisa', 'Het Laatste Avondmaal', 'De Geboorte van Venus', 'De Sixtijnse Kapel'], 1),
  ('Waar stierf Leonardo?', ['In Florence', 'In Milaan', 'In Frankrijk', 'In Rome'], 2)),

R(200, 'B1', 'Il trasloco', """
Se avessi saputo quanto era stressante un trasloco, avrei pensato due volte prima di cambiare casa. Tutto è cominciato a marzo, quando il padrone di casa ha aumentato l'affitto. Con quel canone avremmo pagato più della metà dello stipendio.
Abbiamo cercato per settimane. Alla fine abbiamo trovato un appartamento in periferia, più piccolo ma con un balcone. La banca ci ha concesso un piccolo prestito per la caparra e le spese.
Il giorno del trasloco è stato un disastro: dieci scatoloni, una lavatrice che non passava dalla porta e un vicino che si lamentava del rumore. Avremmo dovuto chiamare una ditta specializzata, ma volevamo risparmiare.
Ora, tre mesi dopo, siamo felici. Il quartiere è tranquillo, i vicini ci hanno portato una torta e la sera guardiamo il tramonto dal balcone. Ne è valsa la pena.
""",
  ('Waarom moesten ze verhuizen?', ['Het huis was te klein', 'De huisbaas verhoogde de huur', 'Ze kregen een nieuwe baan', 'Het gebouw werd gesloopt'], 1),
  ('Wat ging er mis op de verhuisdag?', ['De verhuiswagen kwam niet', 'De wasmachine paste niet door de deur', 'Ze verloren de sleutels', 'Het regende'], 1),
  ('Hoe voelen ze zich drie maanden later?', ['Ze hebben spijt', 'Ze willen weer verhuizen', 'Ze zijn gelukkig', 'Ze hebben ruzie met de buren'], 2)),

R(210, 'B1', "L'esame di italiano", """
Temevo che l'esame di italiano fosse impossibile. Avevo studiato la grammatica per mesi, ma il congiuntivo mi sembrava un mistero: pensavo che nessuno lo usasse davvero. Il mio professore, invece, insisteva che fosse fondamentale.
La prova scritta consisteva in un riassunto di un articolo e in una lettera formale. Ho fatto un paio di errori di punteggiatura, ma il senso era chiaro. Nella prova orale l'esaminatrice mi ha chiesto di descrivere la mia città e di esprimere un'opinione sull'università.
Il momento più difficile è stato quando mi ha chiesto: "Se potesse cambiare una cosa del suo paese, che cosa cambierebbe?" Ho risposto con calma, usando due congiuntivi. Lei ha sorriso.
Una settimana dopo ho ricevuto il risultato: promossa, con un voto sufficiente per iscrivermi alla facoltà di lettere. Se non avessi studiato quel maledetto congiuntivo, non ce l'avrei mai fatta.
""",
  ('Wat vond de schrijfster het moeilijkst aan de grammatica?', ['De lidwoorden', 'Het congiuntivo', 'De werkwoorden op -ire', 'De voorzetsels'], 1),
  ('Waaruit bestond het schriftelijke examen?', ['Een dictee', 'Een samenvatting en een formele brief', 'Een opstel over Rome', 'Een vertaling'], 1),
  ('Wat is het resultaat?', ['Gezakt', 'Geslaagd', 'Uitgesteld', 'Onbekend'], 1)),

R(220, 'B1', 'Lettera a un amico', """
Caro Paolo,
ti scrivo perché ho bisogno di un consiglio. Da qualche mese Marta e io litighiamo per ogni sciocchezza: chi cucina, chi paga le bollette, perché torno tardi dal lavoro. Lei dice che sono diventato freddo; io penso che sia lei a essere troppo gelosa.
La verità è che lo stress mi sta cambiando. Al lavoro ho un capo che pretende tutto e subito, e la sera non ho più la forza di parlare. Marta si sente sola, e ha ragione.
Ieri ho fatto un passo: le ho chiesto scusa e le ho proposto un weekend in montagna, senza telefoni. Ha accettato, ma con un sorriso triste. Ho paura che sia troppo tardi.
Tu che conosci entrambi da anni, cosa faresti al posto mio? Dovrei cambiare lavoro? Oppure dovremmo parlare con uno psicologo?
Rispondimi presto, ti prego.
Un abbraccio, Luca
""",
  ('Waarover maken Luca en Marta ruzie?', ['Over vakantiebestemmingen', 'Over kleine dagelijkse dingen', 'Over geld voor een huis', 'Over de kinderen'], 1),
  ('Wat is volgens Luca de oorzaak van zijn gedrag?', ['Zijn jaloezie', 'Stress door zijn werk', 'Zijn nieuwe vrienden', 'Een ziekte'], 1),
  ('Wat heeft Luca aan Marta voorgesteld?', ['Een weekend in de bergen zonder telefoons', 'Verhuizen naar de stad', 'Een etentje met vrienden', 'Een nieuwe baan zoeken'], 0)),

R(230, 'B1', 'Il Parco del Gran Paradiso', """
Il Gran Paradiso è il parco nazionale più antico d'Italia: fu fondato nel 1922 per proteggere lo stambecco, un animale che all'inizio del Novecento rischiava di scomparire. Oggi nel parco vivono più di duemila stambecchi, oltre a camosci, marmotte e aquile.
Il paesaggio è spettacolare: vette che superano i quattromila metri, ghiacciai, torrenti e boschi di larici. In primavera i prati si riempiono di fiori, mentre in autunno le foglie diventano rosse e gialle.
Il parco, però, deve affrontare nuove sfide. Il cambiamento climatico fa sciogliere i ghiacciai e la siccità estiva colpisce le sorgenti. I guardaparco chiedono ai visitatori di rispettare i sentieri, di non lasciare rifiuti e di non dare cibo agli animali.
Chi ama camminare può scegliere tra percorsi facili nella valle e salite impegnative verso i rifugi. In ogni caso, una bussola e uno zaino con acqua e una giacca pesante sono indispensabili.
""",
  ('Waarom werd het park opgericht?', ['Voor toerisme', 'Om de steenbok te beschermen', 'Om skipistes aan te leggen', 'Om hout te winnen'], 1),
  ('Welk probleem noemt de tekst?', ['Te veel steenbokken', 'Smeltende gletsjers door klimaatverandering', 'Gebrek aan wandelpaden', 'Te weinig bezoekers'], 1),
  ('Wat moeten wandelaars volgens de tekst meenemen?', ['Een tent en een kookstel', 'Een kompas, water en een warme jas', 'Eten voor de dieren', 'Een fiets'], 1)),

R(240, 'B1', 'La Mostra del Cinema', """
Ogni settembre il Lido di Venezia ospita la Mostra del Cinema, il festival cinematografico più antico del mondo. Per dieci giorni la piccola isola si riempie di registi, attori, giornalisti e fan che aspettano per ore davanti al tappeto rosso.
Quest'anno ho seguito il festival per il giornale della mia città. La prima sera ho visto un film italiano in bianco e nero, girato in un teatro abbandonato: la critica lo ha definito un capolavoro, il pubblico un po' meno. Il giorno dopo ho intervistato una giovane fotografa che espone i suoi scatti in una mostra sulla moda degli anni Sessanta.
La cosa più interessante, però, non sono i film ma le conversazioni: in fila per un caffè ho conosciuto un produttore spagnolo che cerca finanziamenti per un documentario sui ghiacciai.
Alla fine il Leone d'Oro è andato a un film coreano. Il mio articolo? È uscito in prima pagina, con una foto della laguna al tramonto.
""",
  ('Waar vindt het filmfestival plaats?', ['In Rome', 'Op het Lido van Venetië', 'In Milaan', 'In Cannes'], 1),
  ('Wat vond de schrijver het interessantst?', ['De films', 'De gesprekken met mensen', 'De rode loper', 'Het eten'], 1),
  ('Wie won de Gouden Leeuw?', ['Een Italiaanse film', 'Een Spaanse documentaire', 'Een Koreaanse film', 'Een Franse film'], 2)),

R(250, 'B1', 'Volontari a Lampedusa', """
Lampedusa è un'isola piccolissima nel Mediterraneo, più vicina all'Africa che alla Sicilia. Da anni è la prima terra che molti migranti vedono dopo un viaggio pericoloso in mare. Le leggi cambiano, i governi discutono, ma le barche continuano ad arrivare.
Marco, un infermiere di Torino, ha passato l'estate sull'isola come volontario. "Non faccio politica," dice. "Quando una persona arriva dopo tre giorni senza acqua, ha diritto a un bicchiere d'acqua. Punto."
L'associazione per cui lavora raccoglie donazioni, offre cure mediche e aiuta con i documenti per il permesso di soggiorno. Il lavoro è duro e a volte scoraggiante: mancano i fondi, e alcuni abitanti si lamentano perché il turismo soffre.
Eppure Marco ha visto anche la solidarietà: pescatori che salvano vite in mare, una parrocchia che apre le porte, ragazzi del paese che portano vestiti puliti. "L'integrazione," conclude, "comincia con un gesto semplice."
""",
  ('Wat is het beroep van Marco?', ['Advocaat', 'Verpleegkundige', 'Visser', 'Priester'], 1),
  ('Wat doet de organisatie waarvoor Marco werkt?', ['Politieke campagnes voeren', 'Donaties inzamelen, medische zorg bieden en helpen met documenten', 'Toeristen rondleiden', 'Boten bouwen'], 1),
  ('Waarover klagen sommige bewoners?', ['Over het weer', 'Dat het toerisme lijdt', 'Over de vissers', 'Over de kerk'], 1)),

R(260, 'B1', 'Una riunione difficile', """
Gentile dottoressa Ferri,
in allegato trova il verbale della riunione di ieri con il fornitore tedesco. Come sa, la trattativa non è stata semplice.
Il primo punto all'ordine del giorno riguardava i prezzi: il fornitore chiede un aumento del dieci per cento a causa dei costi di trasporto. Abbiamo proposto un compromesso al cinque per cento, a condizione che la consegna avvenga entro il 15 del mese. La controparte si è impegnata a darci una conferma scritta entro venerdì.
Il secondo punto era il reclamo del cliente di Bologna sul carico danneggiato in dogana. Ho assicurato al cliente un rimborso completo e ho chiesto al nostro ufficio spedizioni di verificare l'imballaggio.
Le suggerisco di partecipare alla prossima presentazione: il direttore commerciale vorrebbe discutere la strategia per l'export in Francia.
Resto a disposizione per qualsiasi chiarimento.
Cordiali saluti,
Andrea Conti
""",
  ('Wat vraagt de leverancier?', ['Een korting van tien procent', 'Een prijsverhoging van tien procent', 'Een langere levertermijn', 'Een nieuw contract'], 1),
  ('Wat is het voorstel van Andrea?', ['Vijf procent, mits levering vóór de vijftiende', 'Geen verhoging', 'Tien procent zonder voorwaarden', 'Een andere leverancier'], 0),
  ('Wat is er gebeurd met de lading voor de klant in Bologna?', ['Ze is te laat geleverd', 'Ze is bij de douane beschadigd', 'Ze is verdwenen', 'Ze is naar Frankrijk gestuurd'], 1)),

R(270, 'B1', 'Samantha Cristoforetti', """
Samantha Cristoforetti è la prima donna italiana ad aver volato nello spazio. Nata a Milano nel 1977, da bambina guardava le stelle dalle montagne del Trentino e sognava di diventare astronauta. Ha studiato ingegneria, è entrata nell'Aeronautica Militare come pilota e nel 2009 è stata scelta dall'Agenzia Spaziale Europea.
Nel 2014 è partita per la Stazione Spaziale Internazionale, dove è rimasta quasi duecento giorni. Lì ha condotto esperimenti scientifici sul corpo umano: come reagiscono i muscoli, le ossa e il cervello senza gravità. Ha anche preparato il primo espresso nello spazio, con una macchina progettata da un'azienda italiana.
Nel 2022 è tornata in orbita, questa volta come comandante della stazione. Nei suoi libri racconta che la cosa più difficile non è il decollo, ma la pazienza: anni di studio e di prove per pochi mesi tra le stelle.
Oggi è un simbolo per molte ragazze che vogliono studiare scienza. Il suo messaggio è semplice: "Non esistono sogni troppo grandi."
""",
  ('Wat studeerde Samantha Cristoforetti?', ['Geneeskunde', 'Ingenieurswetenschappen', 'Biologie', 'Sterrenkunde'], 1),
  ('Wat onderzocht ze op het ruimtestation?', ['Het klimaat op aarde', 'Hoe het menselijk lichaam reageert zonder zwaartekracht', 'Nieuwe raketten', 'Planten in de ruimte'], 1),
  ('Wat is volgens haar het moeilijkst?', ['De lancering', 'Het geduld tijdens de jarenlange voorbereiding', 'Het eten in de ruimte', 'De terugkeer'], 1)),

R(280, 'B1', 'Una giornata piena', """
Sabato scorso avevo una lista infinita di cose da fare. Alle otto ero già dal meccanico: la macchina aveva bisogno del tagliando e una gomma era quasi a terra. "Torni alle cinque," mi ha detto.
Sono andata a piedi alla posta per ritirare una raccomandata della banca: la nuova polizza dell'assicurazione. In fila ho incontrato la mia vicina, che mi ha ricordato la festa di quartiere della sera.
A casa ho passato l'aspirapolvere, lavato i pavimenti e riparato finalmente la mensola in cucina con il trapano di mio fratello. Nel pomeriggio ho annaffiato le piante sul balcone e piantato i pomodori.
Alle cinque la macchina era pronta, ma il conto era più alto del previsto. Pazienza. Alla festa ho portato una teglia di lasagne e per fortuna erano deliziose. A mezzanotte ero stanca morta, ma soddisfatta: la lista era finita.
""",
  ('Waarom moest de auto naar de garage?', ['Voor een nieuw kenteken', 'Voor een onderhoudsbeurt en een bijna lekke band', 'Voor de verzekering', 'Voor een ongeluk'], 1),
  ('Wat haalde de schrijfster op bij het postkantoor?', ['Een pakket', 'Een aangetekende brief van de bank', 'Een boek', 'Een cadeau'], 1),
  ('Wat bracht ze mee naar het buurtfeest?', ['Een taart', 'Een ovenschaal lasagne', 'Wijn', 'Tomaten'], 1)),

R(290, 'B1', 'Una telefonata', """
"Pronto, sono Giovanni. Potrei parlare con la signora Ricci?"
"Un attimo, gliela passo... Mi dispiace, la linea è disturbata. Può richiamare tra cinque minuti?"
Giovanni richiama. Deve fare un reclamo: il frigorifero che ha comprato la settimana scorsa non funziona e il negozio continua a rimandare la riparazione. Ha deciso di chiamare direttamente la responsabile.
"Buongiorno, signora Ricci. La chiamo perché sono al verde di pazienza," scherza. Poi diventa serio: "Il frigorifero è rotto, ho perso un sacco di cibo e nessuno mi risponde. Chi dorme non piglia pesci, e io non voglio più aspettare."
La signora Ricci si scusa di cuore e promette un tecnico entro domani, più un rimborso per il cibo. "Meglio tardi che mai," risponde Giovanni. "Grazie mille, e in bocca al lupo con gli altri clienti!"
"Crepi!" ride la signora Ricci.
""",
  ('Waarom belt Giovanni?', ['Om een koelkast te bestellen', 'Om een klacht in te dienen over een kapotte koelkast', 'Om een baan te vragen', 'Om een afspraak te verzetten'], 1),
  ('Wat belooft mevrouw Ricci?', ['Een nieuwe koelkast volgende maand', 'Een technicus vóór morgen en een terugbetaling', 'Niets', 'Een korting op een volgende aankoop'], 1),
  ('Wat betekent "in bocca al lupo" in dit gesprek?', ['Eet smakelijk', 'Succes', 'Tot ziens', 'Het spijt me'], 1)),

R(300, 'B1', "Lettera di un'insegnante", """
Gentili studenti,
siete arrivati alla fine del livello B1 e vorrei ringraziarvi per il vostro impegno. Quando abbiamo cominciato, molti di voi credevano che l'italiano fosse solo "pizza, pasta e mandolino". Oggi sapete raccontare un ricordo con l'imperfetto, esprimere un dubbio con il congiuntivo e scrivere una lettera formale senza confondere i registri.
Vi ricordo alcune insidie che ci hanno fatto ridere in classe: la "fattoria" non è una fabbrica, i "parenti" non sono i genitori e "attuale" non vuol dire "in tutti i telegiornali". Sono i falsi amici: piccoli tranelli che rendono la lingua più viva.
Che cosa vi consiglierei adesso? Leggete un romanzo, guardate un film senza sottotitoli, telefonate a un amico italiano anche se avete paura di sbagliare. Se aveste studiato solo la grammatica, non sareste arrivati fin qui; siete arrivati perché avete osato parlare.
Vi auguro di cuore un futuro pieno di parole nuove. In bocca al lupo!
Con affetto,
la vostra insegnante
""",
  ('Wat dachten veel studenten aan het begin?', ['Dat Italiaans onmogelijk was', 'Dat Italiaans alleen over pizza, pasta en mandoline ging', 'Dat ze het al spraken', 'Dat de lerares streng was'], 1),
  ('Wat betekent "la fattoria" volgens de brief?', ['De fabriek', 'De boerderij', 'De familie', 'Het huis'], 1),
  ('Wat raadt de lerares aan?', ['Alleen grammatica studeren', 'Lezen, films zonder ondertiteling kijken en durven praten', 'Naar Italië verhuizen', 'Een nieuw boek kopen'], 1)),
]

# ── Validatie + schrijven ────────────────────────────────────────────────────
ms = [r['milestone'] for r in READINGS]
assert ms == list(range(10, 301, 10)), ms
for r in READINGS:
    n = len(r['text'].split())
    lo, hi = {'A1': (35, 75), 'A2': (80, 140), 'B1': (120, 230)}[r['level']]
    assert lo <= n <= hi, f"{r['id']} {r['level']}: {n} woorden"
    assert len(r['questions']) == 3, r['id']
    for q in r['questions']:
        assert len(q['options']) == 4 and 0 <= q['answer'] < 4 and len(set(q['options'])) == 4, (r['id'], q['q'])
OUT.write_text(json.dumps(READINGS, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f"{len(READINGS)} leesteksten → {OUT.name}; woorden per tekst:", [len(r['text'].split()) for r in READINGS])
