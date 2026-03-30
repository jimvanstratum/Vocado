#!/usr/bin/env python3
"""Genereer B1-lessen 121-180 (60 lessen, 480 woorden) voor Vocado."""

import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURR_FILE = os.path.join(BASE, 'www/data/curriculum.json')
VOCAB_FILE = os.path.join(BASE, 'www/data/vocabulary.json')

# ── LESSEN ────────────────────────────────────────────────────────────────────

new_lessons = [
    # ═══ BLOK 1: IMPERFETTO & VERLEDEN TIJD (121–130) ═══════════════════════
    {
        "id": 121, "title": "Imperfetto — regelmatig", "emoji": "⏳", "level": "B1",
        "description": "Leer de imperfetto voor regelmatige werkwoorden: hoe het vroeger was.",
        "grammar": {
            "title": "Imperfetto: regelmatige vervoeging",
            "body": "De imperfetto beschrijft gewoontes, toestanden en achtergronden in het verleden. Regelmatige vormen:\n\n• -are: parlavo, parlavi, parlava, parlavamo, parlavate, parlavano\n• -ere: scrivevo, scrivevi, scriveva, scrivevamo, scrivevate, scrivevano\n• -ire: dormivo, dormivi, dormiva, dormivamo, dormivate, dormivano\n\nGebruik de imperfetto voor: 'Ik deed altijd…', 'Het was…', 'Terwijl…'."
        },
        "words": ["w1211","w1212","w1213","w1214","w1215","w1216","w1217","w1218"]
    },
    {
        "id": 122, "title": "Imperfetto — onregelmatig", "emoji": "🔀", "level": "B1",
        "description": "De onregelmatige imperfetto-vormen die je het vaakst tegenkomt.",
        "grammar": {
            "title": "Onregelmatige imperfetto",
            "body": "Een paar veelgebruikte werkwoorden zijn onregelmatig in de imperfetto:\n\n• essere: ero, eri, era, eravamo, eravate, erano\n• fare: facevo, facevi, faceva…\n• dire: dicevo, dicevi, diceva…\n• bere: bevevo, bevevi, beveva…\n\nDeze vormen komen heel vaak voor in verhalen en beschrijvingen."
        },
        "words": ["w1219","w1220","w1221","w1222","w1223","w1224","w1225","w1226"]
    },
    {
        "id": 123, "title": "Imperfetto vs. passato prossimo", "emoji": "⚖️", "level": "B1",
        "description": "Wanneer gebruik je de imperfetto en wanneer de passato prossimo?",
        "grammar": {
            "title": "Imperfetto vs. passato prossimo",
            "body": "Het verschil:\n\n• Imperfetto = achtergrond, gewoonte, beschrijving\n  → Pioveva (het regende — toestand)\n• Passato prossimo = afgeronde actie, gebeurtenis\n  → Ho preso l'ombrello (ik pakte de paraplu — actie)\n\nCombinatie: 'Mentre dormivo, ha suonato il telefono.'\n(Terwijl ik sliep, ging de telefoon.)\n\nVuistregel: imperfetto = film (doorlopend), passato prossimo = foto (momentopname)."
        },
        "words": ["w1227","w1228","w1229","w1230","w1231","w1232","w1233","w1234"]
    },
    {
        "id": 124, "title": "Herinneringen", "emoji": "💭", "level": "B1",
        "description": "Vertel over vroeger: je kindertijd, school en herinneringen.",
        "grammar": {
            "title": "Herinneringen vertellen met imperfetto",
            "body": "Gebruik de imperfetto voor herinneringen:\n\n• Da bambino/a… (als kind…)\n• Quando ero piccolo/a… (toen ik klein was…)\n• Mi ricordo che… (ik herinner me dat…)\n• A quei tempi… (in die tijd…)\n\nVoorbeeld: 'Da bambino giocavo sempre nel parco.'\n(Als kind speelde ik altijd in het park.)"
        },
        "words": ["w1235","w1236","w1237","w1238","w1239","w1240","w1241","w1242"]
    },
    {
        "id": 125, "title": "Gewoontes vroeger", "emoji": "🔄", "level": "B1",
        "description": "Beschrijf gewoontes en routines uit het verleden.",
        "grammar": {
            "title": "Gewoontes beschrijven",
            "body": "De imperfetto is ideaal voor herhaalde acties in het verleden:\n\n• Di solito… (gewoonlijk…)\n• Ogni giorno/settimana… (elke dag/week…)\n• Sempre/spesso/a volte… (altijd/vaak/soms…)\n\nVoorbeeld: 'Ogni estate andavamo al mare.'\n(Elke zomer gingen we naar zee.)"
        },
        "words": ["w1243","w1244","w1245","w1246","w1247","w1248","w1249","w1250"]
    },
    {
        "id": 126, "title": "Verhalen vertellen — deel 1", "emoji": "📖", "level": "B1",
        "description": "Leer een verhaal opbouwen met de juiste werkwoordstijden.",
        "grammar": {
            "title": "Vertelstructuur",
            "body": "Een goed verhaal combineert tijden:\n\n1. Achtergrond (imperfetto): 'Era una bella giornata…'\n2. Gebeurtenis (passato prossimo): '…quando ho visto un gatto.'\n3. Beschrijving (imperfetto): 'Il gatto era nero e grande.'\n4. Volgende actie (passato prossimo): 'L'ho seguito.'\n\nDeze afwisseling maakt je verhaal levendig."
        },
        "words": ["w1251","w1252","w1253","w1254","w1255","w1256","w1257","w1258"]
    },
    {
        "id": 127, "title": "Verhalen vertellen — deel 2", "emoji": "📚", "level": "B1",
        "description": "Oefen met complexere verhalen en verbindingswoorden.",
        "grammar": {
            "title": "Verbindingswoorden in verhalen",
            "body": "Maak je verhalen vloeiender met:\n\n• Poi/dopo (daarna) — Poi siamo andati a casa.\n• Improvvisamente (plotseling) — Improvvisamente è arrivata.\n• Nel frattempo (ondertussen) — Nel frattempo pioveva.\n• Alla fine (uiteindelijk) — Alla fine tutto è andato bene.\n• Per fortuna (gelukkig) — Per fortuna non era grave."
        },
        "words": ["w1259","w1260","w1261","w1262","w1263","w1264","w1265","w1266"]
    },
    {
        "id": 128, "title": "Het weer beschrijven", "emoji": "🌦️", "level": "B1",
        "description": "Praat over het weer: nu, vroeger en in de toekomst.",
        "grammar": {
            "title": "Weer in verschillende tijden",
            "body": "Het weer beschrijven in drie tijden:\n\n• Nu: Oggi piove. / Fa caldo. / C'è il sole.\n• Vroeger: Ieri pioveva. / Faceva freddo.\n• Toekomst: Domani farà bel tempo.\n\nBelangrijk: 'fare' wordt veel gebruikt: fa caldo/freddo/bel tempo."
        },
        "words": ["w1267","w1268","w1269","w1270","w1271","w1272","w1273","w1274"]
    },
    {
        "id": 129, "title": "Emoties in het verleden", "emoji": "😢", "level": "B1",
        "description": "Beschrijf gevoelens en emoties van vroeger.",
        "grammar": {
            "title": "Emoties met imperfetto",
            "body": "Emoties en gevoelens in het verleden gebruiken de imperfetto (het is een toestand, geen actie):\n\n• Ero felice/triste/arrabbiato (ik was blij/verdrietig/boos)\n• Mi sentivo stanco/a (ik voelde me moe)\n• Avevo paura (ik was bang)\n• Mi piaceva molto (ik vond het erg leuk)\n\nMaar: 'Ho avuto paura' = ik schrok (eenmalige reactie)."
        },
        "words": ["w1275","w1276","w1277","w1278","w1279","w1280","w1281","w1282"]
    },
    {
        "id": 130, "title": "Toetsles — Blok 1", "emoji": "📝", "level": "B1",
        "description": "Test je kennis van de imperfetto en het vertellen over het verleden.",
        "grammar": {
            "title": "Samenvatting Blok 1",
            "body": "Wat je hebt geleerd:\n\n• Imperfetto: regelmatige en onregelmatige vormen\n• Verschil imperfetto vs. passato prossimo\n• Herinneringen en gewoontes beschrijven\n• Verhalen vertellen met de juiste tijdwisseling\n• Weer en emoties in het verleden\n\nDe imperfetto is één van de belangrijkste tijden in het Italiaans — je gebruikt hem elke dag!"
        },
        "words": ["w1283","w1284","w1285","w1286","w1287","w1288","w1289","w1290"]
    },

    # ═══ BLOK 2: CONDIZIONALE & WENSEN (131–140) ════════════════════════════
    {
        "id": 131, "title": "Condizionale — regelmatig", "emoji": "🌟", "level": "B1",
        "description": "Leer de condizionale presente: 'ik zou willen', 'zou je kunnen?'.",
        "grammar": {
            "title": "Condizionale presente: vorming",
            "body": "De condizionale (zou-vorm) maak je zo:\n\n• -are: parlerei, parleresti, parlerebbe, parleremmo, parlereste, parlerebbero\n• -ere: scriverei, scriveresti, scriverebbe…\n• -ire: dormirei, dormiresti, dormirebbe…\n\nLet op: de stam is dezelfde als de futuro!\nGebruik: beleefd vragen, wensen, advies."
        },
        "words": ["w1291","w1292","w1293","w1294","w1295","w1296","w1297","w1298"]
    },
    {
        "id": 132, "title": "Condizionale — onregelmatig", "emoji": "✨", "level": "B1",
        "description": "De onregelmatige condizionale-vormen die je dagelijks gebruikt.",
        "grammar": {
            "title": "Onregelmatige condizionale",
            "body": "De meest gebruikte onregelmatige vormen:\n\n• essere: sarei, saresti, sarebbe…\n• avere: avrei, avresti, avrebbe…\n• fare: farei, faresti, farebbe…\n• andare: andrei, andresti, andrebbe…\n• potere: potrei, potresti, potrebbe…\n• volere: vorrei, vorresti, vorrebbe…\n• dovere: dovrei, dovresti, dovrebbe…\n\n'Vorrei un caffè' is veel beleefder dan 'Voglio un caffè'."
        },
        "words": ["w1299","w1300","w1301","w1302","w1303","w1304","w1305","w1306"]
    },
    {
        "id": 133, "title": "Beleefd verzoeken", "emoji": "🎩", "level": "B1",
        "description": "Vraag beleefd om dingen met de condizionale.",
        "grammar": {
            "title": "Beleefde verzoeken",
            "body": "De condizionale maakt verzoeken vriendelijk:\n\n• Potrebbe aiutarmi? (Zou u me kunnen helpen?)\n• Vorrei prenotare un tavolo. (Ik zou graag een tafel reserveren.)\n• Mi farebbe un favore? (Zou u me een plezier doen?)\n• Sarebbe possibile…? (Zou het mogelijk zijn…?)\n\nIn winkels en restaurants is de condizionale de standaard."
        },
        "words": ["w1307","w1308","w1309","w1310","w1311","w1312","w1313","w1314"]
    },
    {
        "id": 134, "title": "Wensen & dromen", "emoji": "🌈", "level": "B1",
        "description": "Vertel over je wensen, dromen en wat je zou willen doen.",
        "grammar": {
            "title": "Wensen uitdrukken",
            "body": "De condizionale voor wensen en dromen:\n\n• Mi piacerebbe viaggiare. (Ik zou graag willen reizen.)\n• Vorrei vivere in Italia. (Ik zou in Italië willen wonen.)\n• Sarebbe bello… (Het zou mooi zijn…)\n• Il mio sogno sarebbe… (Mijn droom zou zijn…)\n\nCombineer met 'se potessi' (als ik kon) voor hypothetische wensen."
        },
        "words": ["w1315","w1316","w1317","w1318","w1319","w1320","w1321","w1322"]
    },
    {
        "id": 135, "title": "Advies geven", "emoji": "💡", "level": "B1",
        "description": "Geef en vraag advies met de condizionale.",
        "grammar": {
            "title": "Advies met de condizionale",
            "body": "Advies geven:\n\n• Dovresti studiare di più. (Je zou meer moeten studeren.)\n• Al posto tuo, io… (Op jouw plaats zou ik…)\n• Faresti meglio a… (Je zou er beter aan doen om…)\n• Ti consiglierei di… (Ik zou je aanraden om…)\n\nAdvies vragen:\n• Cosa faresti al mio posto? (Wat zou jij doen op mijn plaats?)\n• Mi consiglieresti di…? (Zou je me aanraden om…?)"
        },
        "words": ["w1323","w1324","w1325","w1326","w1327","w1328","w1329","w1330"]
    },
    {
        "id": 136, "title": "Op restaurant", "emoji": "🍽️", "level": "B1",
        "description": "Bestel beleefd, vraag aanbevelingen en bespreek het menu.",
        "grammar": {
            "title": "Beleefde restauranttaal",
            "body": "In een restaurant:\n\n• Vorrei ordinare… (Ik zou graag bestellen…)\n• Cosa mi consiglierebbe? (Wat zou u me aanraden?)\n• Potrei avere il conto? (Zou ik de rekening mogen?)\n• Per me… (Voor mij…)\n• Come contorno vorrei… (Als bijgerecht zou ik…)\n\nBelangrijk: in Italië betaal je vaak 'il coperto' (couvert)."
        },
        "words": ["w1331","w1332","w1333","w1334","w1335","w1336","w1337","w1338"]
    },
    {
        "id": 137, "title": "Reisplannen maken", "emoji": "✈️", "level": "B1",
        "description": "Plan een reis: bestemming, vervoer en accommodatie.",
        "grammar": {
            "title": "Reisplannen bespreken",
            "body": "Plannen maken met de condizionale:\n\n• Potremmo andare a… (We zouden naar… kunnen gaan.)\n• Mi piacerebbe visitare… (Ik zou graag… bezoeken.)\n• Preferirei prendere il treno. (Ik zou liever de trein nemen.)\n• Dovremmo prenotare in anticipo. (We zouden van tevoren moeten boeken.)\n\nNuttig: 'Quanto costerebbe…?' (Hoeveel zou… kosten?)"
        },
        "words": ["w1339","w1340","w1341","w1342","w1343","w1344","w1345","w1346"]
    },
    {
        "id": 138, "title": "Accommodatie", "emoji": "🏨", "level": "B1",
        "description": "Boek een hotel, bespreek kamers en meld problemen.",
        "grammar": {
            "title": "In het hotel",
            "body": "Bij het boeken en inchecken:\n\n• Vorrei prenotare una camera. (Ik zou graag een kamer boeken.)\n• Avrei bisogno di… (Ik zou… nodig hebben.)\n• A che ora è il check-out? (Hoe laat is het check-out?)\n• La colazione è inclusa? (Is het ontbijt inbegrepen?)\n\nProblemen melden:\n• Non funziona il… (De… werkt niet.)\n• Potrebbe mandare qualcuno? (Zou u iemand kunnen sturen?)"
        },
        "words": ["w1347","w1348","w1349","w1350","w1351","w1352","w1353","w1354"]
    },
    {
        "id": 139, "title": "Vervoer & richting", "emoji": "🚆", "level": "B1",
        "description": "Reis door Italië: treinen, bus en de weg vragen.",
        "grammar": {
            "title": "Vervoer en richting",
            "body": "De weg vragen en richting geven:\n\n• Potrebbe dirmi dove…? (Zou u me kunnen zeggen waar…?)\n• Come posso arrivare a…? (Hoe kan ik bij… komen?)\n• Deve prendere la prima a destra. (U moet de eerste rechts nemen.)\n• Vada dritto, poi giri a sinistra. (Ga rechtdoor, sla dan linksaf.)\n\nTreinen: 'il binario' (perron), 'la coincidenza' (overstap)."
        },
        "words": ["w1355","w1356","w1357","w1358","w1359","w1360","w1361","w1362"]
    },
    {
        "id": 140, "title": "Toetsles — Blok 2", "emoji": "📝", "level": "B1",
        "description": "Test je kennis van de condizionale, beleefdheid en reizen.",
        "grammar": {
            "title": "Samenvatting Blok 2",
            "body": "Wat je hebt geleerd:\n\n• Condizionale presente: regelmatig en onregelmatig\n• Beleefd verzoeken en aanbevelingen\n• Wensen en dromen uitdrukken\n• Advies geven en vragen\n• Restaurant-, reis- en hotelwoordenschat\n\nDe condizionale maakt je Italiaans veel beleefder en natuurlijker!"
        },
        "words": ["w1363","w1364","w1365","w1366","w1367","w1368","w1369","w1370"]
    },

    # ═══ BLOK 3: CONGIUNTIVO & MENINGEN (141–150) ═══════════════════════════
    {
        "id": 141, "title": "Congiuntivo — introductie", "emoji": "🧠", "level": "B1",
        "description": "Maak kennis met de congiuntivo: de modus van meningen en twijfel.",
        "grammar": {
            "title": "Congiuntivo presente: introductie",
            "body": "De congiuntivo gebruik je na werkwoorden van mening, wens of twijfel:\n\n• -are: parli, parli, parli, parliamo, parliate, parlino\n• -ere: scriva, scriva, scriva, scriviamo, scriviate, scrivano\n• -ire: dorma, dorma, dorma, dormiamo, dormiate, dormano\n\nTriggerwoorden: penso che, credo che, spero che, è importante che.\n\nVoorbeeld: 'Penso che lui parli bene l'italiano.'"
        },
        "words": ["w1371","w1372","w1373","w1374","w1375","w1376","w1377","w1378"]
    },
    {
        "id": 142, "title": "Congiuntivo — onregelmatig", "emoji": "🔮", "level": "B1",
        "description": "De onregelmatige congiuntivo-vormen die je het meest nodig hebt.",
        "grammar": {
            "title": "Onregelmatige congiuntivo",
            "body": "De belangrijkste onregelmatige vormen:\n\n• essere: sia, sia, sia, siamo, siate, siano\n• avere: abbia, abbia, abbia, abbiamo, abbiate, abbiano\n• fare: faccia, faccia, faccia…\n• andare: vada, vada, vada…\n• potere: possa, possa, possa…\n• volere: voglia, voglia, voglia…\n• dire: dica, dica, dica…\n\n'Credo che sia una buona idea.' (Ik denk dat het een goed idee is.)"
        },
        "words": ["w1379","w1380","w1381","w1382","w1383","w1384","w1385","w1386"]
    },
    {
        "id": 143, "title": "Meningen geven", "emoji": "💬", "level": "B1",
        "description": "Geef je mening en reageer op de mening van anderen.",
        "grammar": {
            "title": "Meningen met congiuntivo",
            "body": "Je mening geven:\n\n• Penso/Credo che + congiuntivo\n• Secondo me… (Volgens mij…) — GEEN congiuntivo!\n• Mi sembra che + congiuntivo\n• A mio parere… (Naar mijn mening…) — GEEN congiuntivo\n\nReageren:\n• Sono d'accordo. (Ik ben het eens.)\n• Non sono d'accordo. (Ik ben het oneens.)\n• Hai ragione/torto. (Je hebt gelijk/ongelijk.)"
        },
        "words": ["w1387","w1388","w1389","w1390","w1391","w1392","w1393","w1394"]
    },
    {
        "id": 144, "title": "Emoties & congiuntivo", "emoji": "❤️", "level": "B1",
        "description": "Druk emoties uit die de congiuntivo vereisen.",
        "grammar": {
            "title": "Emoties + congiuntivo",
            "body": "Na emotie-uitdrukkingen volgt de congiuntivo:\n\n• Sono contento/a che tu sia qui. (Ik ben blij dat je hier bent.)\n• Mi dispiace che tu stia male. (Het spijt me dat je je slecht voelt.)\n• Ho paura che piova. (Ik ben bang dat het regent.)\n• È un peccato che non possa venire. (Het is jammer dat hij niet kan komen.)\n\nOnthoud: emotie + che = congiuntivo."
        },
        "words": ["w1395","w1396","w1397","w1398","w1399","w1400","w1401","w1402"]
    },
    {
        "id": 145, "title": "Werk & solliciteren", "emoji": "💼", "level": "B1",
        "description": "Praat over je werk, ervaring en sollicitaties.",
        "grammar": {
            "title": "Werktaal",
            "body": "Over werk praten:\n\n• Lavoro come… (Ik werk als…)\n• Mi occupo di… (Ik houd me bezig met…)\n• Ho esperienza in/di… (Ik heb ervaring in/met…)\n• Cerco lavoro come… (Ik zoek werk als…)\n\nSolliciteren:\n• Vorrei candidarmi per… (Ik zou me graag kandidaat stellen voor…)\n• Ho lavorato per cinque anni come… (Ik heb vijf jaar gewerkt als…)"
        },
        "words": ["w1403","w1404","w1405","w1406","w1407","w1408","w1409","w1410"]
    },
    {
        "id": 146, "title": "Op kantoor", "emoji": "🖥️", "level": "B1",
        "description": "Woordenschat voor de werkplek, vergaderingen en e-mails.",
        "grammar": {
            "title": "Kantoor- en vergadertaal",
            "body": "Op het werk:\n\n• Fissare una riunione (een vergadering plannen)\n• Mandare un'e-mail (een e-mail sturen)\n• Il termine / la scadenza (de deadline)\n• Lavorare a un progetto (aan een project werken)\n\nVergadertaal:\n• Vorrei proporre… (Ik zou willen voorstellen…)\n• Siamo tutti d'accordo? (Zijn we het allemaal eens?)"
        },
        "words": ["w1411","w1412","w1413","w1414","w1415","w1416","w1417","w1418"]
    },
    {
        "id": 147, "title": "Beroepen & vaardigheden", "emoji": "👷", "level": "B1",
        "description": "Leer meer beroepen en praat over vaardigheden.",
        "grammar": {
            "title": "Beroepen en vaardigheden",
            "body": "Over vaardigheden praten:\n\n• Sono bravo/a in… (Ik ben goed in…)\n• So usare… (Ik kan… gebruiken.)\n• Ho una buona conoscenza di… (Ik heb goede kennis van…)\n• Parlo correntemente… (Ik spreek vloeiend…)\n\nLet op beroepsnamen:\n• m/v: avvocato/avvocata, ingegnere/ingegnera\n• Sommige zijn gelijk: il/la giornalista, il/la dentista"
        },
        "words": ["w1419","w1420","w1421","w1422","w1423","w1424","w1425","w1426"]
    },
    {
        "id": 148, "title": "Discussiëren", "emoji": "🗣️", "level": "B1",
        "description": "Voer een discussie, weerleg argumenten en verdedig je standpunt.",
        "grammar": {
            "title": "Discussietaal",
            "body": "Argumenteren:\n\n• Da un lato… dall'altro… (Aan de ene kant… aan de andere kant…)\n• Tuttavia / però (echter / maar)\n• Inoltre (bovendien)\n• Per esempio (bijvoorbeeld)\n• In conclusione (tot slot)\n\nTegenspreken:\n• Non sono affatto d'accordo. (Ik ben het er helemaal niet mee eens.)\n• Al contrario… (Integendeel…)"
        },
        "words": ["w1427","w1428","w1429","w1430","w1431","w1432","w1433","w1434"]
    },
    {
        "id": 149, "title": "Gevoelens uitdrukken", "emoji": "🎭", "level": "B1",
        "description": "Praat uitgebreid over gevoelens, zorgen en hoop.",
        "grammar": {
            "title": "Gevoelens en gemoedstoestand",
            "body": "Gevoelens:\n\n• Mi sento… (Ik voel me…)\n• Sono preoccupato/a per… (Ik maak me zorgen over…)\n• Spero che… + congiuntivo (Ik hoop dat…)\n• Temo che… + congiuntivo (Ik vrees dat…)\n\nNuances:\n• stufo/a = het zat zijn\n• deluso/a = teleurgesteld\n• sollevato/a = opgelucht\n• commosso/a = ontroerd"
        },
        "words": ["w1435","w1436","w1437","w1438","w1439","w1440","w1441","w1442"]
    },
    {
        "id": 150, "title": "Toetsles — Blok 3", "emoji": "📝", "level": "B1",
        "description": "Test je kennis van de congiuntivo, meningen en werktaal.",
        "grammar": {
            "title": "Samenvatting Blok 3",
            "body": "Wat je hebt geleerd:\n\n• Congiuntivo presente: regelmatig en onregelmatig\n• Meningen geven en reageren\n• Emoties uitdrukken met congiuntivo\n• Werk- en sollicitatiewoordenschat\n• Discussiëren en argumenteren\n\nDe congiuntivo is uitdagend maar maakt je Italiaans veel rijker!"
        },
        "words": ["w1443","w1444","w1445","w1446","w1447","w1448","w1449","w1450"]
    },

    # ═══ BLOK 4: PRONOMI, PASSIEF & GEZONDHEID (151–160) ════════════════════
    {
        "id": 151, "title": "Pronomi combinati", "emoji": "🔗", "level": "B1",
        "description": "Combineer twee voornaamwoorden: 'ik geef het aan jou'.",
        "grammar": {
            "title": "Gecombineerde voornaamwoorden",
            "body": "Twee voornaamwoorden combineren:\n\n• me lo (het aan mij) — Me lo ha dato. (Hij heeft het aan mij gegeven.)\n• te la (haar/het aan jou) — Te la mando domani.\n• glielo (het aan hem/haar/u) — Glielo dico subito.\n• ce lo (het aan ons) — Ce lo hanno spiegato.\n\nVolgorde: indirect (aan wie) + direct (wat), vóór het werkwoord.\nMe/te/gli/ci/vi + lo/la/li/le/ne."
        },
        "words": ["w1451","w1452","w1453","w1454","w1455","w1456","w1457","w1458"]
    },
    {
        "id": 152, "title": "Pronomi — oefening", "emoji": "🎯", "level": "B1",
        "description": "Oefen gecombineerde voornaamwoorden in dagelijkse situaties.",
        "grammar": {
            "title": "Pronomi combinati in de praktijk",
            "body": "Veel voorkomende combinaties:\n\n• Chi te l'ha detto? (Wie heeft het je verteld?)\n• Me ne dai un po'? (Geef je me er een beetje van?)\n• Glielo chiedo io. (Ik vraag het hem/haar wel.)\n• Non ce l'ho. (Ik heb het niet.)\n\nBij infinitief plak je ze achteraan:\n• Posso dirtelo? (Mag ik het je zeggen?)\n• Devo portarglielo. (Ik moet het hem brengen.)"
        },
        "words": ["w1459","w1460","w1461","w1462","w1463","w1464","w1465","w1466"]
    },
    {
        "id": 153, "title": "Passieve vorm", "emoji": "🔄", "level": "B1",
        "description": "Leer de passieve vorm: 'het boek wordt gelezen'.",
        "grammar": {
            "title": "De passieve vorm",
            "body": "De passieve vorm met essere + voltooid deelwoord:\n\n• Il libro è letto da molti. (Het boek wordt door velen gelezen.)\n• La pizza è stata inventata a Napoli. (De pizza is in Napels uitgevonden.)\n• Le email vengono mandate ogni giorno. (De e-mails worden elke dag verstuurd.)\n\nMet 'venire' (voor gewoontes):\n• I giornali vengono consegnati alle 7. (De kranten worden om 7 uur bezorgd.)"
        },
        "words": ["w1467","w1468","w1469","w1470","w1471","w1472","w1473","w1474"]
    },
    {
        "id": 154, "title": "Bij de dokter", "emoji": "🏥", "level": "B1",
        "description": "Beschrijf klachten, begrijp de dokter en bespreek behandeling.",
        "grammar": {
            "title": "Medische taal",
            "body": "Bij de dokter:\n\n• Mi fa male il/la… (Mijn… doet pijn.)\n• Ho mal di testa/stomaco/gola. (Ik heb hoofd-/maag-/keelpijn.)\n• Ho la febbre. (Ik heb koorts.)\n• Da quanto tempo? (Hoe lang al?)\n• Da tre giorni. (Sinds drie dagen.)\n\nDe dokter zegt:\n• Deve prendere questa medicina. (U moet dit medicijn innemen.)\n• Le prescrivo… (Ik schrijf u… voor.)"
        },
        "words": ["w1475","w1476","w1477","w1478","w1479","w1480","w1481","w1482"]
    },
    {
        "id": 155, "title": "Gezondheid & welzijn", "emoji": "🧘", "level": "B1",
        "description": "Praat over een gezonde levensstijl, sport en voeding.",
        "grammar": {
            "title": "Gezondheidsadvies",
            "body": "Gezondheidsadvies met de condizionale:\n\n• Dovresti fare più sport. (Je zou meer moeten sporten.)\n• Sarebbe meglio dormire 8 ore. (Het zou beter zijn om 8 uur te slapen.)\n• Bisognerebbe mangiare più verdura. (Men zou meer groente moeten eten.)\n\nGewoontes beschrijven:\n• Faccio sport tre volte a settimana. (Ik sport drie keer per week.)\n• Cerco di mangiare sano. (Ik probeer gezond te eten.)"
        },
        "words": ["w1483","w1484","w1485","w1486","w1487","w1488","w1489","w1490"]
    },
    {
        "id": 156, "title": "Het lichaam", "emoji": "🦴", "level": "B1",
        "description": "Lichaamsdelen en fysieke beschrijvingen.",
        "grammar": {
            "title": "Lichaamsdelen en beschrijvingen",
            "body": "Lichaamsdelen:\n\n• la testa, il collo, la spalla, il braccio, la mano\n• la schiena, il petto, la pancia, la gamba, il piede\n\nMeervoud let op:\n• il braccio → le braccia (onregelmatig!)\n• il ginocchio → le ginocchia\n• il dito → le dita\n\nBeschrijven: 'Ho le spalle larghe.' (Ik heb brede schouders.)"
        },
        "words": ["w1491","w1492","w1493","w1494","w1495","w1496","w1497","w1498"]
    },
    {
        "id": 157, "title": "Sport & beweging", "emoji": "⚽", "level": "B1",
        "description": "Praat over sport, wedstrijden en lichaamsbeweging.",
        "grammar": {
            "title": "Over sport praten",
            "body": "Sport beoefenen:\n\n• Giocare a + sport met bal: giocare a calcio/tennis/basket\n• Fare + sport zonder bal: fare nuoto/atletica/yoga\n• Andare a + activiteit: andare a correre/sciare\n\nWedstrijden:\n• La partita (de wedstrijd)\n• Vincere/perdere/pareggiare (winnen/verliezen/gelijkspelen)\n• Il tifoso (de fan) — Faccio il tifo per… (Ik juich voor…)"
        },
        "words": ["w1499","w1500","w1501","w1502","w1503","w1504","w1505","w1506"]
    },
    {
        "id": 158, "title": "Voeding & koken", "emoji": "🍳", "level": "B1",
        "description": "Recepten lezen, ingrediënten bespreken en kooktechnieken.",
        "grammar": {
            "title": "Kooktaal",
            "body": "Kookinstructies (imperativo):\n\n• Taglia le verdure. (Snijd de groenten.)\n• Aggiungi il sale. (Voeg het zout toe.)\n• Mescola bene. (Roer goed.)\n• Cuoci per 20 minuti. (Kook 20 minuten.)\n• Lascia raffreddare. (Laat afkoelen.)\n\nHoeveelheden:\n• un pizzico di (een snufje)\n• un cucchiaio di (een lepel)\n• mezzo chilo di (een halve kilo)"
        },
        "words": ["w1507","w1508","w1509","w1510","w1511","w1512","w1513","w1514"]
    },
    {
        "id": 159, "title": "Milieu & natuur", "emoji": "🌍", "level": "B1",
        "description": "Praat over het milieu, klimaat en duurzaamheid.",
        "grammar": {
            "title": "Milieutaal",
            "body": "Over het milieu praten:\n\n• l'inquinamento (de vervuiling)\n• il riscaldamento globale (de opwarming van de aarde)\n• il cambiamento climatico (de klimaatverandering)\n• riciclare (recyclen)\n\nMeningen:\n• È importante che tutti riciclino. (Het is belangrijk dat iedereen recyclet.)\n• Bisogna proteggere l'ambiente. (We moeten het milieu beschermen.)"
        },
        "words": ["w1515","w1516","w1517","w1518","w1519","w1520","w1521","w1522"]
    },
    {
        "id": 160, "title": "Toetsles — Blok 4", "emoji": "📝", "level": "B1",
        "description": "Test je kennis van voornaamwoorden, passief, gezondheid en milieu.",
        "grammar": {
            "title": "Samenvatting Blok 4",
            "body": "Wat je hebt geleerd:\n\n• Gecombineerde voornaamwoorden (me lo, glielo, ce la…)\n• Passieve vorm (essere/venire + voltooid deelwoord)\n• Medische woordenschat en bij de dokter\n• Sport, voeding en gezonde levensstijl\n• Milieu en duurzaamheid\n\nJe bent al halverwege B1 — geweldig!"
        },
        "words": ["w1523","w1524","w1525","w1526","w1527","w1528","w1529","w1530"]
    },

    # ═══ BLOK 5: GERUNDIO, BIJZINNEN & INDIRECTE REDE (161–170) ═════════════
    {
        "id": 161, "title": "Stare + gerundio", "emoji": "🔄", "level": "B1",
        "description": "Beschrijf wat je nu aan het doen bent met stare + gerundio.",
        "grammar": {
            "title": "Stare + gerundio (progressive)",
            "body": "Wat is er nu bezig?\n\n• Sto parlando (ik ben aan het praten)\n• Sto mangiando (ik ben aan het eten)\n• Sta piovendo (het is aan het regenen)\n\nVorming gerundio:\n• -are → -ando: parlare → parlando\n• -ere → -endo: scrivere → scrivendo\n• -ire → -endo: dormire → dormendo\n\nOnregelmatig: fare → facendo, bere → bevendo, dire → dicendo."
        },
        "words": ["w1531","w1532","w1533","w1534","w1535","w1536","w1537","w1538"]
    },
    {
        "id": 162, "title": "Bijzinnen — oorzaak & reden", "emoji": "🔗", "level": "B1",
        "description": "Verbind zinnen met 'omdat', 'aangezien' en 'want'.",
        "grammar": {
            "title": "Causale bijzinnen",
            "body": "Reden geven:\n\n• Perché (omdat) — Non esco perché piove.\n• Siccome (aangezien) — Siccome piove, resto a casa.\n• Dato che / visto che (gezien het feit dat) — Dato che sei qui, parliamo.\n• Poiché (aangezien, formeler) — Poiché non ha risposto, ho chiamato.\n\nLet op: 'siccome' staat altijd aan het begin van de zin.\n'Perché' kan ook 'waarom' betekenen in vragen."
        },
        "words": ["w1539","w1540","w1541","w1542","w1543","w1544","w1545","w1546"]
    },
    {
        "id": 163, "title": "Bijzinnen — tegenstelling", "emoji": "↔️", "level": "B1",
        "description": "Druk tegenstellingen uit met 'hoewel', 'ook al' en 'maar'.",
        "grammar": {
            "title": "Concessieve bijzinnen",
            "body": "Tegenstelling uitdrukken:\n\n• Anche se + indicativo (ook al) — Esco anche se piove.\n• Nonostante + congiuntivo (ondanks dat) — Nonostante sia stanco, lavoro.\n• Sebbene + congiuntivo (hoewel) — Sebbene piova, usciamo.\n• Eppure / tuttavia (en toch / desondanks) — È stanco, eppure lavora.\n\nLet op: 'nonostante' en 'sebbene' vereisen de congiuntivo!"
        },
        "words": ["w1547","w1548","w1549","w1550","w1551","w1552","w1553","w1554"]
    },
    {
        "id": 164, "title": "Bijzinnen — tijd", "emoji": "⏰", "level": "B1",
        "description": "Gebruik 'terwijl', 'voordat', 'nadat' en 'zodra'.",
        "grammar": {
            "title": "Temporele bijzinnen",
            "body": "Tijd uitdrukken:\n\n• Mentre (terwijl) — Mentre mangiavo, leggevo.\n• Prima di + infinito (voordat) — Prima di uscire, mangia.\n• Prima che + congiuntivo — Prima che piova, andiamo.\n• Dopo + infinito passato (nadat) — Dopo aver mangiato, sono uscito.\n• Appena (zodra) — Appena arrivo, ti chiamo.\n• Finché (totdat/zolang) — Aspetto finché torni."
        },
        "words": ["w1555","w1556","w1557","w1558","w1559","w1560","w1561","w1562"]
    },
    {
        "id": 165, "title": "Indirecte rede — basis", "emoji": "🗨️", "level": "B1",
        "description": "Vertel wat iemand anders heeft gezegd.",
        "grammar": {
            "title": "Indirecte rede",
            "body": "Van directe naar indirecte rede:\n\n• Direct: Marco dice: 'Sono stanco.'\n• Indirect: Marco dice che è stanco. (Marco zegt dat hij moe is.)\n\n• Direct: Anna ha detto: 'Vado al cinema.'\n• Indirect: Anna ha detto che andava al cinema.\n\nBij 'ha detto' verschuift de tijd:\n• presente → imperfetto\n• passato prossimo → trapassato prossimo\n• futuro → condizionale"
        },
        "words": ["w1563","w1564","w1565","w1566","w1567","w1568","w1569","w1570"]
    },
    {
        "id": 166, "title": "Indirecte rede — vragen", "emoji": "❓", "level": "B1",
        "description": "Geef indirecte vragen weer: 'hij vroeg of…'.",
        "grammar": {
            "title": "Indirecte vragen",
            "body": "Indirecte vragen:\n\n• Ja/nee-vraag → se:\n  'Vieni?' → Mi ha chiesto se venivo.\n  (Hij vroeg of ik kwam.)\n\n• Vraagwoord blijft:\n  'Dove vai?' → Mi ha chiesto dove andavo.\n  (Hij vroeg waar ik naartoe ging.)\n\n• Let op de tijdverschuiving bij verleden tijd:\n  'Dove sei stato?' → Mi ha chiesto dove ero stato."
        },
        "words": ["w1571","w1572","w1573","w1574","w1575","w1576","w1577","w1578"]
    },
    {
        "id": 167, "title": "Technologie & internet", "emoji": "💻", "level": "B1",
        "description": "Praat over technologie, apps en het digitale leven.",
        "grammar": {
            "title": "Digitale woordenschat",
            "body": "Technologie in het dagelijks leven:\n\n• Scaricare un'app (een app downloaden)\n• Aggiornare il software (de software updaten)\n• Il caricabatterie (de oplader)\n• La connessione (de verbinding)\n• Essere online/offline (online/offline zijn)\n\n'Il digitale ha cambiato tutto.' (Het digitale heeft alles veranderd.)\n'Non funziona il Wi-Fi.' (De wifi werkt niet.)"
        },
        "words": ["w1579","w1580","w1581","w1582","w1583","w1584","w1585","w1586"]
    },
    {
        "id": 168, "title": "Sociale media", "emoji": "📱", "level": "B1",
        "description": "Praat over sociale media, berichten en online communicatie.",
        "grammar": {
            "title": "Sociale mediataal",
            "body": "Online communiceren:\n\n• Postare / pubblicare (posten / publiceren)\n• Condividere (delen)\n• Mettere mi piace (liken)\n• Seguire / smettere di seguire (volgen / ontvolgen)\n• Il profilo (het profiel)\n\nMeningen over sociale media:\n• Penso che i social siano utili. (Ik denk dat social media nuttig zijn.)\n• Trascorro troppo tempo online. (Ik breng te veel tijd online door.)"
        },
        "words": ["w1587","w1588","w1589","w1590","w1591","w1592","w1593","w1594"]
    },
    {
        "id": 169, "title": "Film, boeken & muziek", "emoji": "🎬", "level": "B1",
        "description": "Bespreek films, boeken en muziek die je leuk vindt.",
        "grammar": {
            "title": "Over entertainment praten",
            "body": "Aanbevelen en bespreken:\n\n• Ti consiglio di leggere… (Ik raad je aan om te lezen…)\n• Hai visto l'ultimo film di…? (Heb je de laatste film van… gezien?)\n• Il libro racconta la storia di… (Het boek vertelt het verhaal van…)\n• La colonna sonora è bellissima. (De soundtrack is prachtig.)\n\nGenres:\n• il romanzo (roman), il giallo (thriller), la commedia (komedie)\n• il documentario, il film d'azione (actiefilm)"
        },
        "words": ["w1595","w1596","w1597","w1598","w1599","w1600","w1601","w1602"]
    },
    {
        "id": 170, "title": "Toetsles — Blok 5", "emoji": "📝", "level": "B1",
        "description": "Test je kennis van bijzinnen, indirecte rede en mediataal.",
        "grammar": {
            "title": "Samenvatting Blok 5",
            "body": "Wat je hebt geleerd:\n\n• Stare + gerundio (progressive)\n• Bijzinnen: oorzaak, tegenstelling en tijd\n• Indirecte rede: uitspraken en vragen\n• Technologie en sociale media\n• Film, boeken en muziek bespreken\n\nJe kunt nu complexe zinnen bouwen en vertellen wat anderen zeggen!"
        },
        "words": ["w1603","w1604","w1605","w1606","w1607","w1608","w1609","w1610"]
    },

    # ═══ BLOK 6: VERGELIJKINGEN, HYPOTHESEN & AFSLUITING (171–180) ══════════
    {
        "id": 171, "title": "Vergelijkingen", "emoji": "📊", "level": "B1",
        "description": "Vergelijk dingen en personen: meer, minder, even.",
        "grammar": {
            "title": "Comparativo",
            "body": "Vergelijkingen:\n\n• Più… di/che (meer… dan)\n  Roma è più grande di Firenze.\n• Meno… di/che (minder… dan)\n  Il treno è meno veloce dell'aereo.\n• Così… come / tanto… quanto (even… als)\n  Marco è alto quanto Luca.\n\nWanneer 'di', wanneer 'che'?\n• di: voor zelfstandige naamwoorden en voornaamwoorden\n• che: voor bijvoeglijke naamwoorden, werkwoorden, bijwoorden"
        },
        "words": ["w1611","w1612","w1613","w1614","w1615","w1616","w1617","w1618"]
    },
    {
        "id": 172, "title": "Superlatieven", "emoji": "🏆", "level": "B1",
        "description": "Beschrijf het meeste, het minste en het allergrootste.",
        "grammar": {
            "title": "Superlativo relativo e assoluto",
            "body": "Superlativo relativo (de meeste/minste):\n\n• il/la più… di (de meeste van)\n  Roma è la città più grande d'Italia.\n• il/la meno… di (de minste van)\n  È il meno caro del menu.\n\nSuperlativo assoluto (-issimo):\n• bello → bellissimo (heel mooi)\n• grande → grandissimo (heel groot)\n• buono → buonissimo / ottimo (heel lekker)\n• cattivo → pessimo (heel slecht)\n\nOnregelmatig: il migliore (de beste), il peggiore (de slechtste)."
        },
        "words": ["w1619","w1620","w1621","w1622","w1623","w1624","w1625","w1626"]
    },
    {
        "id": 173, "title": "Hypothese — type 1", "emoji": "🔮", "level": "B1",
        "description": "Maak reële hypothesen: 'als het regent, blijf ik thuis'.",
        "grammar": {
            "title": "Periodo ipotetico tipo 1 (realis)",
            "body": "Reële hypothesen (het kan echt gebeuren):\n\n• Se + presente, presente/futuro\n  Se piove, resto a casa. (Als het regent, blijf ik thuis.)\n  Se piove, resterò a casa. (Als het regent, zal ik thuisblijven.)\n\nMeer voorbeelden:\n• Se hai fame, mangiamo. (Als je honger hebt, eten we.)\n• Se non studi, non impari. (Als je niet studeert, leer je niet.)"
        },
        "words": ["w1627","w1628","w1629","w1630","w1631","w1632","w1633","w1634"]
    },
    {
        "id": 174, "title": "Hypothese — type 2", "emoji": "💫", "level": "B1",
        "description": "Maak irreële hypothesen: 'als ik rijk was, zou ik…'.",
        "grammar": {
            "title": "Periodo ipotetico tipo 2 (irrealis)",
            "body": "Irreële hypothesen (het is niet waar, maar stel je voor…):\n\n• Se + imperfetto congiuntivo, condizionale\n  Se fossi ricco, viaggerei. (Als ik rijk was, zou ik reizen.)\n  Se avessi tempo, leggerei di più. (Als ik tijd had, zou ik meer lezen.)\n\nMeestgebruikte congiuntivo imperfetto:\n• essere: fossi, fossi, fosse, fossimo, foste, fossero\n• avere: avessi, avessi, avesse, avessimo, aveste, avessero"
        },
        "words": ["w1635","w1636","w1637","w1638","w1639","w1640","w1641","w1642"]
    },
    {
        "id": 175, "title": "Formeel & informeel", "emoji": "👔", "level": "B1",
        "description": "Het verschil tussen formeel (Lei) en informeel (tu) taalgebruik.",
        "grammar": {
            "title": "Register: formeel vs. informeel",
            "body": "Formeel (Lei) vs. informeel (tu):\n\n• Scusi / Scusa (sorry/pardon)\n• Potrebbe / Potresti (zou u/zou je)\n• Mi dica / Dimmi (zegt u het / zeg het me)\n• Le presento… / Ti presento… (ik stel u… voor / ik stel je… voor)\n\nWanneer formeel?\n• Met onbekenden, ouderen, in officiële situaties\n• In winkels en restaurants (standaard: Lei)\n• Met collega's (hangt af van de werkcultuur)"
        },
        "words": ["w1643","w1644","w1645","w1646","w1647","w1648","w1649","w1650"]
    },
    {
        "id": 176, "title": "Italiaanse regio's", "emoji": "🗺️", "level": "B1",
        "description": "Leer over de Italiaanse regio's, steden en hun bijzonderheden.",
        "grammar": {
            "title": "Italiaanse geografie",
            "body": "Italië heeft 20 regio's. Belangrijke uitdrukkingen:\n\n• Il nord/centro/sud (het noorden/midden/zuiden)\n• La regione, la provincia, il comune\n• È famoso/a per… (het is beroemd om…)\n• Si trova in… (het bevindt zich in…)\n\nVoorbeelden:\n• La Toscana è famosa per il vino e l'arte.\n• Napoli si trova nel sud dell'Italia.\n• Milano è il capoluogo della Lombardia."
        },
        "words": ["w1651","w1652","w1653","w1654","w1655","w1656","w1657","w1658"]
    },
    {
        "id": 177, "title": "Italiaanse keuken verdieping", "emoji": "🍝", "level": "B1",
        "description": "Ontdek de regionale keuken van Italië en culinaire tradities.",
        "grammar": {
            "title": "Regionale keuken",
            "body": "Elke regio heeft eigen specialiteiten:\n\n• Napoli: la pizza margherita, il ragù napoletano\n• Bologna: le tagliatelle al ragù, la mortadella\n• Roma: la carbonara, l'amatriciana, la cacio e pepe\n• Sicilia: la granita, gli arancini, il cannolo\n\n'Il piatto tipico di questa zona è…'\n(Het typische gerecht van deze streek is…)"
        },
        "words": ["w1659","w1660","w1661","w1662","w1663","w1664","w1665","w1666"]
    },
    {
        "id": 178, "title": "Cultuur & etiquette", "emoji": "🤌", "level": "B1",
        "description": "Leer over Italiaanse gewoontes, etiquette en sociale normen.",
        "grammar": {
            "title": "Italiaanse etiquette",
            "body": "Belangrijke sociale gewoontes:\n\n• Begroeting: twee kussen op de wang (onder vrienden)\n• Eten: il pranzo is de hoofdmaaltijd, cappuccino alleen 's ochtends\n• Koffie: un caffè = espresso, aan de bar is goedkoper dan aan tafel\n• Gebaren: Italianen gebruiken veel handgebaren\n\n'In Italia si fa così.' (In Italië doen ze het zo.)\n'È maleducazione…' (Het is onbeleefd om…)"
        },
        "words": ["w1667","w1668","w1669","w1670","w1671","w1672","w1673","w1674"]
    },
    {
        "id": 179, "title": "Toekomstplannen", "emoji": "🚀", "level": "B1",
        "description": "Praat over je plannen, ambities en wat je nog wilt bereiken.",
        "grammar": {
            "title": "Over de toekomst praten",
            "body": "Toekomstplannen uitdrukken:\n\n• Ho intenzione di… (Ik ben van plan om…)\n• Sto pensando di… (Ik denk eraan om…)\n• Il mio obiettivo è… (Mijn doel is…)\n• Tra cinque anni vorrei… (Over vijf jaar zou ik…)\n• Spero di riuscire a… (Ik hoop erin te slagen om…)\n\nCombineer futuro + condizionale voor nuance."
        },
        "words": ["w1675","w1676","w1677","w1678","w1679","w1680","w1681","w1682"]
    },
    {
        "id": 180, "title": "🎓 B1 afgerond!", "emoji": "🎓", "level": "B1",
        "description": "Gefeliciteerd! Je hebt B1 afgerond. Kijk terug en blik vooruit.",
        "grammar": {
            "title": "Gefeliciteerd — B1 compleet!",
            "body": "Wat je nu kunt:\n\n• Verhalen vertellen in het verleden (imperfetto + passato prossimo)\n• Beleefd verzoeken en wensen uitdrukken (condizionale)\n• Meningen geven en discussiëren (congiuntivo)\n• Complexe zinnen bouwen (bijzinnen, indirecte rede)\n• Vergelijken en hypothesen maken\n\nJe beheerst nu ~1500 Italiaanse woorden — meer dan genoeg voor dagelijkse conversaties, reizen en het lezen van eenvoudige teksten. Complimenti! 🇮🇹"
        },
        "words": ["w1683","w1684","w1685","w1686","w1687","w1688","w1689","w1690"]
    },
]

# ── WOORDENLIJST ──────────────────────────────────────────────────────────────

new_words = [
    # ── Les 121: Imperfetto regelmatig ──
    {"id":"w1211","it":"raccontare","nl":"vertellen","ph":"rak-kon-TA-re","ex":"Da bambino raccontavo sempre storie.","exNl":"Als kind vertelde ik altijd verhalen.","lesson":121,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1212","it":"crescere","nl":"groeien/opgroeien","ph":"KRES-tsje-re","ex":"Crescevo in una piccola città.","exNl":"Ik groeide op in een kleine stad.","lesson":121,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1213","it":"la memoria","nl":"de herinnering","ph":"la me-MO-rja","ex":"Ho una bella memoria di quel giorno.","exNl":"Ik heb een mooie herinnering aan die dag.","lesson":121,"level":"B1","cat":"memoria"},
    {"id":"w1214","it":"l'infanzia","nl":"de kindertijd","ph":"lin-FAN-tsja","ex":"L'infanzia è un periodo speciale.","exNl":"De kindertijd is een speciale periode.","lesson":121,"level":"B1","cat":"memoria"},
    {"id":"w1215","it":"descrivere","nl":"beschrijven","ph":"des-KRI-ve-re","ex":"Descrivevo il paesaggio con cura.","exNl":"Ik beschreef het landschap met zorg.","lesson":121,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1216","it":"il quartiere","nl":"de wijk/buurt","ph":"il kwar-TJE-re","ex":"Il mio quartiere era molto tranquillo.","exNl":"Mijn wijk was erg rustig.","lesson":121,"level":"B1","cat":"luogo"},
    {"id":"w1217","it":"frequentare","nl":"bezoeken/volgen","ph":"fre-kwen-TA-re","ex":"Frequentavo la scuola elementare.","exNl":"Ik bezocht de basisschool.","lesson":121,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1218","it":"il ricordo","nl":"de herinnering","ph":"il ri-KOR-do","ex":"È un ricordo molto bello.","exNl":"Het is een heel mooie herinnering.","lesson":121,"level":"B1","cat":"memoria"},

    # ── Les 122: Imperfetto onregelmatig ──
    {"id":"w1219","it":"tradurre","nl":"vertalen","ph":"tra-DUR-re","ex":"Traducevo testi dall'italiano al nederlandese.","exNl":"Ik vertaalde teksten van Italiaans naar Nederlands.","lesson":122,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1220","it":"produrre","nl":"produceren","ph":"pro-DUR-re","ex":"La fabbrica produceva scarpe.","exNl":"De fabriek produceerde schoenen.","lesson":122,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1221","it":"proporre","nl":"voorstellen","ph":"pro-POR-re","ex":"Proponeva sempre nuove idee.","exNl":"Hij stelde altijd nieuwe ideeën voor.","lesson":122,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1222","it":"supporre","nl":"veronderstellen","ph":"sup-POR-re","ex":"Supponevo che fosse vero.","exNl":"Ik veronderstelde dat het waar was.","lesson":122,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1223","it":"distrarre","nl":"afleiden","ph":"dis-TRAR-re","ex":"Il rumore mi distraeva.","exNl":"Het lawaai leidde me af.","lesson":122,"level":"B1","cat":"verbo_imperfetto"},
    {"id":"w1224","it":"il rumore","nl":"het lawaai/geluid","ph":"il ru-MO-re","ex":"C'era un rumore strano.","exNl":"Er was een vreemd geluid.","lesson":122,"level":"B1","cat":"sostantivo"},
    {"id":"w1225","it":"la fabbrica","nl":"de fabriek","ph":"la FAB-bri-ka","ex":"La fabbrica era vicino a casa.","exNl":"De fabriek was dicht bij huis.","lesson":122,"level":"B1","cat":"luogo"},
    {"id":"w1226","it":"attrarre","nl":"aantrekken","ph":"at-TRAR-re","ex":"Il museo attraeva molti turisti.","exNl":"Het museum trok veel toeristen aan.","lesson":122,"level":"B1","cat":"verbo_imperfetto"},

    # ── Les 123: Imperfetto vs. passato prossimo ──
    {"id":"w1227","it":"mentre","nl":"terwijl","ph":"MEN-tre","ex":"Mentre dormivo, ha suonato il telefono.","exNl":"Terwijl ik sliep, ging de telefoon.","lesson":123,"level":"B1","cat":"congiunzione"},
    {"id":"w1228","it":"improvvisamente","nl":"plotseling","ph":"im-prov-vi-za-MEN-te","ex":"Improvvisamente è arrivata la polizia.","exNl":"Plotseling arriveerde de politie.","lesson":123,"level":"B1","cat":"avverbio"},
    {"id":"w1229","it":"succedere","nl":"gebeuren","ph":"sut-TSJE-de-re","ex":"Cosa è successo ieri?","exNl":"Wat is er gisteren gebeurd?","lesson":123,"level":"B1","cat":"verbo"},
    {"id":"w1230","it":"accorgersi","nl":"zich realiseren","ph":"ak-KOR-djer-si","ex":"Mi sono accorto che pioveva.","exNl":"Ik realiseerde me dat het regende.","lesson":123,"level":"B1","cat":"verbo"},
    {"id":"w1231","it":"nel frattempo","nl":"ondertussen","ph":"nel frat-TEM-po","ex":"Nel frattempo, io aspettavo.","exNl":"Ondertussen wachtte ik.","lesson":123,"level":"B1","cat":"avverbio"},
    {"id":"w1232","it":"rendersi conto","nl":"zich realiseren","ph":"REN-der-si KON-to","ex":"Mi sono reso conto dell'errore.","exNl":"Ik realiseerde me de fout.","lesson":123,"level":"B1","cat":"espressione"},
    {"id":"w1233","it":"all'improvviso","nl":"opeens","ph":"al-lim-prov-VI-zo","ex":"All'improvviso si è spenta la luce.","exNl":"Opeens ging het licht uit.","lesson":123,"level":"B1","cat":"avverbio"},
    {"id":"w1234","it":"in quel momento","nl":"op dat moment","ph":"in kwel mo-MEN-to","ex":"In quel momento ho capito tutto.","exNl":"Op dat moment begreep ik alles.","lesson":123,"level":"B1","cat":"espressione"},

    # ── Les 124: Herinneringen ──
    {"id":"w1235","it":"da bambino","nl":"als kind","ph":"da bam-BI-no","ex":"Da bambino giocavo nel parco.","exNl":"Als kind speelde ik in het park.","lesson":124,"level":"B1","cat":"espressione"},
    {"id":"w1236","it":"a quei tempi","nl":"in die tijd","ph":"a kwej TEM-pi","ex":"A quei tempi non c'era internet.","exNl":"In die tijd was er geen internet.","lesson":124,"level":"B1","cat":"espressione"},
    {"id":"w1237","it":"ricordarsi","nl":"zich herinneren","ph":"ri-kor-DAR-si","ex":"Mi ricordo le vacanze al mare.","exNl":"Ik herinner me de vakanties aan zee.","lesson":124,"level":"B1","cat":"verbo"},
    {"id":"w1238","it":"la gioventù","nl":"de jeugd","ph":"la djo-ven-TU","ex":"La gioventù passa in fretta.","exNl":"De jeugd gaat snel voorbij.","lesson":124,"level":"B1","cat":"memoria"},
    {"id":"w1239","it":"il compagno","nl":"de klasgenoot/kameraad","ph":"il kom-PAN-jo","ex":"Il mio compagno di scuola si chiamava Marco.","exNl":"Mijn klasgenoot heette Marco.","lesson":124,"level":"B1","cat":"persona"},
    {"id":"w1240","it":"il giocattolo","nl":"het speelgoed","ph":"il djo-KAT-to-lo","ex":"Avevo molti giocattoli.","exNl":"Ik had veel speelgoed.","lesson":124,"level":"B1","cat":"oggetto"},
    {"id":"w1241","it":"la favola","nl":"het sprookje","ph":"la FA-vo-la","ex":"La nonna mi raccontava le favole.","exNl":"Oma vertelde me sprookjes.","lesson":124,"level":"B1","cat":"cultura"},
    {"id":"w1242","it":"il cortile","nl":"de binnenplaats","ph":"il kor-TI-le","ex":"Giocavamo nel cortile della scuola.","exNl":"We speelden op de binnenplaats van school.","lesson":124,"level":"B1","cat":"luogo"},

    # ── Les 125: Gewoontes vroeger ──
    {"id":"w1243","it":"di solito","nl":"gewoonlijk","ph":"di SO-li-to","ex":"Di solito andavo a letto presto.","exNl":"Gewoonlijk ging ik vroeg naar bed.","lesson":125,"level":"B1","cat":"avverbio"},
    {"id":"w1244","it":"ogni tanto","nl":"af en toe","ph":"ON-ji TAN-to","ex":"Ogni tanto uscivamo a cena.","exNl":"Af en toe gingen we uit eten.","lesson":125,"level":"B1","cat":"avverbio"},
    {"id":"w1245","it":"l'abitudine","nl":"de gewoonte","ph":"la-bi-TU-di-ne","ex":"Avevo l'abitudine di leggere prima di dormire.","exNl":"Ik had de gewoonte om te lezen voor het slapengaan.","lesson":125,"level":"B1","cat":"sostantivo"},
    {"id":"w1246","it":"quotidiano","nl":"dagelijks","ph":"kwo-ti-DJA-no","ex":"La vita quotidiana era semplice.","exNl":"Het dagelijks leven was eenvoudig.","lesson":125,"level":"B1","cat":"aggettivo"},
    {"id":"w1247","it":"annoiarsi","nl":"zich vervelen","ph":"an-no-JAR-si","ex":"Mi annoiavo a scuola.","exNl":"Ik verveelde me op school.","lesson":125,"level":"B1","cat":"verbo"},
    {"id":"w1248","it":"divertirsi","nl":"plezier hebben","ph":"di-ver-TIR-si","ex":"Ci divertivamo molto in estate.","exNl":"We hadden veel plezier in de zomer.","lesson":125,"level":"B1","cat":"verbo"},
    {"id":"w1249","it":"la passeggiata","nl":"de wandeling","ph":"la pas-sed-DJA-ta","ex":"Facevamo una passeggiata dopo cena.","exNl":"We maakten een wandeling na het eten.","lesson":125,"level":"B1","cat":"attività"},
    {"id":"w1250","it":"il pomeriggio","nl":"de middag","ph":"il po-me-RID-djo","ex":"Il pomeriggio studiavo sempre.","exNl":"'s Middags studeerde ik altijd.","lesson":125,"level":"B1","cat":"tempo"},

    # ── Les 126: Verhalen vertellen deel 1 ──
    {"id":"w1251","it":"la trama","nl":"het plot/de verhaallijn","ph":"la TRA-ma","ex":"La trama del film era avvincente.","exNl":"Het plot van de film was meeslepend.","lesson":126,"level":"B1","cat":"narrativa"},
    {"id":"w1252","it":"il protagonista","nl":"de hoofdpersoon","ph":"il pro-ta-go-NIS-ta","ex":"Il protagonista era un giovane avvocato.","exNl":"De hoofdpersoon was een jonge advocaat.","lesson":126,"level":"B1","cat":"narrativa"},
    {"id":"w1253","it":"svolgersi","nl":"plaatsvinden","ph":"ZVOL-djer-si","ex":"La storia si svolgeva a Roma.","exNl":"Het verhaal speelde zich af in Rome.","lesson":126,"level":"B1","cat":"verbo"},
    {"id":"w1254","it":"c'era una volta","nl":"er was eens","ph":"TSJE-ra U-na VOL-ta","ex":"C'era una volta un re molto saggio.","exNl":"Er was eens een heel wijze koning.","lesson":126,"level":"B1","cat":"espressione"},
    {"id":"w1255","it":"avvincente","nl":"meeslepend/boeiend","ph":"av-vin-TSJEN-te","ex":"Il libro è davvero avvincente.","exNl":"Het boek is echt meeslepend.","lesson":126,"level":"B1","cat":"aggettivo"},
    {"id":"w1256","it":"il personaggio","nl":"het personage","ph":"il per-so-NAD-djo","ex":"Il personaggio principale era simpatico.","exNl":"Het hoofdpersonage was aardig.","lesson":126,"level":"B1","cat":"narrativa"},
    {"id":"w1257","it":"ambientato","nl":"gesitueerd","ph":"am-bjen-TA-to","ex":"Il romanzo è ambientato nel Medioevo.","exNl":"De roman is gesitueerd in de Middeleeuwen.","lesson":126,"level":"B1","cat":"aggettivo"},
    {"id":"w1258","it":"il capitolo","nl":"het hoofdstuk","ph":"il ka-PI-to-lo","ex":"Ho letto tre capitoli ieri sera.","exNl":"Ik heb gisteren drie hoofdstukken gelezen.","lesson":126,"level":"B1","cat":"narrativa"},

    # ── Les 127: Verhalen vertellen deel 2 ──
    {"id":"w1259","it":"poi","nl":"daarna/vervolgens","ph":"poj","ex":"Poi siamo andati al ristorante.","exNl":"Daarna zijn we naar het restaurant gegaan.","lesson":127,"level":"B1","cat":"avverbio"},
    {"id":"w1260","it":"alla fine","nl":"uiteindelijk","ph":"AL-la FI-ne","ex":"Alla fine tutto è andato bene.","exNl":"Uiteindelijk is alles goed gegaan.","lesson":127,"level":"B1","cat":"avverbio"},
    {"id":"w1261","it":"per fortuna","nl":"gelukkig","ph":"per for-TU-na","ex":"Per fortuna non era grave.","exNl":"Gelukkig was het niet ernstig.","lesson":127,"level":"B1","cat":"espressione"},
    {"id":"w1262","it":"purtroppo","nl":"helaas","ph":"pur-TROP-po","ex":"Purtroppo non posso venire.","exNl":"Helaas kan ik niet komen.","lesson":127,"level":"B1","cat":"avverbio"},
    {"id":"w1263","it":"il risultato","nl":"het resultaat","ph":"il ri-zul-TA-to","ex":"Il risultato è stato sorprendente.","exNl":"Het resultaat was verrassend.","lesson":127,"level":"B1","cat":"sostantivo"},
    {"id":"w1264","it":"riuscire","nl":"erin slagen","ph":"rju-SHI-re","ex":"Sono riuscito a finire in tempo.","exNl":"Ik ben erin geslaagd op tijd te eindigen.","lesson":127,"level":"B1","cat":"verbo"},
    {"id":"w1265","it":"sorprendente","nl":"verrassend","ph":"sor-pren-DEN-te","ex":"La notizia è stata sorprendente.","exNl":"Het nieuws was verrassend.","lesson":127,"level":"B1","cat":"aggettivo"},
    {"id":"w1266","it":"la conclusione","nl":"de conclusie/het einde","ph":"la kon-klu-ZJO-ne","ex":"In conclusione, è stata una bella giornata.","exNl":"Tot slot, het was een mooie dag.","lesson":127,"level":"B1","cat":"sostantivo"},

    # ── Les 128: Het weer beschrijven ──
    {"id":"w1267","it":"il temporale","nl":"de onweersbui","ph":"il tem-po-RA-le","ex":"Ieri c'è stato un forte temporale.","exNl":"Gisteren was er een flinke onweersbui.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1268","it":"la nebbia","nl":"de mist","ph":"la NEB-bja","ex":"Stamattina c'era molta nebbia.","exNl":"Vanochtend was er veel mist.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1269","it":"il fulmine","nl":"de bliksem","ph":"il FUL-mi-ne","ex":"Ho visto un fulmine in lontananza.","exNl":"Ik zag een bliksem in de verte.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1270","it":"il tuono","nl":"de donder","ph":"il TWO-no","ex":"Il tuono era fortissimo.","exNl":"De donder was heel hard.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1271","it":"la grandine","nl":"de hagel","ph":"la GRAN-di-ne","ex":"È caduta la grandine.","exNl":"Er viel hagel.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1272","it":"umido","nl":"vochtig","ph":"U-mi-do","ex":"Il clima qui è molto umido.","exNl":"Het klimaat hier is erg vochtig.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1273","it":"secco","nl":"droog","ph":"SEK-ko","ex":"L'estate è stata molto secca.","exNl":"De zomer was erg droog.","lesson":128,"level":"B1","cat":"meteo"},
    {"id":"w1274","it":"le previsioni","nl":"de voorspellingen","ph":"le pre-vi-ZJO-ni","ex":"Le previsioni dicono che pioverà.","exNl":"De voorspellingen zeggen dat het gaat regenen.","lesson":128,"level":"B1","cat":"meteo"},

    # ── Les 129: Emoties in het verleden ──
    {"id":"w1275","it":"emozionato","nl":"ontroerd/opgewonden","ph":"e-mo-tsjo-NA-to","ex":"Ero molto emozionato per la partenza.","exNl":"Ik was erg opgewonden over het vertrek.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1276","it":"deluso","nl":"teleurgesteld","ph":"de-LU-zo","ex":"Ero deluso dal risultato.","exNl":"Ik was teleurgesteld door het resultaat.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1277","it":"sollevato","nl":"opgelucht","ph":"sol-le-VA-to","ex":"Mi sono sentito sollevato.","exNl":"Ik voelde me opgelucht.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1278","it":"stufo","nl":"het zat","ph":"STU-fo","ex":"Ero stufo di aspettare.","exNl":"Ik was het zat om te wachten.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1279","it":"commosso","nl":"ontroerd","ph":"kom-MOS-so","ex":"Ero commosso dalle sue parole.","exNl":"Ik was ontroerd door zijn woorden.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1280","it":"spaventato","nl":"bang/geschrokken","ph":"spa-ven-TA-to","ex":"Ero spaventato dal temporale.","exNl":"Ik was bang van het onweer.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1281","it":"orgoglioso","nl":"trots","ph":"or-gol-JO-zo","ex":"Ero orgoglioso di mio figlio.","exNl":"Ik was trots op mijn zoon.","lesson":129,"level":"B1","cat":"emozione"},
    {"id":"w1282","it":"geloso","nl":"jaloers","ph":"dje-LO-zo","ex":"Non essere geloso!","exNl":"Wees niet jaloers!","lesson":129,"level":"B1","cat":"emozione"},

    # ── Les 130: Toetsles Blok 1 ──
    {"id":"w1283","it":"il passato","nl":"het verleden","ph":"il pas-SA-to","ex":"Il passato non si può cambiare.","exNl":"Het verleden kun je niet veranderen.","lesson":130,"level":"B1","cat":"tempo"},
    {"id":"w1284","it":"l'epoca","nl":"het tijdperk","ph":"LE-po-ka","ex":"Era un'epoca diversa.","exNl":"Het was een ander tijdperk.","lesson":130,"level":"B1","cat":"tempo"},
    {"id":"w1285","it":"cambiare","nl":"veranderen","ph":"kam-BJA-re","ex":"Tutto è cambiato da allora.","exNl":"Alles is sindsdien veranderd.","lesson":130,"level":"B1","cat":"verbo"},
    {"id":"w1286","it":"scomparire","nl":"verdwijnen","ph":"skom-pa-RI-re","ex":"Quel negozio è scomparso.","exNl":"Die winkel is verdwenen.","lesson":130,"level":"B1","cat":"verbo"},
    {"id":"w1287","it":"rimanere","nl":"blijven/overblijven","ph":"ri-ma-NE-re","ex":"Sono rimasto sorpreso.","exNl":"Ik was verrast.","lesson":130,"level":"B1","cat":"verbo"},
    {"id":"w1288","it":"il secolo","nl":"de eeuw","ph":"il SE-ko-lo","ex":"Nel ventesimo secolo è cambiato molto.","exNl":"In de twintigste eeuw is er veel veranderd.","lesson":130,"level":"B1","cat":"tempo"},
    {"id":"w1289","it":"trasformare","nl":"transformeren","ph":"traz-for-MA-re","ex":"La città si è trasformata.","exNl":"De stad is getransformeerd.","lesson":130,"level":"B1","cat":"verbo"},
    {"id":"w1290","it":"la generazione","nl":"de generatie","ph":"la dje-ne-ra-TSJO-ne","ex":"Ogni generazione è diversa.","exNl":"Elke generatie is anders.","lesson":130,"level":"B1","cat":"persona"},

    # ── Les 131: Condizionale regelmatig ──
    {"id":"w1291","it":"desiderare","nl":"wensen/verlangen","ph":"de-zi-de-RA-re","ex":"Desidererei un mondo più giusto.","exNl":"Ik zou een rechtvaardigere wereld wensen.","lesson":131,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1292","it":"preferire","nl":"de voorkeur geven","ph":"pre-fe-RI-re","ex":"Preferirei restare a casa.","exNl":"Ik zou liever thuisblijven.","lesson":131,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1293","it":"immaginare","nl":"zich voorstellen","ph":"im-ma-dji-NA-re","ex":"Immagineresti di vivere qui?","exNl":"Zou je je voorstellen om hier te wonen?","lesson":131,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1294","it":"accettare","nl":"accepteren","ph":"at-tsjet-TA-re","ex":"Accetterei volentieri l'invito.","exNl":"Ik zou de uitnodiging graag accepteren.","lesson":131,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1295","it":"rinunciare","nl":"afzien van","ph":"ri-nun-TSJA-re","ex":"Non rinuncerei mai a questo lavoro.","exNl":"Ik zou nooit van deze baan afzien.","lesson":131,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1296","it":"trasferirsi","nl":"verhuizen","ph":"traz-fe-RIR-si","ex":"Mi trasferirei in Toscana.","exNl":"Ik zou naar Toscane verhuizen.","lesson":131,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1297","it":"il desiderio","nl":"de wens","ph":"il de-zi-DE-rjo","ex":"Il mio desiderio sarebbe viaggiare.","exNl":"Mijn wens zou zijn om te reizen.","lesson":131,"level":"B1","cat":"sostantivo"},
    {"id":"w1298","it":"volentieri","nl":"graag/met plezier","ph":"vo-len-TJE-ri","ex":"Verrei volentieri alla festa.","exNl":"Ik zou graag naar het feest komen.","lesson":131,"level":"B1","cat":"avverbio"},

    # ── Les 132: Condizionale onregelmatig ──
    {"id":"w1299","it":"rimanere","nl":"blijven","ph":"ri-ma-NE-re","ex":"Rimarrei volentieri ancora un giorno.","exNl":"Ik zou graag nog een dag blijven.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1300","it":"tenere","nl":"houden","ph":"te-NE-re","ex":"Terrei questo libro per sempre.","exNl":"Ik zou dit boek voor altijd houden.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1301","it":"sapere","nl":"weten/kennen","ph":"sa-PE-re","ex":"Saprei rispondere a questa domanda.","exNl":"Ik zou op deze vraag kunnen antwoorden.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1302","it":"vedere","nl":"zien","ph":"ve-DE-re","ex":"Vedrei volentieri quel film.","exNl":"Ik zou die film graag zien.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1303","it":"vivere","nl":"leven/wonen","ph":"VI-ve-re","ex":"Vivrei in una casa al mare.","exNl":"Ik zou in een huis aan zee wonen.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1304","it":"cadere","nl":"vallen","ph":"ka-DE-re","ex":"Senza questo lavoro, cadrei in depressione.","exNl":"Zonder dit werk zou ik in een depressie vallen.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1305","it":"valere","nl":"waard zijn","ph":"va-LE-re","ex":"Varrebbe la pena provare.","exNl":"Het zou de moeite waard zijn om te proberen.","lesson":132,"level":"B1","cat":"verbo_condizionale"},
    {"id":"w1306","it":"la pena","nl":"de moeite","ph":"la PE-na","ex":"Vale la pena visitare Venezia.","exNl":"Het is de moeite waard om Venetië te bezoeken.","lesson":132,"level":"B1","cat":"espressione"},

    # ── Les 133: Beleefd verzoeken ──
    {"id":"w1307","it":"il favore","nl":"de gunst","ph":"il fa-VO-re","ex":"Mi farebbe un favore?","exNl":"Zou u me een gunst doen?","lesson":133,"level":"B1","cat":"sostantivo"},
    {"id":"w1308","it":"gentile","nl":"vriendelijk","ph":"djen-TI-le","ex":"Sarebbe così gentile da aiutarmi?","exNl":"Zou u zo vriendelijk zijn om me te helpen?","lesson":133,"level":"B1","cat":"aggettivo"},
    {"id":"w1309","it":"disturbare","nl":"storen","ph":"dis-tur-BA-re","ex":"Scusi, potrei disturbarla un momento?","exNl":"Sorry, zou ik u even mogen storen?","lesson":133,"level":"B1","cat":"verbo"},
    {"id":"w1310","it":"indicare","nl":"aanwijzen/aangeven","ph":"in-di-KA-re","ex":"Potrebbe indicarmi la strada?","exNl":"Zou u me de weg kunnen wijzen?","lesson":133,"level":"B1","cat":"verbo"},
    {"id":"w1311","it":"prestare","nl":"lenen (aan iemand)","ph":"pres-TA-re","ex":"Mi presteresti la penna?","exNl":"Zou je me je pen willen lenen?","lesson":133,"level":"B1","cat":"verbo"},
    {"id":"w1312","it":"spostare","nl":"verplaatsen","ph":"spos-TA-re","ex":"Potrebbe spostare la macchina?","exNl":"Zou u de auto kunnen verplaatsen?","lesson":133,"level":"B1","cat":"verbo"},
    {"id":"w1313","it":"il permesso","nl":"de toestemming","ph":"il per-MES-so","ex":"Avrei bisogno del suo permesso.","exNl":"Ik zou uw toestemming nodig hebben.","lesson":133,"level":"B1","cat":"sostantivo"},
    {"id":"w1314","it":"dispiacere","nl":"spijten","ph":"dis-pja-TSJE-re","ex":"Le dispiacerebbe ripetere?","exNl":"Zou het u spijten om te herhalen?","lesson":133,"level":"B1","cat":"verbo"},

    # ── Les 134: Wensen & dromen ──
    {"id":"w1315","it":"il sogno","nl":"de droom","ph":"il SON-jo","ex":"Il mio sogno è vivere in Italia.","exNl":"Mijn droom is om in Italië te wonen.","lesson":134,"level":"B1","cat":"sostantivo"},
    {"id":"w1316","it":"realizzare","nl":"verwezenlijken","ph":"re-a-lid-ZA-re","ex":"Vorrei realizzare i miei sogni.","exNl":"Ik zou mijn dromen willen verwezenlijken.","lesson":134,"level":"B1","cat":"verbo"},
    {"id":"w1317","it":"il futuro","nl":"de toekomst","ph":"il fu-TU-ro","ex":"Come vedi il tuo futuro?","exNl":"Hoe zie jij je toekomst?","lesson":134,"level":"B1","cat":"tempo"},
    {"id":"w1318","it":"sperare","nl":"hopen","ph":"spe-RA-re","ex":"Spero di riuscirci.","exNl":"Ik hoop dat het me lukt.","lesson":134,"level":"B1","cat":"verbo"},
    {"id":"w1319","it":"l'ambizione","nl":"de ambitie","ph":"lam-bi-TSJO-ne","ex":"Ha molta ambizione.","exNl":"Hij heeft veel ambitie.","lesson":134,"level":"B1","cat":"sostantivo"},
    {"id":"w1320","it":"raggiungere","nl":"bereiken","ph":"rad-DJUN-dje-re","ex":"Vorrei raggiungere il mio obiettivo.","exNl":"Ik zou mijn doel willen bereiken.","lesson":134,"level":"B1","cat":"verbo"},
    {"id":"w1321","it":"l'obiettivo","nl":"het doel","ph":"lo-bjet-TI-vo","ex":"Il mio obiettivo è parlare italiano.","exNl":"Mijn doel is Italiaans spreken.","lesson":134,"level":"B1","cat":"sostantivo"},
    {"id":"w1322","it":"riuscire","nl":"erin slagen","ph":"rju-SHI-re","ex":"Spero di riuscire a imparare.","exNl":"Ik hoop dat ik erin slaag om te leren.","lesson":134,"level":"B1","cat":"verbo"},

    # ── Les 135: Advies geven ──
    {"id":"w1323","it":"consigliare","nl":"aanraden","ph":"kon-sil-JA-re","ex":"Ti consiglierei di studiare di più.","exNl":"Ik zou je aanraden om meer te studeren.","lesson":135,"level":"B1","cat":"verbo"},
    {"id":"w1324","it":"il consiglio","nl":"het advies","ph":"il kon-SIL-jo","ex":"Mi daresti un consiglio?","exNl":"Zou je me een advies geven?","lesson":135,"level":"B1","cat":"sostantivo"},
    {"id":"w1325","it":"suggerire","nl":"suggereren","ph":"sud-dje-RI-re","ex":"Cosa mi suggeriresti?","exNl":"Wat zou je me suggereren?","lesson":135,"level":"B1","cat":"verbo"},
    {"id":"w1326","it":"evitare","nl":"vermijden","ph":"e-vi-TA-re","ex":"Dovresti evitare lo stress.","exNl":"Je zou stress moeten vermijden.","lesson":135,"level":"B1","cat":"verbo"},
    {"id":"w1327","it":"al posto tuo","nl":"op jouw plaats","ph":"al POS-to TU-o","ex":"Al posto tuo, accetterei.","exNl":"Op jouw plaats zou ik accepteren.","lesson":135,"level":"B1","cat":"espressione"},
    {"id":"w1328","it":"la scelta","nl":"de keuze","ph":"la SHEL-ta","ex":"È una scelta difficile.","exNl":"Het is een moeilijke keuze.","lesson":135,"level":"B1","cat":"sostantivo"},
    {"id":"w1329","it":"decidere","nl":"beslissen","ph":"de-TSJ-de-re","ex":"Dovresti decidere presto.","exNl":"Je zou snel moeten beslissen.","lesson":135,"level":"B1","cat":"verbo"},
    {"id":"w1330","it":"la soluzione","nl":"de oplossing","ph":"la so-lu-TSJO-ne","ex":"Ci sarebbe un'altra soluzione.","exNl":"Er zou een andere oplossing zijn.","lesson":135,"level":"B1","cat":"sostantivo"},

    # ── Les 136: Op restaurant ──
    {"id":"w1331","it":"prenotare","nl":"reserveren","ph":"pre-no-TA-re","ex":"Vorrei prenotare un tavolo per due.","exNl":"Ik zou graag een tafel voor twee reserveren.","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1332","it":"il menù","nl":"het menu","ph":"il me-NU","ex":"Potrei vedere il menù?","exNl":"Zou ik het menu mogen zien?","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1333","it":"il contorno","nl":"het bijgerecht","ph":"il kon-TOR-no","ex":"Come contorno vorrei le patate.","exNl":"Als bijgerecht zou ik aardappelen willen.","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1334","it":"il conto","nl":"de rekening","ph":"il KON-to","ex":"Potrei avere il conto, per favore?","exNl":"Zou ik de rekening mogen, alstublieft?","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1335","it":"il coperto","nl":"het couvert","ph":"il ko-PER-to","ex":"Il coperto costa due euro.","exNl":"Het couvert kost twee euro.","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1336","it":"il piatto del giorno","nl":"het daggerecht","ph":"il PJAT-to del DJOR-no","ex":"Qual è il piatto del giorno?","exNl":"Wat is het daggerecht?","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1337","it":"la mancia","nl":"de fooi","ph":"la MAN-tsja","ex":"In Italia la mancia non è obbligatoria.","exNl":"In Italië is de fooi niet verplicht.","lesson":136,"level":"B1","cat":"ristorante"},
    {"id":"w1338","it":"assaggiare","nl":"proeven","ph":"as-sad-DJA-re","ex":"Vorrei assaggiare il tiramisù.","exNl":"Ik zou de tiramisu willen proeven.","lesson":136,"level":"B1","cat":"ristorante"},

    # ── Les 137: Reisplannen maken ──
    {"id":"w1339","it":"la destinazione","nl":"de bestemming","ph":"la des-ti-na-TSJO-ne","ex":"Quale sarebbe la destinazione ideale?","exNl":"Wat zou de ideale bestemming zijn?","lesson":137,"level":"B1","cat":"viaggio"},
    {"id":"w1340","it":"il volo","nl":"de vlucht","ph":"il VO-lo","ex":"Ho prenotato un volo per Roma.","exNl":"Ik heb een vlucht naar Rome geboekt.","lesson":137,"level":"B1","cat":"viaggio"},
    {"id":"w1341","it":"la valigia","nl":"de koffer","ph":"la va-LI-dja","ex":"Devo ancora fare la valigia.","exNl":"Ik moet nog de koffer pakken.","lesson":137,"level":"B1","cat":"viaggio"},
    {"id":"w1342","it":"il passaporto","nl":"het paspoort","ph":"il pas-sa-POR-to","ex":"Hai controllato il passaporto?","exNl":"Heb je het paspoort gecontroleerd?","lesson":137,"level":"B1","cat":"viaggio"},
    {"id":"w1343","it":"la guida turistica","nl":"de reisgids","ph":"la GWI-da tu-RIS-ti-ka","ex":"La guida turistica consiglia questo museo.","exNl":"De reisgids beveelt dit museum aan.","lesson":137,"level":"B1","cat":"viaggio"},
    {"id":"w1344","it":"in anticipo","nl":"van tevoren","ph":"in an-TI-tsji-po","ex":"Dovremmo prenotare in anticipo.","exNl":"We zouden van tevoren moeten boeken.","lesson":137,"level":"B1","cat":"espressione"},
    {"id":"w1345","it":"l'itinerario","nl":"de route/het reisplan","ph":"li-ti-ne-RA-rjo","ex":"Ho preparato un itinerario.","exNl":"Ik heb een reisplan voorbereid.","lesson":137,"level":"B1","cat":"viaggio"},
    {"id":"w1346","it":"la crociera","nl":"de cruise","ph":"la kro-TSJE-ra","ex":"Faremmo una crociera nel Mediterraneo.","exNl":"We zouden een cruise in de Middellandse Zee maken.","lesson":137,"level":"B1","cat":"viaggio"},

    # ── Les 138: Accommodatie ──
    {"id":"w1347","it":"la camera singola","nl":"de eenpersoonskamer","ph":"la KA-me-ra SIN-go-la","ex":"Vorrei prenotare una camera singola.","exNl":"Ik zou graag een eenpersoonskamer boeken.","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1348","it":"la camera doppia","nl":"de tweepersoonskamer","ph":"la KA-me-ra DOP-pja","ex":"Avete una camera doppia libera?","exNl":"Heeft u een tweepersoonskamer vrij?","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1349","it":"la colazione inclusa","nl":"het ontbijt inbegrepen","ph":"la ko-la-TSJO-ne in-KLU-za","ex":"La colazione è inclusa nel prezzo.","exNl":"Het ontbijt is bij de prijs inbegrepen.","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1350","it":"il soggiorno","nl":"het verblijf","ph":"il sod-DJOR-no","ex":"Il soggiorno è stato piacevole.","exNl":"Het verblijf was aangenaam.","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1351","it":"la reception","nl":"de receptie","ph":"la re-SEP-scion","ex":"Chieda alla reception.","exNl":"Vraag het aan de receptie.","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1352","it":"l'ascensore","nl":"de lift","ph":"la-shen-SO-re","ex":"L'ascensore è in fondo al corridoio.","exNl":"De lift is aan het einde van de gang.","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1353","it":"il reclamo","nl":"de klacht","ph":"il re-KLA-mo","ex":"Vorrei fare un reclamo.","exNl":"Ik zou graag een klacht indienen.","lesson":138,"level":"B1","cat":"alloggio"},
    {"id":"w1354","it":"il parcheggio","nl":"de parkeerplaats","ph":"il par-KED-djo","ex":"C'è un parcheggio per gli ospiti?","exNl":"Is er een parkeerplaats voor gasten?","lesson":138,"level":"B1","cat":"alloggio"},

    # ── Les 139: Vervoer & richting ──
    {"id":"w1355","it":"il binario","nl":"het perron/spoor","ph":"il bi-NA-rjo","ex":"Il treno parte dal binario tre.","exNl":"De trein vertrekt van spoor drie.","lesson":139,"level":"B1","cat":"trasporto"},
    {"id":"w1356","it":"la coincidenza","nl":"de overstap","ph":"la ko-in-tsji-DEN-tsa","ex":"Devo prendere una coincidenza a Bologna.","exNl":"Ik moet overstappen in Bologna.","lesson":139,"level":"B1","cat":"trasporto"},
    {"id":"w1357","it":"l'andata e ritorno","nl":"de heen- en terugreis","ph":"lan-DA-ta e ri-TOR-no","ex":"Un biglietto di andata e ritorno, per favore.","exNl":"Een retourtje, alstublieft.","lesson":139,"level":"B1","cat":"trasporto"},
    {"id":"w1358","it":"dritto","nl":"rechtdoor","ph":"DRIT-to","ex":"Vada dritto per duecento metri.","exNl":"Ga tweehonderd meter rechtdoor.","lesson":139,"level":"B1","cat":"direzione"},
    {"id":"w1359","it":"girare","nl":"afslaan","ph":"dji-RA-re","ex":"Giri a destra al semaforo.","exNl":"Sla rechtsaf bij het stoplicht.","lesson":139,"level":"B1","cat":"direzione"},
    {"id":"w1360","it":"il semaforo","nl":"het stoplicht","ph":"il se-MA-fo-ro","ex":"Al semaforo giri a sinistra.","exNl":"Bij het stoplicht slaat u linksaf.","lesson":139,"level":"B1","cat":"trasporto"},
    {"id":"w1361","it":"l'incrocio","nl":"het kruispunt","ph":"lin-KRO-tsjo","ex":"All'incrocio prenda la seconda a destra.","exNl":"Bij het kruispunt neemt u de tweede rechts.","lesson":139,"level":"B1","cat":"trasporto"},
    {"id":"w1362","it":"la fermata","nl":"de halte","ph":"la fer-MA-ta","ex":"La fermata dell'autobus è là.","exNl":"De bushalte is daar.","lesson":139,"level":"B1","cat":"trasporto"},

    # ── Les 140: Toetsles Blok 2 ──
    {"id":"w1363","it":"cortese","nl":"beleefd/hoffelijk","ph":"kor-TE-ze","ex":"È sempre molto cortese.","exNl":"Hij is altijd erg beleefd.","lesson":140,"level":"B1","cat":"aggettivo"},
    {"id":"w1364","it":"il viaggio","nl":"de reis","ph":"il VJAD-djo","ex":"È stato un bel viaggio.","exNl":"Het was een mooie reis.","lesson":140,"level":"B1","cat":"viaggio"},
    {"id":"w1365","it":"comodo","nl":"comfortabel","ph":"KO-mo-do","ex":"La camera era molto comoda.","exNl":"De kamer was erg comfortabel.","lesson":140,"level":"B1","cat":"aggettivo"},
    {"id":"w1366","it":"il ritardo","nl":"de vertraging","ph":"il ri-TAR-do","ex":"Il treno ha venti minuti di ritardo.","exNl":"De trein heeft twintig minuten vertraging.","lesson":140,"level":"B1","cat":"trasporto"},
    {"id":"w1367","it":"l'orario","nl":"het tijdschema","ph":"lo-RA-rjo","ex":"Controlliamo l'orario dei treni.","exNl":"Laten we het treinschema controleren.","lesson":140,"level":"B1","cat":"trasporto"},
    {"id":"w1368","it":"la prenotazione","nl":"de reservering","ph":"la pre-no-ta-TSJO-ne","ex":"Ho una prenotazione a nome Rossi.","exNl":"Ik heb een reservering op naam Rossi.","lesson":140,"level":"B1","cat":"viaggio"},
    {"id":"w1369","it":"confermare","nl":"bevestigen","ph":"kon-fer-MA-re","ex":"Potrebbe confermare la prenotazione?","exNl":"Zou u de reservering kunnen bevestigen?","lesson":140,"level":"B1","cat":"verbo"},
    {"id":"w1370","it":"annullare","nl":"annuleren","ph":"an-nul-LA-re","ex":"Vorrei annullare la prenotazione.","exNl":"Ik zou de reservering willen annuleren.","lesson":140,"level":"B1","cat":"verbo"},

    # ── Les 141: Congiuntivo introductie ──
    {"id":"w1371","it":"dubitare","nl":"twijfelen","ph":"du-bi-TA-re","ex":"Dubito che sia vero.","exNl":"Ik betwijfel of het waar is.","lesson":141,"level":"B1","cat":"verbo_congiuntivo"},
    {"id":"w1372","it":"supporre","nl":"veronderstellen","ph":"sup-POR-re","ex":"Suppongo che abbia ragione.","exNl":"Ik veronderstel dat hij gelijk heeft.","lesson":141,"level":"B1","cat":"verbo_congiuntivo"},
    {"id":"w1373","it":"sembrare","nl":"lijken/schijnen","ph":"sem-BRA-re","ex":"Sembra che piova stasera.","exNl":"Het lijkt erop dat het vanavond regent.","lesson":141,"level":"B1","cat":"verbo_congiuntivo"},
    {"id":"w1374","it":"necessario","nl":"noodzakelijk","ph":"ne-tshes-SA-rjo","ex":"È necessario che tu venga.","exNl":"Het is noodzakelijk dat je komt.","lesson":141,"level":"B1","cat":"aggettivo"},
    {"id":"w1375","it":"probabile","nl":"waarschijnlijk","ph":"pro-BA-bi-le","ex":"È probabile che arrivi tardi.","exNl":"Het is waarschijnlijk dat hij laat aankomt.","lesson":141,"level":"B1","cat":"aggettivo"},
    {"id":"w1376","it":"impossibile","nl":"onmogelijk","ph":"im-pos-SI-bi-le","ex":"È impossibile che non lo sappia.","exNl":"Het is onmogelijk dat hij het niet weet.","lesson":141,"level":"B1","cat":"aggettivo"},
    {"id":"w1377","it":"la possibilità","nl":"de mogelijkheid","ph":"la pos-si-bi-li-TA","ex":"C'è la possibilità che venga domani.","exNl":"Er is de mogelijkheid dat hij morgen komt.","lesson":141,"level":"B1","cat":"sostantivo"},
    {"id":"w1378","it":"il dubbio","nl":"de twijfel","ph":"il DUB-bjo","ex":"Ho il dubbio che non sia giusto.","exNl":"Ik heb de twijfel dat het niet juist is.","lesson":141,"level":"B1","cat":"sostantivo"},

    # ── Les 142: Congiuntivo onregelmatig ──
    {"id":"w1379","it":"qualunque","nl":"welk(e)… ook","ph":"kwa-LUN-kwe","ex":"Qualunque cosa tu dica, ti ascolto.","exNl":"Wat je ook zegt, ik luister naar je.","lesson":142,"level":"B1","cat":"pronome"},
    {"id":"w1380","it":"ovunque","nl":"waar… ook","ph":"o-VUN-kwe","ex":"Ovunque tu vada, ti seguo.","exNl":"Waar je ook naartoe gaat, ik volg je.","lesson":142,"level":"B1","cat":"avverbio"},
    {"id":"w1381","it":"chiunque","nl":"wie… ook","ph":"kjun-KWE","ex":"Chiunque sia, digli di aspettare.","exNl":"Wie het ook is, zeg hem te wachten.","lesson":142,"level":"B1","cat":"pronome"},
    {"id":"w1382","it":"purché","nl":"mits/op voorwaarde dat","ph":"pur-KE","ex":"Vengo purché tu mi accompagni.","exNl":"Ik kom, mits je me vergezelt.","lesson":142,"level":"B1","cat":"congiunzione"},
    {"id":"w1383","it":"affinché","nl":"opdat","ph":"af-fin-KE","ex":"Studio affinché possa superare l'esame.","exNl":"Ik studeer opdat ik het examen kan halen.","lesson":142,"level":"B1","cat":"congiunzione"},
    {"id":"w1384","it":"benché","nl":"hoewel","ph":"ben-KE","ex":"Benché sia stanco, continuo.","exNl":"Hoewel ik moe ben, ga ik door.","lesson":142,"level":"B1","cat":"congiunzione"},
    {"id":"w1385","it":"a meno che","nl":"tenzij","ph":"a ME-no ke","ex":"Esco, a meno che non piova.","exNl":"Ik ga naar buiten, tenzij het regent.","lesson":142,"level":"B1","cat":"congiunzione"},
    {"id":"w1386","it":"prima che","nl":"voordat","ph":"PRI-ma ke","ex":"Parti prima che faccia buio.","exNl":"Vertrek voordat het donker wordt.","lesson":142,"level":"B1","cat":"congiunzione"},

    # ── Les 143: Meningen geven ──
    {"id":"w1387","it":"l'opinione","nl":"de mening","ph":"lo-pi-NJO-ne","ex":"Qual è la tua opinione?","exNl":"Wat is jouw mening?","lesson":143,"level":"B1","cat":"discussione"},
    {"id":"w1388","it":"secondo me","nl":"volgens mij","ph":"se-KON-do me","ex":"Secondo me, ha ragione.","exNl":"Volgens mij heeft hij gelijk.","lesson":143,"level":"B1","cat":"espressione"},
    {"id":"w1389","it":"d'accordo","nl":"eens/akkoord","ph":"dak-KOR-do","ex":"Sono d'accordo con te.","exNl":"Ik ben het met je eens.","lesson":143,"level":"B1","cat":"espressione"},
    {"id":"w1390","it":"il punto di vista","nl":"het standpunt","ph":"il PUN-to di VIS-ta","ex":"Capisco il tuo punto di vista.","exNl":"Ik begrijp jouw standpunt.","lesson":143,"level":"B1","cat":"discussione"},
    {"id":"w1391","it":"sostenere","nl":"beweren/verdedigen","ph":"sos-te-NE-re","ex":"Sostiene che la situazione sia grave.","exNl":"Hij beweert dat de situatie ernstig is.","lesson":143,"level":"B1","cat":"verbo"},
    {"id":"w1392","it":"convincere","nl":"overtuigen","ph":"kon-VIN-tsje-re","ex":"Non mi hai convinto.","exNl":"Je hebt me niet overtuigd.","lesson":143,"level":"B1","cat":"verbo"},
    {"id":"w1393","it":"ragione","nl":"gelijk","ph":"ra-DJO-ne","ex":"Hai ragione, mi sono sbagliato.","exNl":"Je hebt gelijk, ik had het mis.","lesson":143,"level":"B1","cat":"sostantivo"},
    {"id":"w1394","it":"torto","nl":"ongelijk","ph":"TOR-to","ex":"Ha torto e lo sa.","exNl":"Hij heeft ongelijk en hij weet het.","lesson":143,"level":"B1","cat":"sostantivo"},

    # ── Les 144: Emoties & congiuntivo ──
    {"id":"w1395","it":"contento","nl":"blij/tevreden","ph":"kon-TEN-to","ex":"Sono contento che tu sia qui.","exNl":"Ik ben blij dat je hier bent.","lesson":144,"level":"B1","cat":"emozione"},
    {"id":"w1396","it":"dispiaciuto","nl":"het spijt (me)","ph":"dis-pja-TSU-to","ex":"Sono dispiaciuto per l'errore.","exNl":"Het spijt me vanwege de fout.","lesson":144,"level":"B1","cat":"emozione"},
    {"id":"w1397","it":"il peccato","nl":"de zonde/jammer","ph":"il pek-KA-to","ex":"È un peccato che non possa venire.","exNl":"Het is jammer dat hij niet kan komen.","lesson":144,"level":"B1","cat":"espressione"},
    {"id":"w1398","it":"temere","nl":"vrezen","ph":"te-ME-re","ex":"Temo che non ci sia più tempo.","exNl":"Ik vrees dat er geen tijd meer is.","lesson":144,"level":"B1","cat":"verbo"},
    {"id":"w1399","it":"sperare","nl":"hopen","ph":"spe-RA-re","ex":"Spero che tutto vada bene.","exNl":"Ik hoop dat alles goed gaat.","lesson":144,"level":"B1","cat":"verbo"},
    {"id":"w1400","it":"la preoccupazione","nl":"de bezorgdheid","ph":"la pre-ok-ku-pa-TSJO-ne","ex":"La mia preoccupazione è il tempo.","exNl":"Mijn bezorgdheid is het weer.","lesson":144,"level":"B1","cat":"emozione"},
    {"id":"w1401","it":"meravigliarsi","nl":"zich verbazen","ph":"me-ra-vil-JAR-si","ex":"Mi meraviglio che non lo sappia.","exNl":"Ik verbaas me dat hij het niet weet.","lesson":144,"level":"B1","cat":"verbo"},
    {"id":"w1402","it":"vergognarsi","nl":"zich schamen","ph":"ver-gon-JAR-si","ex":"Mi vergogno di quello che ho fatto.","exNl":"Ik schaam me voor wat ik heb gedaan.","lesson":144,"level":"B1","cat":"verbo"},

    # ── Les 145: Werk & solliciteren ──
    {"id":"w1403","it":"il colloquio","nl":"het sollicitatiegesprek","ph":"il kol-LO-kwjo","ex":"Ho un colloquio di lavoro domani.","exNl":"Ik heb morgen een sollicitatiegesprek.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1404","it":"il curriculum","nl":"het cv","ph":"il kur-RI-ku-lum","ex":"Ho mandato il mio curriculum.","exNl":"Ik heb mijn cv gestuurd.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1405","it":"l'esperienza","nl":"de ervaring","ph":"les-pe-RJEN-tsa","ex":"Ho cinque anni di esperienza.","exNl":"Ik heb vijf jaar ervaring.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1406","it":"il candidato","nl":"de kandidaat","ph":"il kan-di-DA-to","ex":"Ci sono molti candidati.","exNl":"Er zijn veel kandidaten.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1407","it":"assumere","nl":"aannemen (personeel)","ph":"as-SU-me-re","ex":"L'azienda ha assunto dieci persone.","exNl":"Het bedrijf heeft tien mensen aangenomen.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1408","it":"licenziare","nl":"ontslaan","ph":"li-tshen-TSJA-re","ex":"L'hanno licenziato senza motivo.","exNl":"Ze hebben hem zonder reden ontslagen.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1409","it":"lo stipendio","nl":"het salaris","ph":"lo sti-PEN-djo","ex":"Lo stipendio è soddisfacente.","exNl":"Het salaris is bevredigend.","lesson":145,"level":"B1","cat":"lavoro"},
    {"id":"w1410","it":"il contratto","nl":"het contract","ph":"il kon-TRAT-to","ex":"Ho firmato il contratto.","exNl":"Ik heb het contract getekend.","lesson":145,"level":"B1","cat":"lavoro"},

    # ── Les 146: Op kantoor ──
    {"id":"w1411","it":"la riunione","nl":"de vergadering","ph":"la ri-u-NJO-ne","ex":"La riunione è alle dieci.","exNl":"De vergadering is om tien uur.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1412","it":"la scadenza","nl":"de deadline","ph":"la ska-DEN-tsa","ex":"La scadenza è venerdì.","exNl":"De deadline is vrijdag.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1413","it":"il progetto","nl":"het project","ph":"il pro-DJET-to","ex":"Lavoro a un nuovo progetto.","exNl":"Ik werk aan een nieuw project.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1414","it":"il collega","nl":"de collega","ph":"il kol-LE-ga","ex":"I miei colleghi sono simpatici.","exNl":"Mijn collega's zijn aardig.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1415","it":"il capo","nl":"de baas","ph":"il KA-po","ex":"Il capo vuole parlare con te.","exNl":"De baas wil met je praten.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1416","it":"la presentazione","nl":"de presentatie","ph":"la pre-zen-ta-TSJO-ne","ex":"Devo preparare una presentazione.","exNl":"Ik moet een presentatie voorbereiden.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1417","it":"l'obiettivo","nl":"het doel/de doelstelling","ph":"lo-bjet-TI-vo","ex":"Abbiamo raggiunto l'obiettivo.","exNl":"We hebben het doel bereikt.","lesson":146,"level":"B1","cat":"ufficio"},
    {"id":"w1418","it":"il rapporto","nl":"het rapport/de verhouding","ph":"il rap-POR-to","ex":"Devo scrivere un rapporto.","exNl":"Ik moet een rapport schrijven.","lesson":146,"level":"B1","cat":"ufficio"},

    # ── Les 147: Beroepen & vaardigheden ──
    {"id":"w1419","it":"l'avvocato","nl":"de advocaat","ph":"lav-vo-KA-to","ex":"L'avvocato ha difeso il cliente.","exNl":"De advocaat heeft de cliënt verdedigd.","lesson":147,"level":"B1","cat":"professione"},
    {"id":"w1420","it":"l'ingegnere","nl":"de ingenieur","ph":"lin-dje-NJE-re","ex":"Mio fratello è ingegnere.","exNl":"Mijn broer is ingenieur.","lesson":147,"level":"B1","cat":"professione"},
    {"id":"w1421","it":"il giornalista","nl":"de journalist","ph":"il djor-na-LIS-ta","ex":"Il giornalista ha scritto un articolo.","exNl":"De journalist heeft een artikel geschreven.","lesson":147,"level":"B1","cat":"professione"},
    {"id":"w1422","it":"il commercialista","nl":"de accountant","ph":"il kom-mer-tsja-LIS-ta","ex":"Devo parlare con il commercialista.","exNl":"Ik moet met de accountant praten.","lesson":147,"level":"B1","cat":"professione"},
    {"id":"w1423","it":"l'architetto","nl":"de architect","ph":"lar-ki-TET-to","ex":"L'architetto ha progettato la casa.","exNl":"De architect heeft het huis ontworpen.","lesson":147,"level":"B1","cat":"professione"},
    {"id":"w1424","it":"competente","nl":"bekwaam/competent","ph":"kom-pe-TEN-te","ex":"È un professionista molto competente.","exNl":"Hij is een heel bekwame professional.","lesson":147,"level":"B1","cat":"aggettivo"},
    {"id":"w1425","it":"la competenza","nl":"de vaardigheid/competentie","ph":"la kom-pe-TEN-tsa","ex":"Ha molte competenze informatiche.","exNl":"Hij heeft veel computervaardigheden.","lesson":147,"level":"B1","cat":"lavoro"},
    {"id":"w1426","it":"qualificato","nl":"gekwalificeerd","ph":"kwa-li-fi-KA-to","ex":"Cerchiamo personale qualificato.","exNl":"We zoeken gekwalificeerd personeel.","lesson":147,"level":"B1","cat":"aggettivo"},

    # ── Les 148: Discussiëren ──
    {"id":"w1427","it":"tuttavia","nl":"echter/desondanks","ph":"tut-ta-VI-a","ex":"Tuttavia, non sono d'accordo.","exNl":"Desondanks ben ik het er niet mee eens.","lesson":148,"level":"B1","cat":"congiunzione"},
    {"id":"w1428","it":"inoltre","nl":"bovendien","ph":"i-NOL-tre","ex":"Inoltre, il prezzo è troppo alto.","exNl":"Bovendien is de prijs te hoog.","lesson":148,"level":"B1","cat":"avverbio"},
    {"id":"w1429","it":"al contrario","nl":"integendeel","ph":"al kon-TRA-rjo","ex":"Al contrario, penso che sia giusto.","exNl":"Integendeel, ik denk dat het juist is.","lesson":148,"level":"B1","cat":"espressione"},
    {"id":"w1430","it":"in conclusione","nl":"tot slot","ph":"in kon-klu-ZJO-ne","ex":"In conclusione, dobbiamo agire.","exNl":"Tot slot, we moeten handelen.","lesson":148,"level":"B1","cat":"espressione"},
    {"id":"w1431","it":"l'argomento","nl":"het argument/onderwerp","ph":"lar-go-MEN-to","ex":"È un argomento interessante.","exNl":"Het is een interessant onderwerp.","lesson":148,"level":"B1","cat":"discussione"},
    {"id":"w1432","it":"discutere","nl":"discussiëren","ph":"dis-KU-te-re","ex":"Abbiamo discusso a lungo.","exNl":"We hebben lang gediscussieerd.","lesson":148,"level":"B1","cat":"verbo"},
    {"id":"w1433","it":"ammettere","nl":"toegeven","ph":"am-MET-te-re","ex":"Devo ammettere che hai ragione.","exNl":"Ik moet toegeven dat je gelijk hebt.","lesson":148,"level":"B1","cat":"verbo"},
    {"id":"w1434","it":"esagerare","nl":"overdrijven","ph":"e-za-dje-RA-re","ex":"Non esagerare, non è così grave.","exNl":"Overdrijf niet, het is niet zo erg.","lesson":148,"level":"B1","cat":"verbo"},

    # ── Les 149: Gevoelens uitdrukken ──
    {"id":"w1435","it":"preoccupato","nl":"bezorgd","ph":"pre-ok-ku-PA-to","ex":"Sono preoccupato per l'esame.","exNl":"Ik ben bezorgd over het examen.","lesson":149,"level":"B1","cat":"emozione"},
    {"id":"w1436","it":"ansioso","nl":"angstig/nerveus","ph":"AN-sjo-zo","ex":"Sono ansioso per il colloquio.","exNl":"Ik ben nerveus voor het sollicitatiegesprek.","lesson":149,"level":"B1","cat":"emozione"},
    {"id":"w1437","it":"tranquillo","nl":"rustig/kalm","ph":"tran-KWIL-lo","ex":"Stai tranquillo, andrà tutto bene.","exNl":"Blijf kalm, het komt allemaal goed.","lesson":149,"level":"B1","cat":"emozione"},
    {"id":"w1438","it":"la fiducia","nl":"het vertrouwen","ph":"la fi-DU-tsja","ex":"Ho fiducia in te.","exNl":"Ik heb vertrouwen in je.","lesson":149,"level":"B1","cat":"emozione"},
    {"id":"w1439","it":"il coraggio","nl":"de moed","ph":"il ko-RAD-djo","ex":"Ci vuole coraggio per farlo.","exNl":"Er is moed voor nodig om het te doen.","lesson":149,"level":"B1","cat":"emozione"},
    {"id":"w1440","it":"la pazienza","nl":"het geduld","ph":"la pa-TSJEN-tsa","ex":"Bisogna avere pazienza.","exNl":"Je moet geduld hebben.","lesson":149,"level":"B1","cat":"emozione"},
    {"id":"w1441","it":"sopportare","nl":"verdragen","ph":"sop-por-TA-re","ex":"Non sopporto il rumore.","exNl":"Ik kan het lawaai niet verdragen.","lesson":149,"level":"B1","cat":"verbo"},
    {"id":"w1442","it":"lamentarsi","nl":"klagen","ph":"la-men-TAR-si","ex":"Si lamenta sempre del lavoro.","exNl":"Hij klaagt altijd over het werk.","lesson":149,"level":"B1","cat":"verbo"},

    # ── Les 150: Toetsles Blok 3 ──
    {"id":"w1443","it":"il parere","nl":"de mening","ph":"il pa-RE-re","ex":"A mio parere, è una buona idea.","exNl":"Naar mijn mening is het een goed idee.","lesson":150,"level":"B1","cat":"discussione"},
    {"id":"w1444","it":"esprimere","nl":"uitdrukken","ph":"es-PRI-me-re","ex":"È importante esprimere le proprie emozioni.","exNl":"Het is belangrijk om je emoties uit te drukken.","lesson":150,"level":"B1","cat":"verbo"},
    {"id":"w1445","it":"il sentimento","nl":"het gevoel","ph":"il sen-ti-MEN-to","ex":"È un sentimento difficile da spiegare.","exNl":"Het is een moeilijk te verklaren gevoel.","lesson":150,"level":"B1","cat":"emozione"},
    {"id":"w1446","it":"la proposta","nl":"het voorstel","ph":"la pro-POS-ta","ex":"Ho una proposta da fare.","exNl":"Ik heb een voorstel te doen.","lesson":150,"level":"B1","cat":"lavoro"},
    {"id":"w1447","it":"il compromesso","nl":"het compromis","ph":"il kom-pro-MES-so","ex":"Dobbiamo trovare un compromesso.","exNl":"We moeten een compromis vinden.","lesson":150,"level":"B1","cat":"discussione"},
    {"id":"w1448","it":"la responsabilità","nl":"de verantwoordelijkheid","ph":"la res-pon-sa-bi-li-TA","ex":"È una grande responsabilità.","exNl":"Het is een grote verantwoordelijkheid.","lesson":150,"level":"B1","cat":"lavoro"},
    {"id":"w1449","it":"affidabile","nl":"betrouwbaar","ph":"af-fi-DA-bi-le","ex":"È una persona molto affidabile.","exNl":"Het is een heel betrouwbaar persoon.","lesson":150,"level":"B1","cat":"aggettivo"},
    {"id":"w1450","it":"la collaborazione","nl":"de samenwerking","ph":"la kol-la-bo-ra-TSJO-ne","ex":"La collaborazione è fondamentale.","exNl":"De samenwerking is essentieel.","lesson":150,"level":"B1","cat":"lavoro"},

    # ── Les 151: Pronomi combinati ──
    {"id":"w1451","it":"spiegare","nl":"uitleggen","ph":"spje-GA-re","ex":"Me lo ha spiegato chiaramente.","exNl":"Hij heeft het me duidelijk uitgelegd.","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1452","it":"restituire","nl":"teruggeven","ph":"res-ti-tu-I-re","ex":"Glielo restituisco domani.","exNl":"Ik geef het hem morgen terug.","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1453","it":"mostrare","nl":"laten zien","ph":"mos-TRA-re","ex":"Te la mostro subito.","exNl":"Ik laat het je meteen zien.","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1454","it":"regalare","nl":"cadeau geven","ph":"re-ga-LA-re","ex":"Glielo regaliamo per Natale.","exNl":"We geven het hem cadeau voor Kerst.","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1455","it":"promettere","nl":"beloven","ph":"pro-MET-te-re","ex":"Te lo prometto.","exNl":"Ik beloof het je.","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1456","it":"raccomandare","nl":"aanbevelen","ph":"rak-ko-man-DA-re","ex":"Me l'hanno raccomandato tutti.","exNl":"Iedereen heeft het me aanbevolen.","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1457","it":"ricordare","nl":"herinneren","ph":"ri-kor-DA-re","ex":"Me lo ricordi domani?","exNl":"Herinner je me er morgen aan?","lesson":151,"level":"B1","cat":"verbo"},
    {"id":"w1458","it":"insegnare","nl":"onderwijzen/leren","ph":"in-sen-JA-re","ex":"Ce l'ha insegnato il professore.","exNl":"De professor heeft het ons geleerd.","lesson":151,"level":"B1","cat":"verbo"},

    # ── Les 152: Pronomi oefening ──
    {"id":"w1459","it":"passare","nl":"doorgeven","ph":"pas-SA-re","ex":"Me la passi, per favore?","exNl":"Geef je het me door, alsjeblieft?","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1460","it":"preparare","nl":"voorbereiden/klaarmaken","ph":"pre-pa-RA-re","ex":"Te lo preparo io.","exNl":"Ik maak het voor je klaar.","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1461","it":"portare","nl":"brengen","ph":"por-TA-re","ex":"Glielo porto subito.","exNl":"Ik breng het hem meteen.","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1462","it":"confermare","nl":"bevestigen","ph":"kon-fer-MA-re","ex":"Me lo puoi confermare?","exNl":"Kun je het me bevestigen?","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1463","it":"garantire","nl":"garanderen","ph":"ga-ran-TI-re","ex":"Te lo garantisco.","exNl":"Ik garandeer het je.","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1464","it":"nascondere","nl":"verbergen","ph":"nas-KON-de-re","ex":"Perché me lo hai nascosto?","exNl":"Waarom heb je het voor me verborgen?","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1465","it":"rivelare","nl":"onthullen","ph":"ri-ve-LA-re","ex":"Non glielo rivelare!","exNl":"Onthul het hem niet!","lesson":152,"level":"B1","cat":"verbo"},
    {"id":"w1466","it":"comunicare","nl":"meedelen","ph":"ko-mu-ni-KA-re","ex":"Ce lo hanno comunicato ieri.","exNl":"Ze hebben het ons gisteren meegedeeld.","lesson":152,"level":"B1","cat":"verbo"},

    # ── Les 153: Passieve vorm ──
    {"id":"w1467","it":"inventare","nl":"uitvinden","ph":"in-ven-TA-re","ex":"La pizza è stata inventata a Napoli.","exNl":"De pizza is in Napels uitgevonden.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1468","it":"costruire","nl":"bouwen","ph":"kos-tru-I-re","ex":"Il ponte è stato costruito nel 1900.","exNl":"De brug is in 1900 gebouwd.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1469","it":"scoprire","nl":"ontdekken","ph":"sko-PRI-re","ex":"L'America è stata scoperta nel 1492.","exNl":"Amerika is in 1492 ontdekt.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1470","it":"organizzare","nl":"organiseren","ph":"or-ga-nid-ZA-re","ex":"La festa è stata organizzata da Maria.","exNl":"Het feest is door Maria georganiseerd.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1471","it":"approvare","nl":"goedkeuren","ph":"ap-pro-VA-re","ex":"La legge è stata approvata.","exNl":"De wet is goedgekeurd.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1472","it":"consegnare","nl":"bezorgen/afleveren","ph":"kon-sen-JA-re","ex":"I pacchi vengono consegnati ogni mattina.","exNl":"De pakketten worden elke ochtend bezorgd.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1473","it":"pubblicare","nl":"publiceren","ph":"pub-bli-KA-re","ex":"Il libro è stato pubblicato l'anno scorso.","exNl":"Het boek is vorig jaar gepubliceerd.","lesson":153,"level":"B1","cat":"verbo"},
    {"id":"w1474","it":"fondare","nl":"stichten/oprichten","ph":"fon-DA-re","ex":"Roma è stata fondata nel 753 a.C.","exNl":"Rome is gesticht in 753 v.Chr.","lesson":153,"level":"B1","cat":"verbo"},

    # ── Les 154: Bij de dokter ──
    {"id":"w1475","it":"il mal di testa","nl":"de hoofdpijn","ph":"il mal di TES-ta","ex":"Ho un forte mal di testa.","exNl":"Ik heb erge hoofdpijn.","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1476","it":"la febbre","nl":"de koorts","ph":"la FEB-bre","ex":"Ho la febbre a trentotto.","exNl":"Ik heb 38 graden koorts.","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1477","it":"la ricetta","nl":"het recept (medisch)","ph":"la ri-TSJET-ta","ex":"Il dottore mi ha dato una ricetta.","exNl":"De dokter heeft me een recept gegeven.","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1478","it":"la pastiglia","nl":"de pil/tablet","ph":"la pas-TIL-ja","ex":"Prenda due pastiglie al giorno.","exNl":"Neem twee pillen per dag.","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1479","it":"il sintomo","nl":"het symptoom","ph":"il SIN-to-mo","ex":"Quali sono i sintomi?","exNl":"Wat zijn de symptomen?","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1480","it":"la cura","nl":"de behandeling/kuur","ph":"la KU-ra","ex":"La cura dura dieci giorni.","exNl":"De behandeling duurt tien dagen.","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1481","it":"guarire","nl":"genezen","ph":"gwa-RI-re","ex":"Spero di guarire presto.","exNl":"Ik hoop snel te genezen.","lesson":154,"level":"B1","cat":"salute"},
    {"id":"w1482","it":"il pronto soccorso","nl":"de eerste hulp","ph":"il PRON-to sok-KOR-so","ex":"Siamo andati al pronto soccorso.","exNl":"We zijn naar de eerste hulp gegaan.","lesson":154,"level":"B1","cat":"salute"},

    # ── Les 155: Gezondheid & welzijn ──
    {"id":"w1483","it":"la salute","nl":"de gezondheid","ph":"la sa-LU-te","ex":"La salute è la cosa più importante.","exNl":"Gezondheid is het belangrijkste.","lesson":155,"level":"B1","cat":"salute"},
    {"id":"w1484","it":"sano","nl":"gezond","ph":"SA-no","ex":"Cerco di mangiare sano.","exNl":"Ik probeer gezond te eten.","lesson":155,"level":"B1","cat":"aggettivo"},
    {"id":"w1485","it":"la dieta","nl":"het dieet","ph":"la DJE-ta","ex":"Seguo una dieta equilibrata.","exNl":"Ik volg een evenwichtig dieet.","lesson":155,"level":"B1","cat":"salute"},
    {"id":"w1486","it":"allenarsi","nl":"trainen","ph":"al-le-NAR-si","ex":"Mi alleno tre volte a settimana.","exNl":"Ik train drie keer per week.","lesson":155,"level":"B1","cat":"sport"},
    {"id":"w1487","it":"rilassarsi","nl":"ontspannen","ph":"ri-las-SAR-si","ex":"Devo rilassarmi un po'.","exNl":"Ik moet me een beetje ontspannen.","lesson":155,"level":"B1","cat":"benessere"},
    {"id":"w1488","it":"lo stress","nl":"de stress","ph":"lo stres","ex":"Lo stress fa male alla salute.","exNl":"Stress is slecht voor de gezondheid.","lesson":155,"level":"B1","cat":"benessere"},
    {"id":"w1489","it":"il benessere","nl":"het welzijn","ph":"il be-NES-se-re","ex":"Il benessere fisico e mentale.","exNl":"Het fysieke en mentale welzijn.","lesson":155,"level":"B1","cat":"benessere"},
    {"id":"w1490","it":"equilibrato","nl":"evenwichtig","ph":"e-kwi-li-BRA-to","ex":"Una vita equilibrata è fondamentale.","exNl":"Een evenwichtig leven is essentieel.","lesson":155,"level":"B1","cat":"aggettivo"},

    # ── Les 156: Het lichaam ──
    {"id":"w1491","it":"la spalla","nl":"de schouder","ph":"la SPAL-la","ex":"Mi fa male la spalla.","exNl":"Mijn schouder doet pijn.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1492","it":"il ginocchio","nl":"de knie","ph":"il dji-NOK-kjo","ex":"Ho dolore al ginocchio.","exNl":"Ik heb pijn aan mijn knie.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1493","it":"la schiena","nl":"de rug","ph":"la SKJE-na","ex":"Ho mal di schiena.","exNl":"Ik heb rugpijn.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1494","it":"il polso","nl":"de pols","ph":"il POL-so","ex":"Mi sono fatto male al polso.","exNl":"Ik heb mijn pols bezeerd.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1495","it":"la caviglia","nl":"de enkel","ph":"la ka-VIL-ja","ex":"Mi sono storto la caviglia.","exNl":"Ik heb mijn enkel verzwikt.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1496","it":"il gomito","nl":"de elleboog","ph":"il GO-mi-to","ex":"Ho battuto il gomito.","exNl":"Ik heb mijn elleboog gestoten.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1497","it":"il polmone","nl":"de long","ph":"il pol-MO-ne","ex":"I polmoni devono essere sani.","exNl":"De longen moeten gezond zijn.","lesson":156,"level":"B1","cat":"corpo"},
    {"id":"w1498","it":"il fegato","nl":"de lever","ph":"il FE-ga-to","ex":"Il fegato è un organo importante.","exNl":"De lever is een belangrijk orgaan.","lesson":156,"level":"B1","cat":"corpo"},

    # ── Les 157: Sport & beweging ──
    {"id":"w1499","it":"la partita","nl":"de wedstrijd","ph":"la par-TI-ta","ex":"Hai visto la partita ieri?","exNl":"Heb je de wedstrijd gisteren gezien?","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1500","it":"vincere","nl":"winnen","ph":"VIN-tsje-re","ex":"L'Italia ha vinto la partita.","exNl":"Italië heeft de wedstrijd gewonnen.","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1501","it":"perdere","nl":"verliezen","ph":"PER-de-re","ex":"Abbiamo perso due a zero.","exNl":"We hebben met twee-nul verloren.","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1502","it":"pareggiare","nl":"gelijkspelen","ph":"pa-red-DJA-re","ex":"La partita è finita in pareggio.","exNl":"De wedstrijd eindigde in een gelijkspel.","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1503","it":"l'allenamento","nl":"de training","ph":"lal-le-na-MEN-to","ex":"L'allenamento è stato duro.","exNl":"De training was zwaar.","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1504","it":"il tifoso","nl":"de fan/supporter","ph":"il ti-FO-zo","ex":"I tifosi festeggiano la vittoria.","exNl":"De fans vieren de overwinning.","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1505","it":"la squadra","nl":"het team/de ploeg","ph":"la SKWA-dra","ex":"La squadra ha giocato bene.","exNl":"Het team heeft goed gespeeld.","lesson":157,"level":"B1","cat":"sport"},
    {"id":"w1506","it":"il campionato","nl":"het kampioenschap","ph":"il kam-pjo-NA-to","ex":"Il campionato inizia a settembre.","exNl":"Het kampioenschap begint in september.","lesson":157,"level":"B1","cat":"sport"},

    # ── Les 158: Voeding & koken ──
    {"id":"w1507","it":"l'ingrediente","nl":"het ingrediënt","ph":"lin-gre-DJEN-te","ex":"Quali ingredienti servono?","exNl":"Welke ingrediënten zijn er nodig?","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1508","it":"mescolare","nl":"mengen/roeren","ph":"mes-ko-LA-re","ex":"Mescola bene gli ingredienti.","exNl":"Meng de ingrediënten goed.","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1509","it":"tagliare","nl":"snijden","ph":"tal-JA-re","ex":"Taglia le verdure a pezzi piccoli.","exNl":"Snijd de groenten in kleine stukjes.","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1510","it":"aggiungere","nl":"toevoegen","ph":"ad-DJUN-dje-re","ex":"Aggiungi un po' di sale.","exNl":"Voeg een beetje zout toe.","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1511","it":"la padella","nl":"de koekenpan","ph":"la pa-DEL-la","ex":"Scaldi l'olio nella padella.","exNl":"Verwarm de olie in de koekenpan.","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1512","it":"il forno","nl":"de oven","ph":"il FOR-no","ex":"Metti in forno a 180 gradi.","exNl":"Doe in de oven op 180 graden.","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1513","it":"la ricetta","nl":"het recept (koken)","ph":"la ri-TSJET-ta","ex":"Ho trovato una ricetta online.","exNl":"Ik heb een recept online gevonden.","lesson":158,"level":"B1","cat":"cucina"},
    {"id":"w1514","it":"il cucchiaio","nl":"de lepel","ph":"il kuk-KJA-jo","ex":"Un cucchiaio di zucchero.","exNl":"Een lepel suiker.","lesson":158,"level":"B1","cat":"cucina"},

    # ── Les 159: Milieu & natuur ──
    {"id":"w1515","it":"l'ambiente","nl":"het milieu","ph":"lam-BJEN-te","ex":"Dobbiamo proteggere l'ambiente.","exNl":"We moeten het milieu beschermen.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1516","it":"l'inquinamento","nl":"de vervuiling","ph":"lin-kwi-na-MEN-to","ex":"L'inquinamento dell'aria è un problema.","exNl":"De luchtvervuiling is een probleem.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1517","it":"riciclare","nl":"recyclen","ph":"ri-tsji-KLA-re","ex":"È importante riciclare la plastica.","exNl":"Het is belangrijk om plastic te recyclen.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1518","it":"l'energia rinnovabile","nl":"de hernieuwbare energie","ph":"le-ner-DJI-a rin-no-VA-bi-le","ex":"L'energia rinnovabile è il futuro.","exNl":"Hernieuwbare energie is de toekomst.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1519","it":"il riscaldamento globale","nl":"de opwarming van de aarde","ph":"il ris-kal-da-MEN-to glo-BA-le","ex":"Il riscaldamento globale è un problema serio.","exNl":"De opwarming van de aarde is een serieus probleem.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1520","it":"sprecare","nl":"verspillen","ph":"spre-KA-re","ex":"Non sprecare l'acqua.","exNl":"Verspil geen water.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1521","it":"sostenibile","nl":"duurzaam","ph":"sos-te-NI-bi-le","ex":"Cerchiamo soluzioni sostenibili.","exNl":"We zoeken duurzame oplossingen.","lesson":159,"level":"B1","cat":"ambiente"},
    {"id":"w1522","it":"il cambiamento climatico","nl":"de klimaatverandering","ph":"il kam-bja-MEN-to kli-MA-ti-ko","ex":"Il cambiamento climatico preoccupa tutti.","exNl":"De klimaatverandering baart iedereen zorgen.","lesson":159,"level":"B1","cat":"ambiente"},

    # ── Les 160: Toetsles Blok 4 ──
    {"id":"w1523","it":"il risultato","nl":"het resultaat","ph":"il ri-zul-TA-to","ex":"I risultati sono positivi.","exNl":"De resultaten zijn positief.","lesson":160,"level":"B1","cat":"sostantivo"},
    {"id":"w1524","it":"migliorare","nl":"verbeteren","ph":"mil-jo-RA-re","ex":"La situazione sta migliorando.","exNl":"De situatie verbetert.","lesson":160,"level":"B1","cat":"verbo"},
    {"id":"w1525","it":"peggiorare","nl":"verslechteren","ph":"ped-djo-RA-re","ex":"Il tempo sta peggiorando.","exNl":"Het weer verslechtert.","lesson":160,"level":"B1","cat":"verbo"},
    {"id":"w1526","it":"aumentare","nl":"toenemen/verhogen","ph":"au-men-TA-re","ex":"I prezzi sono aumentati.","exNl":"De prijzen zijn gestegen.","lesson":160,"level":"B1","cat":"verbo"},
    {"id":"w1527","it":"diminuire","nl":"afnemen/verminderen","ph":"di-mi-nu-I-re","ex":"La temperatura sta diminuendo.","exNl":"De temperatuur neemt af.","lesson":160,"level":"B1","cat":"verbo"},
    {"id":"w1528","it":"mantenere","nl":"onderhouden/handhaven","ph":"man-te-NE-re","ex":"È importante mantenere la salute.","exNl":"Het is belangrijk om je gezondheid te onderhouden.","lesson":160,"level":"B1","cat":"verbo"},
    {"id":"w1529","it":"la conseguenza","nl":"het gevolg","ph":"la kon-se-GWEN-tsa","ex":"Ogni azione ha delle conseguenze.","exNl":"Elke actie heeft gevolgen.","lesson":160,"level":"B1","cat":"sostantivo"},
    {"id":"w1530","it":"significativo","nl":"significant/belangrijk","ph":"sig-ni-fi-ka-TI-vo","ex":"È un cambiamento significativo.","exNl":"Het is een significante verandering.","lesson":160,"level":"B1","cat":"aggettivo"},

    # ── Les 161: Stare + gerundio ──
    {"id":"w1531","it":"sto parlando","nl":"ik ben aan het praten","ph":"sto par-LAN-do","ex":"Sto parlando con un amico.","exNl":"Ik ben met een vriend aan het praten.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1532","it":"sto leggendo","nl":"ik ben aan het lezen","ph":"sto led-DJEN-do","ex":"Sto leggendo un libro interessante.","exNl":"Ik ben een interessant boek aan het lezen.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1533","it":"sta piovendo","nl":"het is aan het regenen","ph":"sta pjo-VEN-do","ex":"Sta piovendo, prendi l'ombrello.","exNl":"Het regent, neem de paraplu.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1534","it":"sto cercando","nl":"ik ben aan het zoeken","ph":"sto tsher-KAN-do","ex":"Sto cercando le chiavi.","exNl":"Ik ben de sleutels aan het zoeken.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1535","it":"sto imparando","nl":"ik ben aan het leren","ph":"sto im-pa-RAN-do","ex":"Sto imparando l'italiano.","exNl":"Ik ben Italiaans aan het leren.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1536","it":"sta cambiando","nl":"het is aan het veranderen","ph":"sta kam-BJAN-do","ex":"Il mondo sta cambiando velocemente.","exNl":"De wereld verandert snel.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1537","it":"stiamo aspettando","nl":"we zijn aan het wachten","ph":"STJA-mo as-pet-TAN-do","ex":"Stiamo aspettando il treno.","exNl":"We zijn op de trein aan het wachten.","lesson":161,"level":"B1","cat":"gerundio"},
    {"id":"w1538","it":"stanno lavorando","nl":"zij zijn aan het werken","ph":"STAN-no la-vo-RAN-do","ex":"Stanno lavorando al progetto.","exNl":"Ze zijn aan het project aan het werken.","lesson":161,"level":"B1","cat":"gerundio"},

    # ── Les 162: Bijzinnen oorzaak & reden ──
    {"id":"w1539","it":"siccome","nl":"aangezien","ph":"sik-KO-me","ex":"Siccome piove, resto a casa.","exNl":"Aangezien het regent, blijf ik thuis.","lesson":162,"level":"B1","cat":"congiunzione"},
    {"id":"w1540","it":"dato che","nl":"gezien het feit dat","ph":"DA-to ke","ex":"Dato che sei qui, parliamo.","exNl":"Gezien het feit dat je hier bent, praten we.","lesson":162,"level":"B1","cat":"congiunzione"},
    {"id":"w1541","it":"poiché","nl":"aangezien (formeel)","ph":"poj-KE","ex":"Poiché non ha risposto, ho chiamato.","exNl":"Aangezien hij niet antwoordde, belde ik.","lesson":162,"level":"B1","cat":"congiunzione"},
    {"id":"w1542","it":"a causa di","nl":"vanwege","ph":"a KAU-za di","ex":"A causa del traffico, sono arrivato tardi.","exNl":"Vanwege het verkeer ben ik laat aangekomen.","lesson":162,"level":"B1","cat":"espressione"},
    {"id":"w1543","it":"il motivo","nl":"de reden","ph":"il mo-TI-vo","ex":"Qual è il motivo del ritardo?","exNl":"Wat is de reden van de vertraging?","lesson":162,"level":"B1","cat":"sostantivo"},
    {"id":"w1544","it":"dunque","nl":"dus/derhalve","ph":"DUN-kwe","ex":"Dunque, cosa facciamo?","exNl":"Dus, wat doen we?","lesson":162,"level":"B1","cat":"congiunzione"},
    {"id":"w1545","it":"perciò","nl":"daarom","ph":"per-TSO","ex":"Era stanco, perciò è andato a letto.","exNl":"Hij was moe, daarom ging hij naar bed.","lesson":162,"level":"B1","cat":"congiunzione"},
    {"id":"w1546","it":"di conseguenza","nl":"als gevolg daarvan","ph":"di kon-se-GWEN-tsa","ex":"Ha piovuto molto, di conseguenza il fiume è salito.","exNl":"Het heeft veel geregend, als gevolg daarvan is de rivier gestegen.","lesson":162,"level":"B1","cat":"espressione"},

    # ── Les 163: Bijzinnen tegenstelling ──
    {"id":"w1547","it":"anche se","nl":"ook al/zelfs als","ph":"AN-ke se","ex":"Esco anche se piove.","exNl":"Ik ga naar buiten, ook al regent het.","lesson":163,"level":"B1","cat":"congiunzione"},
    {"id":"w1548","it":"nonostante","nl":"ondanks (dat)","ph":"no-nos-TAN-te","ex":"Nonostante la pioggia, siamo usciti.","exNl":"Ondanks de regen zijn we naar buiten gegaan.","lesson":163,"level":"B1","cat":"congiunzione"},
    {"id":"w1549","it":"sebbene","nl":"hoewel","ph":"seb-BE-ne","ex":"Sebbene sia stanco, continuo.","exNl":"Hoewel ik moe ben, ga ik door.","lesson":163,"level":"B1","cat":"congiunzione"},
    {"id":"w1550","it":"eppure","nl":"en toch","ph":"ep-PU-re","ex":"È stanco, eppure lavora.","exNl":"Hij is moe, en toch werkt hij.","lesson":163,"level":"B1","cat":"congiunzione"},
    {"id":"w1551","it":"malgrado","nl":"ondanks","ph":"mal-GRA-do","ex":"Malgrado tutto, sono ottimista.","exNl":"Ondanks alles ben ik optimistisch.","lesson":163,"level":"B1","cat":"congiunzione"},
    {"id":"w1552","it":"invece","nl":"daarentegen","ph":"in-VE-tsje","ex":"Io studio, lui invece gioca.","exNl":"Ik studeer, hij speelt daarentegen.","lesson":163,"level":"B1","cat":"avverbio"},
    {"id":"w1553","it":"comunque","nl":"hoe dan ook/toch","ph":"ko-MUN-kwe","ex":"Comunque vada, sarà un'esperienza.","exNl":"Hoe het ook gaat, het wordt een ervaring.","lesson":163,"level":"B1","cat":"avverbio"},
    {"id":"w1554","it":"piuttosto","nl":"eerder/liever","ph":"pjut-TOS-to","ex":"Piuttosto che uscire, preferisco leggere.","exNl":"Liever dan naar buiten gaan, lees ik.","lesson":163,"level":"B1","cat":"avverbio"},

    # ── Les 164: Bijzinnen tijd ──
    {"id":"w1555","it":"prima di","nl":"voordat/voor","ph":"PRI-ma di","ex":"Prima di uscire, controlla il meteo.","exNl":"Controleer het weer voordat je naar buiten gaat.","lesson":164,"level":"B1","cat":"congiunzione"},
    {"id":"w1556","it":"dopo aver","nl":"nadat (ik/hij) heb/heeft","ph":"DO-po a-VER","ex":"Dopo aver mangiato, siamo usciti.","exNl":"Nadat we gegeten hadden, gingen we naar buiten.","lesson":164,"level":"B1","cat":"congiunzione"},
    {"id":"w1557","it":"appena","nl":"zodra/nauwelijks","ph":"ap-PE-na","ex":"Appena arrivo, ti chiamo.","exNl":"Zodra ik aankom, bel ik je.","lesson":164,"level":"B1","cat":"avverbio"},
    {"id":"w1558","it":"finché","nl":"totdat/zolang","ph":"fin-KE","ex":"Aspetto finché torni.","exNl":"Ik wacht totdat je terugkomt.","lesson":164,"level":"B1","cat":"congiunzione"},
    {"id":"w1559","it":"nel momento in cui","nl":"op het moment dat","ph":"nel mo-MEN-to in kui","ex":"Nel momento in cui l'ho visto, ho capito.","exNl":"Op het moment dat ik hem zag, begreep ik het.","lesson":164,"level":"B1","cat":"espressione"},
    {"id":"w1560","it":"ogni volta che","nl":"telkens wanneer","ph":"ON-ji VOL-ta ke","ex":"Ogni volta che piove, mi viene sonno.","exNl":"Telkens wanneer het regent, word ik slaperig.","lesson":164,"level":"B1","cat":"espressione"},
    {"id":"w1561","it":"ormai","nl":"inmiddels/nu","ph":"or-MAJ","ex":"Ormai è troppo tardi.","exNl":"Inmiddels is het te laat.","lesson":164,"level":"B1","cat":"avverbio"},
    {"id":"w1562","it":"contemporaneamente","nl":"tegelijkertijd","ph":"kon-tem-po-ra-ne-a-MEN-te","ex":"Parlava e mangiava contemporaneamente.","exNl":"Hij praatte en at tegelijkertijd.","lesson":164,"level":"B1","cat":"avverbio"},

    # ── Les 165: Indirecte rede basis ──
    {"id":"w1563","it":"affermare","nl":"beweren/bevestigen","ph":"af-fer-MA-re","ex":"Ha affermato che era innocente.","exNl":"Hij beweerde dat hij onschuldig was.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1564","it":"dichiarare","nl":"verklaren","ph":"di-kja-RA-re","ex":"Ha dichiarato di essere pronto.","exNl":"Hij verklaarde dat hij klaar was.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1565","it":"rispondere","nl":"antwoorden","ph":"ris-PON-de-re","ex":"Ha risposto che non poteva venire.","exNl":"Hij antwoordde dat hij niet kon komen.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1566","it":"aggiungere","nl":"toevoegen (zeggen)","ph":"ad-DJUN-dje-re","ex":"Ha aggiunto che sarebbe tornato.","exNl":"Hij voegde eraan toe dat hij zou terugkomen.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1567","it":"raccontare","nl":"vertellen","ph":"rak-kon-TA-re","ex":"Mi ha raccontato che aveva viaggiato.","exNl":"Hij vertelde me dat hij had gereisd.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1568","it":"spiegare","nl":"uitleggen","ph":"spje-GA-re","ex":"Mi ha spiegato che non era possibile.","exNl":"Hij legde me uit dat het niet mogelijk was.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1569","it":"avvertire","nl":"waarschuwen","ph":"av-ver-TI-re","ex":"Mi ha avvertito che c'era traffico.","exNl":"Hij waarschuwde me dat er verkeer was.","lesson":165,"level":"B1","cat":"verbo"},
    {"id":"w1570","it":"confermare","nl":"bevestigen","ph":"kon-fer-MA-re","ex":"Ha confermato che la riunione era alle tre.","exNl":"Hij bevestigde dat de vergadering om drie uur was.","lesson":165,"level":"B1","cat":"verbo"},

    # ── Les 166: Indirecte rede vragen ──
    {"id":"w1571","it":"chiedere","nl":"vragen","ph":"KJE-de-re","ex":"Mi ha chiesto se volevo uscire.","exNl":"Hij vroeg me of ik naar buiten wilde.","lesson":166,"level":"B1","cat":"verbo"},
    {"id":"w1572","it":"domandare","nl":"vragen (formeler)","ph":"do-man-DA-re","ex":"Mi ha domandato dove abitavo.","exNl":"Hij vroeg me waar ik woonde.","lesson":166,"level":"B1","cat":"verbo"},
    {"id":"w1573","it":"informarsi","nl":"informeren/navragen","ph":"in-for-MAR-si","ex":"Si è informato sui prezzi.","exNl":"Hij informeerde naar de prijzen.","lesson":166,"level":"B1","cat":"verbo"},
    {"id":"w1574","it":"volere sapere","nl":"willen weten","ph":"vo-LE-re sa-PE-re","ex":"Voleva sapere quando partivamo.","exNl":"Hij wilde weten wanneer we vertrokken.","lesson":166,"level":"B1","cat":"espressione"},
    {"id":"w1575","it":"la domanda","nl":"de vraag","ph":"la do-MAN-da","ex":"Mi ha fatto una domanda difficile.","exNl":"Hij stelde me een moeilijke vraag.","lesson":166,"level":"B1","cat":"sostantivo"},
    {"id":"w1576","it":"la risposta","nl":"het antwoord","ph":"la ris-POS-ta","ex":"La risposta era semplice.","exNl":"Het antwoord was eenvoudig.","lesson":166,"level":"B1","cat":"sostantivo"},
    {"id":"w1577","it":"riferire","nl":"melden/doorgeven","ph":"ri-fe-RI-re","ex":"Mi ha riferito che c'era un problema.","exNl":"Hij meldde me dat er een probleem was.","lesson":166,"level":"B1","cat":"verbo"},
    {"id":"w1578","it":"precisare","nl":"verduidelijken","ph":"pre-tsji-ZA-re","ex":"Ha precisato che l'incontro era a Roma.","exNl":"Hij verduidelijkte dat de ontmoeting in Rome was.","lesson":166,"level":"B1","cat":"verbo"},

    # ── Les 167: Technologie & internet ──
    {"id":"w1579","it":"scaricare","nl":"downloaden","ph":"ska-ri-KA-re","ex":"Devo scaricare un'app nuova.","exNl":"Ik moet een nieuwe app downloaden.","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1580","it":"aggiornare","nl":"updaten/bijwerken","ph":"ad-djor-NA-re","ex":"Devo aggiornare il telefono.","exNl":"Ik moet mijn telefoon updaten.","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1581","it":"il caricabatterie","nl":"de oplader","ph":"il ka-ri-ka-bat-te-RI-e","ex":"Hai un caricabatterie?","exNl":"Heb je een oplader?","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1582","it":"la connessione","nl":"de verbinding","ph":"la kon-nes-SJO-ne","ex":"La connessione è molto lenta.","exNl":"De verbinding is erg traag.","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1583","it":"il dispositivo","nl":"het apparaat","ph":"il dis-po-zi-TI-vo","ex":"Questo dispositivo è nuovo.","exNl":"Dit apparaat is nieuw.","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1584","it":"la password","nl":"het wachtwoord","ph":"la PAS-word","ex":"Ho dimenticato la password.","exNl":"Ik ben het wachtwoord vergeten.","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1585","it":"il sito web","nl":"de website","ph":"il SI-to web","ex":"Visita il nostro sito web.","exNl":"Bezoek onze website.","lesson":167,"level":"B1","cat":"tecnologia"},
    {"id":"w1586","it":"cliccare","nl":"klikken","ph":"klik-KA-re","ex":"Clicca sul link per registrarti.","exNl":"Klik op de link om je te registreren.","lesson":167,"level":"B1","cat":"tecnologia"},

    # ── Les 168: Sociale media ──
    {"id":"w1587","it":"condividere","nl":"delen","ph":"kon-di-VI-de-re","ex":"Ha condiviso una foto online.","exNl":"Hij heeft een foto online gedeeld.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1588","it":"pubblicare","nl":"publiceren/posten","ph":"pub-bli-KA-re","ex":"Ha pubblicato un post interessante.","exNl":"Hij heeft een interessant bericht gepost.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1589","it":"seguire","nl":"volgen","ph":"se-GWI-re","ex":"Ti seguo sui social.","exNl":"Ik volg je op social media.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1590","it":"il profilo","nl":"het profiel","ph":"il pro-FI-lo","ex":"Ho aggiornato il mio profilo.","exNl":"Ik heb mijn profiel bijgewerkt.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1591","it":"il contenuto","nl":"de inhoud/content","ph":"il kon-te-NU-to","ex":"Il contenuto è molto interessante.","exNl":"De inhoud is erg interessant.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1592","it":"il messaggio","nl":"het bericht","ph":"il mes-SAD-djo","ex":"Ti ho mandato un messaggio.","exNl":"Ik heb je een bericht gestuurd.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1593","it":"la notifica","nl":"de melding","ph":"la no-TI-fi-ka","ex":"Ho ricevuto una notifica.","exNl":"Ik heb een melding ontvangen.","lesson":168,"level":"B1","cat":"social"},
    {"id":"w1594","it":"la privacy","nl":"de privacy","ph":"la PRAJ-va-si","ex":"La privacy online è importante.","exNl":"Online privacy is belangrijk.","lesson":168,"level":"B1","cat":"social"},

    # ── Les 169: Film, boeken & muziek ──
    {"id":"w1595","it":"il romanzo","nl":"de roman","ph":"il ro-MAN-zo","ex":"Ho letto un romanzo bellissimo.","exNl":"Ik heb een prachtige roman gelezen.","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1596","it":"il giallo","nl":"de thriller/detective","ph":"il DJAL-lo","ex":"Mi piacciono i gialli di Camilleri.","exNl":"Ik hou van de thrillers van Camilleri.","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1597","it":"la colonna sonora","nl":"de soundtrack","ph":"la ko-LON-na so-NO-ra","ex":"La colonna sonora è magnifica.","exNl":"De soundtrack is prachtig.","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1598","it":"il regista","nl":"de regisseur","ph":"il re-DJIS-ta","ex":"Il regista ha vinto un premio.","exNl":"De regisseur heeft een prijs gewonnen.","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1599","it":"il genere","nl":"het genre","ph":"il DJE-ne-re","ex":"Che genere di film preferisci?","exNl":"Welk genre film heb je het liefst?","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1600","it":"la commedia","nl":"de komedie","ph":"la kom-ME-dja","ex":"Andiamo a vedere una commedia.","exNl":"Laten we een komedie gaan zien.","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1601","it":"il documentario","nl":"de documentaire","ph":"il do-ku-men-TA-rjo","ex":"Ho visto un documentario sulla natura.","exNl":"Ik heb een documentaire over de natuur gezien.","lesson":169,"level":"B1","cat":"cultura"},
    {"id":"w1602","it":"il capolavoro","nl":"het meesterwerk","ph":"il ka-po-la-VO-ro","ex":"Questo film è un capolavoro.","exNl":"Deze film is een meesterwerk.","lesson":169,"level":"B1","cat":"cultura"},

    # ── Les 170: Toetsles Blok 5 ──
    {"id":"w1603","it":"la comunicazione","nl":"de communicatie","ph":"la ko-mu-ni-ka-TSJO-ne","ex":"La comunicazione è fondamentale.","exNl":"Communicatie is essentieel.","lesson":170,"level":"B1","cat":"sostantivo"},
    {"id":"w1604","it":"esprimersi","nl":"zich uitdrukken","ph":"es-PRI-mer-si","ex":"Sa esprimersi molto bene.","exNl":"Hij kan zich heel goed uitdrukken.","lesson":170,"level":"B1","cat":"verbo"},
    {"id":"w1605","it":"il linguaggio","nl":"het taalgebruik","ph":"il lin-GWAD-djo","ex":"Il linguaggio formale è diverso.","exNl":"Het formele taalgebruik is anders.","lesson":170,"level":"B1","cat":"sostantivo"},
    {"id":"w1606","it":"tradurre","nl":"vertalen","ph":"tra-DUR-re","ex":"Puoi tradurre questa frase?","exNl":"Kun je deze zin vertalen?","lesson":170,"level":"B1","cat":"verbo"},
    {"id":"w1607","it":"interpretare","nl":"interpreteren/tolken","ph":"in-ter-pre-TA-re","ex":"Come interpreti questa frase?","exNl":"Hoe interpreteer je deze zin?","lesson":170,"level":"B1","cat":"verbo"},
    {"id":"w1608","it":"il significato","nl":"de betekenis","ph":"il sig-ni-fi-KA-to","ex":"Qual è il significato di questa parola?","exNl":"Wat is de betekenis van dit woord?","lesson":170,"level":"B1","cat":"sostantivo"},
    {"id":"w1609","it":"comprendere","nl":"begrijpen","ph":"kom-PREN-de-re","ex":"Comprendo il tuo punto di vista.","exNl":"Ik begrijp jouw standpunt.","lesson":170,"level":"B1","cat":"verbo"},
    {"id":"w1610","it":"fraintendere","nl":"verkeerd begrijpen","ph":"fra-in-TEN-de-re","ex":"Mi hai frainteso.","exNl":"Je hebt me verkeerd begrepen.","lesson":170,"level":"B1","cat":"verbo"},

    # ── Les 171: Vergelijkingen ──
    {"id":"w1611","it":"migliore","nl":"beter/beste","ph":"mil-JO-re","ex":"Questo è il migliore ristorante.","exNl":"Dit is het beste restaurant.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1612","it":"peggiore","nl":"slechter/slechtste","ph":"ped-DJO-re","ex":"La situazione è peggiore di ieri.","exNl":"De situatie is slechter dan gisteren.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1613","it":"maggiore","nl":"groter/ouder","ph":"mad-DJO-re","ex":"Mio fratello maggiore si chiama Paolo.","exNl":"Mijn oudere broer heet Paolo.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1614","it":"minore","nl":"kleiner/jonger","ph":"mi-NO-re","ex":"La mia sorella minore ha vent'anni.","exNl":"Mijn jongere zus is twintig jaar.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1615","it":"superiore","nl":"hoger/superieur","ph":"su-pe-RJO-re","ex":"La qualità è superiore.","exNl":"De kwaliteit is hoger.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1616","it":"inferiore","nl":"lager/inferieur","ph":"in-fe-RJO-re","ex":"Il prezzo è inferiore al previsto.","exNl":"De prijs is lager dan verwacht.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1617","it":"uguale","nl":"gelijk/hetzelfde","ph":"u-GWA-le","ex":"Siamo tutti uguali.","exNl":"We zijn allemaal gelijk.","lesson":171,"level":"B1","cat":"comparativo"},
    {"id":"w1618","it":"diverso","nl":"anders/verschillend","ph":"di-VER-so","ex":"Ogni persona è diversa.","exNl":"Ieder persoon is anders.","lesson":171,"level":"B1","cat":"comparativo"},

    # ── Les 172: Superlatieven ──
    {"id":"w1619","it":"bellissimo","nl":"heel mooi/prachtig","ph":"bel-LIS-si-mo","ex":"Il panorama è bellissimo.","exNl":"Het uitzicht is prachtig.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1620","it":"grandissimo","nl":"heel groot/enorm","ph":"gran-DIS-si-mo","ex":"Ha un grandissimo talento.","exNl":"Hij heeft enorm veel talent.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1621","it":"ottimo","nl":"uitstekend","ph":"OT-ti-mo","ex":"Il cibo era ottimo.","exNl":"Het eten was uitstekend.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1622","it":"pessimo","nl":"heel slecht","ph":"PES-si-mo","ex":"Il servizio era pessimo.","exNl":"De service was heel slecht.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1623","it":"velocissimo","nl":"heel snel","ph":"ve-lo-TSHIS-si-mo","ex":"Il treno è velocissimo.","exNl":"De trein is heel snel.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1624","it":"lentissimo","nl":"heel langzaam","ph":"len-TIS-si-mo","ex":"Il wifi è lentissimo.","exNl":"De wifi is heel langzaam.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1625","it":"facilissimo","nl":"heel makkelijk","ph":"fa-tshi-LIS-si-mo","ex":"L'esercizio era facilissimo.","exNl":"De oefening was heel makkelijk.","lesson":172,"level":"B1","cat":"superlativo"},
    {"id":"w1626","it":"difficilissimo","nl":"heel moeilijk","ph":"dif-fi-tshi-LIS-si-mo","ex":"L'esame era difficilissimo.","exNl":"Het examen was heel moeilijk.","lesson":172,"level":"B1","cat":"superlativo"},

    # ── Les 173: Hypothese type 1 ──
    {"id":"w1627","it":"la condizione","nl":"de voorwaarde","ph":"la kon-di-TSJO-ne","ex":"A una condizione: devi studiare.","exNl":"Op één voorwaarde: je moet studeren.","lesson":173,"level":"B1","cat":"ipotesi"},
    {"id":"w1628","it":"nel caso in cui","nl":"in het geval dat","ph":"nel KA-zo in kui","ex":"Nel caso in cui piova, restiamo dentro.","exNl":"In het geval dat het regent, blijven we binnen.","lesson":173,"level":"B1","cat":"espressione"},
    {"id":"w1629","it":"a patto che","nl":"op voorwaarde dat","ph":"a PAT-to ke","ex":"Vengo a patto che tu venga.","exNl":"Ik kom, op voorwaarde dat jij ook komt.","lesson":173,"level":"B1","cat":"espressione"},
    {"id":"w1630","it":"altrimenti","nl":"anders/zo niet","ph":"al-tri-MEN-ti","ex":"Sbrigati, altrimenti perdiamo il treno.","exNl":"Schiet op, anders missen we de trein.","lesson":173,"level":"B1","cat":"avverbio"},
    {"id":"w1631","it":"eventualmente","nl":"eventueel/mogelijk","ph":"e-ven-tual-MEN-te","ex":"Eventualmente potremmo cambiare piano.","exNl":"Eventueel zouden we van plan kunnen veranderen.","lesson":173,"level":"B1","cat":"avverbio"},
    {"id":"w1632","it":"qualora","nl":"indien/mocht","ph":"kwa-LO-ra","ex":"Qualora dovesse piovere, portiamo l'ombrello.","exNl":"Mocht het regenen, nemen we de paraplu mee.","lesson":173,"level":"B1","cat":"congiunzione"},
    {"id":"w1633","it":"supponiamo che","nl":"stel dat","ph":"sup-po-NJA-mo ke","ex":"Supponiamo che non venga, che facciamo?","exNl":"Stel dat hij niet komt, wat doen we?","lesson":173,"level":"B1","cat":"espressione"},
    {"id":"w1634","it":"nel peggiore dei casi","nl":"in het ergste geval","ph":"nel ped-DJO-re dej KA-zi","ex":"Nel peggiore dei casi, prendiamo un taxi.","exNl":"In het ergste geval nemen we een taxi.","lesson":173,"level":"B1","cat":"espressione"},

    # ── Les 174: Hypothese type 2 ──
    {"id":"w1635","it":"se fossi","nl":"als ik was/zou zijn","ph":"se FOS-si","ex":"Se fossi ricco, viaggerei sempre.","exNl":"Als ik rijk was, zou ik altijd reizen.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1636","it":"se avessi","nl":"als ik had/zou hebben","ph":"se a-VES-si","ex":"Se avessi più tempo, leggerei di più.","exNl":"Als ik meer tijd had, zou ik meer lezen.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1637","it":"se potessi","nl":"als ik kon/zou kunnen","ph":"se po-TES-si","ex":"Se potessi, andrei in vacanza.","exNl":"Als ik kon, zou ik op vakantie gaan.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1638","it":"se sapessi","nl":"als ik wist/zou weten","ph":"se sa-PES-si","ex":"Se sapessi la risposta, te la direi.","exNl":"Als ik het antwoord wist, zou ik het je zeggen.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1639","it":"se dovessi","nl":"als ik moest/zou moeten","ph":"se do-VES-si","ex":"Se dovessi scegliere, prenderei questo.","exNl":"Als ik moest kiezen, zou ik deze nemen.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1640","it":"se volessi","nl":"als ik wilde/zou willen","ph":"se vo-LES-si","ex":"Se volessi, potrei farlo.","exNl":"Als ik wilde, zou ik het kunnen doen.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1641","it":"se andassi","nl":"als ik ging/zou gaan","ph":"se an-DAS-si","ex":"Se andassi a Roma, visiterei il Colosseo.","exNl":"Als ik naar Rome zou gaan, zou ik het Colosseum bezoeken.","lesson":174,"level":"B1","cat":"ipotesi"},
    {"id":"w1642","it":"se facessi","nl":"als ik deed/zou doen","ph":"se fa-TSHES-si","ex":"Se facessi sport, mi sentirei meglio.","exNl":"Als ik zou sporten, zou ik me beter voelen.","lesson":174,"level":"B1","cat":"ipotesi"},

    # ── Les 175: Formeel & informeel ──
    {"id":"w1643","it":"formale","nl":"formeel","ph":"for-MA-le","ex":"Il tono della lettera è formale.","exNl":"De toon van de brief is formeel.","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1644","it":"informale","nl":"informeel","ph":"in-for-MA-le","ex":"Usiamo un tono informale tra amici.","exNl":"We gebruiken een informele toon onder vrienden.","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1645","it":"dare del Lei","nl":"u zeggen (vousvoyeren)","ph":"DA-re del lej","ex":"In Italia si dà del Lei agli sconosciuti.","exNl":"In Italië zeg je 'u' tegen onbekenden.","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1646","it":"dare del tu","nl":"je/jij zeggen (tutoyeren)","ph":"DA-re del tu","ex":"Ci diamo del tu?","exNl":"Zeggen we je/jij tegen elkaar?","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1647","it":"la cortesia","nl":"de beleefdheid","ph":"la kor-te-ZI-a","ex":"La cortesia è molto apprezzata.","exNl":"Beleefdheid wordt erg gewaardeerd.","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1648","it":"l'educazione","nl":"de opvoeding/beleefdheid","ph":"le-du-ka-TSJO-ne","ex":"È una questione di educazione.","exNl":"Het is een kwestie van opvoeding.","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1649","it":"appropriato","nl":"gepast","ph":"ap-pro-prja-TO","ex":"Non è un linguaggio appropriato.","exNl":"Dat is geen gepast taalgebruik.","lesson":175,"level":"B1","cat":"registro"},
    {"id":"w1650","it":"il registro","nl":"het register/taalregister","ph":"il re-DJIS-tro","ex":"Cambia registro a seconda del contesto.","exNl":"Hij past zijn taalregister aan per context.","lesson":175,"level":"B1","cat":"registro"},

    # ── Les 176: Italiaanse regio's ──
    {"id":"w1651","it":"la regione","nl":"de regio","ph":"la re-DJO-ne","ex":"L'Italia ha venti regioni.","exNl":"Italië heeft twintig regio's.","lesson":176,"level":"B1","cat":"geografia"},
    {"id":"w1652","it":"il capoluogo","nl":"de hoofdstad (regio)","ph":"il ka-po-LWO-go","ex":"Milano è il capoluogo della Lombardia.","exNl":"Milaan is de hoofdstad van Lombardije.","lesson":176,"level":"B1","cat":"geografia"},
    {"id":"w1653","it":"la costa","nl":"de kust","ph":"la KOS-ta","ex":"La costa amalfitana è bellissima.","exNl":"De Amalfikust is prachtig.","lesson":176,"level":"B1","cat":"geografia"},
    {"id":"w1654","it":"la collina","nl":"de heuvel","ph":"la kol-LI-na","ex":"La casa si trova in collina.","exNl":"Het huis ligt op een heuvel.","lesson":176,"level":"B1","cat":"geografia"},
    {"id":"w1655","it":"la pianura","nl":"de vlakte","ph":"la pja-NU-ra","ex":"La Pianura Padana è molto fertile.","exNl":"De Povlakte is erg vruchtbaar.","lesson":176,"level":"B1","cat":"geografia"},
    {"id":"w1656","it":"il paesaggio","nl":"het landschap","ph":"il pa-e-ZAD-djo","ex":"Il paesaggio toscano è unico.","exNl":"Het Toscaanse landschap is uniek.","lesson":176,"level":"B1","cat":"geografia"},
    {"id":"w1657","it":"il patrimonio","nl":"het erfgoed","ph":"il pa-tri-MO-njo","ex":"L'Italia ha un grande patrimonio culturale.","exNl":"Italië heeft een groot cultureel erfgoed.","lesson":176,"level":"B1","cat":"cultura"},
    {"id":"w1658","it":"caratteristico","nl":"karakteristiek/typisch","ph":"ka-rat-te-RIS-ti-ko","ex":"È un borgo molto caratteristico.","exNl":"Het is een heel karakteristiek dorpje.","lesson":176,"level":"B1","cat":"aggettivo"},

    # ── Les 177: Italiaanse keuken verdieping ──
    {"id":"w1659","it":"la specialità","nl":"de specialiteit","ph":"la spe-tsja-li-TA","ex":"La specialità della casa è la pasta.","exNl":"De specialiteit van het huis is de pasta.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1660","it":"il piatto tipico","nl":"het typische gerecht","ph":"il PJAT-to TI-pi-ko","ex":"Il piatto tipico di Bologna sono le tagliatelle.","exNl":"Het typische gerecht van Bologna is tagliatelle.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1661","it":"la ricetta tradizionale","nl":"het traditionele recept","ph":"la ri-TSJET-ta tra-di-tsjo-NA-le","ex":"Questa è la ricetta tradizionale.","exNl":"Dit is het traditionele recept.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1662","it":"il sapore","nl":"de smaak","ph":"il sa-PO-re","ex":"Ha un sapore delizioso.","exNl":"Het heeft een heerlijke smaak.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1663","it":"la porzione","nl":"de portie","ph":"la por-TSJO-ne","ex":"Le porzioni sono molto generose.","exNl":"De porties zijn erg royaal.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1664","it":"il vigneto","nl":"de wijngaard","ph":"il vin-JE-to","ex":"Abbiamo visitato un vigneto in Toscana.","exNl":"We hebben een wijngaard in Toscane bezocht.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1665","it":"l'olio d'oliva","nl":"de olijfolie","ph":"LO-ljo do-LI-va","ex":"L'olio d'oliva italiano è famoso.","exNl":"De Italiaanse olijfolie is beroemd.","lesson":177,"level":"B1","cat":"cucina"},
    {"id":"w1666","it":"il formaggio","nl":"de kaas","ph":"il for-MAD-djo","ex":"Il Parmigiano è il re dei formaggi.","exNl":"De Parmezaan is de koning van de kazen.","lesson":177,"level":"B1","cat":"cucina"},

    # ── Les 178: Cultuur & etiquette ──
    {"id":"w1667","it":"la tradizione","nl":"de traditie","ph":"la tra-di-TSJO-ne","ex":"È una tradizione molto antica.","exNl":"Het is een heel oude traditie.","lesson":178,"level":"B1","cat":"cultura"},
    {"id":"w1668","it":"l'usanza","nl":"de gewoonte/het gebruik","ph":"lu-ZAN-tsa","ex":"È un'usanza tipicamente italiana.","exNl":"Het is een typisch Italiaans gebruik.","lesson":178,"level":"B1","cat":"cultura"},
    {"id":"w1669","it":"il gesto","nl":"het gebaar","ph":"il DJES-to","ex":"Gli italiani usano molti gesti.","exNl":"Italianen gebruiken veel gebaren.","lesson":178,"level":"B1","cat":"cultura"},
    {"id":"w1670","it":"maleducato","nl":"onbeleefd","ph":"ma-le-du-KA-to","ex":"È maleducato parlare con la bocca piena.","exNl":"Het is onbeleefd om met volle mond te praten.","lesson":178,"level":"B1","cat":"cultura"},
    {"id":"w1671","it":"il galateo","nl":"de etiquette","ph":"il ga-la-TE-o","ex":"Il galateo a tavola è importante.","exNl":"Tafel-etiquette is belangrijk.","lesson":178,"level":"B1","cat":"cultura"},
    {"id":"w1672","it":"rispettare","nl":"respecteren","ph":"ris-pet-TA-re","ex":"Bisogna rispettare le tradizioni locali.","exNl":"Je moet de lokale tradities respecteren.","lesson":178,"level":"B1","cat":"verbo"},
    {"id":"w1673","it":"la mentalità","nl":"de mentaliteit","ph":"la men-ta-li-TA","ex":"La mentalità varia da regione a regione.","exNl":"De mentaliteit verschilt per regio.","lesson":178,"level":"B1","cat":"cultura"},
    {"id":"w1674","it":"ospitale","nl":"gastvrij","ph":"os-pi-TA-le","ex":"Gli italiani sono molto ospitali.","exNl":"De Italianen zijn erg gastvrij.","lesson":178,"level":"B1","cat":"aggettivo"},

    # ── Les 179: Toekomstplannen ──
    {"id":"w1675","it":"l'intenzione","nl":"de intentie/het voornemen","ph":"lin-ten-TSJO-ne","ex":"Ho intenzione di cambiare lavoro.","exNl":"Ik ben van plan om van baan te veranderen.","lesson":179,"level":"B1","cat":"futuro"},
    {"id":"w1676","it":"il traguardo","nl":"het doel/de mijlpaal","ph":"il tra-GWAR-do","ex":"Ho raggiunto un importante traguardo.","exNl":"Ik heb een belangrijke mijlpaal bereikt.","lesson":179,"level":"B1","cat":"futuro"},
    {"id":"w1677","it":"impegnarsi","nl":"zich inzetten","ph":"im-pen-JAR-si","ex":"Mi impegno a studiare ogni giorno.","exNl":"Ik zet me in om elke dag te studeren.","lesson":179,"level":"B1","cat":"verbo"},
    {"id":"w1678","it":"migliorarsi","nl":"zichzelf verbeteren","ph":"mil-jo-RAR-si","ex":"Cerco sempre di migliorarmi.","exNl":"Ik probeer mezelf altijd te verbeteren.","lesson":179,"level":"B1","cat":"verbo"},
    {"id":"w1679","it":"il progresso","nl":"de vooruitgang","ph":"il pro-GRES-so","ex":"Ho fatto molto progresso.","exNl":"Ik heb veel vooruitgang geboekt.","lesson":179,"level":"B1","cat":"sostantivo"},
    {"id":"w1680","it":"la sfida","nl":"de uitdaging","ph":"la SFI-da","ex":"Ogni giorno è una nuova sfida.","exNl":"Elke dag is een nieuwe uitdaging.","lesson":179,"level":"B1","cat":"sostantivo"},
    {"id":"w1681","it":"la determinazione","nl":"de vastberadenheid","ph":"la de-ter-mi-na-TSJO-ne","ex":"Ci vuole determinazione per imparare.","exNl":"Er is vastberadenheid nodig om te leren.","lesson":179,"level":"B1","cat":"sostantivo"},
    {"id":"w1682","it":"costante","nl":"constant/volhardend","ph":"kos-TAN-te","ex":"L'impegno costante dà risultati.","exNl":"Constante inzet levert resultaten op.","lesson":179,"level":"B1","cat":"aggettivo"},

    # ── Les 180: 🎓 B1 afgerond! ──
    {"id":"w1683","it":"il livello","nl":"het niveau","ph":"il li-VEL-lo","ex":"Hai raggiunto il livello B1!","exNl":"Je hebt niveau B1 bereikt!","lesson":180,"level":"B1","cat":"istruzione"},
    {"id":"w1684","it":"padroneggiare","nl":"beheersen","ph":"pa-dro-ned-DJA-re","ex":"Ora padroneggi molte strutture.","exNl":"Nu beheers je veel structuren.","lesson":180,"level":"B1","cat":"verbo"},
    {"id":"w1685","it":"fluente","nl":"vloeiend","ph":"flu-EN-te","ex":"Parli in modo sempre più fluente.","exNl":"Je spreekt steeds vloeiender.","lesson":180,"level":"B1","cat":"aggettivo"},
    {"id":"w1686","it":"la competenza linguistica","nl":"de taalvaardigheid","ph":"la kom-pe-TEN-tsa lin-GWIS-ti-ka","ex":"La tua competenza linguistica è cresciuta.","exNl":"Je taalvaardigheid is gegroeid.","lesson":180,"level":"B1","cat":"istruzione"},
    {"id":"w1687","it":"complimenti","nl":"gefeliciteerd","ph":"kom-pli-MEN-ti","ex":"Complimenti per il tuo impegno!","exNl":"Gefeliciteerd met je inzet!","lesson":180,"level":"B1","cat":"espressione"},
    {"id":"w1688","it":"il percorso","nl":"het traject/de route","ph":"il per-KOR-so","ex":"È stato un bel percorso.","exNl":"Het was een mooi traject.","lesson":180,"level":"B1","cat":"sostantivo"},
    {"id":"w1689","it":"proseguire","nl":"doorgaan/vervolgen","ph":"pro-se-GWI-re","ex":"Prosegui così, sei bravissimo!","exNl":"Ga zo door, je bent heel goed!","lesson":180,"level":"B1","cat":"verbo"},
    {"id":"w1690","it":"il successo","nl":"het succes","ph":"il sut-TSHES-so","ex":"Il tuo successo è meritato.","exNl":"Jouw succes is verdiend.","lesson":180,"level":"B1","cat":"sostantivo"},
]

# ── LADEN & SAMENVOEGEN ───────────────────────────────────────────────────────

with open(CURR_FILE, encoding='utf-8') as f:
    cur = json.load(f)
with open(VOCAB_FILE, encoding='utf-8') as f:
    vocab = json.load(f)

# Duplicaatcontrole (alleen waarschuwing, niet overslaan — B1-lessen verwijzen naar deze IDs)
existing_it = {w['it'].lower() for w in vocab}
dupes = [w['it'] for w in new_words if w['it'].lower() in existing_it]
if dupes:
    print(f'ℹ️  {len(dupes)} woorden komen ook in A1/A2 voor (worden opnieuw toegevoegd met B1-ID)')

# ID-controle
existing_ids = {w['id'] for w in vocab}
id_dupes = [w['id'] for w in new_words if w['id'] in existing_ids]
if id_dupes:
    print(f'⚠️  Dubbele IDs gevonden: {id_dupes}')

# Lesson-ID-controle
existing_lesson_ids = {l['id'] for l in cur}
lesson_dupes = [l['id'] for l in new_lessons if l['id'] in existing_lesson_ids]
if lesson_dupes:
    print(f'⚠️  Dubbele les-IDs gevonden: {lesson_dupes}')

# Toevoegen
cur.extend(new_lessons)
vocab.extend(new_words)

# ── SCHRIJVEN ─────────────────────────────────────────────────────────────────

with open(CURR_FILE, 'w', encoding='utf-8') as f:
    json.dump(cur, f, ensure_ascii=False, indent=2)
with open(VOCAB_FILE, 'w', encoding='utf-8') as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

print(f'✓ {len(new_lessons)} nieuwe B1-lessen toegevoegd (121-180)')
print(f'✓ {len(new_words)} nieuwe woorden toegevoegd')
print(f'  Totaal lessen: {len(cur)}')
print(f'  Totaal woorden: {len(vocab)}')
