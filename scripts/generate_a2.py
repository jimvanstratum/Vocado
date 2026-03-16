"""Genereert 30 nieuwe A2-lessen (91-120) met 8 woorden elk = 240 nieuwe woorden."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURR_FILE = os.path.join(BASE, 'www/data/curriculum.json')
VOCAB_FILE = os.path.join(BASE, 'www/data/vocabulary.json')

# ── Nieuwe lessen ──────────────────────────────────────────────────────────────
new_lessons = [
  {
    "id": 91, "title": "Tijdsuitdrukkingen — verleden", "emoji": "⏮️", "level": "A2",
    "description": "Praat over wat er gisteren, vorige week of jaren geleden is gebeurd.",
    "grammar": {
      "title": "Tijdsaanduidingen bij het passato prossimo",
      "body": ("Tijdsuitdrukkingen staan vaak aan het begin of einde van de zin. "
               "'Ieri ho lavorato' = Gisteren heb ik gewerkt. "
               "'Due anni fa sono andato a Roma' = Twee jaar geleden ben ik naar Rome gegaan. "
               "'La settimana scorsa' = vorige week, 'il mese scorso' = vorige maand, 'l'anno scorso' = vorig jaar. "
               "'Fa' = geleden: 'tre giorni fa' = drie dagen geleden.")
    },
    "words": [f"w{721+i}" for i in range(8)]
  },
  {
    "id": 92, "title": "Dagelijkse routine", "emoji": "🌅", "level": "A2",
    "description": "Beschrijf je dag — van opstaan tot naar bed gaan.",
    "grammar": {
      "title": "Reflexieve werkwoorden in de routine",
      "body": ("Veel routinewerkwoorden zijn reflexief: 'mi alzo' (ik sta op), 'mi lavo' (ik was me), "
               "'mi vesto' (ik kleed me aan), 'mi addormento' (ik val in slaap). "
               "Reflexief: mi/ti/si/ci/vi/si + werkwoord. "
               "'A che ora ti alzi?' = Hoe laat sta jij op? Deze werkwoorden zijn onmisbaar voor A2.")
    },
    "words": [f"w{729+i}" for i in range(8)]
  },
  {
    "id": 93, "title": "Afspraken maken", "emoji": "📅", "level": "A2",
    "description": "Plan een ontmoeting, stel een tijd voor en bevestig of annuleer.",
    "grammar": {
      "title": "Afspraken maken — uitdrukkingen",
      "body": ("'Ci vediamo domani?' = Zien we elkaar morgen? "
               "'Ti va di...' = Heb je zin om...? 'Ti va di andare al cinema?' = Heb je zin om naar de film te gaan? "
               "'Sono libero/a' = ik ben vrij. 'Non posso, ho già un impegno' = ik kan niet, ik heb al iets. "
               "'Ci sentiamo!' = we bellen/spreken elkaar! — veelgebruikte afsluiting.")
    },
    "words": [f"w{737+i}" for i in range(8)]
  },
  {
    "id": 94, "title": "Plannen voor de toekomst", "emoji": "🗓️", "level": "A2",
    "description": "Vertel wat je van plan bent — volgende week, volgend jaar.",
    "grammar": {
      "title": "Toekomst uitdrukken: futuro vs. presente",
      "body": ("In informeel Italiaans gebruik je voor nabije toekomst vaak de tegenwoordige tijd: "
               "'Domani vado al mare' = Morgen ga ik naar het strand. "
               "Het futuro semplice gebruik je voor verdere toekomst of beloften: "
               "'L'anno prossimo andrò in Spagna' = Volgend jaar ga ik naar Spanje. "
               "'Penso di' + infinitief = ik ben van plan om: 'Penso di comprare una macchina'.")
    },
    "words": [f"w{745+i}" for i in range(8)]
  },
  {
    "id": 95, "title": "Op de markt", "emoji": "🧺", "level": "A2",
    "description": "Koop vers voedsel, vraag om het gewicht en onderhandel over de prijs.",
    "grammar": {
      "title": "Hoeveelheden en gewichten",
      "body": ("'Un chilo di...' = een kilo... 'Un etto di...' = 100 gram... (etto = hectogram, typisch Italiaans). "
               "'Un litro di latte' = een liter melk. 'Mezzo chilo' = een halve kilo. "
               "'Quanto costa?' = hoeveel kost het? 'Me ne dia due etti' = geeft u me 200 gram. "
               "Op Italiaanse markten is 'un etto' de standaardmaat voor kaas en vleeswaren.")
    },
    "words": [f"w{753+i}" for i in range(8)]
  },
  {
    "id": 96, "title": "Koken & recepten", "emoji": "👨‍🍳", "level": "A2",
    "description": "Volg een eenvoudig recept en bespreek ingrediënten en bereidingswijzen.",
    "grammar": {
      "title": "De imperatief in recepten",
      "body": ("Recepten gebruiken de imperatief (gebiedende wijs): "
               "'Taglia la cipolla' = snijd de ui. 'Aggiungi l'olio' = voeg olie toe. "
               "'Mescola bene' = meng goed. 'Cuoci per 20 minuti' = kook 20 minuten. "
               "Kooktermen zijn ook in informele gesprekken handig: 'Come lo fai il sugo?' = Hoe maak jij de saus?")
    },
    "words": [f"w{761+i}" for i in range(8)]
  },
  {
    "id": 97, "title": "Bioscoop & uitgaan", "emoji": "🎬", "level": "A2",
    "description": "Kies een film, koop kaartjes en bespreek wat je hebt gezien.",
    "grammar": {
      "title": "Meningen geven over films en voorstellingen",
      "body": ("'Mi è piaciuto molto' = ik vond het erg leuk (mannelijk/onzijdig). "
               "'Mi è piaciuta molto' = ik vond het erg leuk (vrouwelijk). "
               "'Che film c'è stasera?' = welke film draait er vanavond? "
               "'È già tutto esaurito' = het is al uitverkocht. "
               "'Preferisco i film in lingua originale' = ik geef de voorkeur aan films in de originele taal.")
    },
    "words": [f"w{769+i}" for i in range(8)]
  },
  {
    "id": 98, "title": "Vrienden & sociale plannen", "emoji": "👫", "level": "A2",
    "description": "Spreek af met vrienden, nodig iemand uit en bespreek wat je hebt gedaan.",
    "grammar": {
      "title": "Uitnodigen en reageren",
      "body": ("'Ti va di venire a cena da me?' = Heb je zin om bij mij te komen eten? "
               "'Con piacere!' = met plezier! 'Purtroppo non posso' = helaas kan ik niet. "
               "'Ci penso e ti faccio sapere' = ik denk erover na en laat je weten. "
               "'Porta qualcosa da bere' = neem iets te drinken mee. "
               "Sociale uitnodigingen zijn cruciaal in de Italiaanse cultuur.")
    },
    "words": [f"w{777+i}" for i in range(8)]
  },
  {
    "id": 99, "title": "Huis zoeken & huren", "emoji": "🏠", "level": "A2",
    "description": "Zoek een appartement, vraag naar huurprijs en beschrijf je wensen.",
    "grammar": {
      "title": "Beschrijven van woningen",
      "body": ("'Cerco un appartamento in affitto' = ik zoek een huurappartement. "
               "'Quante camere ha?' = hoeveel kamers heeft het? "
               "'È ammobiliato?' = is het gemeubileerd? "
               "'Il canone d'affitto' = de huurprijs. 'Le spese sono incluse?' = zijn de kosten inbegrepen? "
               "Italianen wonen vaak in appartementen — 'condominio' = appartementencomplex.")
    },
    "words": [f"w{785+i}" for i in range(8)]
  },
  {
    "id": 100, "title": "🎉 100 lessen!", "emoji": "🏆", "level": "A2",
    "description": "Gefeliciteerd met 100 lessen! Een bijzondere mijlpaal — bespreek je prestaties.",
    "grammar": {
      "title": "Trots zijn — complimenten geven en ontvangen",
      "body": ("'Ce l'ho fatta!' = het is me gelukt! 'Sono orgoglioso/a di me' = ik ben trots op mezelf. "
               "'Complimenti!' = gefeliciteerd! 'Sei bravissimo/a!' = je bent heel goed! "
               "'Ho imparato tantissimo' = ik heb heel veel geleerd. "
               "Je beheerst nu 800 Italiaanse woorden en hebt 100 lessen afgerond. "
               "Cento lezioni — un traguardo straordinario! 🇮🇹🏆")
    },
    "words": [f"w{793+i}" for i in range(8)]
  },
  {
    "id": 101, "title": "Bij de bank", "emoji": "🏦", "level": "A2",
    "description": "Open een rekening, wissel geld en begrijp bankterminologie.",
    "grammar": {
      "title": "Bankzaken in Italië",
      "body": ("'Vorrei aprire un conto corrente' = ik zou een betaalrekening willen openen. "
               "'Posso fare un bonifico?' = kan ik een overboeking doen? "
               "'Il bancomat' = de pinautomaat (ook ATM). 'Prelevare' = geld opnemen. "
               "'Versare' = storten. 'Il saldo' = het saldo. "
               "In Italië betaalt men vaak contant — 'Si paga anche con carta?' = kan ik ook met kaart betalen?")
    },
    "words": [f"w{801+i}" for i in range(8)]
  },
  {
    "id": 102, "title": "Feestjes & gelegenheden", "emoji": "🎉", "level": "A2",
    "description": "Vier verjaardagen, bruiloften en Italiaanse festiviteiten.",
    "grammar": {
      "title": "Wensen en gelukwensen",
      "body": ("'Auguri!' = gefeliciteerd! / veel geluk! (meest gebruikte gelukwens). "
               "'Tanti auguri di buon compleanno!' = veel felicitaties voor je verjaardag! "
               "'Buon anniversario!' = gelukkige verjaardag (van een evenement). "
               "'Cin cin!' = proost! 'Alla salute!' = op de gezondheid! "
               "'Auguri' is universeel in Italië — voor verjaardagen, Kerst, Pasen én herstellen.")
    },
    "words": [f"w{809+i}" for i in range(8)]
  },
  {
    "id": 103, "title": "Klachten & problemen", "emoji": "😤", "level": "A2",
    "description": "Dien een klacht in, beschrijf een probleem en vraag om oplossingen.",
    "grammar": {
      "title": "Een klacht uiten — beleefd maar duidelijk",
      "body": ("'C'è un problema con...' = er is een probleem met... "
               "'Non funziona' = het werkt niet. 'È rotto/a' = het is kapot. "
               "'Vorrei parlare con il responsabile' = ik zou de manager willen spreken. "
               "'Chiedo un rimborso' = ik vraag om terugbetaling. "
               "In Italië is beleefd maar vasthoudend het meest effectief bij klachten.")
    },
    "words": [f"w{817+i}" for i in range(8)]
  },
  {
    "id": 104, "title": "Beschrijven van mensen", "emoji": "👤", "level": "A2",
    "description": "Beschrijf het uiterlijk en de persoonlijkheid van mensen gedetailleerder.",
    "grammar": {
      "title": "Bijvoeglijke naamwoorden voor uiterlijk",
      "body": ("Bijvoeglijke naamwoorden passen aan op geslacht en getal. "
               "'Ha i capelli corti e ricci' = hij/zij heeft kort krullend haar. "
               "'È di media altezza' = hij/zij is van gemiddelde lengte. "
               "'Porta gli occhiali' = hij/zij draagt een bril. "
               "'Sembra simpatico/a' = hij/zij lijkt aardig. 'Sembra' (lijken) + bijvoeglijk naamwoord = indruk beschrijven.")
    },
    "words": [f"w{825+i}" for i in range(8)]
  },
  {
    "id": 105, "title": "Reizen plannen", "emoji": "✈️", "level": "A2",
    "description": "Plan een reis, boek vervoer en accommodatie, maak een reisschema.",
    "grammar": {
      "title": "Toekomst met 'ho intenzione di' en 'penso di'",
      "body": ("'Ho intenzione di' + infinitief = ik ben van plan om (concreet plan). "
               "'Penso di' + infinitief = ik denk erover om (minder zeker). "
               "'Ho intenzione di visitare Firenze' = ik ben van plan Florence te bezoeken. "
               "'Penso di partire in agosto' = ik denk erover om in augustus te vertrekken. "
               "'Spero di' + infinitief = ik hoop om: 'Spero di trovare un buon albergo'.")
    },
    "words": [f"w{833+i}" for i in range(8)]
  },
  {
    "id": 106, "title": "Vervoer & mobiliteit", "emoji": "🚇", "level": "A2",
    "description": "Navigeer door Italiaanse steden met metro, bus en tram.",
    "grammar": {
      "title": "Vervoer — kaartjes en routebeschrijving",
      "body": ("'Devo prendere la metropolitana' = ik moet de metro nemen. "
               "'Devo cambiare alla stazione centrale' = ik moet overstappen op het centraal station. "
               "'Quante fermate?' = hoeveel haltes? 'È diretto?' = is het een directe verbinding? "
               "'Il prossimo treno parte alle...' = de volgende trein vertrekt om... "
               "Italië heeft uitstekend openbaar vervoer — 'Trenitalia' en 'Italo' zijn de twee hoofdaanbieders.")
    },
    "words": [f"w{841+i}" for i in range(8)]
  },
  {
    "id": 107, "title": "Spijt & wensen", "emoji": "😔", "level": "A2",
    "description": "Druk spijt uit over het verleden en wensen voor de toekomst.",
    "grammar": {
      "title": "Spijt uitdrukken: avrei dovuto, mi dispiace",
      "body": ("'Mi dispiace' = het spijt me / wat jammer. 'Peccato!' = wat jammer! "
               "'Avrei dovuto' + infinitief = ik had moeten (conditionele verleden): 'Avrei dovuto studiare di più'. "
               "'Se potessi...' = als ik kon... (herkenning). "
               "'Vorrei essere stato/a' = ik had willen zijn — je kunt ook simpeler: 'Avrei voluto...' = ik had willen...")
    },
    "words": [f"w{849+i}" for i in range(8)]
  },
  {
    "id": 108, "title": "Culinaire tradities", "emoji": "🍝", "level": "A2",
    "description": "Ontdek de rijke Italiaanse keuken — regionale gerechten en tradities.",
    "grammar": {
      "title": "Regionale verschillen in Italië",
      "body": ("Italië heeft sterk regionale keuken: Noord (rijst, polenta, boter), Midden (pasta, olijfolie), Zuid (tomaat, aubergine). "
               "'È tipico della regione' = het is typisch voor de regio. "
               "'Si mangia molto' + gerecht + 'in' + regio. "
               "'La cucina italiana' verschilt enorm per regio — 'ogni campanile ha la sua ricetta' = elk dorp heeft zijn eigen recept.")
    },
    "words": [f"w{857+i}" for i in range(8)]
  },
  {
    "id": 109, "title": "Gezondheid & leefstijl", "emoji": "🥗", "level": "A2",
    "description": "Praat over gezonde gewoonten, voeding en je leefstijl.",
    "grammar": {
      "title": "Frequentie uitdrukken",
      "body": ("'Ogni giorno' = elke dag. 'Due volte alla settimana' = twee keer per week. "
               "'Una volta al mese' = één keer per maand. 'Di tanto in tanto' = van tijd tot tijd. "
               "'Non... mai' = nooit: 'Non fumo mai'. 'Raramente' = zelden. 'Spesso' = vaak. "
               "Frequentie-uitdrukkingen zijn handig voor het beschrijven van gewoonten en routines.")
    },
    "words": [f"w{865+i}" for i in range(8)]
  },
  {
    "id": 110, "title": "Sport & outdoor", "emoji": "⛰️", "level": "A2",
    "description": "Praat over sport, outdoor-activiteiten en Italiaanse sportcultuur.",
    "grammar": {
      "title": "Giocare vs. fare — sport uitdrukken",
      "body": ("'Giocare a' + balsport: 'giocare a calcio/tennis/pallavolo'. "
               "'Fare' + andere sport: 'fare nuoto/ciclismo/corsa/yoga'. "
               "'Tifare per' = supporter zijn van: 'Tifo per la Juventus'. "
               "'La Serie A' = de Italiaanse voetbalcompetitie. Het calcio (voetbal) is een nationale passie — "
               "ook als je het niet volgt, is het een cruciaal gespreksonderwerp!")
    },
    "words": [f"w{873+i}" for i in range(8)]
  },
  {
    "id": 111, "title": "Winkelen & mode", "emoji": "👗", "level": "A2",
    "description": "Koop kleding, vraag om een andere maat en bespreek stijl en mode.",
    "grammar": {
      "title": "Passen en maten in Italië",
      "body": ("'Posso provarlo/a?' = mag ik het passen? 'Dov'è il camerino?' = waar is de paskamer? "
               "'Ce l'avete in taglia più grande?' = heeft u het in een grotere maat? "
               "'Questo mi sta bene?' = staat dit me goed? 'Mi sta un po' stretto' = het zit me een beetje te strak. "
               "Italiaanse maten verschillen van Nederlandse — controleer altijd de maattabel.")
    },
    "words": [f"w{881+i}" for i in range(8)]
  },
  {
    "id": 112, "title": "Technologie & internet", "emoji": "💻", "level": "A2",
    "description": "Praat over smartphones, apps en het digitale leven.",
    "grammar": {
      "title": "Technologisch woordenschat in Italiaans",
      "body": ("Veel technologische termen zijn Engels in Italiaans: 'il click', 'il file', 'lo smartphone'. "
               "Anderen zijn geïtalianiseerd: 'scaricare' = downloaden, 'caricare' = uploaden/opladen. "
               "'Mandare un messaggio' = een bericht sturen. 'Condividere' = delen. "
               "'La connessione' = de verbinding. 'Il WiFi' = wifi (uitgesproken als 'wi-fi'). "
               "Jongere Italianen gebruiken veel Engelse technologietermen direct.")
    },
    "words": [f"w{889+i}" for i in range(8)]
  },
  {
    "id": 113, "title": "Het weer & de natuur", "emoji": "🌦️", "level": "A2",
    "description": "Beschrijf het weer uitgebreider en praat over de Italiaanse natuur.",
    "grammar": {
      "title": "Weersomstandigheden — gevorderde uitdrukkingen",
      "body": ("'Che tempo fa?' = hoe is het weer? (standaardvraag). "
               "'C'è la nebbia' = het is mistig. 'Tira vento' = het waait. 'Grandina' = het hagelt. "
               "'Un temporale' = een onweersbui. 'È afoso' = het is drukkend/benauwd. "
               "Noordelijk Italië is bekend om mist ('la pianura padana'), het zuiden om droogte ('la siccità'). "
               "Het klimaat varieert enorm — van Alpijnse sneeuw tot mediterrane warmte.")
    },
    "words": [f"w{897+i}" for i in range(8)]
  },
  {
    "id": 114, "title": "Werk & loopbaan", "emoji": "💼", "level": "A2",
    "description": "Solliciteer, beschrijf je werkervaring en praat over je carrière.",
    "grammar": {
      "title": "Werkervaring beschrijven — ho lavorato come...",
      "body": ("'Lavoro come' + beroep = ik werk als... 'Ho lavorato per' + bedrijf = ik heb gewerkt voor... "
               "'Ho X anni di esperienza' = ik heb X jaar ervaring. "
               "'Sono disponibile a' + infinitief = ik ben beschikbaar om... "
               "'Cerco un impiego' = ik zoek een baan. 'Un colloquio di lavoro' = een sollicitatiegesprek. "
               "Italië heeft een sterke kleine-ondernemerscultuur — 'lavorare in proprio' = voor jezelf werken.")
    },
    "words": [f"w{905+i}" for i in range(8)]
  },
  {
    "id": 115, "title": "Kunst & musea", "emoji": "🎨", "level": "A2",
    "description": "Bezoek een Italiaans museum, bespreek kunstwerken en culturele schatten.",
    "grammar": {
      "title": "Musea en kunstwerken bespreken",
      "body": ("'Questo quadro mi colpisce molto' = dit schilderij treft me heel erg. "
               "'È stato dipinto da' + kunstenaar = het is geschilderd door... "
               "'Risale al' + eeuw/jaar = het dateert uit... 'È esposto al' + museum = het is tentoongesteld in... "
               "Italië heeft meer UNESCO-werelderfgoedsites dan enig ander land. "
               "'Il patrimonio culturale' = het culturele erfgoed — een trots van elke Italiaan.")
    },
    "words": [f"w{913+i}" for i in range(8)]
  },
  {
    "id": 116, "title": "Italiaanse tradities", "emoji": "🎭", "level": "A2",
    "description": "Verken Italiaanse feestdagen, tradities en regionale gewoonten.",
    "grammar": {
      "title": "Feestdagen en tradities uitleggen",
      "body": ("'Si festeggia il...' = men viert het op de... 'È tradizione fare...' = het is traditie om... "
               "'Ferragosto' (15 augustus) = nationale vakantiedag — bijna heel Italië is dicht. "
               "'Capodanno' = Nieuwjaar. 'Pasqua' = Pasen. 'Natale' = Kerstmis. "
               "'La Festa della Repubblica' (2 juni) = nationale feestdag. "
               "Italianen nemen tradities serieus — regionale varianten zijn net zo belangrijk als nationale.")
    },
    "words": [f"w{921+i}" for i in range(8)]
  },
  {
    "id": 117, "title": "Onderwijs & leren", "emoji": "📚", "level": "A2",
    "description": "Praat over school, universiteit en het leren van talen.",
    "grammar": {
      "title": "Het Italiaanse schoolsysteem",
      "body": ("'La scuola elementare' = basisschool (6-11 jaar). 'La scuola media' = middelbare school onderbouw. "
               "'Il liceo' = gymnasium/atheneum. 'L'università' = universiteit. "
               "'Studiare' vs. 'imparare': 'studiare' = studeren/bestuderen, 'imparare' = leren/onthouden. "
               "'Sono iscritto/a all'università' = ik ben ingeschreven aan de universiteit. "
               "Italië heeft veel prestigieuze universiteiten — Bologna (1088) is de oudste ter wereld!")
    },
    "words": [f"w{929+i}" for i in range(8)]
  },
  {
    "id": 118, "title": "Media & nieuws", "emoji": "📰", "level": "A2",
    "description": "Praat over nieuws, sociale media en hoe Italianen informatie consumeren.",
    "grammar": {
      "title": "Nieuws bespreken — meningen over actualiteit",
      "body": ("'Ho sentito che...' = ik heb gehoord dat... 'Secondo le notizie...' = volgens het nieuws... "
               "'È una buona/brutta notizia' = het is goed/slecht nieuws. "
               "'Cosa ne pensi?' = wat denk jij ervan? 'Non sono d'accordo' = ik ben het er niet mee eens. "
               "Italianen volgen nieuws via televisione (RAI is de staatszender), giornali en social media. "
               "'Il TG' (telegiornale) = het journaal.")
    },
    "words": [f"w{937+i}" for i in range(8)]
  },
  {
    "id": 119, "title": "Duurzaamheid & milieu", "emoji": "🌿", "level": "A2",
    "description": "Bespreek milieuvraagstukken en duurzame keuzes in het dagelijks leven.",
    "grammar": {
      "title": "Milieu — actueel woordgebruik",
      "body": ("'Bisogna' + infinitief = het is nodig om / men moet: 'Bisogna riciclare'. "
               "'È importante' + infinitief: 'È importante risparmiare energia'. "
               "'Fare la raccolta differenziata' = afval scheiden (verplicht in Italië). "
               "'Ridurre' = verminderen, 'riusare' = hergebruiken, 'riciclare' = recyclen — le tre R. "
               "Italië heeft strenge recyclingregels — elke gemeente heeft zijn eigen systeem.")
    },
    "words": [f"w{945+i}" for i in range(8)]
  },
  {
    "id": 120, "title": "🎓 A2 afgerond!", "emoji": "🎓", "level": "A2",
    "description": "Je hebt A2 afgerond! Kijk terug op je leertraject en blik vooruit naar B1.",
    "grammar": {
      "title": "Gefeliciteerd — A2 compleet!",
      "body": ("Je beheerst nu ~960 Italiaanse woorden en de basisstructuren van A2. "
               "Je kunt je redden in alledaagse situaties: winkelen, reizen, werk, sociale contacten. "
               "A2 is het niveau waarop je echte gesprekken kunt beginnen met Italianen. "
               "'Sono molto orgoglioso/a di te!' = ik ben heel trots op jou! "
               "Complimenti — sei fantastico/a! De volgende stap is B1: meer nuance, meer grammatica, meer zelfvertrouwen. 🇮🇹🎓")
    },
    "words": [f"w{953+i}" for i in range(8)]
  },
]

# ── Nieuwe woorden (240) ───────────────────────────────────────────────────────
new_words = [
  # Les 91: Tijdsuitdrukkingen verleden
  {"id":"w721","it":"ieri","nl":"gisteren","ph":"ie-ri","ex":"Ieri ho incontrato un vecchio amico.","exNl":"Gisteren ontmoette ik een oude vriend.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w722","it":"l'altro ieri","nl":"eergisteren","ph":"lal-tro ie-ri","ex":"L'altro ieri siamo andati al mare.","exNl":"Eergisteren gingen we naar het strand.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w723","it":"la settimana scorsa","nl":"vorige week","ph":"la set-ti-ma-na skor-sa","ex":"La settimana scorsa ho lavorato molto.","exNl":"Vorige week heb ik veel gewerkt.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w724","it":"il mese scorso","nl":"vorige maand","ph":"il me-ze skor-so","ex":"Il mese scorso sono andato a Venezia.","exNl":"Vorige maand ben ik naar Venetië gegaan.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w725","it":"l'anno scorso","nl":"vorig jaar","ph":"lan-no skor-so","ex":"L'anno scorso ho imparato l'italiano.","exNl":"Vorig jaar heb ik Italiaans geleerd.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w726","it":"fa","nl":"geleden","ph":"fa","ex":"Due anni fa sono stato a Roma.","exNl":"Twee jaar geleden was ik in Rome.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w727","it":"una volta","nl":"ooit / een keer","ph":"u-na vol-ta","ex":"Una volta ho mangiato una pizza enorme.","exNl":"Ooit heb ik een enorme pizza gegeten.","lesson":91,"level":"A2","cat":"tempo_passato"},
  {"id":"w728","it":"nel frattempo","nl":"ondertussen","ph":"nel frat-tem-po","ex":"Nel frattempo, ho preparato la cena.","exNl":"Ondertussen heb ik het avondeten klaargemaakt.","lesson":91,"level":"A2","cat":"tempo_passato"},

  # Les 92: Dagelijkse routine
  {"id":"w729","it":"svegliarsi","nl":"wakker worden","ph":"zve-ljar-si","ex":"Mi sveglio alle sei ogni mattina.","exNl":"Ik word elke ochtend om zes uur wakker.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w730","it":"alzarsi","nl":"opstaan","ph":"al-zar-si","ex":"Mi alzo subito dopo il caffè.","exNl":"Ik sta op direct na de koffie.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w731","it":"lavarsi","nl":"zich wassen","ph":"la-var-si","ex":"Mi lavo la faccia ogni mattina.","exNl":"Ik was mijn gezicht elke ochtend.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w732","it":"vestirsi","nl":"zich aankleden","ph":"ves-tir-si","ex":"Mi vesto velocemente per andare al lavoro.","exNl":"Ik kleed me snel aan om naar het werk te gaan.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w733","it":"fare colazione","nl":"ontbijten","ph":"fa-re ko-la-tsio-ne","ex":"Faccio colazione con un caffè e un cornetto.","exNl":"Ik ontbijt met een koffie en een croissant.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w734","it":"andare al lavoro","nl":"naar het werk gaan","ph":"an-da-re al la-vo-ro","ex":"Vado al lavoro in bicicletta.","exNl":"Ik ga met de fiets naar het werk.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w735","it":"riposarsi","nl":"uitrusten","ph":"ri-po-zar-si","ex":"Mi riposo un po' dopo pranzo.","exNl":"Ik rust even uit na de lunch.","lesson":92,"level":"A2","cat":"routine"},
  {"id":"w736","it":"addormentarsi","nl":"in slaap vallen","ph":"ad-dor-men-tar-si","ex":"Mi addormento sempre prima di mezzanotte.","exNl":"Ik val altijd voor middernacht in slaap.","lesson":92,"level":"A2","cat":"routine"},

  # Les 93: Afspraken maken
  {"id":"w737","it":"appuntamento","nl":"afspraak","ph":"ap-pun-ta-men-to","ex":"Ho un appuntamento dal dentista alle tre.","exNl":"Ik heb een afspraak bij de tandarts om drie uur.","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w738","it":"fissare","nl":"vastleggen / afspreken","ph":"fis-sa-re","ex":"Possiamo fissare un appuntamento per domani?","exNl":"Kunnen we morgen een afspraak vastleggen?","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w739","it":"libero","nl":"vrij / beschikbaar","ph":"li-be-ro","ex":"Sono libera venerdì sera.","exNl":"Ik ben vrijdagavond vrij.","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w740","it":"ti va di","nl":"heb je zin om","ph":"ti va di","ex":"Ti va di andare a cena insieme stasera?","exNl":"Heb je zin om vanavond samen uit eten te gaan?","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w741","it":"purtroppo","nl":"helaas","ph":"pur-trop-po","ex":"Purtroppo non posso venire alla festa.","exNl":"Helaas kan ik niet naar het feest komen.","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w742","it":"rimandare","nl":"uitstellen","ph":"ri-man-da-re","ex":"Dobbiamo rimandare la riunione a domani.","exNl":"We moeten de vergadering tot morgen uitstellen.","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w743","it":"disdire","nl":"afzeggen","ph":"dis-di-re","ex":"Ho dovuto disdire l'appuntamento.","exNl":"Ik moest de afspraak afzeggen.","lesson":93,"level":"A2","cat":"appuntamenti"},
  {"id":"w744","it":"ci vediamo","nl":"we zien elkaar","ph":"tsi ve-dia-mo","ex":"Ci vediamo domani alle dieci!","exNl":"We zien elkaar morgen om tien uur!","lesson":93,"level":"A2","cat":"appuntamenti"},

  # Les 94: Plannen voor de toekomst
  {"id":"w745","it":"avere intenzione di","nl":"van plan zijn om","ph":"a-ve-re in-ten-tsio-ne di","ex":"Ho intenzione di imparare il cinese.","exNl":"Ik ben van plan Chinees te leren.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w746","it":"sognare di","nl":"dromen van","ph":"so-nja-re di","ex":"Sogno di vivere in Italia un giorno.","exNl":"Ik droom ervan om ooit in Italië te wonen.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w747","it":"il prossimo anno","nl":"volgend jaar","ph":"il pros-si-mo an-no","ex":"Il prossimo anno mi sposo.","exNl":"Volgend jaar ga ik trouwen.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w748","it":"tra poco","nl":"over een tijdje / straks","ph":"tra po-ko","ex":"Tra poco andiamo a mangiare.","exNl":"Straks gaan we eten.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w749","it":"prima o poi","nl":"vroeg of laat","ph":"pri-ma o poi","ex":"Prima o poi visiterò tutta l'Italia.","exNl":"Vroeg of laat bezoek ik heel Italië.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w750","it":"in futuro","nl":"in de toekomst","ph":"in fu-tu-ro","ex":"In futuro vorrei cambiare lavoro.","exNl":"In de toekomst wil ik van baan veranderen.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w751","it":"risparmiare","nl":"sparen","ph":"ris-par-mia-re","ex":"Sto risparmiando per comprare una casa.","exNl":"Ik spaar om een huis te kopen.","lesson":94,"level":"A2","cat":"progetti"},
  {"id":"w752","it":"raggiungere","nl":"bereiken / halen","ph":"rad-dzhun-dzhre","ex":"Voglio raggiungere il mio obiettivo.","exNl":"Ik wil mijn doel bereiken.","lesson":94,"level":"A2","cat":"progetti"},

  # Les 95: Op de markt
  {"id":"w753","it":"il mercato","nl":"de markt","ph":"il mer-ka-to","ex":"Il sabato vado sempre al mercato.","exNl":"Op zaterdag ga ik altijd naar de markt.","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w754","it":"un etto","nl":"100 gram (een ons)","ph":"un et-to","ex":"Mi dà due etti di prosciutto?","exNl":"Kunt u mij 200 gram ham geven?","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w755","it":"fresco","nl":"vers","ph":"fres-ko","ex":"Questo pesce è freschissimo.","exNl":"Deze vis is heel vers.","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w756","it":"stagionale","nl":"seizoensgebonden","ph":"sta-dzho-na-le","ex":"Compro solo verdura stagionale.","exNl":"Ik koop alleen seizoensgebonden groenten.","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w757","it":"il venditore","nl":"de verkoper","ph":"il ven-di-to-re","ex":"Il venditore mi ha dato uno sconto.","exNl":"De verkoper gaf me een korting.","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w758","it":"pesare","nl":"wegen","ph":"pe-za-re","ex":"Può pesare questi pomodori?","exNl":"Kunt u deze tomaten wegen?","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w759","it":"il resto","nl":"het wisselgeld","ph":"il res-to","ex":"Il resto è per lei.","exNl":"Het wisselgeld is voor u.","lesson":95,"level":"A2","cat":"mercato2"},
  {"id":"w760","it":"biologico","nl":"biologisch","ph":"bio-lo-dzji-ko","ex":"Preferisco la frutta biologica.","exNl":"Ik geef de voorkeur aan biologisch fruit.","lesson":95,"level":"A2","cat":"mercato2"},

  # Les 96: Koken & recepten
  {"id":"w761","it":"la ricetta","nl":"het recept","ph":"la ri-tjet-ta","ex":"Hai la ricetta della carbonara?","exNl":"Heb jij het recept voor carbonara?","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w762","it":"tagliare","nl":"snijden","ph":"ta-lja-re","ex":"Taglia la cipolla a pezzetti.","exNl":"Snijd de ui in kleine stukjes.","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w763","it":"mescolare","nl":"mengen / roeren","ph":"mes-ko-la-re","ex":"Mescola bene gli ingredienti.","exNl":"Meng de ingrediënten goed.","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w764","it":"aggiungere","nl":"toevoegen","ph":"ad-dzhun-dzhre","ex":"Aggiungi un pizzico di sale.","exNl":"Voeg een snufje zout toe.","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w765","it":"cuocere","nl":"koken / garen","ph":"kwo-tsjere","ex":"Cuoci la pasta per dieci minuti.","exNl":"Kook de pasta tien minuten.","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w766","it":"la padella","nl":"de koekenpan","ph":"la pa-del-la","ex":"Scalda l'olio nella padella.","exNl":"Verwarm de olie in de koekenpan.","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w767","it":"il forno","nl":"de oven","ph":"il for-no","ex":"Metti la pizza in forno a 200 gradi.","exNl":"Zet de pizza in de oven op 200 graden.","lesson":96,"level":"A2","cat":"cucina2"},
  {"id":"w768","it":"assaggiare","nl":"proeven","ph":"as-sad-dzhare","ex":"Assaggia e aggiusta di sale.","exNl":"Proef en stel bij met zout.","lesson":96,"level":"A2","cat":"cucina2"},

  # Les 97: Bioscoop & uitgaan
  {"id":"w769","it":"il cinema","nl":"de bioscoop","ph":"il tji-ne-ma","ex":"Andiamo al cinema questo weekend?","exNl":"Gaan we dit weekend naar de bioscoop?","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w770","it":"il film","nl":"de film","ph":"il film","ex":"Hai già visto questo film?","exNl":"Heb jij deze film al gezien?","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w771","it":"il biglietto","nl":"het kaartje","ph":"il bi-ljet-to","ex":"Ho comprato due biglietti online.","exNl":"Ik heb twee kaartjes online gekocht.","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w772","it":"la trama","nl":"het verhaal / de plot","ph":"la tra-ma","ex":"La trama del film è molto originale.","exNl":"Het verhaal van de film is heel origineel.","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w773","it":"recitare","nl":"acteren / spelen","ph":"re-tshi-ta-re","ex":"L'attore recita benissimo.","exNl":"De acteur speelt uitstekend.","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w774","it":"doppiato","nl":"nagesynchroniseerd","ph":"dop-pia-to","ex":"In Italia quasi tutti i film sono doppiati.","exNl":"In Italië zijn bijna alle films nagesynchroniseerd.","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w775","it":"mi è piaciuto","nl":"ik vond het leuk","ph":"mi è pia-tsjiu-to","ex":"Mi è piaciuto molto il finale.","exNl":"Ik vond het einde erg leuk.","lesson":97,"level":"A2","cat":"cinema"},
  {"id":"w776","it":"emozionante","nl":"aangrijpend / spannend","ph":"e-mo-tsio-nan-te","ex":"È stato uno spettacolo emozionante.","exNl":"Het was een aangrijpende voorstelling.","lesson":97,"level":"A2","cat":"cinema"},

  # Les 98: Vrienden & sociale plannen
  {"id":"w777","it":"il/la migliore amico/a","nl":"de beste vriend(in)","ph":"il mi-ljore a-mi-ko","ex":"Il mio migliore amico abita a Milano.","exNl":"Mijn beste vriend woont in Milaan.","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w778","it":"uscire insieme","nl":"samen uitgaan","ph":"u-sjire in-sie-me","ex":"Usciamo insieme stasera?","exNl":"Gaan we vanavond samen uit?","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w779","it":"invitare","nl":"uitnodigen","ph":"in-vi-ta-re","ex":"Ho invitato tutti i miei amici alla festa.","exNl":"Ik heb al mijn vrienden voor het feest uitgenodigd.","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w780","it":"la compagnia","nl":"het gezelschap","ph":"la kom-pa-nia","ex":"Mi piace la tua compagnia.","exNl":"Ik vind jouw gezelschap prettig.","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w781","it":"fare due chiacchiere","nl":"een praatje maken","ph":"fa-re due kiak-kiere","ex":"Vieni a fare due chiacchiere da me?","exNl":"Kom je bij mij een praatje maken?","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w782","it":"il ritrovo","nl":"de ontmoetingsplek","ph":"il ri-tro-vo","ex":"Il bar è il nostro ritrovo abituale.","exNl":"Het café is onze gebruikelijke ontmoetingsplek.","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w783","it":"divertirsi","nl":"zich amuseren / plezier hebben","ph":"di-ver-tir-si","ex":"Ci siamo divertiti tantissimo!","exNl":"We hebben ons heel erg geamuseerd!","lesson":98,"level":"A2","cat":"amici"},
  {"id":"w784","it":"stare in compagnia","nl":"gezelschap houden","ph":"sta-re in kom-pa-nia","ex":"Mi piace stare in compagnia degli amici.","exNl":"Ik vind het fijn om bij vrienden te zijn.","lesson":98,"level":"A2","cat":"amici"},

  # Les 99: Huis zoeken & huren
  {"id":"w785","it":"l'appartamento in affitto","nl":"het huurappartement","ph":"lap-par-ta-men-to in af-fit-to","ex":"Cerco un appartamento in affitto in centro.","exNl":"Ik zoek een huurappartement in het centrum.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w786","it":"il canone","nl":"de huurprijs","ph":"il ka-no-ne","ex":"Il canone d'affitto è di 800 euro al mese.","exNl":"De huurprijs is 800 euro per maand.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w787","it":"ammobiliato","nl":"gemeubileerd","ph":"am-mo-bi-lja-to","ex":"L'appartamento è completamente ammobiliato.","exNl":"Het appartement is volledig gemeubileerd.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w788","it":"le spese","nl":"de kosten / bijkomende kosten","ph":"le spe-ze","ex":"Le spese condominiali sono incluse.","exNl":"De servicekosten zijn inbegrepen.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w789","it":"il contratto","nl":"het contract","ph":"il kon-trat-to","ex":"Ho firmato il contratto di affitto.","exNl":"Ik heb het huurcontract getekend.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w790","it":"il proprietario","nl":"de eigenaar / verhuurder","ph":"il pro-prie-ta-rio","ex":"Il proprietario abita al piano di sotto.","exNl":"De verhuurder woont op de verdieping eronder.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w791","it":"la cauzione","nl":"de borg","ph":"la kau-tsio-ne","ex":"Ho pagato due mesi di cauzione.","exNl":"Ik heb twee maanden borg betaald.","lesson":99,"level":"A2","cat":"casa2"},
  {"id":"w792","it":"traslocare","nl":"verhuizen","ph":"tras-lo-ka-re","ex":"Il mese prossimo trasloco in un nuovo appartamento.","exNl":"Volgende maand verhuis ik naar een nieuw appartement.","lesson":99,"level":"A2","cat":"casa2"},

  # Les 100: 100 lessen!
  {"id":"w793","it":"il traguardo","nl":"de mijlpaal / de finish","ph":"il tra-gwar-do","ex":"Raggiungere 100 lezioni è un grande traguardo!","exNl":"100 lessen halen is een grote mijlpaal!","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w794","it":"i progressi","nl":"de vooruitgang","ph":"i pro-gres-si","ex":"Ho fatto grandi progressi nell'italiano.","exNl":"Ik heb grote vooruitgang geboekt in het Italiaans.","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w795","it":"migliorare","nl":"verbeteren","ph":"mi-ljora-re","ex":"Ogni giorno miglioro il mio italiano.","exNl":"Elke dag verbeter ik mijn Italiaans.","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w796","it":"impegnarsi","nl":"zich inzetten","ph":"im-pe-njar-si","ex":"Mi sono impegnato molto per arrivare fin qui.","exNl":"Ik heb me erg ingezet om hier te komen.","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w797","it":"la costanza","nl":"de volharding","ph":"la kos-tan-tsa","ex":"La costanza è la chiave del successo.","exNl":"Volharding is de sleutel tot succes.","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w798","it":"essere orgoglioso di","nl":"trots zijn op","ph":"es-sere or-gol-joso di","ex":"Sono orgoglioso di me stesso!","exNl":"Ik ben trots op mezelf!","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w799","it":"continuare","nl":"doorgaan / verdergaan","ph":"kon-ti-nu-are","ex":"Continua così — stai andando benissimo!","exNl":"Ga zo door — je doet het uitstekend!","lesson":100,"level":"A2","cat":"ripasso"},
  {"id":"w800","it":"fantastico","nl":"fantastisch","ph":"fan-tas-ti-ko","ex":"Hai fatto qualcosa di fantastico!","exNl":"Je hebt iets fantastisch gedaan!","lesson":100,"level":"A2","cat":"ripasso"},

  # Les 101: Bij de bank
  {"id":"w801","it":"il conto corrente","nl":"de betaalrekening","ph":"il kon-to kor-ren-te","ex":"Voglio aprire un conto corrente.","exNl":"Ik wil een betaalrekening openen.","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w802","it":"prelevare","nl":"geld opnemen","ph":"pre-le-va-re","ex":"Ho prelevato 200 euro dal bancomat.","exNl":"Ik heb 200 euro opgenomen van de geldautomaat.","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w803","it":"versare","nl":"storten","ph":"ver-sa-re","ex":"Ho versato lo stipendio in banca.","exNl":"Ik heb het salaris op de bank gestort.","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w804","it":"il bonifico","nl":"de overboeking","ph":"il bo-ni-fi-ko","ex":"Ho fatto un bonifico al mio padrone di casa.","exNl":"Ik heb een overboeking gedaan naar mijn verhuurder.","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w805","it":"il saldo","nl":"het saldo","ph":"il sal-do","ex":"Qual è il saldo del mio conto?","exNl":"Wat is het saldo van mijn rekening?","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w806","it":"la carta di credito","nl":"de creditcard","ph":"la kar-ta di kre-di-to","ex":"Posso pagare con la carta di credito?","exNl":"Kan ik betalen met de creditcard?","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w807","it":"il tasso di interesse","nl":"de rente","ph":"il tas-so di in-te-res-se","ex":"Il tasso di interesse è molto basso ora.","exNl":"De rente is nu heel laag.","lesson":101,"level":"A2","cat":"banca"},
  {"id":"w808","it":"lo sportello","nl":"het loket","ph":"lo spor-tel-lo","ex":"Mi rivolgo allo sportello per informazioni.","exNl":"Ik wend me tot het loket voor informatie.","lesson":101,"level":"A2","cat":"banca"},

  # Les 102: Feestjes & gelegenheden
  {"id":"w809","it":"auguri","nl":"gefeliciteerd / veel geluk","ph":"au-gu-ri","ex":"Tanti auguri per il tuo compleanno!","exNl":"Veel felicitaties voor je verjaardag!","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w810","it":"festeggiare","nl":"vieren","ph":"fes-ted-dzhare","ex":"Festeggiamo il tuo successo stasera!","exNl":"We vieren vanavond jouw succes!","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w811","it":"il regalo","nl":"het cadeau","ph":"il re-ga-lo","ex":"Ho comprato un bel regalo per mia madre.","exNl":"Ik heb een mooi cadeau voor mijn moeder gekocht.","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w812","it":"brindare","nl":"toasten / klinken","ph":"brin-da-re","ex":"Brindano alla salute degli sposi.","exNl":"Ze toasten op de gezondheid van de bruid en bruidegom.","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w813","it":"il matrimonio","nl":"het huwelijk / de bruiloft","ph":"il ma-tri-mo-nio","ex":"Siamo stati invitati al matrimonio di Anna.","exNl":"We zijn uitgenodigd voor de bruiloft van Anna.","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w814","it":"la cerimonia","nl":"de ceremonie","ph":"la tshe-ri-mo-nia","ex":"La cerimonia si svolge in chiesa.","exNl":"De ceremonie vindt plaats in de kerk.","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w815","it":"organizzare","nl":"organiseren","ph":"or-ga-nid-dza-re","ex":"Ho organizzato una festa a sorpresa.","exNl":"Ik heb een verrassingsfeest georganiseerd.","lesson":102,"level":"A2","cat":"feste"},
  {"id":"w816","it":"cin cin","nl":"proost","ph":"tshin tshin","ex":"Cin cin! Alla salute di tutti!","exNl":"Proost! Op ieders gezondheid!","lesson":102,"level":"A2","cat":"feste"},

  # Les 103: Klachten & problemen
  {"id":"w817","it":"reclamare","nl":"klagen / reclameren","ph":"re-kla-ma-re","ex":"Ho dovuto reclamare per il servizio scadente.","exNl":"Ik moest klagen over de slechte service.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w818","it":"non funziona","nl":"het werkt niet","ph":"non fun-tsio-na","ex":"Il riscaldamento non funziona da tre giorni.","exNl":"De verwarming werkt al drie dagen niet.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w819","it":"il guasto","nl":"de storing / het defect","ph":"il gwas-to","ex":"C'è un guasto alla lavatrice.","exNl":"Er is een defect aan de wasmachine.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w820","it":"chiedere un rimborso","nl":"om terugbetaling vragen","ph":"kje-dere un rim-bor-so","ex":"Voglio chiedere un rimborso completo.","exNl":"Ik wil om volledige terugbetaling vragen.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w821","it":"il responsabile","nl":"de verantwoordelijke / de manager","ph":"il res-pon-sa-bi-le","ex":"Vorrei parlare con il responsabile.","exNl":"Ik zou de manager willen spreken.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w822","it":"insoddisfatto","nl":"ontevreden","ph":"in-sod-dis-fat-to","ex":"Sono insoddisfatto del servizio ricevuto.","exNl":"Ik ben ontevreden over de ontvangen service.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w823","it":"risolvere","nl":"oplossen","ph":"ri-zol-vere","ex":"Dobbiamo risolvere questo problema subito.","exNl":"We moeten dit probleem direct oplossen.","lesson":103,"level":"A2","cat":"lamentele"},
  {"id":"w824","it":"la garanzia","nl":"de garantie","ph":"la ga-ran-tsia","ex":"Il prodotto è ancora in garanzia.","exNl":"Het product is nog onder garantie.","lesson":103,"level":"A2","cat":"lamentele"},

  # Les 104: Beschrijven van mensen
  {"id":"w825","it":"i capelli","nl":"het haar","ph":"i ka-pel-li","ex":"Ha i capelli lunghi e ricci.","exNl":"Ze heeft lang krullend haar.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w826","it":"la barba","nl":"de baard","ph":"la bar-ba","ex":"Ha una barba corta e curata.","exNl":"Hij heeft een korte, verzorgde baard.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w827","it":"di media altezza","nl":"van gemiddelde lengte","ph":"di me-dia al-tez-za","ex":"È di media altezza, circa 1,75.","exNl":"Hij is van gemiddelde lengte, ongeveer 1,75.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w828","it":"robusto","nl":"stevig gebouwd","ph":"ro-bus-to","ex":"È un uomo robusto e sportivo.","exNl":"Hij is een stevige, sportieve man.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w829","it":"gli occhiali","nl":"de bril","ph":"li ok-kja-li","ex":"Porta gli occhiali da quando era piccolo.","exNl":"Hij draagt een bril sinds hij klein was.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w830","it":"sembrare","nl":"lijken / eruitzien als","ph":"sem-bra-re","ex":"Sembra molto più giovane della sua età.","exNl":"Hij/zij lijkt veel jonger dan zijn/haar leeftijd.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w831","it":"somigliare a","nl":"lijken op","ph":"so-mi-lja-re a","ex":"Somiglia molto a sua madre.","exNl":"Ze lijkt veel op haar moeder.","lesson":104,"level":"A2","cat":"persone"},
  {"id":"w832","it":"la carnagione","nl":"het huidskleur","ph":"la kar-na-dzho-ne","ex":"Ha la carnagione chiara e gli occhi azzurri.","exNl":"Ze heeft een lichte huidskleur en blauwe ogen.","lesson":104,"level":"A2","cat":"persone"},

  # Les 105: Reizen plannen
  {"id":"w833","it":"prenotare","nl":"reserveren / boeken","ph":"pre-no-ta-re","ex":"Ho prenotato un volo per Roma.","exNl":"Ik heb een vlucht naar Rome geboekt.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w834","it":"l'itinerario","nl":"het reisschema / de route","ph":"li-ti-ne-ra-rio","ex":"Abbiamo pianificato un itinerario di dieci giorni.","exNl":"We hebben een reisschema van tien dagen gepland.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w835","it":"la guida turistica","nl":"de reisgids","ph":"la gwi-da tu-ris-ti-ka","ex":"Ho comprato una guida turistica di Sicilia.","exNl":"Ik heb een reisgids van Sicilië gekocht.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w836","it":"il visto","nl":"het visum","ph":"il vis-to","ex":"Per andare in Cina serve il visto.","exNl":"Om naar China te gaan heb je een visum nodig.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w837","it":"l'assicurazione viaggio","nl":"de reisverzekering","ph":"las-si-ku-ra-tsio-ne viad-dzho","ex":"Ho stipulato un'assicurazione viaggio.","exNl":"Ik heb een reisverzekering afgesloten.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w838","it":"il bagaglio a mano","nl":"het handbagage","ph":"il ba-ga-lio a ma-no","ex":"Posso portare solo il bagaglio a mano.","exNl":"Ik mag alleen handbagage meenemen.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w839","it":"la meta","nl":"de bestemming","ph":"la me-ta","ex":"La nostra meta è la Costiera Amalfitana.","exNl":"Onze bestemming is de Amalfikust.","lesson":105,"level":"A2","cat":"viaggio2"},
  {"id":"w840","it":"il soggiorno","nl":"het verblijf","ph":"il sod-dzhor-no","ex":"Il soggiorno a Firenze è stato meraviglioso.","exNl":"Het verblijf in Florence was geweldig.","lesson":105,"level":"A2","cat":"viaggio2"},

  # Les 106: Vervoer & mobiliteit
  {"id":"w841","it":"la metropolitana","nl":"de metro","ph":"la me-tro-po-li-ta-na","ex":"Prendo la metropolitana ogni mattina.","exNl":"Ik neem elke ochtend de metro.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w842","it":"cambiare","nl":"overstappen","ph":"kam-bia-re","ex":"Devo cambiare alla stazione Termini.","exNl":"Ik moet overstappen op station Termini.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w843","it":"la fermata","nl":"de halte","ph":"la fer-ma-ta","ex":"La fermata è a due isolati da qui.","exNl":"De halte is twee straten verderop.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w844","it":"l'abbonamento","nl":"het abonnement","ph":"lab-bo-na-men-to","ex":"Ho comprato un abbonamento mensile.","exNl":"Ik heb een maandabonnement gekocht.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w845","it":"in orario","nl":"op tijd","ph":"in o-ra-rio","ex":"Il treno è arrivato esattamente in orario.","exNl":"De trein arriveerde precies op tijd.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w846","it":"il ritardo","nl":"de vertraging","ph":"il ri-tar-do","ex":"C'è un ritardo di venti minuti.","exNl":"Er is een vertraging van twintig minuten.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w847","it":"noleggiare","nl":"huren","ph":"no-led-dzhare","ex":"Vorrei noleggiare una macchina per una settimana.","exNl":"Ik zou een auto willen huren voor een week.","lesson":106,"level":"A2","cat":"mobilita"},
  {"id":"w848","it":"il pedaggio","nl":"de tolheffing","ph":"il pe-dad-dzho","ex":"In Italia le autostrade hanno il pedaggio.","exNl":"In Italië hebben de snelwegen tolheffing.","lesson":106,"level":"A2","cat":"mobilita"},

  # Les 107: Spijt & wensen
  {"id":"w849","it":"mi dispiace","nl":"het spijt me / wat jammer","ph":"mi dis-pia-tsje","ex":"Mi dispiace molto per quello che è successo.","exNl":"Het spijt me erg voor wat er is gebeurd.","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w850","it":"peccato","nl":"wat jammer","ph":"pek-ka-to","ex":"Peccato che tu non possa venire!","exNl":"Wat jammer dat jij niet kunt komen!","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w851","it":"avrei voluto","nl":"ik had willen","ph":"a-vrei vo-lu-to","ex":"Avrei voluto studiare medicina.","exNl":"Ik had geneeskunde willen studeren.","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w852","it":"il rimpianto","nl":"de spijt","ph":"il rim-pjan-to","ex":"Non ho rimpianti nella mia vita.","exNl":"Ik heb geen spijt in mijn leven.","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w853","it":"se avessi","nl":"als ik had","ph":"se a-ves-si","ex":"Se avessi più tempo, viaggerei di più.","exNl":"Als ik meer tijd had, zou ik meer reizen.","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w854","it":"sbagliare","nl":"een fout maken","ph":"zba-lja-re","ex":"Ho sbagliato a non accettare quell'offerta.","exNl":"Ik heb een fout gemaakt door dat aanbod niet te accepteren.","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w855","it":"perdonare","nl":"vergeven","ph":"per-do-na-re","ex":"Ti perdono, ma non dimenticare.","exNl":"Ik vergeef je, maar vergeet het niet.","lesson":107,"level":"A2","cat":"rimpianti"},
  {"id":"w856","it":"sperare","nl":"hopen","ph":"spe-ra-re","ex":"Spero di rivederti presto.","exNl":"Ik hoop je snel weer te zien.","lesson":107,"level":"A2","cat":"rimpianti"},

  # Les 108: Culinaire tradities
  {"id":"w857","it":"la cucina regionale","nl":"de regionale keuken","ph":"la ku-tsji-na re-dzho-na-le","ex":"La cucina regionale italiana è molto varia.","exNl":"De Italiaanse regionale keuken is heel gevarieerd.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w858","it":"il piatto tipico","nl":"het typische gerecht","ph":"il pjat-to ti-pi-ko","ex":"La pizza è il piatto tipico di Napoli.","exNl":"Pizza is het typische gerecht van Napels.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w859","it":"gli ingredienti","nl":"de ingrediënten","ph":"li in-gre-dien-ti","ex":"Gli ingredienti della carbonara sono semplici.","exNl":"De ingrediënten van carbonara zijn eenvoudig.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w860","it":"il sapore","nl":"de smaak","ph":"il sa-po-re","ex":"Questo vino ha un sapore fruttato.","exNl":"Deze wijn heeft een fruitige smaak.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w861","it":"piccante","nl":"pittig / scherp","ph":"pik-kan-te","ex":"Il peperoncino rende tutto più piccante.","exNl":"De chilipeper maakt alles pittiger.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w862","it":"la tradizione culinaria","nl":"de culinaire traditie","ph":"la tra-di-tsio-ne ku-li-na-ria","ex":"La tradizione culinaria è parte dell'identità italiana.","exNl":"De culinaire traditie is deel van de Italiaanse identiteit.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w863","it":"a base di","nl":"op basis van","ph":"a ba-ze di","ex":"La pasta è a base di farina e uova.","exNl":"Pasta is op basis van bloem en eieren.","lesson":108,"level":"A2","cat":"gastronomia"},
  {"id":"w864","it":"il vino locale","nl":"de lokale wijn","ph":"il vi-no lo-ka-le","ex":"Preferisco il vino locale al ristorante.","exNl":"In het restaurant geef ik de voorkeur aan de lokale wijn.","lesson":108,"level":"A2","cat":"gastronomia"},

  # Les 109: Gezondheid & leefstijl
  {"id":"w865","it":"l'alimentazione","nl":"de voeding / het dieet","ph":"la-li-men-ta-tsio-ne","ex":"Una buona alimentazione è fondamentale per la salute.","exNl":"Goede voeding is essentieel voor de gezondheid.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w866","it":"fare movimento","nl":"bewegen / lichaamsbeweging","ph":"fa-re mo-vi-men-to","ex":"È importante fare movimento ogni giorno.","exNl":"Het is belangrijk om elke dag te bewegen.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w867","it":"evitare","nl":"vermijden","ph":"e-vi-ta-re","ex":"Cerco di evitare gli zuccheri raffinati.","exNl":"Ik probeer geraffineerde suikers te vermijden.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w868","it":"l'equilibrio","nl":"het evenwicht / de balans","ph":"le-kwi-li-brio","ex":"Cerco un equilibrio tra lavoro e vita privata.","exNl":"Ik zoek een balans tussen werk en privéleven.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w869","it":"rilassarsi","nl":"ontspannen","ph":"ri-las-sar-si","ex":"Il weekend mi rilasso completamente.","exNl":"In het weekend ontspan ik me helemaal.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w870","it":"lo stress","nl":"de stress","ph":"lo stres","ex":"Ho troppo stress al lavoro ultimamente.","exNl":"Ik heb de laatste tijd te veel stress op het werk.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w871","it":"dormire a sufficienza","nl":"voldoende slapen","ph":"dor-mire a suf-fi-tsjen-tsa","ex":"Bisogna dormire a sufficienza per stare bene.","exNl":"Het is nodig om voldoende te slapen om je goed te voelen.","lesson":109,"level":"A2","cat":"stile_vita"},
  {"id":"w872","it":"il benessere","nl":"het welzijn / het welbevinden","ph":"il be-nes-sere","ex":"Il benessere fisico e mentale sono ugualmente importanti.","exNl":"Fysiek en mentaal welzijn zijn even belangrijk.","lesson":109,"level":"A2","cat":"stile_vita"},

  # Les 110: Sport & outdoor
  {"id":"w873","it":"l'escursione","nl":"de wandeltocht / de excursie","ph":"les-kur-sio-ne","ex":"Abbiamo fatto una lunga escursione in montagna.","exNl":"We hebben een lange wandeltocht in de bergen gemaakt.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w874","it":"allenarsi","nl":"trainen","ph":"al-le-nar-si","ex":"Mi alleno tre volte alla settimana in palestra.","exNl":"Ik train drie keer per week in de sportschool.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w875","it":"la gara","nl":"de wedstrijd","ph":"la ga-ra","ex":"Ho partecipato a una gara di nuoto.","exNl":"Ik heb deelgenomen aan een zwemwedstrijd.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w876","it":"tifare","nl":"aanmoedigen / supporteren","ph":"ti-fa-re","ex":"Tifo per la Juventus da tanti anni.","exNl":"Ik support al jaren voor Juventus.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w877","it":"il campionato","nl":"het kampioenschap","ph":"il kam-pio-na-to","ex":"La Serie A è il campionato italiano di calcio.","exNl":"De Serie A is het Italiaanse voetbalkampioenschap.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w878","it":"vincere","nl":"winnen","ph":"vin-tsje-re","ex":"La nostra squadra ha vinto 3 a 1.","exNl":"Ons team heeft gewonnen met 3-1.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w879","it":"perdere","nl":"verliezen","ph":"per-de-re","ex":"Abbiamo perso, ma ci siamo divertiti.","exNl":"We hebben verloren, maar we hebben plezier gehad.","lesson":110,"level":"A2","cat":"sport2"},
  {"id":"w880","it":"il record","nl":"het record","ph":"il re-kord","ex":"Ha battuto il record mondiale!","exNl":"Hij/zij heeft het wereldrecord gebroken!","lesson":110,"level":"A2","cat":"sport2"},

  # Les 111: Winkelen & mode
  {"id":"w881","it":"la taglia","nl":"de kledingmaat","ph":"la ta-lja","ex":"Che taglia porta? — Porto una M.","exNl":"Welke maat heeft u? — Ik draag maat M.","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w882","it":"il camerino","nl":"de paskamer","ph":"il ka-me-ri-no","ex":"Dov'è il camerino? Vorrei provare questo.","exNl":"Waar is de paskamer? Ik zou dit willen passen.","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w883","it":"stare bene","nl":"staan / passen (kleding)","ph":"sta-re be-ne","ex":"Questo vestito ti sta benissimo!","exNl":"Deze jurk staat je uitstekend!","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w884","it":"stretto","nl":"te krap / te nauw","ph":"stret-to","ex":"Questi pantaloni sono un po' stretti.","exNl":"Deze broek is een beetje te krap.","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w885","it":"largo","nl":"wijd / te groot","ph":"lar-go","ex":"Questa giacca è troppo larga per me.","exNl":"Dit jasje is te groot voor mij.","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w886","it":"lo sconto","nl":"de korting","ph":"lo skon-to","ex":"C'è uno sconto del 30% sui saldi.","exNl":"Er is 30% korting in de uitverkoop.","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w887","it":"i saldi","nl":"de uitverkoop","ph":"i sal-di","ex":"D'estate i saldi iniziano a luglio.","exNl":"In de zomer beginnen de uitverkopen in juli.","lesson":111,"level":"A2","cat":"moda"},
  {"id":"w888","it":"fare shopping","nl":"winkelen gaan","ph":"fa-re sjop-ping","ex":"Il sabato pomeriggio vado a fare shopping.","exNl":"Op zaterdagmiddag ga ik winkelen.","lesson":111,"level":"A2","cat":"moda"},

  # Les 112: Technologie & internet
  {"id":"w889","it":"scaricare","nl":"downloaden","ph":"ska-ri-ka-re","ex":"Ho scaricato l'app sul mio telefono.","exNl":"Ik heb de app op mijn telefoon gedownload.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w890","it":"caricare","nl":"uploaden / opladen","ph":"ka-ri-ka-re","ex":"Devo caricare il telefono — è quasi scarico.","exNl":"Ik moet de telefoon opladen — hij is bijna leeg.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w891","it":"condividere","nl":"delen","ph":"kon-di-vi-de-re","ex":"Ha condiviso il video sui social media.","exNl":"Ze heeft de video op sociale media gedeeld.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w892","it":"la password","nl":"het wachtwoord","ph":"la pas-word","ex":"Ho dimenticato la password del mio account.","exNl":"Ik ben het wachtwoord van mijn account vergeten.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w893","it":"la connessione","nl":"de verbinding","ph":"la kon-nes-sio-ne","ex":"La connessione internet è lenta oggi.","exNl":"De internetverbinding is vandaag traag.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w894","it":"il messaggio","nl":"het bericht","ph":"il mes-sad-dzho","ex":"Ti mando un messaggio su WhatsApp.","exNl":"Ik stuur je een bericht op WhatsApp.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w895","it":"videochiamata","nl":"videogesprek","ph":"vi-de-o-kja-ma-ta","ex":"Facciamo una videochiamata con la famiglia.","exNl":"We doen een videogesprek met de familie.","lesson":112,"level":"A2","cat":"digitale"},
  {"id":"w896","it":"aggiornare","nl":"bijwerken / updaten","ph":"ad-dzhor-na-re","ex":"Devi aggiornare il sistema operativo.","exNl":"Je moet het besturingssysteem bijwerken.","lesson":112,"level":"A2","cat":"digitale"},

  # Les 113: Het weer & de natuur
  {"id":"w897","it":"il temporale","nl":"het onweer","ph":"il tem-po-ra-le","ex":"Stanotte c'è stato un temporale violento.","exNl":"Afgelopen nacht was er een hevig onweer.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w898","it":"la nebbia","nl":"de mist","ph":"la neb-bia","ex":"In inverno la pianura padana è spesso coperta di nebbia.","exNl":"In de winter is de Povlakte vaak bedekt met mist.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w899","it":"afoso","nl":"benauwd / drukkend","ph":"a-fo-zo","ex":"D'estate a Roma fa un caldo afoso.","exNl":"In de zomer is het in Rome drukkend heet.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w900","it":"la siccità","nl":"de droogte","ph":"la sit-tshi-ta","ex":"Quest'estate c'è stata una grave siccità al sud.","exNl":"Deze zomer was er een ernstige droogte in het zuiden.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w901","it":"grandine","nl":"hagelstenen","ph":"gran-di-ne","ex":"Durante il temporale è caduta la grandine.","exNl":"Tijdens het onweer viel er hagel.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w902","it":"il tramonto","nl":"de zonsondergang","ph":"il tra-mon-to","ex":"Il tramonto sul mare è spettacolare.","exNl":"De zonsondergang op zee is spectaculair.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w903","it":"il paesaggio","nl":"het landschap","ph":"il pae-zad-dzho","ex":"Il paesaggio toscano è famoso in tutto il mondo.","exNl":"Het Toscaanse landschap is wereldberoemd.","lesson":113,"level":"A2","cat":"meteo"},
  {"id":"w904","it":"il clima","nl":"het klimaat","ph":"il kli-ma","ex":"L'Italia ha un clima molto vario da nord a sud.","exNl":"Italië heeft een heel gevarieerd klimaat van noord naar zuid.","lesson":113,"level":"A2","cat":"meteo"},

  # Les 114: Werk & loopbaan
  {"id":"w905","it":"il colloquio","nl":"het sollicitatiegesprek","ph":"il kol-lo-kwio","ex":"Ho un colloquio di lavoro domani mattina.","exNl":"Ik heb morgenochtend een sollicitatiegesprek.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w906","it":"il curriculum","nl":"het cv","ph":"il kur-ri-ku-lum","ex":"Ho aggiornato il mio curriculum vitae.","exNl":"Ik heb mijn cv bijgewerkt.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w907","it":"assumere","nl":"aannemen / in dienst nemen","ph":"as-su-me-re","ex":"L'azienda ha assunto dieci nuovi dipendenti.","exNl":"Het bedrijf heeft tien nieuwe medewerkers aangenomen.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w908","it":"licenziarsi","nl":"ontslag nemen","ph":"li-tjen-tsjar-si","ex":"Mi sono licenziato per trovare qualcosa di meglio.","exNl":"Ik heb ontslag genomen om iets beters te vinden.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w909","it":"lo stipendio","nl":"het salaris","ph":"lo sti-pen-dio","ex":"Il mio stipendio è aumentato quest'anno.","exNl":"Mijn salaris is dit jaar gestegen.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w910","it":"la promozione","nl":"de promotie / bevordering","ph":"la pro-mo-tsio-ne","ex":"Ho ricevuto una promozione al lavoro.","exNl":"Ik heb een promotie gekregen op het werk.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w911","it":"il collega","nl":"de collega","ph":"il kol-le-ga","ex":"I miei colleghi sono molto simpatici.","exNl":"Mijn collega's zijn heel aardig.","lesson":114,"level":"A2","cat":"carriera"},
  {"id":"w912","it":"lavorare da casa","nl":"thuiswerken","ph":"la-vo-ra-re da ka-za","ex":"Due giorni alla settimana lavoro da casa.","exNl":"Twee dagen per week werk ik thuis.","lesson":114,"level":"A2","cat":"carriera"},

  # Les 115: Kunst & musea
  {"id":"w913","it":"il museo","nl":"het museum","ph":"il mu-ze-o","ex":"Gli Uffizi di Firenze sono un museo straordinario.","exNl":"De Uffizi in Florence is een buitengewoon museum.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w914","it":"la mostra","nl":"de tentoonstelling","ph":"la mos-tra","ex":"C'è una mostra di Caravaggio in città.","exNl":"Er is een tentoonstelling van Caravaggio in de stad.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w915","it":"il quadro","nl":"het schilderij","ph":"il kwa-dro","ex":"Questo quadro mi emoziona ogni volta.","exNl":"Dit schilderij ontroert me elke keer.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w916","it":"la scultura","nl":"het beeldhouwwerk","ph":"la skul-tu-ra","ex":"Il David di Michelangelo è una scultura magnifica.","exNl":"De David van Michelangelo is een prachtig beeldhouwwerk.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w917","it":"l'opera d'arte","nl":"het kunstwerk","ph":"lo-pe-ra dar-te","ex":"Ogni chiesa italiana è piena di opere d'arte.","exNl":"Elke Italiaanse kerk is vol met kunstwerken.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w918","it":"dipingere","nl":"schilderen","ph":"di-pin-dzhe-re","ex":"Leonardo da Vinci ha dipinto la Gioconda.","exNl":"Leonardo da Vinci heeft de Mona Lisa geschilderd.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w919","it":"il capolavoro","nl":"het meesterwerk","ph":"il ka-po-la-vo-ro","ex":"La Cappella Sistina è un assoluto capolavoro.","exNl":"De Sixtijnse Kapel is een absoluut meesterwerk.","lesson":115,"level":"A2","cat":"arte"},
  {"id":"w920","it":"il patrimonio","nl":"het erfgoed","ph":"il pa-tri-mo-nio","ex":"L'Italia custodisce un immenso patrimonio culturale.","exNl":"Italië beheert een immens cultureel erfgoed.","lesson":115,"level":"A2","cat":"arte"},

  # Les 116: Italiaanse tradities
  {"id":"w921","it":"il Ferragosto","nl":"Ferragosto (15 augustus)","ph":"il fer-ra-gos-to","ex":"A Ferragosto quasi tutto è chiuso in Italia.","exNl":"Met Ferragosto is bijna alles gesloten in Italië.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w922","it":"il Carnevale","nl":"het Carnaval","ph":"il kar-ne-va-le","ex":"Il Carnevale di Venezia è famoso in tutto il mondo.","exNl":"Het Carnaval van Venetië is wereldberoemd.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w923","it":"la Pasqua","nl":"Pasen","ph":"la pas-kwa","ex":"A Pasqua si mangiano le uova di cioccolato.","exNl":"Met Pasen eet men chocolade-eieren.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w924","it":"la Festa della Repubblica","nl":"Dag van de Republiek (2 juni)","ph":"la fes-ta del-la re-pub-bli-ka","ex":"Il 2 giugno si celebra la Festa della Repubblica.","exNl":"Op 2 juni wordt de Dag van de Republiek gevierd.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w925","it":"il presepe","nl":"de kerststal","ph":"il pre-ze-pe","ex":"In Italia allestire il presepe è una tradizione natalizia.","exNl":"In Italië is het bouwen van een kerststal een kersttaditie.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w926","it":"la sagra","nl":"het dorpsfeest (culinair)","ph":"la za-gra","ex":"Ogni estate ci sono sagre in tutta Italia.","exNl":"Elke zomer zijn er dorpsfeesten door heel Italië.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w927","it":"il campanile","nl":"de klokkentoren","ph":"il kam-pa-ni-le","ex":"Ogni paese italiano ha il suo campanile.","exNl":"Elk Italiaans dorp heeft zijn eigen klokkentoren.","lesson":116,"level":"A2","cat":"tradizioni"},
  {"id":"w928","it":"la piazza","nl":"het plein","ph":"la pjad-dza","ex":"La piazza è il cuore della vita sociale italiana.","exNl":"Het plein is het hart van het Italiaanse sociale leven.","lesson":116,"level":"A2","cat":"tradizioni"},

  # Les 117: Onderwijs & leren
  {"id":"w929","it":"iscriversi","nl":"zich inschrijven","ph":"is-kri-ver-si","ex":"Mi sono iscritto all'università di Bologna.","exNl":"Ik heb me ingeschreven aan de Universiteit van Bologna.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w930","it":"la laurea","nl":"het universitair diploma","ph":"la lau-re-a","ex":"Ho conseguito la laurea in economia.","exNl":"Ik heb mijn universitair diploma economie behaald.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w931","it":"sostenere un esame","nl":"een examen afleggen","ph":"sos-te-ne-re un e-za-me","ex":"Domani sostengo l'esame di italiano.","exNl":"Morgen leg ik het Italiaans examen af.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w932","it":"il voto","nl":"het cijfer","ph":"il vo-to","ex":"Ho preso un bel voto all'esame.","exNl":"Ik heb een goed cijfer gehaald voor het examen.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w933","it":"la borsa di studio","nl":"de studiebeurs","ph":"la bor-sa di stu-dio","ex":"Ha vinto una borsa di studio per studiare a Firenze.","exNl":"Ze heeft een studiebeurs gewonnen om in Florence te studeren.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w934","it":"fare pratica","nl":"oefenen","ph":"fa-re pra-ti-ka","ex":"Per imparare bene devi fare molta pratica.","exNl":"Om goed te leren moet je veel oefenen.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w935","it":"la lingua madre","nl":"de moedertaal","ph":"la lin-gwa ma-dre","ex":"La mia lingua madre è l'olandese.","exNl":"Mijn moedertaal is Nederlands.","lesson":117,"level":"A2","cat":"istruzione2"},
  {"id":"w936","it":"bilingue","nl":"tweetalig","ph":"bi-lin-gwe","ex":"I miei figli crescono bilingui.","exNl":"Mijn kinderen groeien tweetalig op.","lesson":117,"level":"A2","cat":"istruzione2"},

  # Les 118: Media & nieuws
  {"id":"w937","it":"il telegiornale","nl":"het journaal","ph":"il te-le-dzhor-na-le","ex":"Guardo il telegiornale ogni sera alle otto.","exNl":"Ik kijk elke avond om acht uur naar het journaal.","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w938","it":"il giornale","nl":"de krant","ph":"il dzhor-na-le","ex":"Leggo il giornale ogni mattina al bar.","exNl":"Ik lees elke ochtend de krant in het café.","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w939","it":"la notizia","nl":"het nieuws / het bericht","ph":"la no-ti-tsia","ex":"Hai sentito l'ultima notizia?","exNl":"Heb je het laatste nieuws gehoord?","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w940","it":"il social network","nl":"het sociale netwerk","ph":"il so-sjal net-work","ex":"Passo troppo tempo sui social network.","exNl":"Ik breng te veel tijd door op sociale netwerken.","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w941","it":"la pubblicità","nl":"de reclame","ph":"la pub-bli-tshi-ta","ex":"In Italia la pubblicità televisiva è molto creativa.","exNl":"In Italië is televisiereclame heel creatief.","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w942","it":"seguire","nl":"volgen","ph":"se-gwi-re","ex":"Seguo molti canali italiani su YouTube.","exNl":"Ik volg veel Italiaanse kanalen op YouTube.","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w943","it":"commentare","nl":"reageren / commentaar geven","ph":"kom-men-ta-re","ex":"Non commento mai sui post degli altri.","exNl":"Ik reageer nooit op de berichten van anderen.","lesson":118,"level":"A2","cat":"media2"},
  {"id":"w944","it":"le fake news","nl":"de nepnieuws","ph":"le feik njuz","ex":"Bisogna verificare le fonti prima di condividere.","exNl":"Je moet de bronnen controleren voordat je deelt.","lesson":118,"level":"A2","cat":"media2"},

  # Les 119: Duurzaamheid & milieu
  {"id":"w945","it":"riciclare","nl":"recyclen","ph":"ri-tshi-kla-re","ex":"In Italia è obbligatorio riciclare i rifiuti.","exNl":"In Italië is het verplicht om afval te recyclen.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w946","it":"la raccolta differenziata","nl":"het gescheiden afval inzamelen","ph":"la rak-kol-ta dif-fe-ren-tsja-ta","ex":"Faccio sempre la raccolta differenziata.","exNl":"Ik doe altijd aan gescheiden afvalinzameling.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w947","it":"risparmiare energia","nl":"energie besparen","ph":"ris-par-mia-re e-ner-dzhia","ex":"Ho installato pannelli solari per risparmiare energia.","exNl":"Ik heb zonnepanelen geïnstalleerd om energie te besparen.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w948","it":"le energie rinnovabili","nl":"de hernieuwbare energie","ph":"le e-ner-dzhie rin-no-va-bi-li","ex":"L'Italia investe sempre di più nelle energie rinnovabili.","exNl":"Italië investeert steeds meer in hernieuwbare energie.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w949","it":"ridurre","nl":"verminderen","ph":"ri-dur-re","ex":"Dobbiamo ridurre l'uso della plastica.","exNl":"We moeten het gebruik van plastic verminderen.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w950","it":"la borsa riutilizzabile","nl":"de herbruikbare tas","ph":"la bor-sa riu-ti-lid-dza-bi-le","ex":"Porto sempre una borsa riutilizzabile al supermercato.","exNl":"Ik neem altijd een herbruikbare tas mee naar de supermarkt.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w951","it":"l'impronta carbonica","nl":"de koolstofvoetafdruk","ph":"lim-pron-ta kar-bo-ni-ka","ex":"Voglio ridurre la mia impronta carbonica.","exNl":"Ik wil mijn koolstofvoetafdruk verkleinen.","lesson":119,"level":"A2","cat":"sostenibilita"},
  {"id":"w952","it":"sostenibile","nl":"duurzaam","ph":"sos-te-ni-bi-le","ex":"Cerco di fare scelte più sostenibili ogni giorno.","exNl":"Ik probeer elke dag duurzamere keuzes te maken.","lesson":119,"level":"A2","cat":"sostenibilita"},

  # Les 120: A2 afgerond!
  {"id":"w953","it":"la fluidità","nl":"de vloeiendheid","ph":"la flu-i-di-ta","ex":"Sto migliorando la mia fluidità in italiano.","exNl":"Ik verbeter mijn vloeiendheid in het Italiaans.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w954","it":"la pronuncia","nl":"de uitspraak","ph":"la pro-nun-tsja","ex":"La mia pronuncia è migliorata tantissimo.","exNl":"Mijn uitspraak is enorm verbeterd.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w955","it":"la grammatica","nl":"de grammatica","ph":"la gram-ma-ti-ka","ex":"Capisco meglio la grammatica italiana ora.","exNl":"Ik begrijp de Italiaanse grammatica nu beter.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w956","it":"il vocabolario","nl":"de woordenschat","ph":"il vo-ka-bo-la-rio","ex":"Il mio vocabolario si è ampliato molto.","exNl":"Mijn woordenschat is sterk uitgebreid.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w957","it":"conversare","nl":"een gesprek voeren","ph":"kon-ver-sa-re","ex":"Riesco a conversare con gli italiani senza troppi problemi.","exNl":"Ik slaag erin om zonder al te veel problemen met Italianen te praten.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w958","it":"capire","nl":"begrijpen","ph":"ka-pi-re","ex":"Capisco quasi tutto quando parlano lentamente.","exNl":"Ik begrijp bijna alles als ze langzaam praten.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w959","it":"esprimersi","nl":"zich uitdrukken","ph":"es-pri-mer-si","ex":"Riesco ad esprimermi in molte situazioni.","exNl":"Ik slaag erin me in veel situaties uit te drukken.","lesson":120,"level":"A2","cat":"ripasso_a2"},
  {"id":"w960","it":"il prossimo passo","nl":"de volgende stap","ph":"il pros-si-mo pas-so","ex":"Il prossimo passo è il livello B1 — ce la fai!","exNl":"De volgende stap is niveau B1 — je kunt het!","lesson":120,"level":"A2","cat":"ripasso_a2"},
]

# ── Laad bestaande data ────────────────────────────────────────────────────────
with open(CURR_FILE) as f:
    cur = json.load(f)
with open(VOCAB_FILE) as f:
    vocab = json.load(f)

# Check duplicaten
existing_it = {w['it'].lower() for w in vocab}
dupes = [w['it'] for w in new_words if w['it'].lower() in existing_it]
if dupes:
    print(f'⚠️  Duplicaten gevonden: {dupes}')

# Voeg toe
cur.extend(new_lessons)
vocab.extend(new_words)

with open(CURR_FILE, 'w', encoding='utf-8') as f:
    json.dump(cur, f, ensure_ascii=False, indent=2)
with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

print(f'✓ {len(new_lessons)} nieuwe lessen toegevoegd (91-120)')
print(f'✓ {len(new_words)} nieuwe woorden toegevoegd (w721-w960)')
print(f'  Totaal lessen: {len(cur)}')
print(f'  Totaal woorden: {len(vocab)}')
