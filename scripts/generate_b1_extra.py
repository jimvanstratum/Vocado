#!/usr/bin/env python3
"""
Vocado — B1-uitbreiding: lessen 181–300 (120 lessen, 960 woorden)
Voert samen met bestaande curriculum.json en vocabulary.json.
"""
import json, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR   = os.path.join(SCRIPT_DIR, '..', 'www', 'data')

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 7: Passato remoto & Italiaanse geschiedenis (lessen 181–190)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS = [
  {"id":181,"title":"Passato remoto — regelmatig","emoji":"📜","level":"B1",
   "description":"Leer de passato remoto van regelmatige werkwoorden.",
   "grammar":{"title":"Passato remoto — regelmatig",
   "body":"De passato remoto beschrijft afgesloten handelingen in het (verre) verleden. Je vindt hem vooral in boeken, kranten en verhalen.\n\n-are → parlai, parlasti, parlò, parlammo, parlaste, parlarono\n-ere → credei (credetti), credesti, credé (credette), credemmo, credeste, crederono (credettero)\n-ire → dormii, dormisti, dormì, dormimmo, dormiste, dormirono\n\nVuistregel: in Noord-Italië gebruikt men vaker de passato prossimo; in Zuid-Italië en in geschreven taal is de passato remoto gangbaar."},
   "words":["w1691","w1692","w1693","w1694","w1695","w1696","w1697","w1698"]},

  {"id":182,"title":"Passato remoto — onregelmatig","emoji":"📜","level":"B1",
   "description":"De belangrijkste onregelmatige vormen van de passato remoto.",
   "grammar":{"title":"Passato remoto — onregelmatig",
   "body":"Veel veelgebruikte werkwoorden zijn onregelmatig in de passato remoto. De 1e, 3e persoon enkelvoud en 3e persoon meervoud zijn afwijkend; de overige volgen het regelmatige patroon.\n\nessere → fui, fosti, fu, fummo, foste, furono\navere → ebbi, avesti, ebbe, avemmo, aveste, ebbero\nfare → feci, facesti, fece, facemmo, faceste, fecero\ndire → dissi, dicesti, disse, dicemmo, diceste, dissero\nvenire → venni, venisti, venne, venimmo, veniste, vennero"},
   "words":["w1699","w1700","w1701","w1702","w1703","w1704","w1705","w1706"]},

  {"id":183,"title":"Italiaanse geschiedenis","emoji":"🏛️","level":"B1",
   "description":"Praat over historische gebeurtenissen met de passato remoto.",
   "grammar":{"title":"Passato remoto in context",
   "body":"De passato remoto wordt vaak gebruikt bij historische feiten:\n\nRoma fu fondata nel 753 a.C. — Rome werd gesticht in 753 v.Chr.\nDante scrisse la Divina Commedia. — Dante schreef de Goddelijke Komedie.\n\nLet op: bij persoonlijke ervaringen gebruik je in gesproken Italiaans liever de passato prossimo."},
   "words":["w1707","w1708","w1709","w1710","w1711","w1712","w1713","w1714"]},

  {"id":184,"title":"Kunst & architectuur","emoji":"🎨","level":"B1",
   "description":"Woorden over Italiaanse kunst en bouwwerken.",
   "grammar":{"title":"Kunst beschrijven",
   "body":"Bij het beschrijven van kunst en architectuur gebruik je vaak de passato remoto (voor historische feiten) en het passief:\n\nIl Colosseo fu costruito dai Romani. — Het Colosseum werd gebouwd door de Romeinen.\nQuesto quadro fu dipinto da Caravaggio. — Dit schilderij werd geschilderd door Caravaggio."},
   "words":["w1715","w1716","w1717","w1718","w1719","w1720","w1721","w1722"]},

  {"id":185,"title":"Beroemde Italianen","emoji":"🌟","level":"B1",
   "description":"Leer over bekende Italiaanse personen en hun bijdragen.",
   "grammar":{"title":"Biografieën vertellen",
   "body":"Bij biografieën combineer je de passato remoto met tijdsaanduidingen:\n\nLeonardo nacque nel 1452 e morì nel 1519. — Leonardo werd geboren in 1452 en stierf in 1519.\n\nnascere → nacqui, nascesti, nacque, nascemmo, nasceste, nacquero\nmorire → morii, moristi, morì, morimmo, moriste, morirono"},
   "words":["w1723","w1724","w1725","w1726","w1727","w1728","w1729","w1730"]},

  {"id":186,"title":"De Renaissance","emoji":"🖼️","level":"B1",
   "description":"De Italiaanse Renaissance en haar invloed op Europa.",
   "grammar":{"title":"Historische periodes beschrijven",
   "body":"Gebruik de passato remoto voor historische feiten en het imperfetto voor beschrijvingen van de tijd:\n\nDurante il Rinascimento, Firenze era il centro dell'arte. — Tijdens de Renaissance was Florence het centrum van de kunst.\nMichelangelo scolpì il David nel 1504. — Michelangelo beeldhouwde de David in 1504."},
   "words":["w1731","w1732","w1733","w1734","w1735","w1736","w1737","w1738"]},

  {"id":187,"title":"Moderne geschiedenis","emoji":"📰","level":"B1",
   "description":"Italiaanse geschiedenis van de 19e en 20e eeuw.",
   "grammar":{"title":"Moderne geschiedenis vertellen",
   "body":"Bij recente geschiedenis gebruik je zowel passato remoto (formeel/geschreven) als passato prossimo (gesproken):\n\nL'Italia fu unificata nel 1861. (passato remoto, formeel)\nL'Italia è stata unificata nel 1861. (passato prossimo, gesproken)"},
   "words":["w1739","w1740","w1741","w1742","w1743","w1744","w1745","w1746"]},

  {"id":188,"title":"Tradities & feestdagen","emoji":"🎄","level":"B1",
   "description":"Italiaanse feestdagen en tradities door het jaar heen.",
   "grammar":{"title":"Tradities beschrijven",
   "body":"Bij tradities gebruik je vaak het presens (gewoonte) of imperfetto (vroeger):\n\nA Natale si mangia il panettone. — Met Kerst eet men panettone.\nQuando ero piccolo, a Pasqua andavamo sempre dai nonni. — Toen ik klein was, gingen we met Pasen altijd naar opa en oma."},
   "words":["w1747","w1748","w1749","w1750","w1751","w1752","w1753","w1754"]},

  {"id":189,"title":"Italiaanse muziek","emoji":"🎵","level":"B1",
   "description":"Van opera tot moderne Italiaanse muziek.",
   "grammar":{"title":"Over muziek praten",
   "body":"Nuttige constructies bij het praten over muziek:\n\nQuesta canzone è stata scritta da… — Dit lied is geschreven door…\nMi piace ascoltare… — Ik luister graag naar…\nSuonare uno strumento — een instrument bespelen\nCantare una canzone — een lied zingen"},
   "words":["w1755","w1756","w1757","w1758","w1759","w1760","w1761","w1762"]},

  {"id":190,"title":"Toetsles B1 — Blok 7","emoji":"📋","level":"B1",
   "description":"Toets over lessen 181–190: passato remoto & Italiaanse cultuur.",
   "grammar":{"title":"Toetsles B1 — Blok 7 (les 181–190)","body":"In dit blok heb je geleerd:\n• De passato remoto (regelmatig en onregelmatig)\n• Historische feiten beschrijven\n• Kunst, architectuur en muziek bespreken\n• Italiaanse tradities en feestdagen"},
   "words":["w1763","w1764","w1765","w1766","w1767","w1768","w1769","w1770"]},
]

WORDS = [
  # ── Les 181: Passato remoto — regelmatig ──
  {"id":"w1691","it":"fondare","nl":"stichten","ph":"fon-DA-re","ex":"I Romani fondarono Roma.","exNl":"De Romeinen stichtten Rome.","lesson":181,"level":"B1","cat":"verbo"},
  {"id":"w1692","it":"conquistare","nl":"veroveren","ph":"kon-kwis-TA-re","ex":"Cesare conquistò la Gallia.","exNl":"Caesar veroverde Gallië.","lesson":181,"level":"B1","cat":"verbo"},
  {"id":"w1693","it":"governare","nl":"regeren","ph":"go-ver-NA-re","ex":"Il re governò per trent'anni.","exNl":"De koning regeerde dertig jaar.","lesson":181,"level":"B1","cat":"verbo"},
  {"id":"w1694","it":"scoprire","nl":"ontdekken","ph":"sko-PRI-re","ex":"Colombo scoprì l'America.","exNl":"Columbus ontdekte Amerika.","lesson":181,"level":"B1","cat":"verbo"},
  {"id":"w1695","it":"costruire","nl":"bouwen","ph":"kos-tru-I-re","ex":"Costruirono un grande ponte.","exNl":"Ze bouwden een grote brug.","lesson":181,"level":"B1","cat":"verbo"},
  {"id":"w1696","it":"combattere","nl":"vechten, strijden","ph":"kom-BAT-te-re","ex":"I soldati combatterono con coraggio.","exNl":"De soldaten vochten met moed.","lesson":181,"level":"B1","cat":"verbo"},
  {"id":"w1697","it":"la battaglia","nl":"de slag, het gevecht","ph":"bat-TA-lja","ex":"La battaglia durò tre giorni.","exNl":"De slag duurde drie dagen.","lesson":181,"level":"B1","cat":"sostantivo"},
  {"id":"w1698","it":"il secolo","nl":"de eeuw","ph":"SE-ko-lo","ex":"Nel diciottesimo secolo ci furono molte guerre.","exNl":"In de achttiende eeuw waren er veel oorlogen.","lesson":181,"level":"B1","cat":"sostantivo"},

  # ── Les 182: Passato remoto — onregelmatig ──
  {"id":"w1699","it":"scrivere","nl":"schrijven (p.r.: scrisse)","ph":"SKRI-ve-re","ex":"Dante scrisse la Divina Commedia.","exNl":"Dante schreef de Goddelijke Komedie.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1700","it":"prendere","nl":"nemen, pakken (p.r.: prese)","ph":"PREN-de-re","ex":"Prese una decisione importante.","exNl":"Hij nam een belangrijk besluit.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1701","it":"mettere","nl":"zetten, leggen (p.r.: mise)","ph":"MET-te-re","ex":"Mise il libro sul tavolo.","exNl":"Hij legde het boek op tafel.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1702","it":"nascere","nl":"geboren worden (p.r.: nacque)","ph":"NA-she-re","ex":"Mozart nacque nel 1756.","exNl":"Mozart werd geboren in 1756.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1703","it":"vivere","nl":"leven (p.r.: visse)","ph":"VI-ve-re","ex":"Visse a Firenze per molti anni.","exNl":"Hij leefde vele jaren in Florence.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1704","it":"morire","nl":"sterven (p.r.: morì)","ph":"mo-RI-re","ex":"Leonardo morì in Francia.","exNl":"Leonardo stierf in Frankrijk.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1705","it":"cadere","nl":"vallen (p.r.: cadde)","ph":"ka-DE-re","ex":"L'Impero Romano cadde nel 476.","exNl":"Het Romeinse Rijk viel in 476.","lesson":182,"level":"B1","cat":"verbo"},
  {"id":"w1706","it":"vincere","nl":"winnen (p.r.: vinse)","ph":"VIN-tsje-re","ex":"L'Italia vinse la Coppa del Mondo.","exNl":"Italië won het WK.","lesson":182,"level":"B1","cat":"verbo"},

  # ── Les 183: Italiaanse geschiedenis ──
  {"id":"w1707","it":"l'impero","nl":"het rijk, het keizerrijk","ph":"im-PE-ro","ex":"L'Impero Romano fu molto potente.","exNl":"Het Romeinse Rijk was zeer machtig.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1708","it":"la repubblica","nl":"de republiek","ph":"re-PUB-bli-ka","ex":"L'Italia divenne una repubblica nel 1946.","exNl":"Italië werd een republiek in 1946.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1709","it":"il re","nl":"de koning","ph":"RE","ex":"Il re governò con saggezza.","exNl":"De koning regeerde met wijsheid.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1710","it":"la regina","nl":"de koningin","ph":"re-DJI-na","ex":"La regina amava la musica.","exNl":"De koningin hield van muziek.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1711","it":"la guerra","nl":"de oorlog","ph":"GWER-ra","ex":"La Seconda Guerra Mondiale finì nel 1945.","exNl":"De Tweede Wereldoorlog eindigde in 1945.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1712","it":"la pace","nl":"de vrede","ph":"PA-tsje","ex":"Dopo la guerra venne la pace.","exNl":"Na de oorlog kwam de vrede.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1713","it":"il popolo","nl":"het volk","ph":"PO-po-lo","ex":"Il popolo italiano è molto diverso.","exNl":"Het Italiaanse volk is zeer divers.","lesson":183,"level":"B1","cat":"sostantivo"},
  {"id":"w1714","it":"unire","nl":"verenigen","ph":"u-NI-re","ex":"Garibaldi unì l'Italia.","exNl":"Garibaldi verenigde Italië.","lesson":183,"level":"B1","cat":"verbo"},

  # ── Les 184: Kunst & architectuur ──
  {"id":"w1715","it":"il quadro","nl":"het schilderij","ph":"KWA-dro","ex":"Questo quadro è di Botticelli.","exNl":"Dit schilderij is van Botticelli.","lesson":184,"level":"B1","cat":"sostantivo"},
  {"id":"w1716","it":"la scultura","nl":"het beeldhouwwerk","ph":"skul-TU-ra","ex":"La scultura è fatta di marmo.","exNl":"Het beeldhouwwerk is van marmer gemaakt.","lesson":184,"level":"B1","cat":"sostantivo"},
  {"id":"w1717","it":"il marmo","nl":"het marmer","ph":"MAR-mo","ex":"Il David di Michelangelo è in marmo.","exNl":"De David van Michelangelo is van marmer.","lesson":184,"level":"B1","cat":"sostantivo"},
  {"id":"w1718","it":"l'affresco","nl":"het fresco","ph":"af-FRES-ko","ex":"Gli affreschi della Cappella Sistina sono famosi.","exNl":"De fresco's van de Sixtijnse Kapel zijn beroemd.","lesson":184,"level":"B1","cat":"sostantivo"},
  {"id":"w1719","it":"la cattedrale","nl":"de kathedraal","ph":"kat-te-DRA-le","ex":"La cattedrale di Milano è gotica.","exNl":"De kathedraal van Milaan is gotisch.","lesson":184,"level":"B1","cat":"sostantivo"},
  {"id":"w1720","it":"la cupola","nl":"de koepel","ph":"KU-po-la","ex":"La cupola di Brunelleschi è a Firenze.","exNl":"De koepel van Brunelleschi staat in Florence.","lesson":184,"level":"B1","cat":"sostantivo"},
  {"id":"w1721","it":"dipingere","nl":"schilderen (p.r.: dipinse)","ph":"di-PIN-dje-re","ex":"Raffaello dipinse molti capolavori.","exNl":"Rafaël schilderde vele meesterwerken.","lesson":184,"level":"B1","cat":"verbo"},
  {"id":"w1722","it":"il capolavoro","nl":"het meesterwerk","ph":"ka-po-la-VO-ro","ex":"La Gioconda è un capolavoro.","exNl":"De Mona Lisa is een meesterwerk.","lesson":184,"level":"B1","cat":"sostantivo"},

  # ── Les 185: Beroemde Italianen ──
  {"id":"w1723","it":"lo scienziato","nl":"de wetenschapper","ph":"sjen-TSJA-to","ex":"Galileo fu un grande scienziato.","exNl":"Galileo was een groot wetenschapper.","lesson":185,"level":"B1","cat":"sostantivo"},
  {"id":"w1724","it":"l'inventore","nl":"de uitvinder","ph":"in-ven-TO-re","ex":"Leonardo fu inventore e artista.","exNl":"Leonardo was uitvinder en kunstenaar.","lesson":185,"level":"B1","cat":"sostantivo"},
  {"id":"w1725","it":"il compositore","nl":"de componist","ph":"kom-po-zi-TO-re","ex":"Verdi fu un grande compositore.","exNl":"Verdi was een groot componist.","lesson":185,"level":"B1","cat":"sostantivo"},
  {"id":"w1726","it":"il poeta","nl":"de dichter","ph":"po-E-ta","ex":"Petrarca fu un poeta importante.","exNl":"Petrarca was een belangrijk dichter.","lesson":185,"level":"B1","cat":"sostantivo"},
  {"id":"w1727","it":"l'opera","nl":"het werk; de opera","ph":"O-pe-ra","ex":"Le opere di Verdi sono famose.","exNl":"De werken van Verdi zijn beroemd.","lesson":185,"level":"B1","cat":"sostantivo"},
  {"id":"w1728","it":"il genio","nl":"het genie","ph":"DJE-nio","ex":"Leonardo da Vinci era un genio.","exNl":"Leonardo da Vinci was een genie.","lesson":185,"level":"B1","cat":"sostantivo"},
  {"id":"w1729","it":"influenzare","nl":"beïnvloeden","ph":"in-flu-en-TSA-re","ex":"L'Italia influenzò tutta l'Europa.","exNl":"Italië beïnvloedde heel Europa.","lesson":185,"level":"B1","cat":"verbo"},
  {"id":"w1730","it":"celebre","nl":"beroemd, vermaard","ph":"TSJE-le-bre","ex":"È un artista celebre in tutto il mondo.","exNl":"Het is een wereldberoemde kunstenaar.","lesson":185,"level":"B1","cat":"aggettivo"},

  # ── Les 186: De Renaissance ──
  {"id":"w1731","it":"il Rinascimento","nl":"de Renaissance","ph":"ri-na-shi-MEN-to","ex":"Il Rinascimento iniziò in Italia.","exNl":"De Renaissance begon in Italië.","lesson":186,"level":"B1","cat":"sostantivo"},
  {"id":"w1732","it":"l'umanesimo","nl":"het humanisme","ph":"u-ma-NE-zi-mo","ex":"L'umanesimo mise l'uomo al centro.","exNl":"Het humanisme plaatste de mens centraal.","lesson":186,"level":"B1","cat":"sostantivo"},
  {"id":"w1733","it":"scolpire","nl":"beeldhouwen","ph":"skol-PI-re","ex":"Michelangelo scolpì il David.","exNl":"Michelangelo beeldhouwde de David.","lesson":186,"level":"B1","cat":"verbo"},
  {"id":"w1734","it":"la bottega","nl":"het atelier, de werkplaats","ph":"bot-TE-ga","ex":"I giovani artisti lavoravano in bottega.","exNl":"Jonge kunstenaars werkten in het atelier.","lesson":186,"level":"B1","cat":"sostantivo"},
  {"id":"w1735","it":"il mecenate","nl":"de mecenas, beschermheer","ph":"me-tsje-NA-te","ex":"Lorenzo de' Medici fu un grande mecenate.","exNl":"Lorenzo de' Medici was een groot mecenas.","lesson":186,"level":"B1","cat":"sostantivo"},
  {"id":"w1736","it":"fiorire","nl":"bloeien, opbloeien","ph":"fjo-RI-re","ex":"L'arte fiorì durante il Rinascimento.","exNl":"De kunst bloeide op tijdens de Renaissance.","lesson":186,"level":"B1","cat":"verbo"},
  {"id":"w1737","it":"la prospettiva","nl":"het perspectief","ph":"pros-pet-TI-va","ex":"Brunelleschi inventò la prospettiva.","exNl":"Brunelleschi vond het perspectief uit.","lesson":186,"level":"B1","cat":"sostantivo"},
  {"id":"w1738","it":"rinascere","nl":"herboren worden, herleven","ph":"ri-NA-she-re","ex":"La cultura classica rinacque in Italia.","exNl":"De klassieke cultuur herleefde in Italië.","lesson":186,"level":"B1","cat":"verbo"},

  # ── Les 187: Moderne geschiedenis ──
  {"id":"w1739","it":"l'unificazione","nl":"de eenwording","ph":"u-ni-fi-ka-TSJO-ne","ex":"L'unificazione d'Italia avvenne nel 1861.","exNl":"De eenwording van Italië vond plaats in 1861.","lesson":187,"level":"B1","cat":"sostantivo"},
  {"id":"w1740","it":"la Resistenza","nl":"het Verzet","ph":"re-zis-TEN-tsa","ex":"La Resistenza combatté contro il fascismo.","exNl":"Het Verzet vocht tegen het fascisme.","lesson":187,"level":"B1","cat":"sostantivo"},
  {"id":"w1741","it":"la Costituzione","nl":"de grondwet","ph":"kos-ti-tu-TSJO-ne","ex":"La Costituzione italiana è del 1948.","exNl":"De Italiaanse grondwet is uit 1948.","lesson":187,"level":"B1","cat":"sostantivo"},
  {"id":"w1742","it":"il referendum","nl":"het referendum","ph":"re-fe-REN-dum","ex":"Nel 1946 ci fu un referendum sulla monarchia.","exNl":"In 1946 was er een referendum over de monarchie.","lesson":187,"level":"B1","cat":"sostantivo"},
  {"id":"w1743","it":"la monarchia","nl":"de monarchie","ph":"mo-nar-KI-a","ex":"L'Italia abolì la monarchia nel 1946.","exNl":"Italië schafte de monarchie af in 1946.","lesson":187,"level":"B1","cat":"sostantivo"},
  {"id":"w1744","it":"la dittatura","nl":"de dictatuur","ph":"dit-ta-TU-ra","ex":"La dittatura fascista durò vent'anni.","exNl":"De fascistische dictatuur duurde twintig jaar.","lesson":187,"level":"B1","cat":"sostantivo"},
  {"id":"w1745","it":"liberare","nl":"bevrijden","ph":"li-be-RA-re","ex":"Gli Alleati liberarono l'Italia nel 1945.","exNl":"De Geallieerden bevrijdden Italië in 1945.","lesson":187,"level":"B1","cat":"verbo"},
  {"id":"w1746","it":"il dopoguerra","nl":"de naoorlogse periode","ph":"do-po-GWER-ra","ex":"Nel dopoguerra l'Italia si ricostruì.","exNl":"In de naoorlogse periode herbouwde Italië zich.","lesson":187,"level":"B1","cat":"sostantivo"},

  # ── Les 188: Tradities & feestdagen ──
  {"id":"w1747","it":"il Natale","nl":"Kerstmis","ph":"na-TA-le","ex":"A Natale tutta la famiglia si riunisce.","exNl":"Met Kerstmis komt de hele familie samen.","lesson":188,"level":"B1","cat":"sostantivo"},
  {"id":"w1748","it":"la Pasqua","nl":"Pasen","ph":"PAS-kwa","ex":"A Pasqua si mangiano le uova di cioccolato.","exNl":"Met Pasen eet men chocolade-eieren.","lesson":188,"level":"B1","cat":"sostantivo"},
  {"id":"w1749","it":"il Carnevale","nl":"carnaval","ph":"kar-ne-VA-le","ex":"Il Carnevale di Venezia è famoso.","exNl":"Het carnaval van Venetië is beroemd.","lesson":188,"level":"B1","cat":"sostantivo"},
  {"id":"w1750","it":"la maschera","nl":"het masker","ph":"MAS-ke-ra","ex":"A Carnevale tutti portano le maschere.","exNl":"Met carnaval draagt iedereen maskers.","lesson":188,"level":"B1","cat":"sostantivo"},
  {"id":"w1751","it":"il panettone","nl":"de panettone (kerstbrood)","ph":"pa-net-TO-ne","ex":"Il panettone è un dolce tipico natalizio.","exNl":"Panettone is een typisch kerstgebak.","lesson":188,"level":"B1","cat":"sostantivo"},
  {"id":"w1752","it":"il Ferragosto","nl":"Maria-Hemelvaart (15 aug.)","ph":"fer-ra-GOS-to","ex":"A Ferragosto molti italiani vanno al mare.","exNl":"Met Ferragosto gaan veel Italianen naar zee.","lesson":188,"level":"B1","cat":"sostantivo"},
  {"id":"w1753","it":"festeggiare","nl":"vieren, feesten","ph":"fes-ted-DJA-re","ex":"Festeggiamo il Capodanno con i fuochi d'artificio.","exNl":"We vieren Oud en Nieuw met vuurwerk.","lesson":188,"level":"B1","cat":"verbo"},
  {"id":"w1754","it":"la tradizione","nl":"de traditie","ph":"tra-di-TSJO-ne","ex":"È una tradizione molto antica.","exNl":"Het is een heel oude traditie.","lesson":188,"level":"B1","cat":"sostantivo"},

  # ── Les 189: Italiaanse muziek ──
  {"id":"w1755","it":"l'opera lirica","nl":"de opera","ph":"O-pe-ra LI-ri-ka","ex":"L'opera lirica nacque in Italia.","exNl":"De opera ontstond in Italië.","lesson":189,"level":"B1","cat":"sostantivo"},
  {"id":"w1756","it":"il tenore","nl":"de tenor","ph":"te-NO-re","ex":"Pavarotti fu un grande tenore.","exNl":"Pavarotti was een groot tenor.","lesson":189,"level":"B1","cat":"sostantivo"},
  {"id":"w1757","it":"il soprano","nl":"de sopraan","ph":"so-PRA-no","ex":"La soprano cantò un'aria bellissima.","exNl":"De sopraan zong een prachtige aria.","lesson":189,"level":"B1","cat":"sostantivo"},
  {"id":"w1758","it":"la melodia","nl":"de melodie","ph":"me-lo-DI-a","ex":"Questa melodia è molto orecchiabile.","exNl":"Deze melodie blijft goed hangen.","lesson":189,"level":"B1","cat":"sostantivo"},
  {"id":"w1759","it":"il palcoscenico","nl":"het podium, het toneel","ph":"pal-ko-SHE-ni-ko","ex":"I cantanti salirono sul palcoscenico.","exNl":"De zangers betraden het podium.","lesson":189,"level":"B1","cat":"sostantivo"},
  {"id":"w1760","it":"applaudire","nl":"applaudisseren","ph":"ap-plau-DI-re","ex":"Il pubblico applaudì a lungo.","exNl":"Het publiek applaudisseerde lang.","lesson":189,"level":"B1","cat":"verbo"},
  {"id":"w1761","it":"il cantautore","nl":"de singer-songwriter","ph":"kan-tau-TO-re","ex":"De André fu un famoso cantautore.","exNl":"De André was een beroemde singer-songwriter.","lesson":189,"level":"B1","cat":"sostantivo"},
  {"id":"w1762","it":"il ritmo","nl":"het ritme","ph":"RIT-mo","ex":"La musica italiana ha un ritmo allegro.","exNl":"Italiaanse muziek heeft een vrolijk ritme.","lesson":189,"level":"B1","cat":"sostantivo"},

  # ── Les 190: Toetsles Blok 7 ──
  {"id":"w1763","it":"la civiltà","nl":"de beschaving","ph":"tsji-vil-TA","ex":"La civiltà romana durò secoli.","exNl":"De Romeinse beschaving duurde eeuwen.","lesson":190,"level":"B1","cat":"sostantivo"},
  {"id":"w1764","it":"il patrimonio","nl":"het erfgoed","ph":"pa-tri-MO-nio","ex":"L'Italia ha un ricco patrimonio culturale.","exNl":"Italië heeft een rijk cultureel erfgoed.","lesson":190,"level":"B1","cat":"sostantivo"},
  {"id":"w1765","it":"tramandare","nl":"doorgeven, overleveren","ph":"tra-man-DA-re","ex":"Queste storie sono state tramandate per generazioni.","exNl":"Deze verhalen zijn generaties lang doorgegeven.","lesson":190,"level":"B1","cat":"verbo"},
  {"id":"w1766","it":"l'epoca","nl":"het tijdperk","ph":"E-po-ka","ex":"Fu un'epoca di grandi cambiamenti.","exNl":"Het was een tijdperk van grote veranderingen.","lesson":190,"level":"B1","cat":"sostantivo"},
  {"id":"w1767","it":"antico","nl":"oud, antiek","ph":"an-TI-ko","ex":"Roma è una città molto antica.","exNl":"Rome is een heel oude stad.","lesson":190,"level":"B1","cat":"aggettivo"},
  {"id":"w1768","it":"medievale","nl":"middeleeuws","ph":"me-dje-VA-le","ex":"Siena ha un centro medievale bellissimo.","exNl":"Siena heeft een prachtig middeleeuws centrum.","lesson":190,"level":"B1","cat":"aggettivo"},
  {"id":"w1769","it":"moderno","nl":"modern","ph":"mo-DER-no","ex":"L'arte moderna è molto diversa.","exNl":"Moderne kunst is heel anders.","lesson":190,"level":"B1","cat":"aggettivo"},
  {"id":"w1770","it":"contemporaneo","nl":"hedendaags","ph":"kon-tem-po-RA-ne-o","ex":"L'arte contemporanea è spesso astratta.","exNl":"Hedendaagse kunst is vaak abstract.","lesson":190,"level":"B1","cat":"aggettivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 8: Condizionale passato & financiën (lessen 191–200)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":191,"title":"Condizionale passato — vorming","emoji":"💭","level":"B1",
   "description":"Leer de condizionale passato voor hypothetische situaties in het verleden.",
   "grammar":{"title":"Condizionale passato",
   "body":"De condizionale passato = condizionale van avere/essere + voltooid deelwoord.\n\navrei parlato — ik zou gesproken hebben\nsarei andato/a — ik zou gegaan zijn\n\nGebruik:\n• Spijt: Avrei dovuto studiare di più. — Ik had meer moeten studeren.\n• Onvervulde wens: Sarei voluto venire. — Ik had willen komen.\n• Toekomst in het verleden: Disse che sarebbe venuto. — Hij zei dat hij zou komen."},
   "words":["w1771","w1772","w1773","w1774","w1775","w1776","w1777","w1778"]},

  {"id":192,"title":"Spijt uitdrukken","emoji":"😔","level":"B1",
   "description":"Gebruik de condizionale passato om spijt uit te drukken.",
   "grammar":{"title":"Spijt met condizionale passato",
   "body":"Gebruik avrei dovuto / avrei potuto + infinitief voor spijt:\n\nAvrei dovuto ascoltarti. — Ik had naar je moeten luisteren.\nAvrei potuto fare di meglio. — Ik had beter kunnen doen.\nNon avrei dovuto dire quello. — Ik had dat niet moeten zeggen.\n\nVuistregel: dovere/potere/volere in condizionale passato + infinitief."},
   "words":["w1779","w1780","w1781","w1782","w1783","w1784","w1785","w1786"]},

  {"id":193,"title":"Wensen in het verleden","emoji":"🌠","level":"B1",
   "description":"Praat over dingen die je had willen doen.",
   "grammar":{"title":"Wensen met condizionale passato",
   "body":"Avrei voluto + infinitief = ik had willen…\n\nAvrei voluto viaggiare di più. — Ik had meer willen reizen.\nSaremmo voluti restare. — We hadden willen blijven.\n\nMet magari: Magari avessi studiato medicina! — Had ik maar geneeskunde gestudeerd!"},
   "words":["w1787","w1788","w1789","w1790","w1791","w1792","w1793","w1794"]},

  {"id":194,"title":"Financiën & bankzaken","emoji":"🏦","level":"B1",
   "description":"Woordenschat voor de bank en geldzaken.",
   "grammar":{"title":"Bankzaken regelen",
   "body":"Nuttige zinnen bij de bank:\n\nVorrei aprire un conto corrente. — Ik zou graag een lopende rekening openen.\nPosso fare un bonifico? — Kan ik een overboeking doen?\nQual è il tasso d'interesse? — Wat is de rente?"},
   "words":["w1795","w1796","w1797","w1798","w1799","w1800","w1801","w1802"]},

  {"id":195,"title":"Economie & geld","emoji":"💶","level":"B1",
   "description":"Basiswoorden over economie en de arbeidsmarkt.",
   "grammar":{"title":"Over economie praten",
   "body":"Belangrijke economische termen:\n\nL'economia cresce / è in crescita. — De economie groeit.\nLa disoccupazione è alta / bassa. — De werkloosheid is hoog / laag.\nIl costo della vita è aumentato. — De kosten van levensonderhoud zijn gestegen."},
   "words":["w1803","w1804","w1805","w1806","w1807","w1808","w1809","w1810"]},

  {"id":196,"title":"Belastingen & administratie","emoji":"📄","level":"B1",
   "description":"Woorden voor belastingen en officiële documenten.",
   "grammar":{"title":"Administratieve taal",
   "body":"Formele uitdrukkingen bij de overheid:\n\nDevo presentare la dichiarazione dei redditi. — Ik moet belastingaangifte doen.\nHo bisogno di un certificato di residenza. — Ik heb een bewijs van inschrijving nodig.\nDove posso richiedere il permesso di soggiorno? — Waar kan ik een verblijfsvergunning aanvragen?"},
   "words":["w1811","w1812","w1813","w1814","w1815","w1816","w1817","w1818"]},

  {"id":197,"title":"Wonen & huren","emoji":"🏠","level":"B1",
   "description":"Woordenschat voor het huren en kopen van een woning.",
   "grammar":{"title":"Een woning zoeken",
   "body":"Nuttige zinnen bij het zoeken naar een woning:\n\nCerco un appartamento in affitto. — Ik zoek een huurappartement.\nQuant'è l'affitto mensile? — Hoeveel is de maandelijkse huur?\nLe spese sono incluse? — Zijn de servicekosten inbegrepen?\nIl contratto è di quattro anni. — Het contract is voor vier jaar."},
   "words":["w1819","w1820","w1821","w1822","w1823","w1824","w1825","w1826"]},

  {"id":198,"title":"Verhuizen","emoji":"📦","level":"B1",
   "description":"Woorden en uitdrukkingen over verhuizen.",
   "grammar":{"title":"Verhuizen beschrijven",
   "body":"Trasferirsi = verhuizen (reflexief):\n\nMi sono trasferito/a a Roma. — Ik ben naar Rome verhuisd.\nCi trasferiremo il mese prossimo. — We verhuizen volgende maand.\n\nAndere nuttige woorden: fare i bagagli (inpakken), il trasloco (de verhuizing), sistemare (inrichten)."},
   "words":["w1827","w1828","w1829","w1830","w1831","w1832","w1833","w1834"]},

  {"id":199,"title":"Buurt & omgeving","emoji":"🏘️","level":"B1",
   "description":"Beschrijf je buurt en directe omgeving.",
   "grammar":{"title":"Je buurt beschrijven",
   "body":"Nuttige constructies:\n\nAbito in un quartiere tranquillo. — Ik woon in een rustige buurt.\nNelle vicinanze c'è… — In de buurt is er…\nÈ ben collegato con i mezzi. — Het is goed bereikbaar met het OV.\nIl quartiere è sicuro / vivace / verde. — De buurt is veilig / levendig / groen."},
   "words":["w1835","w1836","w1837","w1838","w1839","w1840","w1841","w1842"]},

  {"id":200,"title":"Toetsles B1 — Blok 8","emoji":"📋","level":"B1",
   "description":"Toets over lessen 191–200: condizionale passato & financiën.",
   "grammar":{"title":"Toetsles B1 — Blok 8 (les 191–200)","body":"In dit blok heb je geleerd:\n• De condizionale passato\n• Spijt en wensen in het verleden uitdrukken\n• Financiële en administratieve termen\n• Wonen, huren en verhuizen bespreken"},
   "words":["w1843","w1844","w1845","w1846","w1847","w1848","w1849","w1850"]},
]

WORDS += [
  # ── Les 191: Condizionale passato — vorming ──
  {"id":"w1771","it":"avrei voluto","nl":"ik had willen","ph":"av-REI vo-LU-to","ex":"Avrei voluto vederti.","exNl":"Ik had je willen zien.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1772","it":"avrei dovuto","nl":"ik had moeten","ph":"av-REI do-VU-to","ex":"Avrei dovuto chiamarti prima.","exNl":"Ik had je eerder moeten bellen.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1773","it":"avrei potuto","nl":"ik had kunnen","ph":"av-REI po-TU-to","ex":"Avrei potuto aiutarti.","exNl":"Ik had je kunnen helpen.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1774","it":"sarei andato","nl":"ik zou gegaan zijn","ph":"sa-REI an-DA-to","ex":"Sarei andato volentieri.","exNl":"Ik zou graag gegaan zijn.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1775","it":"avrebbe detto","nl":"hij/zij zou gezegd hebben","ph":"av-REB-be DET-to","ex":"Non avrebbe mai detto una cosa simile.","exNl":"Hij zou nooit zoiets gezegd hebben.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1776","it":"sarebbe stato","nl":"het zou geweest zijn","ph":"sa-REB-be STA-to","ex":"Sarebbe stato meglio restare.","exNl":"Het zou beter geweest zijn om te blijven.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1777","it":"pentirsi","nl":"spijt hebben, berouw hebben","ph":"pen-TIR-si","ex":"Mi sono pentito di quella decisione.","exNl":"Ik heb spijt van die beslissing.","lesson":191,"level":"B1","cat":"verbo"},
  {"id":"w1778","it":"il rimpianto","nl":"het berouw, de spijt","ph":"rim-PJAN-to","ex":"Non ho nessun rimpianto.","exNl":"Ik heb geen enkel berouw.","lesson":191,"level":"B1","cat":"sostantivo"},

  # ── Les 192: Spijt uitdrukken ──
  {"id":"w1779","it":"purtroppo","nl":"helaas","ph":"pur-TROP-po","ex":"Purtroppo non sono riuscito a venire.","exNl":"Helaas ben ik er niet in geslaagd te komen.","lesson":192,"level":"B1","cat":"avverbio"},
  {"id":"w1780","it":"il rammarico","nl":"het leedwezen, de spijt","ph":"ram-MA-ri-ko","ex":"Esprimo il mio rammarico.","exNl":"Ik betuig mijn leedwezen.","lesson":192,"level":"B1","cat":"sostantivo"},
  {"id":"w1781","it":"scusarsi","nl":"zich verontschuldigen","ph":"sku-ZAR-si","ex":"Mi scuso per il ritardo.","exNl":"Ik verontschuldig me voor de vertraging.","lesson":192,"level":"B1","cat":"verbo"},
  {"id":"w1782","it":"rimediare","nl":"herstellen, goedmaken","ph":"ri-me-DJA-re","ex":"Voglio rimediare al mio errore.","exNl":"Ik wil mijn fout goedmaken.","lesson":192,"level":"B1","cat":"verbo"},
  {"id":"w1783","it":"l'errore","nl":"de fout","ph":"er-RO-re","ex":"Ho fatto un errore grave.","exNl":"Ik heb een ernstige fout gemaakt.","lesson":192,"level":"B1","cat":"sostantivo"},
  {"id":"w1784","it":"ammettere","nl":"toegeven","ph":"am-MET-te-re","ex":"Devo ammettere che avevi ragione.","exNl":"Ik moet toegeven dat je gelijk had.","lesson":192,"level":"B1","cat":"verbo"},
  {"id":"w1785","it":"perdonare","nl":"vergeven","ph":"per-do-NA-re","ex":"Ti perdono per quello che hai fatto.","exNl":"Ik vergeef je voor wat je gedaan hebt.","lesson":192,"level":"B1","cat":"verbo"},
  {"id":"w1786","it":"la colpa","nl":"de schuld","ph":"KOL-pa","ex":"Non è colpa tua.","exNl":"Het is niet jouw schuld.","lesson":192,"level":"B1","cat":"sostantivo"},

  # ── Les 193: Wensen in het verleden ──
  {"id":"w1787","it":"magari","nl":"misschien; was het maar","ph":"ma-GA-ri","ex":"Magari avessi più tempo!","exNl":"Had ik maar meer tijd!","lesson":193,"level":"B1","cat":"avverbio"},
  {"id":"w1788","it":"il sogno","nl":"de droom","ph":"SO-njo","ex":"Il mio sogno era diventare medico.","exNl":"Mijn droom was om arts te worden.","lesson":193,"level":"B1","cat":"sostantivo"},
  {"id":"w1789","it":"realizzare","nl":"verwezenlijken, realiseren","ph":"re-a-lid-ZA-re","ex":"Ho realizzato il mio sogno.","exNl":"Ik heb mijn droom verwezenlijkt.","lesson":193,"level":"B1","cat":"verbo"},
  {"id":"w1790","it":"rimandare","nl":"uitstellen","ph":"ri-man-DA-re","ex":"Ho rimandato la decisione troppo a lungo.","exNl":"Ik heb het besluit te lang uitgesteld.","lesson":193,"level":"B1","cat":"verbo"},
  {"id":"w1791","it":"l'occasione","nl":"de gelegenheid, de kans","ph":"ok-ka-ZJO-ne","ex":"Ho perso una grande occasione.","exNl":"Ik heb een grote kans gemist.","lesson":193,"level":"B1","cat":"sostantivo"},
  {"id":"w1792","it":"sprecare","nl":"verspillen","ph":"spre-KA-re","ex":"Non sprecare questa opportunità.","exNl":"Verspil deze kans niet.","lesson":193,"level":"B1","cat":"verbo"},
  {"id":"w1793","it":"la scelta","nl":"de keuze","ph":"SHEL-ta","ex":"È stata una scelta difficile.","exNl":"Het was een moeilijke keuze.","lesson":193,"level":"B1","cat":"sostantivo"},
  {"id":"w1794","it":"rimpiangere","nl":"betreuren","ph":"rim-PJAN-dje-re","ex":"Non rimpiango nulla.","exNl":"Ik betreur niets.","lesson":193,"level":"B1","cat":"verbo"},

  # ── Les 194: Financiën & bankzaken ──
  {"id":"w1795","it":"il conto corrente","nl":"de lopende rekening","ph":"KON-to kor-REN-te","ex":"Vorrei aprire un conto corrente.","exNl":"Ik zou graag een lopende rekening openen.","lesson":194,"level":"B1","cat":"sostantivo"},
  {"id":"w1796","it":"il bonifico","nl":"de overboeking","ph":"bo-NI-fi-ko","ex":"Ho fatto un bonifico di 500 euro.","exNl":"Ik heb een overboeking van 500 euro gedaan.","lesson":194,"level":"B1","cat":"sostantivo"},
  {"id":"w1797","it":"il tasso d'interesse","nl":"de rente","ph":"TAS-so din-te-RES-se","ex":"Il tasso d'interesse è molto basso.","exNl":"De rente is heel laag.","lesson":194,"level":"B1","cat":"sostantivo"},
  {"id":"w1798","it":"il prestito","nl":"de lening","ph":"PRES-ti-to","ex":"Ho chiesto un prestito alla banca.","exNl":"Ik heb een lening aangevraagd bij de bank.","lesson":194,"level":"B1","cat":"sostantivo"},
  {"id":"w1799","it":"il mutuo","nl":"de hypotheek","ph":"MU-tu-o","ex":"Abbiamo un mutuo di trent'anni.","exNl":"We hebben een hypotheek van dertig jaar.","lesson":194,"level":"B1","cat":"sostantivo"},
  {"id":"w1800","it":"risparmiare","nl":"sparen, besparen","ph":"ris-par-MJA-re","ex":"Cerco di risparmiare ogni mese.","exNl":"Ik probeer elke maand te sparen.","lesson":194,"level":"B1","cat":"verbo"},
  {"id":"w1801","it":"il risparmio","nl":"de besparing, het spaargeld","ph":"ris-PAR-mjo","ex":"Ho usato i miei risparmi.","exNl":"Ik heb mijn spaargeld gebruikt.","lesson":194,"level":"B1","cat":"sostantivo"},
  {"id":"w1802","it":"investire","nl":"investeren","ph":"in-ves-TI-re","ex":"Voglio investire in azioni.","exNl":"Ik wil in aandelen investeren.","lesson":194,"level":"B1","cat":"verbo"},

  # ── Les 195: Economie & geld ──
  {"id":"w1803","it":"l'economia","nl":"de economie","ph":"e-ko-no-MI-a","ex":"L'economia italiana è in ripresa.","exNl":"De Italiaanse economie is in herstel.","lesson":195,"level":"B1","cat":"sostantivo"},
  {"id":"w1804","it":"la disoccupazione","nl":"de werkloosheid","ph":"di-zok-ku-pa-TSJO-ne","ex":"La disoccupazione giovanile è alta.","exNl":"De jeugdwerkloosheid is hoog.","lesson":195,"level":"B1","cat":"sostantivo"},
  {"id":"w1805","it":"l'inflazione","nl":"de inflatie","ph":"in-fla-TSJO-ne","ex":"L'inflazione è aumentata quest'anno.","exNl":"De inflatie is dit jaar gestegen.","lesson":195,"level":"B1","cat":"sostantivo"},
  {"id":"w1806","it":"la crisi","nl":"de crisis","ph":"KRI-zi","ex":"La crisi economica ha colpito molti paesi.","exNl":"De economische crisis trof veel landen.","lesson":195,"level":"B1","cat":"sostantivo"},
  {"id":"w1807","it":"il debito","nl":"de schuld","ph":"DE-bi-to","ex":"L'Italia ha un grande debito pubblico.","exNl":"Italië heeft een grote staatsschuld.","lesson":195,"level":"B1","cat":"sostantivo"},
  {"id":"w1808","it":"la crescita","nl":"de groei","ph":"KRESH-i-ta","ex":"La crescita economica è lenta.","exNl":"De economische groei is traag.","lesson":195,"level":"B1","cat":"sostantivo"},
  {"id":"w1809","it":"esportare","nl":"exporteren","ph":"es-por-TA-re","ex":"L'Italia esporta molto vino.","exNl":"Italië exporteert veel wijn.","lesson":195,"level":"B1","cat":"verbo"},
  {"id":"w1810","it":"importare","nl":"importeren","ph":"im-por-TA-re","ex":"Importiamo petrolio dall'estero.","exNl":"We importeren olie uit het buitenland.","lesson":195,"level":"B1","cat":"verbo"},

  # ── Les 196: Belastingen & administratie ──
  {"id":"w1811","it":"la tassa","nl":"de belasting","ph":"TAS-sa","ex":"Le tasse in Italia sono alte.","exNl":"De belastingen in Italië zijn hoog.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1812","it":"la dichiarazione dei redditi","nl":"de belastingaangifte","ph":"di-kja-ra-TSJO-ne dei RED-di-ti","ex":"Devo fare la dichiarazione dei redditi.","exNl":"Ik moet belastingaangifte doen.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1813","it":"il certificato","nl":"het certificaat, het bewijs","ph":"tsjer-ti-fi-KA-to","ex":"Ho bisogno di un certificato di nascita.","exNl":"Ik heb een geboortecertificaat nodig.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1814","it":"il documento","nl":"het document","ph":"do-ku-MEN-to","ex":"Porti un documento d'identità.","exNl":"Neem een identiteitsdocument mee.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1815","it":"la residenza","nl":"de woonplaats, het verblijf","ph":"re-zi-DEN-tsa","ex":"Ho cambiato residenza il mese scorso.","exNl":"Ik heb vorige maand mijn woonplaats gewijzigd.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1816","it":"il permesso di soggiorno","nl":"de verblijfsvergunning","ph":"per-MES-so di sod-DJOR-no","ex":"Devo rinnovare il permesso di soggiorno.","exNl":"Ik moet mijn verblijfsvergunning verlengen.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1817","it":"la firma","nl":"de handtekening","ph":"FIR-ma","ex":"Metta la firma qui, per favore.","exNl":"Zet hier uw handtekening, alstublieft.","lesson":196,"level":"B1","cat":"sostantivo"},
  {"id":"w1818","it":"compilare","nl":"invullen (formulier)","ph":"kom-pi-LA-re","ex":"Deve compilare questo modulo.","exNl":"U moet dit formulier invullen.","lesson":196,"level":"B1","cat":"verbo"},

  # ── Les 197: Wonen & huren ──
  {"id":"w1819","it":"l'affitto","nl":"de huur","ph":"af-FIT-to","ex":"L'affitto è di 800 euro al mese.","exNl":"De huur is 800 euro per maand.","lesson":197,"level":"B1","cat":"sostantivo"},
  {"id":"w1820","it":"il proprietario","nl":"de eigenaar, de huisbaas","ph":"pro-prje-TA-rio","ex":"Il proprietario è molto gentile.","exNl":"De huisbaas is heel aardig.","lesson":197,"level":"B1","cat":"sostantivo"},
  {"id":"w1821","it":"l'inquilino","nl":"de huurder","ph":"in-kwi-LI-no","ex":"L'inquilino precedente ha lasciato l'appartamento pulito.","exNl":"De vorige huurder heeft het appartement schoon achtergelaten.","lesson":197,"level":"B1","cat":"sostantivo"},
  {"id":"w1822","it":"il contratto","nl":"het contract","ph":"kon-TRAT-to","ex":"Abbiamo firmato il contratto d'affitto.","exNl":"We hebben het huurcontract getekend.","lesson":197,"level":"B1","cat":"sostantivo"},
  {"id":"w1823","it":"la caparra","nl":"de borg, het waarborgsom","ph":"ka-PAR-ra","ex":"La caparra è di due mesi d'affitto.","exNl":"De borg is twee maanden huur.","lesson":197,"level":"B1","cat":"sostantivo"},
  {"id":"w1824","it":"le spese condominiali","nl":"de servicekosten","ph":"SPE-ze kon-do-mi-NJA-li","ex":"Le spese condominiali sono incluse.","exNl":"De servicekosten zijn inbegrepen.","lesson":197,"level":"B1","cat":"sostantivo"},
  {"id":"w1825","it":"ristrutturare","nl":"renoveren","ph":"ris-trut-tu-RA-re","ex":"Vogliamo ristrutturare il bagno.","exNl":"We willen de badkamer renoveren.","lesson":197,"level":"B1","cat":"verbo"},
  {"id":"w1826","it":"il monolocale","nl":"de studio (eenkamerwoning)","ph":"mo-no-lo-KA-le","ex":"Affitto un monolocale in centro.","exNl":"Ik huur een studio in het centrum.","lesson":197,"level":"B1","cat":"sostantivo"},

  # ── Les 198: Verhuizen ──
  {"id":"w1827","it":"trasferirsi","nl":"verhuizen","ph":"tras-fe-RIR-si","ex":"Mi trasferisco a Milano.","exNl":"Ik verhuis naar Milaan.","lesson":198,"level":"B1","cat":"verbo"},
  {"id":"w1828","it":"il trasloco","nl":"de verhuizing","ph":"tras-LO-ko","ex":"Il trasloco è stato molto faticoso.","exNl":"De verhuizing was heel vermoeiend.","lesson":198,"level":"B1","cat":"sostantivo"},
  {"id":"w1829","it":"imballare","nl":"inpakken","ph":"im-bal-LA-re","ex":"Devo imballare tutti i libri.","exNl":"Ik moet alle boeken inpakken.","lesson":198,"level":"B1","cat":"verbo"},
  {"id":"w1830","it":"lo scatolone","nl":"de verhuisdoos","ph":"ska-to-LO-ne","ex":"Ho comprato venti scatoloni.","exNl":"Ik heb twintig verhuisdozen gekocht.","lesson":198,"level":"B1","cat":"sostantivo"},
  {"id":"w1831","it":"sistemare","nl":"inrichten, op orde brengen","ph":"sis-te-MA-re","ex":"Devo ancora sistemare la camera.","exNl":"Ik moet de kamer nog inrichten.","lesson":198,"level":"B1","cat":"verbo"},
  {"id":"w1832","it":"il vicino","nl":"de buurman","ph":"vi-TSJI-no","ex":"I vicini sono molto simpatici.","exNl":"De buren zijn heel aardig.","lesson":198,"level":"B1","cat":"sostantivo"},
  {"id":"w1833","it":"ambientarsi","nl":"wennen, zich aanpassen","ph":"am-bjen-TAR-si","ex":"Mi sto ambientando nella nuova città.","exNl":"Ik ben aan het wennen in de nieuwe stad.","lesson":198,"level":"B1","cat":"verbo"},
  {"id":"w1834","it":"la nostalgia","nl":"het heimwee","ph":"nos-tal-DJI-a","ex":"Ho nostalgia della mia città.","exNl":"Ik heb heimwee naar mijn stad.","lesson":198,"level":"B1","cat":"sostantivo"},

  # ── Les 199: Buurt & omgeving ──
  {"id":"w1835","it":"il quartiere","nl":"de wijk, de buurt","ph":"kwar-TJE-re","ex":"Abito in un quartiere tranquillo.","exNl":"Ik woon in een rustige buurt.","lesson":199,"level":"B1","cat":"sostantivo"},
  {"id":"w1836","it":"il marciapiede","nl":"het trottoir","ph":"mar-tsja-PJE-de","ex":"Il marciapiede è molto largo.","exNl":"Het trottoir is heel breed.","lesson":199,"level":"B1","cat":"sostantivo"},
  {"id":"w1837","it":"l'incrocio","nl":"het kruispunt","ph":"in-KRO-tsjo","ex":"Gira a destra all'incrocio.","exNl":"Sla rechtsaf bij het kruispunt.","lesson":199,"level":"B1","cat":"sostantivo"},
  {"id":"w1838","it":"il parcheggio","nl":"de parkeerplaats","ph":"par-KED-djo","ex":"C'è un parcheggio vicino alla stazione.","exNl":"Er is een parkeerplaats bij het station.","lesson":199,"level":"B1","cat":"sostantivo"},
  {"id":"w1839","it":"la periferia","nl":"de buitenwijk, de rand","ph":"pe-ri-fe-RI-a","ex":"Viviamo in periferia, fuori dal centro.","exNl":"We wonen in de buitenwijk, buiten het centrum.","lesson":199,"level":"B1","cat":"sostantivo"},
  {"id":"w1840","it":"il parco giochi","nl":"de speeltuin","ph":"PAR-ko DJO-ki","ex":"I bambini giocano al parco giochi.","exNl":"De kinderen spelen op de speeltuin.","lesson":199,"level":"B1","cat":"sostantivo"},
  {"id":"w1841","it":"collegato","nl":"verbonden, bereikbaar","ph":"kol-le-GA-to","ex":"Il quartiere è ben collegato con la metro.","exNl":"De buurt is goed bereikbaar met de metro.","lesson":199,"level":"B1","cat":"aggettivo"},
  {"id":"w1842","it":"vivace","nl":"levendig","ph":"vi-VA-tsje","ex":"È un quartiere molto vivace di sera.","exNl":"Het is 's avonds een heel levendige buurt.","lesson":199,"level":"B1","cat":"aggettivo"},

  # ── Les 200: Toetsles Blok 8 ──
  {"id":"w1843","it":"il bilancio","nl":"het budget, de balans","ph":"bi-LAN-tsjo","ex":"Dobbiamo rispettare il bilancio familiare.","exNl":"We moeten het gezinsbudget respecteren.","lesson":200,"level":"B1","cat":"sostantivo"},
  {"id":"w1844","it":"la rata","nl":"de termijn (betaling)","ph":"RA-ta","ex":"Pago il mutuo in rate mensili.","exNl":"Ik betaal de hypotheek in maandelijkse termijnen.","lesson":200,"level":"B1","cat":"sostantivo"},
  {"id":"w1845","it":"la ricevuta","nl":"het ontvangstbewijs","ph":"ri-tsje-VU-ta","ex":"Conserva sempre la ricevuta.","exNl":"Bewaar altijd het ontvangstbewijs.","lesson":200,"level":"B1","cat":"sostantivo"},
  {"id":"w1846","it":"la bolletta","nl":"de rekening (gas/licht)","ph":"bol-LET-ta","ex":"La bolletta del gas è arrivata.","exNl":"De gasrekening is aangekomen.","lesson":200,"level":"B1","cat":"sostantivo"},
  {"id":"w1847","it":"saldare","nl":"betalen, vereffenen","ph":"sal-DA-re","ex":"Ho saldato il debito.","exNl":"Ik heb de schuld betaald.","lesson":200,"level":"B1","cat":"verbo"},
  {"id":"w1848","it":"conveniente","nl":"voordelig, gunstig","ph":"kon-ve-NJEN-te","ex":"Questo affitto è molto conveniente.","exNl":"Deze huur is heel voordelig.","lesson":200,"level":"B1","cat":"aggettivo"},
  {"id":"w1849","it":"il reddito","nl":"het inkomen","ph":"RED-di-to","ex":"Il reddito medio è aumentato.","exNl":"Het gemiddelde inkomen is gestegen.","lesson":200,"level":"B1","cat":"sostantivo"},
  {"id":"w1850","it":"il conto","nl":"de rekening","ph":"KON-to","ex":"Posso avere il conto, per favore?","exNl":"Mag ik de rekening, alstublieft?","lesson":200,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 9: Congiuntivo imperfetto & onderwijs (lessen 201–210)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":201,"title":"Congiuntivo imperfetto — vorming","emoji":"🧠","level":"B1",
   "description":"Leer het imperfetto van de congiuntivo.",
   "grammar":{"title":"Congiuntivo imperfetto",
   "body":"De congiuntivo imperfetto gebruik je na che in het verleden, of bij onwerkelijke wensen:\n\n-are: parlassi, parlassi, parlasse, parlassimo, parlaste, parlassero\n-ere: credessi, credessi, credesse, credessimo, credeste, credessero\n-ire: dormissi, dormissi, dormisse, dormissimo, dormiste, dormissero\n\nVoorbeelden:\nPensavo che parlasse italiano. — Ik dacht dat hij Italiaans sprak.\nSe avessi tempo, viaggerei. — Als ik tijd had, zou ik reizen."},
   "words":["w1851","w1852","w1853","w1854","w1855","w1856","w1857","w1858"]},

  {"id":202,"title":"Congiuntivo imperfetto — onregelmatig","emoji":"🧠","level":"B1",
   "description":"Onregelmatige vormen van de congiuntivo imperfetto.",
   "grammar":{"title":"Onregelmatige congiuntivo imperfetto",
   "body":"Enkele veelgebruikte onregelmatige vormen:\n\nessere: fossi, fossi, fosse, fossimo, foste, fossero\navere: avessi, avessi, avesse, avessimo, aveste, avessero\nfare: facessi…\ndire: dicessi…\nstare: stessi…\ndare: dessi…\n\nSe fossi ricco, comprerei una villa. — Als ik rijk was, zou ik een villa kopen."},
   "words":["w1859","w1860","w1861","w1862","w1863","w1864","w1865","w1866"]},

  {"id":203,"title":"Twijfel & onzekerheid","emoji":"🤔","level":"B1",
   "description":"Druk twijfel en onzekerheid uit met de congiuntivo.",
   "grammar":{"title":"Twijfel uitdrukken",
   "body":"De congiuntivo volgt op uitdrukkingen van twijfel en onzekerheid:\n\nNon sono sicuro che sia vero. — Ik weet niet zeker of het waar is.\nDubito che venga domani. — Ik betwijfel of hij morgen komt.\nNon credo che abbia ragione. — Ik geloof niet dat hij gelijk heeft.\nÈ possibile che piova. — Het is mogelijk dat het regent."},
   "words":["w1867","w1868","w1869","w1870","w1871","w1872","w1873","w1874"]},

  {"id":204,"title":"Meningen nuanceren","emoji":"💬","level":"B1",
   "description":"Leer je mening genuanceerd uitdrukken.",
   "grammar":{"title":"Meningen nuanceren",
   "body":"Gebruik deze structuren om je mening te nuanceren:\n\nDirei che… — Ik zou zeggen dat…\nA mio parere / Secondo me… — Naar mijn mening…\nPer quanto ne so… — Voor zover ik weet…\nDa un lato… dall'altro… — Aan de ene kant… aan de andere kant…\nNon è detto che + congiuntivo — Het staat niet vast dat…"},
   "words":["w1875","w1876","w1877","w1878","w1879","w1880","w1881","w1882"]},

  {"id":205,"title":"Onderwijs & studie","emoji":"📚","level":"B1",
   "description":"Woorden over school, studie en opleidingen.",
   "grammar":{"title":"Over onderwijs praten",
   "body":"Het Italiaanse onderwijssysteem:\n\nla scuola elementare — de basisschool (6–11 jaar)\nla scuola media — de middelbare school (11–14 jaar)\nil liceo — het gymnasium/atheneum (14–19 jaar)\nl'università — de universiteit\n\nFrequentare la scuola — naar school gaan\nLaurearai in… — afstuderen in…"},
   "words":["w1883","w1884","w1885","w1886","w1887","w1888","w1889","w1890"]},

  {"id":206,"title":"Universiteit & wetenschap","emoji":"🎓","level":"B1",
   "description":"Praat over universitaire studies en onderzoek.",
   "grammar":{"title":"Universitaire taal",
   "body":"Nuttige termen:\n\nla laurea triennale — de bachelor (3 jaar)\nla laurea magistrale — de master (2 jaar)\nil dottorato — de promotie, het doctoraat\nla tesi — het afstudeerwerk, de scriptie\nsostenere un esame — examen doen\nsuperare un esame — een examen halen"},
   "words":["w1891","w1892","w1893","w1894","w1895","w1896","w1897","w1898"]},

  {"id":207,"title":"Lezen & schrijven","emoji":"📖","level":"B1",
   "description":"Woordenschat over boeken, lezen en schrijven.",
   "grammar":{"title":"Over lezen en schrijven praten",
   "body":"Nuttige uitdrukkingen:\n\nSto leggendo un romanzo di Ferrante. — Ik lees een roman van Ferrante.\nL'autore ha scritto dieci libri. — De auteur heeft tien boeken geschreven.\nIl capitolo tratta di… — Het hoofdstuk gaat over…\nConsiglio questo libro. — Ik raad dit boek aan."},
   "words":["w1899","w1900","w1901","w1902","w1903","w1904","w1905","w1906"]},

  {"id":208,"title":"Examen & beoordeling","emoji":"📝","level":"B1",
   "description":"Woorden over examens, toetsen en beoordelingen.",
   "grammar":{"title":"Examens bespreken",
   "body":"In Italië worden cijfers op 30 punten gegeven (universiteit) of op 10 (school):\n\nHo preso 28 su 30 all'esame. — Ik haalde 28 van de 30 op het examen.\nSono stato bocciato / promosso. — Ik ben gezakt / geslaagd.\nIl voto minimo è 18/30. — Het minimumcijfer is 18/30."},
   "words":["w1907","w1908","w1909","w1910","w1911","w1912","w1913","w1914"]},

  {"id":209,"title":"Taalgebruik & stijl","emoji":"✍️","level":"B1",
   "description":"Over registers, stijl en taalgebruik.",
   "grammar":{"title":"Registers in het Italiaans",
   "body":"Het Italiaans kent duidelijke registers:\n\nFormeel: Lei (u), Egregio Dottore, La prego di…\nInformeel: tu, Ciao!, Dai!\n\nLet op: in e-mails en brieven is het formele register veel gebruikelijker dan in het Nederlands."},
   "words":["w1915","w1916","w1917","w1918","w1919","w1920","w1921","w1922"]},

  {"id":210,"title":"Toetsles B1 — Blok 9","emoji":"📋","level":"B1",
   "description":"Toets over lessen 201–210: congiuntivo imperfetto & onderwijs.",
   "grammar":{"title":"Toetsles B1 — Blok 9 (les 201–210)","body":"In dit blok heb je geleerd:\n• De congiuntivo imperfetto (regelmatig en onregelmatig)\n• Twijfel en onzekerheid uitdrukken\n• Meningen nuanceren\n• Onderwijs, studie en taalgebruik bespreken"},
   "words":["w1923","w1924","w1925","w1926","w1927","w1928","w1929","w1930"]},
]

WORDS += [
  # ── Les 201: Congiuntivo imperfetto — vorming ──
  {"id":"w1851","it":"se fossi","nl":"als ik was/were","ph":"se FOS-si","ex":"Se fossi ricco, viaggerei.","exNl":"Als ik rijk was, zou ik reizen.","lesson":201,"level":"B1","cat":"verbo"},
  {"id":"w1852","it":"se avessi","nl":"als ik had","ph":"se a-VES-si","ex":"Se avessi tempo, verrei.","exNl":"Als ik tijd had, zou ik komen.","lesson":201,"level":"B1","cat":"verbo"},
  {"id":"w1853","it":"pensavo che","nl":"ik dacht dat","ph":"pen-SA-vo ke","ex":"Pensavo che parlasse francese.","exNl":"Ik dacht dat hij Frans sprak.","lesson":201,"level":"B1","cat":"espressione"},
  {"id":"w1854","it":"volevo che","nl":"ik wilde dat","ph":"vo-LE-vo ke","ex":"Volevo che venissi con me.","exNl":"Ik wilde dat je met me meekwam.","lesson":201,"level":"B1","cat":"espressione"},
  {"id":"w1855","it":"come se","nl":"alsof","ph":"KO-me se","ex":"Parla come se fosse italiano.","exNl":"Hij praat alsof hij Italiaans is.","lesson":201,"level":"B1","cat":"congiunzione"},
  {"id":"w1856","it":"senza che","nl":"zonder dat","ph":"SEN-tsa ke","ex":"È partito senza che lo sapessi.","exNl":"Hij vertrok zonder dat ik het wist.","lesson":201,"level":"B1","cat":"congiunzione"},
  {"id":"w1857","it":"prima che","nl":"voordat","ph":"PRI-ma ke","ex":"Chiamami prima che esca.","exNl":"Bel me voordat je weggaat.","lesson":201,"level":"B1","cat":"congiunzione"},
  {"id":"w1858","it":"a condizione che","nl":"op voorwaarde dat","ph":"a kon-di-TSJO-ne ke","ex":"Vengo a condizione che tu venga.","exNl":"Ik kom op voorwaarde dat jij ook komt.","lesson":201,"level":"B1","cat":"congiunzione"},

  # ── Les 202: Congiuntivo imperfetto — onregelmatig ──
  {"id":"w1859","it":"se potessi","nl":"als ik kon/zou kunnen","ph":"se po-TES-si","ex":"Se potessi, cambierei lavoro.","exNl":"Als ik kon, zou ik van baan veranderen.","lesson":202,"level":"B1","cat":"verbo"},
  {"id":"w1860","it":"se sapessi","nl":"als ik wist","ph":"se sa-PES-si","ex":"Se sapessi la risposta, te la direi.","exNl":"Als ik het antwoord wist, zou ik het je zeggen.","lesson":202,"level":"B1","cat":"verbo"},
  {"id":"w1861","it":"se facessi","nl":"als ik deed/maakte","ph":"se fa-TSHES-si","ex":"Se facessi più sport, sarei in forma.","exNl":"Als ik meer sportte, zou ik fit zijn.","lesson":202,"level":"B1","cat":"verbo"},
  {"id":"w1862","it":"se dicessi","nl":"als ik zei","ph":"se di-TSHES-si","ex":"Se dicessi la verità, mi crederesti?","exNl":"Als ik de waarheid zei, zou je me geloven?","lesson":202,"level":"B1","cat":"verbo"},
  {"id":"w1863","it":"se stessi","nl":"als ik was (stare)","ph":"se STES-si","ex":"Se stessi meglio, uscirei.","exNl":"Als ik me beter voelde, zou ik uitgaan.","lesson":202,"level":"B1","cat":"verbo"},
  {"id":"w1864","it":"se dessi","nl":"als ik gaf","ph":"se DES-si","ex":"Se ti dessi un consiglio, lo seguiresti?","exNl":"Als ik je een advies gaf, zou je het opvolgen?","lesson":202,"level":"B1","cat":"verbo"},
  {"id":"w1865","it":"qualora","nl":"indien, mocht","ph":"kwa-LO-ra","ex":"Qualora avessi bisogno, chiamami.","exNl":"Mocht je hulp nodig hebben, bel me.","lesson":202,"level":"B1","cat":"congiunzione"},
  {"id":"w1866","it":"nel caso in cui","nl":"in het geval dat","ph":"nel KA-zo in KUI","ex":"Nel caso in cui piovesse, resto a casa.","exNl":"In het geval dat het regent, blijf ik thuis.","lesson":202,"level":"B1","cat":"congiunzione"},

  # ── Les 203: Twijfel & onzekerheid ──
  {"id":"w1867","it":"dubitare","nl":"betwijfelen","ph":"du-bi-TA-re","ex":"Dubito che sia possibile.","exNl":"Ik betwijfel of het mogelijk is.","lesson":203,"level":"B1","cat":"verbo"},
  {"id":"w1868","it":"la certezza","nl":"de zekerheid","ph":"tsjer-TET-tsa","ex":"Non ho nessuna certezza.","exNl":"Ik heb geen enkele zekerheid.","lesson":203,"level":"B1","cat":"sostantivo"},
  {"id":"w1869","it":"il dubbio","nl":"de twijfel","ph":"DUB-bjo","ex":"Ho molti dubbi su questa scelta.","exNl":"Ik heb veel twijfels over deze keuze.","lesson":203,"level":"B1","cat":"sostantivo"},
  {"id":"w1870","it":"supporre","nl":"veronderstellen","ph":"sup-POR-re","ex":"Suppongo che sia vero.","exNl":"Ik veronderstel dat het waar is.","lesson":203,"level":"B1","cat":"verbo"},
  {"id":"w1871","it":"ipotizzare","nl":"vermoeden, hypothetiseren","ph":"i-po-tid-ZA-re","ex":"Ipotizzo che il treno sia in ritardo.","exNl":"Ik vermoed dat de trein vertraagd is.","lesson":203,"level":"B1","cat":"verbo"},
  {"id":"w1872","it":"apparentemente","nl":"blijkbaar, schijnbaar","ph":"ap-pa-ren-te-MEN-te","ex":"Apparentemente non è venuto.","exNl":"Blijkbaar is hij niet gekomen.","lesson":203,"level":"B1","cat":"avverbio"},
  {"id":"w1873","it":"eventualmente","nl":"eventueel","ph":"e-ven-tu-al-MEN-te","ex":"Eventualmente possiamo cambiare piano.","exNl":"Eventueel kunnen we van plan veranderen.","lesson":203,"level":"B1","cat":"avverbio"},
  {"id":"w1874","it":"probabile","nl":"waarschijnlijk","ph":"pro-BA-bi-le","ex":"È probabile che piova domani.","exNl":"Het is waarschijnlijk dat het morgen regent.","lesson":203,"level":"B1","cat":"aggettivo"},

  # ── Les 204: Meningen nuanceren ──
  {"id":"w1875","it":"a mio parere","nl":"naar mijn mening","ph":"a MI-o pa-RE-re","ex":"A mio parere, è una buona idea.","exNl":"Naar mijn mening is het een goed idee.","lesson":204,"level":"B1","cat":"espressione"},
  {"id":"w1876","it":"da un lato","nl":"aan de ene kant","ph":"da un LA-to","ex":"Da un lato capisco, dall'altro no.","exNl":"Aan de ene kant begrijp ik het, aan de andere niet.","lesson":204,"level":"B1","cat":"espressione"},
  {"id":"w1877","it":"per quanto ne so","nl":"voor zover ik weet","ph":"per KWAN-to ne SO","ex":"Per quanto ne so, il negozio è chiuso.","exNl":"Voor zover ik weet is de winkel dicht.","lesson":204,"level":"B1","cat":"espressione"},
  {"id":"w1878","it":"non è detto che","nl":"het staat niet vast dat","ph":"non e DET-to ke","ex":"Non è detto che abbia ragione.","exNl":"Het staat niet vast dat hij gelijk heeft.","lesson":204,"level":"B1","cat":"espressione"},
  {"id":"w1879","it":"tuttavia","nl":"echter, toch","ph":"tut-ta-VI-a","ex":"È difficile; tuttavia ci proverò.","exNl":"Het is moeilijk; toch zal ik het proberen.","lesson":204,"level":"B1","cat":"congiunzione"},
  {"id":"w1880","it":"piuttosto","nl":"eerder, liever","ph":"pjut-TOS-to","ex":"Piuttosto che lamentarmi, agisco.","exNl":"In plaats van te klagen, handel ik.","lesson":204,"level":"B1","cat":"avverbio"},
  {"id":"w1881","it":"in effetti","nl":"inderdaad, eigenlijk","ph":"in ef-FET-ti","ex":"In effetti hai ragione.","exNl":"Inderdaad, je hebt gelijk.","lesson":204,"level":"B1","cat":"espressione"},
  {"id":"w1882","it":"al contrario","nl":"integendeel","ph":"al kon-TRA-rjo","ex":"Non è noioso, al contrario!","exNl":"Het is niet saai, integendeel!","lesson":204,"level":"B1","cat":"espressione"},

  # ── Les 205: Onderwijs & studie ──
  {"id":"w1883","it":"la scuola elementare","nl":"de basisschool","ph":"SKWO-la e-le-men-TA-re","ex":"I bambini vanno alla scuola elementare.","exNl":"De kinderen gaan naar de basisschool.","lesson":205,"level":"B1","cat":"sostantivo"},
  {"id":"w1884","it":"il liceo","nl":"het gymnasium","ph":"li-TSHE-o","ex":"Frequento il liceo classico.","exNl":"Ik ga naar het klassiek gymnasium.","lesson":205,"level":"B1","cat":"sostantivo"},
  {"id":"w1885","it":"la materia","nl":"het schoolvak","ph":"ma-TE-rja","ex":"La mia materia preferita è storia.","exNl":"Mijn lievelingsvak is geschiedenis.","lesson":205,"level":"B1","cat":"sostantivo"},
  {"id":"w1886","it":"l'insegnante","nl":"de docent, de leraar","ph":"in-se-NJAN-te","ex":"L'insegnante è molto brava.","exNl":"De docent is heel goed.","lesson":205,"level":"B1","cat":"sostantivo"},
  {"id":"w1887","it":"la pagella","nl":"het rapport","ph":"pa-DJEL-la","ex":"Ho preso bei voti nella pagella.","exNl":"Ik heb goede cijfers op mijn rapport.","lesson":205,"level":"B1","cat":"sostantivo"},
  {"id":"w1888","it":"la lezione","nl":"de les","ph":"le-TSJO-ne","ex":"Oggi abbiamo tre lezioni.","exNl":"Vandaag hebben we drie lessen.","lesson":205,"level":"B1","cat":"sostantivo"},
  {"id":"w1889","it":"diplomarsi","nl":"afstuderen (middelbare school)","ph":"di-plo-MAR-si","ex":"Mi sono diplomato nel 2020.","exNl":"Ik ben in 2020 afgestudeerd.","lesson":205,"level":"B1","cat":"verbo"},
  {"id":"w1890","it":"il compito","nl":"het huiswerk, de opdracht","ph":"KOM-pi-to","ex":"Devo fare i compiti per domani.","exNl":"Ik moet het huiswerk voor morgen maken.","lesson":205,"level":"B1","cat":"sostantivo"},

  # ── Les 206: Universiteit & wetenschap ──
  {"id":"w1891","it":"la laurea","nl":"het universitaire diploma","ph":"LAU-re-a","ex":"Ho una laurea in ingegneria.","exNl":"Ik heb een diploma in techniek.","lesson":206,"level":"B1","cat":"sostantivo"},
  {"id":"w1892","it":"laurearsi","nl":"afstuderen (universiteit)","ph":"lau-re-AR-si","ex":"Mi sono laureato in economia.","exNl":"Ik ben afgestudeerd in economie.","lesson":206,"level":"B1","cat":"verbo"},
  {"id":"w1893","it":"la tesi","nl":"de scriptie, het proefschrift","ph":"TE-zi","ex":"Sto scrivendo la tesi di laurea.","exNl":"Ik schrijf mijn afstudeerscriptie.","lesson":206,"level":"B1","cat":"sostantivo"},
  {"id":"w1894","it":"il dottorato","nl":"het doctoraat, de promotie","ph":"dot-to-RA-to","ex":"Sta facendo il dottorato in fisica.","exNl":"Hij is bezig met zijn promotie in natuurkunde.","lesson":206,"level":"B1","cat":"sostantivo"},
  {"id":"w1895","it":"la ricerca","nl":"het onderzoek","ph":"ri-TSJER-ka","ex":"La ricerca scientifica è fondamentale.","exNl":"Wetenschappelijk onderzoek is essentieel.","lesson":206,"level":"B1","cat":"sostantivo"},
  {"id":"w1896","it":"il laboratorio","nl":"het laboratorium","ph":"la-bo-ra-TO-rjo","ex":"Lavora nel laboratorio di chimica.","exNl":"Hij werkt in het scheikundelaboratorium.","lesson":206,"level":"B1","cat":"sostantivo"},
  {"id":"w1897","it":"la borsa di studio","nl":"de studiebeurs","ph":"BOR-sa di STU-djo","ex":"Ha ottenuto una borsa di studio.","exNl":"Hij heeft een studiebeurs gekregen.","lesson":206,"level":"B1","cat":"sostantivo"},
  {"id":"w1898","it":"il professore","nl":"de professor","ph":"pro-fes-SO-re","ex":"Il professore tiene la lezione il martedì.","exNl":"De professor geeft les op dinsdag.","lesson":206,"level":"B1","cat":"sostantivo"},

  # ── Les 207: Lezen & schrijven ──
  {"id":"w1899","it":"il romanzo","nl":"de roman","ph":"ro-MAN-tso","ex":"Sto leggendo un romanzo italiano.","exNl":"Ik lees een Italiaanse roman.","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1900","it":"il racconto","nl":"het korte verhaal","ph":"rak-KON-to","ex":"I racconti di Calvino sono bellissimi.","exNl":"De korte verhalen van Calvino zijn prachtig.","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1901","it":"la poesia","nl":"het gedicht, de poëzie","ph":"po-e-ZI-a","ex":"Amo la poesia di Montale.","exNl":"Ik hou van de poëzie van Montale.","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1902","it":"il capitolo","nl":"het hoofdstuk","ph":"ka-PI-to-lo","ex":"Ho letto tre capitoli stasera.","exNl":"Ik heb vanavond drie hoofdstukken gelezen.","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1903","it":"l'autore","nl":"de auteur","ph":"au-TO-re","ex":"Chi è l'autore di questo libro?","exNl":"Wie is de auteur van dit boek?","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1904","it":"la trama","nl":"het verhaal, de plot","ph":"TRA-ma","ex":"La trama del libro è avvincente.","exNl":"De plot van het boek is meeslepend.","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1905","it":"il personaggio","nl":"het personage","ph":"per-so-NAD-djo","ex":"Il personaggio principale è una donna.","exNl":"Het hoofdpersonage is een vrouw.","lesson":207,"level":"B1","cat":"sostantivo"},
  {"id":"w1906","it":"pubblicare","nl":"publiceren, uitgeven","ph":"pub-bli-KA-re","ex":"L'autore ha pubblicato un nuovo libro.","exNl":"De auteur heeft een nieuw boek uitgegeven.","lesson":207,"level":"B1","cat":"verbo"},

  # ── Les 208: Examen & beoordeling ──
  {"id":"w1907","it":"l'esame","nl":"het examen","ph":"e-ZA-me","ex":"Domani ho l'esame di storia.","exNl":"Morgen heb ik het geschiedenisexamen.","lesson":208,"level":"B1","cat":"sostantivo"},
  {"id":"w1908","it":"il voto","nl":"het cijfer","ph":"VO-to","ex":"Ho preso un bel voto.","exNl":"Ik heb een mooi cijfer gehaald.","lesson":208,"level":"B1","cat":"sostantivo"},
  {"id":"w1909","it":"bocciare","nl":"laten zakken","ph":"bot-TSHA-re","ex":"Sono stato bocciato all'esame.","exNl":"Ik ben gezakt voor het examen.","lesson":208,"level":"B1","cat":"verbo"},
  {"id":"w1910","it":"promuovere","nl":"laten slagen, bevorderen","ph":"pro-MWO-ve-re","ex":"Sono stato promosso con 28/30.","exNl":"Ik ben geslaagd met 28/30.","lesson":208,"level":"B1","cat":"verbo"},
  {"id":"w1911","it":"la verifica","nl":"de toets, de controle","ph":"ve-RI-fi-ka","ex":"Mercoledì c'è la verifica di matematica.","exNl":"Woensdag is de wiskundetoets.","lesson":208,"level":"B1","cat":"sostantivo"},
  {"id":"w1912","it":"preparare","nl":"voorbereiden","ph":"pre-pa-RA-re","ex":"Mi sto preparando per l'esame.","exNl":"Ik bereid me voor op het examen.","lesson":208,"level":"B1","cat":"verbo"},
  {"id":"w1913","it":"la domanda","nl":"de vraag","ph":"do-MAN-da","ex":"L'esame aveva dieci domande.","exNl":"Het examen had tien vragen.","lesson":208,"level":"B1","cat":"sostantivo"},
  {"id":"w1914","it":"il risultato","nl":"het resultaat","ph":"ri-zul-TA-to","ex":"I risultati saranno pubblicati domani.","exNl":"De resultaten worden morgen gepubliceerd.","lesson":208,"level":"B1","cat":"sostantivo"},

  # ── Les 209: Taalgebruik & stijl ──
  {"id":"w1915","it":"il registro","nl":"het register, het taalniveau","ph":"re-DJIS-tro","ex":"In questa email usa un registro formale.","exNl":"Gebruik in deze e-mail een formeel register.","lesson":209,"level":"B1","cat":"sostantivo"},
  {"id":"w1916","it":"formale","nl":"formeel","ph":"for-MA-le","ex":"Il tono della lettera è formale.","exNl":"De toon van de brief is formeel.","lesson":209,"level":"B1","cat":"aggettivo"},
  {"id":"w1917","it":"informale","nl":"informeel","ph":"in-for-MA-le","ex":"Tra amici parliamo in modo informale.","exNl":"Onder vrienden spreken we informeel.","lesson":209,"level":"B1","cat":"aggettivo"},
  {"id":"w1918","it":"il sinonimo","nl":"het synoniem","ph":"si-NO-ni-mo","ex":"'Bello' e 'carino' sono sinonimi.","exNl":"'Bello' en 'carino' zijn synoniemen.","lesson":209,"level":"B1","cat":"sostantivo"},
  {"id":"w1919","it":"il contrario","nl":"het tegenovergestelde","ph":"kon-TRA-rjo","ex":"Qual è il contrario di 'grande'?","exNl":"Wat is het tegenovergestelde van 'groot'?","lesson":209,"level":"B1","cat":"sostantivo"},
  {"id":"w1920","it":"la frase","nl":"de zin","ph":"FRA-ze","ex":"Scrivi una frase completa.","exNl":"Schrijf een volledige zin.","lesson":209,"level":"B1","cat":"sostantivo"},
  {"id":"w1921","it":"la grammatica","nl":"de grammatica","ph":"gram-MA-ti-ka","ex":"La grammatica italiana è complessa.","exNl":"De Italiaanse grammatica is complex.","lesson":209,"level":"B1","cat":"sostantivo"},
  {"id":"w1922","it":"il vocabolario","nl":"de woordenschat","ph":"vo-ka-bo-LA-rjo","ex":"Il mio vocabolario italiano cresce ogni giorno.","exNl":"Mijn Italiaanse woordenschat groeit elke dag.","lesson":209,"level":"B1","cat":"sostantivo"},

  # ── Les 210: Toetsles Blok 9 ──
  {"id":"w1923","it":"l'apprendimento","nl":"het leren, het leerproces","ph":"ap-pren-di-MEN-to","ex":"L'apprendimento delle lingue richiede tempo.","exNl":"Het leren van talen kost tijd.","lesson":210,"level":"B1","cat":"sostantivo"},
  {"id":"w1924","it":"la competenza","nl":"de competentie, de vaardigheid","ph":"kom-pe-TEN-tsa","ex":"Ha buone competenze linguistiche.","exNl":"Hij heeft goede taalvaardigheden.","lesson":210,"level":"B1","cat":"sostantivo"},
  {"id":"w1925","it":"migliorare","nl":"verbeteren","ph":"mi-ljo-RA-re","ex":"Voglio migliorare il mio italiano.","exNl":"Ik wil mijn Italiaans verbeteren.","lesson":210,"level":"B1","cat":"verbo"},
  {"id":"w1926","it":"raggiungere","nl":"bereiken","ph":"rad-DJUN-dje-re","ex":"Ho raggiunto il livello B1.","exNl":"Ik heb niveau B1 bereikt.","lesson":210,"level":"B1","cat":"verbo"},
  {"id":"w1927","it":"padroneggiare","nl":"beheersen","ph":"pa-dro-ned-DJA-re","ex":"Padroneggia tre lingue straniere.","exNl":"Hij beheerst drie vreemde talen.","lesson":210,"level":"B1","cat":"verbo"},
  {"id":"w1928","it":"esprimersi","nl":"zich uitdrukken","ph":"es-PRI-mer-si","ex":"Sa esprimersi bene in italiano.","exNl":"Hij kan zich goed uitdrukken in het Italiaans.","lesson":210,"level":"B1","cat":"verbo"},
  {"id":"w1929","it":"la pronuncia","nl":"de uitspraak","ph":"pro-NUN-tsja","ex":"La sua pronuncia è molto buona.","exNl":"Zijn uitspraak is heel goed.","lesson":210,"level":"B1","cat":"sostantivo"},
  {"id":"w1930","it":"fluente","nl":"vloeiend","ph":"flu-EN-te","ex":"Parlo italiano in modo fluente.","exNl":"Ik spreek vloeiend Italiaans.","lesson":210,"level":"B1","cat":"aggettivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 10: Relaties & emoties verdieping (lessen 211–220)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":211,"title":"Relaties & vriendschap","emoji":"🤝","level":"B1",
   "description":"Praat over vriendschappen en relaties.",
   "grammar":{"title":"Reflexieve werkwoorden in relaties",
   "body":"Veel werkwoorden over relaties zijn reflexief of wederkerig:\n\nincontrarsi — elkaar ontmoeten\nconoscersi — elkaar leren kennen\nvedersi — elkaar zien\nlasciarsi — uit elkaar gaan\nfidarsi di — vertrouwen op\n\nCi siamo conosciuti all'università. — We hebben elkaar leren kennen op de universiteit."},
   "words":["w1931","w1932","w1933","w1934","w1935","w1936","w1937","w1938"]},

  {"id":212,"title":"Liefde & romantiek","emoji":"❤️","level":"B1",
   "description":"Woorden en uitdrukkingen over de liefde.",
   "grammar":{"title":"Over liefde praten",
   "body":"Nuttige uitdrukkingen:\n\ninnamorarsi di — verliefd worden op\nessere innamorato/a di — verliefd zijn op\nandare d'accordo con — goed overweg kunnen met\nfare una proposta — een aanzoek doen\nTi amo / Ti voglio bene — Ik hou van je (romantisch / niet-romantisch)"},
   "words":["w1939","w1940","w1941","w1942","w1943","w1944","w1945","w1946"]},

  {"id":213,"title":"Conflicten & verzoening","emoji":"🕊️","level":"B1",
   "description":"Praat over ruzies, conflicten en verzoening.",
   "grammar":{"title":"Conflicten beschrijven",
   "body":"Uitdrukkingen voor conflicten:\n\nlitigare con — ruziën met\nfare la pace — vrede sluiten\nchiedere scusa — excuses vragen\nandare d'accordo — het eens zijn\nnon sopportare — niet kunnen uitstaan\n\nAbbiamo litigato, ma poi abbiamo fatto la pace. — We hadden ruzie, maar daarna hebben we vrede gesloten."},
   "words":["w1947","w1948","w1949","w1950","w1951","w1952","w1953","w1954"]},

  {"id":214,"title":"Karakter & persoonlijkheid","emoji":"🎭","level":"B1",
   "description":"Beschrijf iemands karakter en persoonlijkheid.",
   "grammar":{"title":"Karaktereigenschappen",
   "body":"Gebruik essere + aggettivo voor karakterbeschrijvingen:\n\nÈ una persona gentile e generosa. — Het is een aardig en gul persoon.\nÈ piuttosto testardo/a. — Hij/zij is nogal koppig.\n\nLet op: simpatico = sympathiek/leuk, NON het Nederlandse 'simpel'."},
   "words":["w1955","w1956","w1957","w1958","w1959","w1960","w1961","w1962"]},

  {"id":215,"title":"Psychologie & gevoelens","emoji":"🧠","level":"B1",
   "description":"Diepere gevoelens en psychologische termen.",
   "grammar":{"title":"Gevoelens uitdrukken",
   "body":"Gebruik sentirsi + aggettivo of provare + sostantivo:\n\nMi sento felice / triste / ansioso. — Ik voel me gelukkig / verdrietig / angstig.\nProvo gioia / paura / vergogna. — Ik voel vreugde / angst / schaamte.\n\nMet congiuntivo: Sono felice che tu stia bene. — Ik ben blij dat het goed met je gaat."},
   "words":["w1963","w1964","w1965","w1966","w1967","w1968","w1969","w1970"]},

  {"id":216,"title":"Dromen & ambities","emoji":"🌟","level":"B1",
   "description":"Praat over je dromen en ambities voor de toekomst.",
   "grammar":{"title":"Dromen en plannen uitdrukken",
   "body":"Constructies voor dromen en ambities:\n\nIl mio sogno è + infinito — Mijn droom is om…\nSpero di + infinito — Ik hoop te…\nMi piacerebbe + infinito — Ik zou graag… willen\nHo intenzione di + infinito — Ik ben van plan om…"},
   "words":["w1971","w1972","w1973","w1974","w1975","w1976","w1977","w1978"]},

  {"id":217,"title":"Succes & falen","emoji":"🏆","level":"B1",
   "description":"Woorden over succes, mislukking en doorzettingsvermogen.",
   "grammar":{"title":"Succes en falen beschrijven",
   "body":"Nuttige werkwoorden:\n\nriuscire a + infinito — erin slagen om…\nfallire — falen, mislukken\nfarcela — het redden, het voor elkaar krijgen\narendersi — zich overgeven, opgeven\n\nCe l'ho fatta! — Ik heb het gered!\nNon mollare! — Geef niet op!"},
   "words":["w1979","w1980","w1981","w1982","w1983","w1984","w1985","w1986"]},

  {"id":218,"title":"Geluk & tevredenheid","emoji":"😊","level":"B1",
   "description":"Praat over geluk, tevredenheid en welzijn.",
   "grammar":{"title":"Over geluk praten",
   "body":"Uitdrukkingen voor geluk en tevredenheid:\n\nSono contento/a di + infinito — Ik ben blij om…\nMi rende felice — Het maakt me gelukkig\nessere soddisfatto/a di — tevreden zijn met\ngodersi la vita — van het leven genieten\nstare bene con se stessi — lekker in je vel zitten"},
   "words":["w1987","w1988","w1989","w1990","w1991","w1992","w1993","w1994"]},

  {"id":219,"title":"Stress & ontspanning","emoji":"🧘","level":"B1",
   "description":"Woorden over stress, druk en ontspanning.",
   "grammar":{"title":"Over stress en ontspanning praten",
   "body":"Nuttige uitdrukkingen:\n\nEssere stressato/a — gestrest zijn\nSono sotto pressione — Ik sta onder druk\nHo bisogno di rilassarmi — Ik heb ontspanning nodig\nStaccare la spina — de stekker eruit trekken (figuurlijk)\nPrendersi una pausa — een pauze nemen"},
   "words":["w1995","w1996","w1997","w1998","w1999","w2000","w2001","w2002"]},

  {"id":220,"title":"Toetsles B1 — Blok 10","emoji":"📋","level":"B1",
   "description":"Toets over lessen 211–220: relaties & emoties.",
   "grammar":{"title":"Toetsles B1 — Blok 10 (les 211–220)","body":"In dit blok heb je geleerd:\n• Reflexieve werkwoorden in relaties\n• Over liefde, conflicten en verzoening praten\n• Karakter en gevoelens beschrijven\n• Dromen, ambities, succes en falen bespreken"},
   "words":["w2003","w2004","w2005","w2006","w2007","w2008","w2009","w2010"]},
]

WORDS += [
  # ── Les 211: Relaties & vriendschap ──
  {"id":"w1931","it":"l'amicizia","nl":"de vriendschap","ph":"a-mi-TSJI-tsja","ex":"L'amicizia è un valore importante.","exNl":"Vriendschap is een belangrijke waarde.","lesson":211,"level":"B1","cat":"sostantivo"},
  {"id":"w1932","it":"fidarsi","nl":"vertrouwen (op)","ph":"fi-DAR-si","ex":"Mi fido completamente di te.","exNl":"Ik vertrouw volledig op je.","lesson":211,"level":"B1","cat":"verbo"},
  {"id":"w1933","it":"il legame","nl":"de band, de verbinding","ph":"le-GA-me","ex":"Abbiamo un legame molto forte.","exNl":"We hebben een heel sterke band.","lesson":211,"level":"B1","cat":"sostantivo"},
  {"id":"w1934","it":"confidarsi","nl":"zich toevertrouwen","ph":"kon-fi-DAR-si","ex":"Mi confido sempre con la mia migliore amica.","exNl":"Ik vertrouw me altijd toe aan mijn beste vriendin.","lesson":211,"level":"B1","cat":"verbo"},
  {"id":"w1935","it":"sostenere","nl":"steunen, ondersteunen","ph":"sos-te-NE-re","ex":"I veri amici ti sostengono sempre.","exNl":"Echte vrienden steunen je altijd.","lesson":211,"level":"B1","cat":"verbo"},
  {"id":"w1936","it":"il compagno","nl":"de partner, de kameraad","ph":"kom-PA-njo","ex":"È il mio compagno di scuola.","exNl":"Hij is mijn schoolkameraad.","lesson":211,"level":"B1","cat":"sostantivo"},
  {"id":"w1937","it":"tradire","nl":"verraden","ph":"tra-DI-re","ex":"Non tradire la fiducia di un amico.","exNl":"Verraad het vertrouwen van een vriend niet.","lesson":211,"level":"B1","cat":"verbo"},
  {"id":"w1938","it":"la fiducia","nl":"het vertrouwen","ph":"fi-DU-tsja","ex":"La fiducia è la base dell'amicizia.","exNl":"Vertrouwen is de basis van vriendschap.","lesson":211,"level":"B1","cat":"sostantivo"},

  # ── Les 212: Liefde & romantiek ──
  {"id":"w1939","it":"innamorarsi","nl":"verliefd worden","ph":"in-na-mo-RAR-si","ex":"Mi sono innamorato di lei subito.","exNl":"Ik werd meteen verliefd op haar.","lesson":212,"level":"B1","cat":"verbo"},
  {"id":"w1940","it":"il fidanzato","nl":"de verloofde, het vriendje","ph":"fi-dan-TSA-to","ex":"Ti presento il mio fidanzato.","exNl":"Ik stel je voor aan mijn vriend.","lesson":212,"level":"B1","cat":"sostantivo"},
  {"id":"w1941","it":"sposarsi","nl":"trouwen","ph":"spo-ZAR-si","ex":"Ci sposiamo a giugno.","exNl":"We trouwen in juni.","lesson":212,"level":"B1","cat":"verbo"},
  {"id":"w1942","it":"il matrimonio","nl":"het huwelijk, de bruiloft","ph":"ma-tri-MO-nio","ex":"Il matrimonio è stato bellissimo.","exNl":"De bruiloft was prachtig.","lesson":212,"level":"B1","cat":"sostantivo"},
  {"id":"w1943","it":"la coppia","nl":"het stel, het koppel","ph":"KOP-pja","ex":"Sono una coppia molto unita.","exNl":"Ze zijn een heel hecht stel.","lesson":212,"level":"B1","cat":"sostantivo"},
  {"id":"w1944","it":"il bacio","nl":"de kus","ph":"BA-tsjo","ex":"Le diede un bacio sulla guancia.","exNl":"Hij gaf haar een kus op de wang.","lesson":212,"level":"B1","cat":"sostantivo"},
  {"id":"w1945","it":"abbracciare","nl":"omhelzen","ph":"ab-brat-TSHA-re","ex":"Mi ha abbracciato forte.","exNl":"Hij omhelsde me stevig.","lesson":212,"level":"B1","cat":"verbo"},
  {"id":"w1946","it":"la convivenza","nl":"het samenwonen","ph":"kon-vi-VEN-tsa","ex":"La convivenza richiede compromessi.","exNl":"Samenwonen vereist compromissen.","lesson":212,"level":"B1","cat":"sostantivo"},

  # ── Les 213: Conflicten & verzoening ──
  {"id":"w1947","it":"litigare","nl":"ruziën","ph":"li-ti-GA-re","ex":"Abbiamo litigato per una sciocchezza.","exNl":"We hebben ruzie gemaakt om een kleinigheid.","lesson":213,"level":"B1","cat":"verbo"},
  {"id":"w1948","it":"la lite","nl":"de ruzie","ph":"LI-te","ex":"È stata una lite terribile.","exNl":"Het was een verschrikkelijke ruzie.","lesson":213,"level":"B1","cat":"sostantivo"},
  {"id":"w1949","it":"fare la pace","nl":"vrede sluiten","ph":"FA-re la PA-tsje","ex":"Alla fine abbiamo fatto la pace.","exNl":"Uiteindelijk hebben we vrede gesloten.","lesson":213,"level":"B1","cat":"espressione"},
  {"id":"w1950","it":"il compromesso","nl":"het compromis","ph":"kom-pro-MES-so","ex":"Dobbiamo trovare un compromesso.","exNl":"We moeten een compromis vinden.","lesson":213,"level":"B1","cat":"sostantivo"},
  {"id":"w1951","it":"sopportare","nl":"verdragen, uitstaan","ph":"sop-por-TA-re","ex":"Non sopporto le bugie.","exNl":"Ik kan leugens niet uitstaan.","lesson":213,"level":"B1","cat":"verbo"},
  {"id":"w1952","it":"il malinteso","nl":"het misverstand","ph":"ma-lin-TE-zo","ex":"È stato solo un malinteso.","exNl":"Het was alleen maar een misverstand.","lesson":213,"level":"B1","cat":"sostantivo"},
  {"id":"w1953","it":"riconciliarsi","nl":"zich verzoenen","ph":"ri-kon-tsji-LJAR-si","ex":"Si sono riconciliati dopo la lite.","exNl":"Ze hebben zich verzoend na de ruzie.","lesson":213,"level":"B1","cat":"verbo"},
  {"id":"w1954","it":"il rancore","nl":"de wrok","ph":"ran-KO-re","ex":"Non porto rancore a nessuno.","exNl":"Ik koester tegen niemand wrok.","lesson":213,"level":"B1","cat":"sostantivo"},

  # ── Les 214: Karakter & persoonlijkheid ──
  {"id":"w1955","it":"generoso","nl":"gul, vrijgevig","ph":"dje-ne-RO-zo","ex":"È una persona molto generosa.","exNl":"Het is een heel gul persoon.","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1956","it":"testardo","nl":"koppig, eigenwijs","ph":"tes-TAR-do","ex":"È testardo come un mulo.","exNl":"Hij is koppig als een ezel.","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1957","it":"sensibile","nl":"gevoelig","ph":"sen-SI-bi-le","ex":"È una persona molto sensibile.","exNl":"Het is een heel gevoelig persoon.","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1958","it":"affidabile","nl":"betrouwbaar","ph":"af-fi-DA-bi-le","ex":"È un collega molto affidabile.","exNl":"Het is een heel betrouwbare collega.","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1959","it":"egoista","nl":"egoïstisch","ph":"e-go-IS-ta","ex":"Non essere così egoista!","exNl":"Wees niet zo egoïstisch!","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1960","it":"paziente","nl":"geduldig","ph":"pa-TSJEN-te","ex":"Bisogna essere pazienti con i bambini.","exNl":"Je moet geduldig zijn met kinderen.","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1961","it":"orgoglioso","nl":"trots","ph":"or-go-LJO-zo","ex":"Sono orgoglioso dei miei figli.","exNl":"Ik ben trots op mijn kinderen.","lesson":214,"level":"B1","cat":"aggettivo"},
  {"id":"w1962","it":"umile","nl":"bescheiden, nederig","ph":"U-mi-le","ex":"Nonostante il successo, è rimasto umile.","exNl":"Ondanks het succes is hij bescheiden gebleven.","lesson":214,"level":"B1","cat":"aggettivo"},

  # ── Les 215: Psychologie & gevoelens ──
  {"id":"w1963","it":"l'ansia","nl":"de angst, de onrust","ph":"AN-sja","ex":"Soffro di ansia prima degli esami.","exNl":"Ik lijd aan angst voor examens.","lesson":215,"level":"B1","cat":"sostantivo"},
  {"id":"w1964","it":"la vergogna","nl":"de schaamte","ph":"ver-GO-nja","ex":"Provo vergogna per quello che ho fatto.","exNl":"Ik schaam me voor wat ik gedaan heb.","lesson":215,"level":"B1","cat":"sostantivo"},
  {"id":"w1965","it":"la gelosia","nl":"de jaloezie","ph":"dje-lo-ZI-a","ex":"La gelosia distrugge le relazioni.","exNl":"Jaloezie vernietigt relaties.","lesson":215,"level":"B1","cat":"sostantivo"},
  {"id":"w1966","it":"la solitudine","nl":"de eenzaamheid","ph":"so-li-TU-di-ne","ex":"A volte la solitudine fa bene.","exNl":"Soms doet eenzaamheid goed.","lesson":215,"level":"B1","cat":"sostantivo"},
  {"id":"w1967","it":"la gratitudine","nl":"de dankbaarheid","ph":"gra-ti-TU-di-ne","ex":"Provo una grande gratitudine.","exNl":"Ik voel grote dankbaarheid.","lesson":215,"level":"B1","cat":"sostantivo"},
  {"id":"w1968","it":"depresso","nl":"depressief, neerslachtig","ph":"de-PRES-so","ex":"Si sente un po' depresso ultimamente.","exNl":"Hij voelt zich de laatste tijd wat depressief.","lesson":215,"level":"B1","cat":"aggettivo"},
  {"id":"w1969","it":"l'autostima","nl":"het zelfvertrouwen","ph":"au-to-STI-ma","ex":"L'autostima è molto importante.","exNl":"Zelfvertrouwen is heel belangrijk.","lesson":215,"level":"B1","cat":"sostantivo"},
  {"id":"w1970","it":"emozionarsi","nl":"ontroerd raken","ph":"e-mo-tsjo-NAR-si","ex":"Mi emoziono facilmente.","exNl":"Ik raak snel ontroerd.","lesson":215,"level":"B1","cat":"verbo"},

  # ── Les 216: Dromen & ambities ──
  {"id":"w1971","it":"l'ambizione","nl":"de ambitie","ph":"am-bi-TSJO-ne","ex":"Ha molta ambizione nella vita.","exNl":"Hij heeft veel ambitie in het leven.","lesson":216,"level":"B1","cat":"sostantivo"},
  {"id":"w1972","it":"l'obiettivo","nl":"het doel","ph":"o-bjet-TI-vo","ex":"Il mio obiettivo è imparare l'italiano.","exNl":"Mijn doel is Italiaans leren.","lesson":216,"level":"B1","cat":"sostantivo"},
  {"id":"w1973","it":"la sfida","nl":"de uitdaging","ph":"SFI-da","ex":"Ogni sfida è un'opportunità.","exNl":"Elke uitdaging is een kans.","lesson":216,"level":"B1","cat":"sostantivo"},
  {"id":"w1974","it":"la determinazione","nl":"de vastberadenheid","ph":"de-ter-mi-na-TSJO-ne","ex":"Ha una grande determinazione.","exNl":"Hij heeft een grote vastberadenheid.","lesson":216,"level":"B1","cat":"sostantivo"},
  {"id":"w1975","it":"aspirare a","nl":"streven naar, aspireren","ph":"as-pi-RA-re a","ex":"Aspiro a diventare avvocato.","exNl":"Ik streef ernaar om advocaat te worden.","lesson":216,"level":"B1","cat":"verbo"},
  {"id":"w1976","it":"impegnarsi","nl":"zich inzetten","ph":"im-pe-NJAR-si","ex":"Mi impegno ogni giorno per migliorare.","exNl":"Ik zet me elke dag in om te verbeteren.","lesson":216,"level":"B1","cat":"verbo"},
  {"id":"w1977","it":"la motivazione","nl":"de motivatie","ph":"mo-ti-va-TSJO-ne","ex":"La motivazione è fondamentale.","exNl":"Motivatie is essentieel.","lesson":216,"level":"B1","cat":"sostantivo"},
  {"id":"w1978","it":"la passione","nl":"de passie","ph":"pas-SJO-ne","ex":"La mia passione è la musica.","exNl":"Mijn passie is muziek.","lesson":216,"level":"B1","cat":"sostantivo"},

  # ── Les 217: Succes & falen ──
  {"id":"w1979","it":"riuscire","nl":"erin slagen, lukken","ph":"rju-SHI-re","ex":"Sono riuscito a superare l'esame.","exNl":"Ik ben erin geslaagd het examen te halen.","lesson":217,"level":"B1","cat":"verbo"},
  {"id":"w1980","it":"fallire","nl":"falen, mislukken","ph":"fal-LI-re","ex":"Il progetto è fallito.","exNl":"Het project is mislukt.","lesson":217,"level":"B1","cat":"verbo"},
  {"id":"w1981","it":"farcela","nl":"het redden, het klaarspelen","ph":"far-TSJE-la","ex":"Ce l'ho fatta!","exNl":"Ik heb het gered!","lesson":217,"level":"B1","cat":"verbo"},
  {"id":"w1982","it":"arrendersi","nl":"opgeven, zich overgeven","ph":"ar-REN-der-si","ex":"Non mi arrendo mai.","exNl":"Ik geef nooit op.","lesson":217,"level":"B1","cat":"verbo"},
  {"id":"w1983","it":"la sconfitta","nl":"de nederlaag","ph":"skon-FIT-ta","ex":"Dalla sconfitta si impara.","exNl":"Van een nederlaag leer je.","lesson":217,"level":"B1","cat":"sostantivo"},
  {"id":"w1984","it":"la vittoria","nl":"de overwinning","ph":"vit-TO-rja","ex":"La vittoria è stata meritata.","exNl":"De overwinning was verdiend.","lesson":217,"level":"B1","cat":"sostantivo"},
  {"id":"w1985","it":"il traguardo","nl":"de finish, het doel","ph":"tra-GWAR-do","ex":"Ho raggiunto un grande traguardo.","exNl":"Ik heb een groot doel bereikt.","lesson":217,"level":"B1","cat":"sostantivo"},
  {"id":"w1986","it":"perseverare","nl":"volharden","ph":"per-se-ve-RA-re","ex":"Chi persevera, alla fine vince.","exNl":"Wie volhardt, wint uiteindelijk.","lesson":217,"level":"B1","cat":"verbo"},

  # ── Les 218: Geluk & tevredenheid ──
  {"id":"w1987","it":"la felicità","nl":"het geluk","ph":"fe-li-tsji-TA","ex":"La felicità è nelle piccole cose.","exNl":"Geluk zit in de kleine dingen.","lesson":218,"level":"B1","cat":"sostantivo"},
  {"id":"w1988","it":"soddisfatto","nl":"tevreden, voldaan","ph":"sod-dis-FAT-to","ex":"Sono soddisfatto del mio lavoro.","exNl":"Ik ben tevreden met mijn werk.","lesson":218,"level":"B1","cat":"aggettivo"},
  {"id":"w1989","it":"godersi","nl":"genieten van","ph":"go-DER-si","ex":"Mi godo ogni momento.","exNl":"Ik geniet van elk moment.","lesson":218,"level":"B1","cat":"verbo"},
  {"id":"w1990","it":"la serenità","nl":"de sereniteit, de rust","ph":"se-re-ni-TA","ex":"Ho trovato la serenità.","exNl":"Ik heb rust gevonden.","lesson":218,"level":"B1","cat":"sostantivo"},
  {"id":"w1991","it":"apprezzare","nl":"waarderen","ph":"ap-pret-TSA-re","ex":"Apprezzo molto la tua amicizia.","exNl":"Ik waardeer je vriendschap heel erg.","lesson":218,"level":"B1","cat":"verbo"},
  {"id":"w1992","it":"grato","nl":"dankbaar","ph":"GRA-to","ex":"Ti sono grato per il tuo aiuto.","exNl":"Ik ben je dankbaar voor je hulp.","lesson":218,"level":"B1","cat":"aggettivo"},
  {"id":"w1993","it":"il benessere","nl":"het welzijn, het welbevinden","ph":"be-nes-SE-re","ex":"Il benessere mentale è fondamentale.","exNl":"Geestelijk welzijn is essentieel.","lesson":218,"level":"B1","cat":"sostantivo"},
  {"id":"w1994","it":"equilibrato","nl":"evenwichtig, uitgebalanceerd","ph":"e-kwi-li-BRA-to","ex":"Cerca di avere una vita equilibrata.","exNl":"Probeer een evenwichtig leven te leiden.","lesson":218,"level":"B1","cat":"aggettivo"},

  # ── Les 219: Stress & ontspanning ──
  {"id":"w1995","it":"lo stress","nl":"de stress","ph":"STRESS","ex":"Lo stress del lavoro mi stanca.","exNl":"De werkstress put me uit.","lesson":219,"level":"B1","cat":"sostantivo"},
  {"id":"w1996","it":"la pressione","nl":"de druk","ph":"pres-SJO-ne","ex":"Sono sotto pressione al lavoro.","exNl":"Ik sta onder druk op het werk.","lesson":219,"level":"B1","cat":"sostantivo"},
  {"id":"w1997","it":"rilassarsi","nl":"zich ontspannen","ph":"ri-las-SAR-si","ex":"Mi rilasso leggendo un libro.","exNl":"Ik ontspan me door een boek te lezen.","lesson":219,"level":"B1","cat":"verbo"},
  {"id":"w1998","it":"la meditazione","nl":"de meditatie","ph":"me-di-ta-TSJO-ne","ex":"La meditazione aiuta a ridurre lo stress.","exNl":"Meditatie helpt om stress te verminderen.","lesson":219,"level":"B1","cat":"sostantivo"},
  {"id":"w1999","it":"esaurito","nl":"uitgeput, op","ph":"e-zau-RI-to","ex":"Sono completamente esaurito.","exNl":"Ik ben helemaal uitgeput.","lesson":219,"level":"B1","cat":"aggettivo"},
  {"id":"w2000","it":"staccare","nl":"loskoppelen, uitschakelen","ph":"stak-KA-re","ex":"Devo staccare dal lavoro.","exNl":"Ik moet loskomen van het werk.","lesson":219,"level":"B1","cat":"verbo"},
  {"id":"w2001","it":"la pausa","nl":"de pauze","ph":"PAU-za","ex":"Prendiamoci una pausa caffè.","exNl":"Laten we een koffiepauze nemen.","lesson":219,"level":"B1","cat":"sostantivo"},
  {"id":"w2002","it":"respirare","nl":"ademen","ph":"res-pi-RA-re","ex":"Respira profondamente e rilassati.","exNl":"Adem diep in en ontspan je.","lesson":219,"level":"B1","cat":"verbo"},

  # ── Les 220: Toetsles Blok 10 ──
  {"id":"w2003","it":"la relazione","nl":"de relatie","ph":"re-la-TSJO-ne","ex":"Hanno una relazione a distanza.","exNl":"Ze hebben een langeafstandsrelatie.","lesson":220,"level":"B1","cat":"sostantivo"},
  {"id":"w2004","it":"maturo","nl":"volwassen, rijp","ph":"ma-TU-ro","ex":"È una persona molto matura.","exNl":"Het is een heel volwassen persoon.","lesson":220,"level":"B1","cat":"aggettivo"},
  {"id":"w2005","it":"la consapevolezza","nl":"het bewustzijn","ph":"kon-sa-pe-vo-LET-tsa","ex":"La consapevolezza di sé è importante.","exNl":"Zelfbewustzijn is belangrijk.","lesson":220,"level":"B1","cat":"sostantivo"},
  {"id":"w2006","it":"superare","nl":"overwinnen, te boven komen","ph":"su-pe-RA-re","ex":"Ha superato un momento difficile.","exNl":"Hij heeft een moeilijk moment overwonnen.","lesson":220,"level":"B1","cat":"verbo"},
  {"id":"w2007","it":"vulnerabile","nl":"kwetsbaar","ph":"vul-ne-RA-bi-le","ex":"Tutti siamo vulnerabili a volte.","exNl":"We zijn allemaal soms kwetsbaar.","lesson":220,"level":"B1","cat":"aggettivo"},
  {"id":"w2008","it":"il coraggio","nl":"de moed","ph":"ko-RAD-djo","ex":"Ci vuole coraggio per cambiare.","exNl":"Er is moed nodig om te veranderen.","lesson":220,"level":"B1","cat":"sostantivo"},
  {"id":"w2009","it":"affrontare","nl":"onder ogen zien, aanpakken","ph":"af-fron-TA-re","ex":"Devi affrontare i tuoi problemi.","exNl":"Je moet je problemen onder ogen zien.","lesson":220,"level":"B1","cat":"verbo"},
  {"id":"w2010","it":"la resilienza","nl":"de veerkracht","ph":"re-zi-LJEN-tsa","ex":"La resilienza è la capacità di riprendersi.","exNl":"Veerkracht is het vermogen om je te herstellen.","lesson":220,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 11: Natuur, dieren & milieu (lessen 221–230)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":221,"title":"Huisdieren","emoji":"🐕","level":"B1",
   "description":"Woorden over huisdieren en dierenverzorging.",
   "grammar":{"title":"Verkleinwoorden (-ino/-etto)",
   "body":"In het Italiaans maak je verkleinwoorden met suffixen:\n\n-ino/a: gatto → gattino (katje), cane → cagnolino (hondje)\n-etto/a: casa → casetta (huisje), gonna → gonnelletta (rokje)\n-ello/a: albero → alberello (boompje)\n-uccio/a: freddo → fredduccio (een beetje koud)\n\nVerkleinwoorden drukken ook genegenheid uit: amore → amorino"},
   "words":["w2011","w2012","w2013","w2014","w2015","w2016","w2017","w2018"]},

  {"id":222,"title":"Wilde dieren","emoji":"🦁","level":"B1",
   "description":"Dieren in het wild en in de dierentuin.",
   "grammar":{"title":"Dieren beschrijven",
   "body":"Nuttige constructies bij dierenbeschrijvingen:\n\nÈ un animale che vive in… — Het is een dier dat leeft in…\nSi nutre di… — Het voedt zich met…\nÈ in via di estinzione — Het is met uitsterven bedreigd\nL'habitat naturale è… — De natuurlijke leefomgeving is…"},
   "words":["w2019","w2020","w2021","w2022","w2023","w2024","w2025","w2026"]},

  {"id":223,"title":"Planten & tuinieren","emoji":"🌿","level":"B1",
   "description":"Woorden over planten, bloemen en tuinieren.",
   "grammar":{"title":"Over planten praten",
   "body":"Nuttige termen:\n\ncoltivare — kweken, verbouwen\ninnaffiare — water geven\npotare — snoeien\nfiorire — bloeien\nseminare — zaaien\nil raccolto — de oogst"},
   "words":["w2027","w2028","w2029","w2030","w2031","w2032","w2033","w2034"]},

  {"id":224,"title":"Landschappen & geografie","emoji":"🏔️","level":"B1",
   "description":"Geografische termen en landschapsbeschrijvingen.",
   "grammar":{"title":"Landschappen beschrijven",
   "body":"Gebruik aggettivi om landschappen te beschrijven:\n\nun paesaggio mozzafiato — een adembenemend landschap\nuna vallata verde — een groene vallei\nuna costa frastagliata — een grillige kustlijn\nil terreno è pianeggiante — het terrein is vlak"},
   "words":["w2035","w2036","w2037","w2038","w2039","w2040","w2041","w2042"]},

  {"id":225,"title":"De zee & het strand","emoji":"🏖️","level":"B1",
   "description":"Woorden over de zee, het strand en watersport.",
   "grammar":{"title":"Aan zee",
   "body":"Italiaans strandvocabulaire:\n\nandare al mare — naar zee gaan\nprendere il sole — zonnebaden\nfare il bagno — zwemmen (in zee)\nil lettino — de ligstoel\nl'ombrellone — de parasol\nla crema solare — de zonnebrand"},
   "words":["w2043","w2044","w2045","w2046","w2047","w2048","w2049","w2050"]},

  {"id":226,"title":"Bergen & wandelen","emoji":"⛰️","level":"B1",
   "description":"Woorden over bergen, wandelen en bergsporten.",
   "grammar":{"title":"In de bergen",
   "body":"Nuttige uitdrukkingen voor bergtochten:\n\nfare un'escursione — een wandeltocht maken\nsalire in cima — naar de top klimmen\nil sentiero — het pad\nil rifugio — de berghut\nla vetta — de top\nil dislivello — het hoogteverschil"},
   "words":["w2051","w2052","w2053","w2054","w2055","w2056","w2057","w2058"]},

  {"id":227,"title":"Klimaat & klimaatverandering","emoji":"🌍","level":"B1",
   "description":"Praat over klimaat en klimaatverandering.",
   "grammar":{"title":"Over het klimaat praten",
   "body":"Nuttige uitdrukkingen:\n\nIl clima sta cambiando. — Het klimaat verandert.\nLa temperatura media è aumentata. — De gemiddelde temperatuur is gestegen.\nBisogna ridurre le emissioni di CO₂. — We moeten de CO₂-uitstoot verminderen.\nL'effetto serra — het broeikaseffect"},
   "words":["w2059","w2060","w2061","w2062","w2063","w2064","w2065","w2066"]},

  {"id":228,"title":"Duurzaamheid & recycling","emoji":"♻️","level":"B1",
   "description":"Woorden over duurzaamheid en milieubewust leven.",
   "grammar":{"title":"Over duurzaamheid praten",
   "body":"Afvalscheiding in Italië (raccolta differenziata):\n\nla plastica — plastic\nil vetro — glas\nla carta — papier\nl'umido — GFT-afval\nl'indifferenziato — restafval\n\nIn Italië is afvalscheiding verplicht en verschilt de regeling per gemeente."},
   "words":["w2067","w2068","w2069","w2070","w2071","w2072","w2073","w2074"]},

  {"id":229,"title":"Energie & grondstoffen","emoji":"⚡","level":"B1",
   "description":"Woorden over energie, grondstoffen en technologie.",
   "grammar":{"title":"Over energie praten",
   "body":"Energiebronnen:\n\nl'energia solare — zonne-energie\nl'energia eolica — windenergie\nl'energia nucleare — kernenergie\ni combustibili fossili — fossiele brandstoffen\nle fonti rinnovabili — hernieuwbare bronnen\n\nL'Italia punta sulle energie rinnovabili. — Italië zet in op hernieuwbare energie."},
   "words":["w2075","w2076","w2077","w2078","w2079","w2080","w2081","w2082"]},

  {"id":230,"title":"Toetsles B1 — Blok 11","emoji":"📋","level":"B1",
   "description":"Toets over lessen 221–230: natuur, dieren & milieu.",
   "grammar":{"title":"Toetsles B1 — Blok 11 (les 221–230)","body":"In dit blok heb je geleerd:\n• Verkleinwoorden (-ino/-etto)\n• Dieren, planten en landschappen beschrijven\n• Over klimaat, duurzaamheid en energie praten"},
   "words":["w2083","w2084","w2085","w2086","w2087","w2088","w2089","w2090"]},
]

WORDS += [
  # ── Les 221: Huisdieren ──
  {"id":"w2011","it":"il cucciolo","nl":"het jong (dier), de puppy","ph":"KU-tsho-lo","ex":"Il cucciolo è molto giocherellone.","exNl":"De puppy is heel speels.","lesson":221,"level":"B1","cat":"sostantivo"},
  {"id":"w2012","it":"il gattino","nl":"het katje","ph":"gat-TI-no","ex":"Il gattino dorme sul divano.","exNl":"Het katje slaapt op de bank.","lesson":221,"level":"B1","cat":"sostantivo"},
  {"id":"w2013","it":"il veterinario","nl":"de dierenarts","ph":"ve-te-ri-NA-rjo","ex":"Porto il cane dal veterinario.","exNl":"Ik breng de hond naar de dierenarts.","lesson":221,"level":"B1","cat":"sostantivo"},
  {"id":"w2014","it":"la gabbia","nl":"de kooi","ph":"GAB-bja","ex":"L'uccellino è nella gabbia.","exNl":"Het vogeltje zit in de kooi.","lesson":221,"level":"B1","cat":"sostantivo"},
  {"id":"w2015","it":"il guinzaglio","nl":"de riem (hond)","ph":"gwin-TSA-ljo","ex":"Tieni il cane al guinzaglio.","exNl":"Houd de hond aan de riem.","lesson":221,"level":"B1","cat":"sostantivo"},
  {"id":"w2016","it":"la zampa","nl":"de poot","ph":"TSAM-pa","ex":"Il gatto mi ha graffiato con la zampa.","exNl":"De kat heeft me gekrabd met zijn poot.","lesson":221,"level":"B1","cat":"sostantivo"},
  {"id":"w2017","it":"abbaiare","nl":"blaffen","ph":"ab-ba-JA-re","ex":"Il cane abbaia tutta la notte.","exNl":"De hond blaft de hele nacht.","lesson":221,"level":"B1","cat":"verbo"},
  {"id":"w2018","it":"accarezzare","nl":"aaien, strelen","ph":"ak-ka-ret-TSA-re","ex":"Mi piace accarezzare il gatto.","exNl":"Ik aai graag de kat.","lesson":221,"level":"B1","cat":"verbo"},

  # ── Les 222: Wilde dieren ──
  {"id":"w2019","it":"il lupo","nl":"de wolf","ph":"LU-po","ex":"Il lupo vive nei boschi.","exNl":"De wolf leeft in de bossen.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2020","it":"l'orso","nl":"de beer","ph":"OR-so","ex":"L'orso bruno vive sulle Alpi.","exNl":"De bruine beer leeft in de Alpen.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2021","it":"il delfino","nl":"de dolfijn","ph":"del-FI-no","ex":"I delfini nuotano vicino alla barca.","exNl":"De dolfijnen zwemmen bij de boot.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2022","it":"l'aquila","nl":"de adelaar","ph":"A-kwi-la","ex":"L'aquila vola sopra le montagne.","exNl":"De adelaar vliegt boven de bergen.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2023","it":"la volpe","nl":"de vos","ph":"VOL-pe","ex":"La volpe è un animale furbo.","exNl":"De vos is een slim dier.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2024","it":"il cervo","nl":"het hert","ph":"TSJER-vo","ex":"Ho visto un cervo nel bosco.","exNl":"Ik heb een hert gezien in het bos.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2025","it":"la specie","nl":"de soort","ph":"SPE-tsje","ex":"Questa specie è protetta.","exNl":"Deze soort is beschermd.","lesson":222,"level":"B1","cat":"sostantivo"},
  {"id":"w2026","it":"selvatico","nl":"wild, in het wild levend","ph":"sel-VA-ti-ko","ex":"È un animale selvatico, non domestico.","exNl":"Het is een wild dier, niet een huisdier.","lesson":222,"level":"B1","cat":"aggettivo"},

  # ── Les 223: Planten & tuinieren ──
  {"id":"w2027","it":"la pianta","nl":"de plant","ph":"PJAN-ta","ex":"Ho comprato una pianta per il balcone.","exNl":"Ik heb een plant gekocht voor het balkon.","lesson":223,"level":"B1","cat":"sostantivo"},
  {"id":"w2028","it":"il fiore","nl":"de bloem","ph":"FJO-re","ex":"I fiori sbocciano in primavera.","exNl":"De bloemen bloeien in de lente.","lesson":223,"level":"B1","cat":"sostantivo"},
  {"id":"w2029","it":"il seme","nl":"het zaad","ph":"SE-me","ex":"Ho piantato i semi di pomodoro.","exNl":"Ik heb tomatenzaden geplant.","lesson":223,"level":"B1","cat":"sostantivo"},
  {"id":"w2030","it":"innaffiare","nl":"water geven","ph":"in-naf-FJA-re","ex":"Devo innaffiare le piante ogni giorno.","exNl":"Ik moet elke dag de planten water geven.","lesson":223,"level":"B1","cat":"verbo"},
  {"id":"w2031","it":"la radice","nl":"de wortel","ph":"ra-DI-tsje","ex":"Le radici dell'albero sono profonde.","exNl":"De wortels van de boom zijn diep.","lesson":223,"level":"B1","cat":"sostantivo"},
  {"id":"w2032","it":"il raccolto","nl":"de oogst","ph":"rak-KOL-to","ex":"Quest'anno il raccolto è stato abbondante.","exNl":"Dit jaar was de oogst overvloedig.","lesson":223,"level":"B1","cat":"sostantivo"},
  {"id":"w2033","it":"coltivare","nl":"verbouwen, kweken","ph":"kol-ti-VA-re","ex":"Coltiviamo pomodori nell'orto.","exNl":"We verbouwen tomaten in de moestuin.","lesson":223,"level":"B1","cat":"verbo"},
  {"id":"w2034","it":"l'orto","nl":"de moestuin","ph":"OR-to","ex":"Abbiamo un piccolo orto in giardino.","exNl":"We hebben een kleine moestuin in de tuin.","lesson":223,"level":"B1","cat":"sostantivo"},

  # ── Les 224: Landschappen & geografie ──
  {"id":"w2035","it":"la collina","nl":"de heuvel","ph":"kol-LI-na","ex":"La Toscana è famosa per le sue colline.","exNl":"Toscane is beroemd om zijn heuvels.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2036","it":"la pianura","nl":"de vlakte","ph":"pja-NU-ra","ex":"La Pianura Padana è molto fertile.","exNl":"De Povlakte is heel vruchtbaar.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2037","it":"la valle","nl":"de vallei, het dal","ph":"VAL-le","ex":"La valle è circondata dalle montagne.","exNl":"De vallei is omgeven door bergen.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2038","it":"il vulcano","nl":"de vulkaan","ph":"vul-KA-no","ex":"L'Etna è il vulcano più alto d'Europa.","exNl":"De Etna is de hoogste vulkaan van Europa.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2039","it":"il fiume","nl":"de rivier","ph":"FJU-me","ex":"Il Po è il fiume più lungo d'Italia.","exNl":"De Po is de langste rivier van Italië.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2040","it":"il lago","nl":"het meer","ph":"LA-go","ex":"Il Lago di Garda è bellissimo.","exNl":"Het Gardameer is prachtig.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2041","it":"la costa","nl":"de kust","ph":"KOS-ta","ex":"La costa amalfitana è patrimonio UNESCO.","exNl":"De Amalfikust is UNESCO-erfgoed.","lesson":224,"level":"B1","cat":"sostantivo"},
  {"id":"w2042","it":"l'isola","nl":"het eiland","ph":"I-zo-la","ex":"La Sardegna è una grande isola.","exNl":"Sardinië is een groot eiland.","lesson":224,"level":"B1","cat":"sostantivo"},

  # ── Les 225: De zee & het strand ──
  {"id":"w2043","it":"l'onda","nl":"de golf (zee)","ph":"ON-da","ex":"Le onde oggi sono molto alte.","exNl":"De golven zijn vandaag heel hoog.","lesson":225,"level":"B1","cat":"sostantivo"},
  {"id":"w2044","it":"la sabbia","nl":"het zand","ph":"SAB-bja","ex":"I bambini giocano sulla sabbia.","exNl":"De kinderen spelen op het zand.","lesson":225,"level":"B1","cat":"sostantivo"},
  {"id":"w2045","it":"l'ombrellone","nl":"de parasol (strand)","ph":"om-brel-LO-ne","ex":"Affittiamo un ombrellone per la giornata.","exNl":"We huren een parasol voor de dag.","lesson":225,"level":"B1","cat":"sostantivo"},
  {"id":"w2046","it":"tuffarsi","nl":"(een) duik nemen","ph":"tuf-FAR-si","ex":"Mi tuffo dal trampolino.","exNl":"Ik duik van de duikplank.","lesson":225,"level":"B1","cat":"verbo"},
  {"id":"w2047","it":"la crema solare","nl":"de zonnebrand(crème)","ph":"KRE-ma so-LA-re","ex":"Metti la crema solare, il sole è forte.","exNl":"Smeer zonnebrand, de zon is sterk.","lesson":225,"level":"B1","cat":"sostantivo"},
  {"id":"w2048","it":"il porto","nl":"de haven","ph":"POR-to","ex":"Le barche sono ormeggiate nel porto.","exNl":"De boten liggen aangemeerd in de haven.","lesson":225,"level":"B1","cat":"sostantivo"},
  {"id":"w2049","it":"la barca a vela","nl":"de zeilboot","ph":"BAR-ka a VE-la","ex":"Facciamo un giro in barca a vela.","exNl":"We maken een tochtje met de zeilboot.","lesson":225,"level":"B1","cat":"sostantivo"},
  {"id":"w2050","it":"abbronzarsi","nl":"bruin worden","ph":"ab-bron-DZAR-si","ex":"Mi abbronzo facilmente.","exNl":"Ik word snel bruin.","lesson":225,"level":"B1","cat":"verbo"},

  # ── Les 226: Bergen & wandelen ──
  {"id":"w2051","it":"l'escursione","nl":"de wandeltocht, de excursie","ph":"es-kur-SJO-ne","ex":"Domani facciamo un'escursione in montagna.","exNl":"Morgen maken we een bergtocht.","lesson":226,"level":"B1","cat":"sostantivo"},
  {"id":"w2052","it":"il sentiero","nl":"het pad, het wandelpad","ph":"sen-TJE-ro","ex":"Il sentiero è ben segnalato.","exNl":"Het pad is goed gemarkeerd.","lesson":226,"level":"B1","cat":"sostantivo"},
  {"id":"w2053","it":"la vetta","nl":"de top, de piek","ph":"VET-ta","ex":"Abbiamo raggiunto la vetta!","exNl":"We hebben de top bereikt!","lesson":226,"level":"B1","cat":"sostantivo"},
  {"id":"w2054","it":"il rifugio","nl":"de berghut","ph":"ri-FU-djo","ex":"Dormiamo nel rifugio stanotte.","exNl":"We slapen vannacht in de berghut.","lesson":226,"level":"B1","cat":"sostantivo"},
  {"id":"w2055","it":"lo zaino","nl":"de rugzak","ph":"DZAI-no","ex":"Ho messo tutto nello zaino.","exNl":"Ik heb alles in de rugzak gedaan.","lesson":226,"level":"B1","cat":"sostantivo"},
  {"id":"w2056","it":"arrampicarsi","nl":"klimmen","ph":"ar-ram-pi-KAR-si","ex":"Mi piace arrampicarmi sulle rocce.","exNl":"Ik klim graag op de rotsen.","lesson":226,"level":"B1","cat":"verbo"},
  {"id":"w2057","it":"il ghiacciaio","nl":"de gletsjer","ph":"gjat-TSHA-jo","ex":"I ghiacciai si stanno sciogliendo.","exNl":"De gletsjers smelten.","lesson":226,"level":"B1","cat":"sostantivo"},
  {"id":"w2058","it":"il panorama","nl":"het panorama, het uitzicht","ph":"pa-no-RA-ma","ex":"Dalla vetta il panorama è spettacolare.","exNl":"Vanaf de top is het uitzicht spectaculair.","lesson":226,"level":"B1","cat":"sostantivo"},

  # ── Les 227: Klimaat & klimaatverandering ──
  {"id":"w2059","it":"il cambiamento climatico","nl":"de klimaatverandering","ph":"kam-bja-MEN-to kli-MA-ti-ko","ex":"Il cambiamento climatico è un problema globale.","exNl":"Klimaatverandering is een wereldwijd probleem.","lesson":227,"level":"B1","cat":"sostantivo"},
  {"id":"w2060","it":"il riscaldamento globale","nl":"de opwarming van de aarde","ph":"ris-kal-da-MEN-to glo-BA-le","ex":"Il riscaldamento globale causa lo scioglimento dei ghiacci.","exNl":"De opwarming van de aarde veroorzaakt het smelten van ijs.","lesson":227,"level":"B1","cat":"sostantivo"},
  {"id":"w2061","it":"l'emissione","nl":"de uitstoot","ph":"e-mis-SJO-ne","ex":"Dobbiamo ridurre le emissioni di CO₂.","exNl":"We moeten de CO₂-uitstoot verminderen.","lesson":227,"level":"B1","cat":"sostantivo"},
  {"id":"w2062","it":"l'effetto serra","nl":"het broeikaseffect","ph":"ef-FET-to SER-ra","ex":"L'effetto serra riscalda il pianeta.","exNl":"Het broeikaseffect warmt de planeet op.","lesson":227,"level":"B1","cat":"sostantivo"},
  {"id":"w2063","it":"la siccità","nl":"de droogte","ph":"sit-tsji-TA","ex":"La siccità ha distrutto i raccolti.","exNl":"De droogte heeft de oogsten vernietigd.","lesson":227,"level":"B1","cat":"sostantivo"},
  {"id":"w2064","it":"l'inondazione","nl":"de overstroming","ph":"i-non-da-TSJO-ne","ex":"Le inondazioni hanno colpito il nord.","exNl":"De overstromingen troffen het noorden.","lesson":227,"level":"B1","cat":"sostantivo"},
  {"id":"w2065","it":"sciogliersi","nl":"smelten","ph":"SHOL-jer-si","ex":"I ghiacci polari si stanno sciogliendo.","exNl":"Het poolijs smelt.","lesson":227,"level":"B1","cat":"verbo"},
  {"id":"w2066","it":"inquinare","nl":"vervuilen","ph":"in-kwi-NA-re","ex":"Le fabbriche inquinano l'aria.","exNl":"De fabrieken vervuilen de lucht.","lesson":227,"level":"B1","cat":"verbo"},

  # ── Les 228: Duurzaamheid & recycling ──
  {"id":"w2067","it":"riciclare","nl":"recyclen","ph":"ri-tsji-KLA-re","ex":"È importante riciclare la plastica.","exNl":"Het is belangrijk om plastic te recyclen.","lesson":228,"level":"B1","cat":"verbo"},
  {"id":"w2068","it":"la raccolta differenziata","nl":"het afval scheiden","ph":"rak-KOL-ta dif-fe-ren-TSJA-ta","ex":"In Italia la raccolta differenziata è obbligatoria.","exNl":"In Italië is afvalscheiding verplicht.","lesson":228,"level":"B1","cat":"sostantivo"},
  {"id":"w2069","it":"i rifiuti","nl":"het afval","ph":"ri-FJU-ti","ex":"Non gettare i rifiuti per terra.","exNl":"Gooi geen afval op de grond.","lesson":228,"level":"B1","cat":"sostantivo"},
  {"id":"w2070","it":"sostenibile","nl":"duurzaam","ph":"sos-te-NI-bi-le","ex":"Dobbiamo vivere in modo sostenibile.","exNl":"We moeten duurzaam leven.","lesson":228,"level":"B1","cat":"aggettivo"},
  {"id":"w2071","it":"lo spreco","nl":"de verspilling","ph":"SPRE-ko","ex":"Lo spreco alimentare è un grande problema.","exNl":"Voedselverspilling is een groot probleem.","lesson":228,"level":"B1","cat":"sostantivo"},
  {"id":"w2072","it":"ridurre","nl":"verminderen","ph":"ri-DUR-re","ex":"Cerco di ridurre il consumo di plastica.","exNl":"Ik probeer mijn plasticgebruik te verminderen.","lesson":228,"level":"B1","cat":"verbo"},
  {"id":"w2073","it":"riutilizzare","nl":"hergebruiken","ph":"ri-u-ti-lid-ZA-re","ex":"Puoi riutilizzare questa borsa.","exNl":"Je kunt deze tas hergebruiken.","lesson":228,"level":"B1","cat":"verbo"},
  {"id":"w2074","it":"biodegradabile","nl":"biologisch afbreekbaar","ph":"bi-o-de-gra-DA-bi-le","ex":"Questo sacchetto è biodegradabile.","exNl":"Dit zakje is biologisch afbreekbaar.","lesson":228,"level":"B1","cat":"aggettivo"},

  # ── Les 229: Energie & grondstoffen ──
  {"id":"w2075","it":"l'energia solare","nl":"de zonne-energie","ph":"e-ner-DJI-a so-LA-re","ex":"I pannelli solari producono energia solare.","exNl":"Zonnepanelen produceren zonne-energie.","lesson":229,"level":"B1","cat":"sostantivo"},
  {"id":"w2076","it":"l'energia eolica","nl":"de windenergie","ph":"e-ner-DJI-a e-O-li-ka","ex":"L'energia eolica è pulita.","exNl":"Windenergie is schoon.","lesson":229,"level":"B1","cat":"sostantivo"},
  {"id":"w2077","it":"il pannello solare","nl":"het zonnepaneel","ph":"pan-NEL-lo so-LA-re","ex":"Abbiamo installato pannelli solari sul tetto.","exNl":"We hebben zonnepanelen op het dak geïnstalleerd.","lesson":229,"level":"B1","cat":"sostantivo"},
  {"id":"w2078","it":"il petrolio","nl":"de aardolie, de petroleum","ph":"pe-TRO-ljo","ex":"Il prezzo del petrolio è aumentato.","exNl":"De olieprijs is gestegen.","lesson":229,"level":"B1","cat":"sostantivo"},
  {"id":"w2079","it":"il carbone","nl":"de steenkool","ph":"kar-BO-ne","ex":"Le centrali a carbone inquinano molto.","exNl":"Kolencentrales vervuilen veel.","lesson":229,"level":"B1","cat":"sostantivo"},
  {"id":"w2080","it":"rinnovabile","nl":"hernieuwbaar","ph":"rin-no-VA-bi-le","ex":"Le fonti rinnovabili sono il futuro.","exNl":"Hernieuwbare bronnen zijn de toekomst.","lesson":229,"level":"B1","cat":"aggettivo"},
  {"id":"w2081","it":"il consumo","nl":"het verbruik","ph":"kon-SU-mo","ex":"Dobbiamo ridurre il consumo energetico.","exNl":"We moeten het energieverbruik verminderen.","lesson":229,"level":"B1","cat":"sostantivo"},
  {"id":"w2082","it":"la centrale elettrica","nl":"de elektriciteitscentrale","ph":"tsjen-TRA-le e-LET-tri-ka","ex":"La centrale elettrica produce energia per la città.","exNl":"De elektriciteitscentrale produceert energie voor de stad.","lesson":229,"level":"B1","cat":"sostantivo"},

  # ── Les 230: Toetsles Blok 11 ──
  {"id":"w2083","it":"l'ecosistema","nl":"het ecosysteem","ph":"e-ko-sis-TE-ma","ex":"L'ecosistema marino è fragile.","exNl":"Het mariene ecosysteem is fragiel.","lesson":230,"level":"B1","cat":"sostantivo"},
  {"id":"w2084","it":"proteggere","nl":"beschermen","ph":"pro-TED-dje-re","ex":"Dobbiamo proteggere la natura.","exNl":"We moeten de natuur beschermen.","lesson":230,"level":"B1","cat":"verbo"},
  {"id":"w2085","it":"la riserva naturale","nl":"het natuurreservaat","ph":"ri-ZER-va na-tu-RA-le","ex":"La riserva naturale è aperta al pubblico.","exNl":"Het natuurreservaat is open voor publiek.","lesson":230,"level":"B1","cat":"sostantivo"},
  {"id":"w2086","it":"minacciato","nl":"bedreigd","ph":"mi-nat-TSHA-to","ex":"Molte specie sono minacciate.","exNl":"Veel soorten zijn bedreigd.","lesson":230,"level":"B1","cat":"aggettivo"},
  {"id":"w2087","it":"l'impronta ecologica","nl":"de ecologische voetafdruk","ph":"im-PRON-ta e-ko-LO-dji-ka","ex":"Ognuno può ridurre la propria impronta ecologica.","exNl":"Iedereen kan zijn eigen ecologische voetafdruk verkleinen.","lesson":230,"level":"B1","cat":"sostantivo"},
  {"id":"w2088","it":"conservare","nl":"bewaren, behouden","ph":"kon-ser-VA-re","ex":"Dobbiamo conservare le risorse naturali.","exNl":"We moeten de natuurlijke bronnen behouden.","lesson":230,"level":"B1","cat":"verbo"},
  {"id":"w2089","it":"la biodiversità","nl":"de biodiversiteit","ph":"bi-o-di-ver-si-TA","ex":"La biodiversità è essenziale per il pianeta.","exNl":"Biodiversiteit is essentieel voor de planeet.","lesson":230,"level":"B1","cat":"sostantivo"},
  {"id":"w2090","it":"estinguersi","nl":"uitsterven","ph":"es-TIN-gwer-si","ex":"I dinosauri si sono estinti milioni di anni fa.","exNl":"De dinosauriërs stierven miljoenen jaren geleden uit.","lesson":230,"level":"B1","cat":"verbo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 12: Kunst, media & entertainment (lessen 231–240)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":231,"title":"Film & bioscoop","emoji":"🎬","level":"B1",
   "description":"Woorden over film, bioscoop en cinema.",
   "grammar":{"title":"Over films praten",
   "body":"Nuttige constructies:\n\nÈ un film che parla di… — Het is een film die gaat over…\nIl film è diretto da… — De film is geregisseerd door…\nÈ stato girato in Italia. — Hij is opgenomen in Italië.\nIl film mi ha commosso / fatto ridere / annoiato. — De film heeft me ontroerd / aan het lachen gemaakt / verveeld."},
   "words":["w2091","w2092","w2093","w2094","w2095","w2096","w2097","w2098"]},

  {"id":232,"title":"Theater & opera","emoji":"🎭","level":"B1",
   "description":"Woorden over theater, opera en podiumkunsten.",
   "grammar":{"title":"Theater & opera",
   "body":"Italië is het geboorteland van de opera. Nuttige termen:\n\nil sipario — het (toneel)doek\nla prima — de première\nil bis — de toegift\nandare in scena — opgevoerd worden\nil libretto — het libretto (tekst van een opera)"},
   "words":["w2099","w2100","w2101","w2102","w2103","w2104","w2105","w2106"]},

  {"id":233,"title":"Schilderkunst & musea","emoji":"🖌️","level":"B1",
   "description":"Praat over kunst en museumbezoek.",
   "grammar":{"title":"Kunst bespreken",
   "body":"Nuttige uitdrukkingen in een museum:\n\nQuesta opera rappresenta… — Dit werk stelt … voor.\nÈ un esempio di arte barocca. — Het is een voorbeeld van barokke kunst.\nL'ingresso costa… — De toegang kost…\nÈ vietato fare foto con il flash. — Foto's met flits zijn verboden."},
   "words":["w2107","w2108","w2109","w2110","w2111","w2112","w2113","w2114"]},

  {"id":234,"title":"Fotografie & design","emoji":"📷","level":"B1",
   "description":"Woorden over fotografie, design en esthetiek.",
   "grammar":{"title":"Over fotografie praten",
   "body":"Nuttige termen:\n\nscattare una foto — een foto nemen\nil primo piano — de close-up\nlo sfondo — de achtergrond\nla luce naturale — het natuurlijke licht\nritoccare — retoucheren\nil bianco e nero — zwart-wit"},
   "words":["w2115","w2116","w2117","w2118","w2119","w2120","w2121","w2122"]},

  {"id":235,"title":"Kranten & journalistiek","emoji":"📰","level":"B1",
   "description":"Woorden over nieuws, kranten en journalistiek.",
   "grammar":{"title":"Krantenkoppen lezen",
   "body":"Italiaanse krantenkoppen gebruiken vaak:\n\n• Het presens voor recente gebeurtenissen\n• Geen lidwoord: Governo approva legge (i.p.v. Il governo ha approvato la legge)\n• Condizionale voor onbevestigd nieuws: Il ministro sarebbe dimesso — De minister zou afgetreden zijn"},
   "words":["w2123","w2124","w2125","w2126","w2127","w2128","w2129","w2130"]},

  {"id":236,"title":"Radio & televisie","emoji":"📺","level":"B1",
   "description":"Woorden over radio, televisie en medialandschap.",
   "grammar":{"title":"Over media praten",
   "body":"Het Italiaanse medialandschap:\n\nla RAI — de publieke omroep (Radiotelevisione Italiana)\nMediaset — de grootste commerciële omroep\nil telegiornale (TG) — het journaal\nil programma / la trasmissione — het programma\nin diretta — live\nin differita — uitgesteld"},
   "words":["w2131","w2132","w2133","w2134","w2135","w2136","w2137","w2138"]},

  {"id":237,"title":"Reclame & marketing","emoji":"📢","level":"B1",
   "description":"Woorden over reclame, marketing en consumentengedrag.",
   "grammar":{"title":"Reclametaal",
   "body":"Reclame-uitdrukkingen:\n\nlo spot pubblicitario — de reclamespot\nil marchio — het merk\nlo slogan — de slogan\nil consumatore — de consument\nlanciare un prodotto — een product lanceren\nfare pubblicità — reclame maken"},
   "words":["w2139","w2140","w2141","w2142","w2143","w2144","w2145","w2146"]},

  {"id":238,"title":"Mode & trends","emoji":"👗","level":"B1",
   "description":"Woorden over de Italiaanse mode-industrie.",
   "grammar":{"title":"Over mode praten",
   "body":"Italië is een modewereld-grootmacht. Nuttige termen:\n\nla sfilata — de modeshow\nlo stilista — de modeontwerper\nla passerella — de catwalk\nessere alla moda / fuori moda — in de mode / uit de mode zijn\nil Made in Italy — het label 'Made in Italy'"},
   "words":["w2147","w2148","w2149","w2150","w2151","w2152","w2153","w2154"]},

  {"id":239,"title":"Evenementen & festivals","emoji":"🎪","level":"B1",
   "description":"Woorden over evenementen, festivals en culturele agenda.",
   "grammar":{"title":"Evenementen beschrijven",
   "body":"Nuttige zinnen:\n\nL'evento si svolge / si tiene il… — Het evenement vindt plaats op…\nIl festival dura tre giorni. — Het festival duurt drie dagen.\nI biglietti sono esauriti. — De kaartjes zijn uitverkocht.\nL'ingresso è gratuito / a pagamento. — De toegang is gratis / tegen betaling."},
   "words":["w2155","w2156","w2157","w2158","w2159","w2160","w2161","w2162"]},

  {"id":240,"title":"Toetsles B1 — Blok 12","emoji":"📋","level":"B1",
   "description":"Toets over lessen 231–240: kunst, media & entertainment.",
   "grammar":{"title":"Toetsles B1 — Blok 12 (les 231–240)","body":"In dit blok heb je geleerd:\n• Over film, theater en opera praten\n• Kunst en fotografie bespreken\n• Media, reclame en mode beschrijven\n• Evenementen en festivals bespreken"},
   "words":["w2163","w2164","w2165","w2166","w2167","w2168","w2169","w2170"]},
]

WORDS += [
  # ── Les 231: Film & bioscoop ──
  {"id":"w2091","it":"il regista","nl":"de regisseur","ph":"re-DJIS-ta","ex":"Fellini è stato un grande regista.","exNl":"Fellini was een groot regisseur.","lesson":231,"level":"B1","cat":"sostantivo"},
  {"id":"w2092","it":"la sceneggiatura","nl":"het draaiboek, het scenario","ph":"she-ned-dja-TU-ra","ex":"La sceneggiatura ha vinto un premio.","exNl":"Het scenario won een prijs.","lesson":231,"level":"B1","cat":"sostantivo"},
  {"id":"w2093","it":"l'attore","nl":"de acteur","ph":"at-TO-re","ex":"L'attore ha recitato molto bene.","exNl":"De acteur speelde heel goed.","lesson":231,"level":"B1","cat":"sostantivo"},
  {"id":"w2094","it":"la colonna sonora","nl":"de filmmuziek, de soundtrack","ph":"ko-LON-na so-NO-ra","ex":"La colonna sonora è di Morricone.","exNl":"De filmmuziek is van Morricone.","lesson":231,"level":"B1","cat":"sostantivo"},
  {"id":"w2095","it":"il sottotitolo","nl":"de ondertitel","ph":"sot-to-TI-to-lo","ex":"Guardo il film con i sottotitoli.","exNl":"Ik kijk de film met ondertitels.","lesson":231,"level":"B1","cat":"sostantivo"},
  {"id":"w2096","it":"girare","nl":"opnemen, draaien (film)","ph":"dji-RA-re","ex":"Il film è stato girato a Roma.","exNl":"De film is opgenomen in Rome.","lesson":231,"level":"B1","cat":"verbo"},
  {"id":"w2097","it":"il documentario","nl":"de documentaire","ph":"do-ku-men-TA-rjo","ex":"Ho visto un bel documentario sulla natura.","exNl":"Ik heb een mooie natuurdocumentaire gezien.","lesson":231,"level":"B1","cat":"sostantivo"},
  {"id":"w2098","it":"la recensione","nl":"de recensie","ph":"re-tsjen-SJO-ne","ex":"Le recensioni del film sono ottime.","exNl":"De recensies van de film zijn uitstekend.","lesson":231,"level":"B1","cat":"sostantivo"},

  # ── Les 232: Theater & opera ──
  {"id":"w2099","it":"il sipario","nl":"het (toneel)doek","ph":"si-PA-rjo","ex":"Il sipario si alza alle otto.","exNl":"Het doek gaat om acht uur op.","lesson":232,"level":"B1","cat":"sostantivo"},
  {"id":"w2100","it":"la scena","nl":"het toneel, de scène","ph":"SHE-na","ex":"L'attrice entra in scena.","exNl":"De actrice betreedt het toneel.","lesson":232,"level":"B1","cat":"sostantivo"},
  {"id":"w2101","it":"recitare","nl":"acteren, toneelspelen","ph":"re-tsji-TA-re","ex":"Recita al Teatro alla Scala.","exNl":"Hij treedt op in het Teatro alla Scala.","lesson":232,"level":"B1","cat":"verbo"},
  {"id":"w2102","it":"il libretto","nl":"het libretto (operatekst)","ph":"li-BRET-to","ex":"Il libretto è scritto in italiano.","exNl":"Het libretto is in het Italiaans geschreven.","lesson":232,"level":"B1","cat":"sostantivo"},
  {"id":"w2103","it":"l'atto","nl":"het bedrijf (theater)","ph":"AT-to","ex":"L'opera ha tre atti.","exNl":"De opera heeft drie bedrijven.","lesson":232,"level":"B1","cat":"sostantivo"},
  {"id":"w2104","it":"il pubblico","nl":"het publiek","ph":"PUB-bli-ko","ex":"Il pubblico ha applaudito a lungo.","exNl":"Het publiek applaudisseerde lang.","lesson":232,"level":"B1","cat":"sostantivo"},
  {"id":"w2105","it":"la prima","nl":"de première","ph":"PRI-ma","ex":"Stasera c'è la prima dello spettacolo.","exNl":"Vanavond is de première van de voorstelling.","lesson":232,"level":"B1","cat":"sostantivo"},
  {"id":"w2106","it":"lo spettacolo","nl":"de voorstelling, het optreden","ph":"spet-TA-ko-lo","ex":"Lo spettacolo è stato magnifico.","exNl":"De voorstelling was geweldig.","lesson":232,"level":"B1","cat":"sostantivo"},

  # ── Les 233: Schilderkunst & musea ──
  {"id":"w2107","it":"il museo","nl":"het museum","ph":"mu-ZE-o","ex":"Visitiamo il museo degli Uffizi.","exNl":"We bezoeken het Uffizi-museum.","lesson":233,"level":"B1","cat":"sostantivo"},
  {"id":"w2108","it":"la mostra","nl":"de tentoonstelling","ph":"MOS-tra","ex":"C'è una mostra di arte moderna.","exNl":"Er is een tentoonstelling van moderne kunst.","lesson":233,"level":"B1","cat":"sostantivo"},
  {"id":"w2109","it":"il pittore","nl":"de schilder","ph":"pit-TO-re","ex":"Caravaggio fu un grande pittore.","exNl":"Caravaggio was een groot schilder.","lesson":233,"level":"B1","cat":"sostantivo"},
  {"id":"w2110","it":"il ritratto","nl":"het portret","ph":"ri-TRAT-to","ex":"La Gioconda è il ritratto più famoso al mondo.","exNl":"De Mona Lisa is het beroemdste portret ter wereld.","lesson":233,"level":"B1","cat":"sostantivo"},
  {"id":"w2111","it":"la cornice","nl":"de lijst (schilderij)","ph":"kor-NI-tsje","ex":"Il quadro ha una cornice dorata.","exNl":"Het schilderij heeft een vergulde lijst.","lesson":233,"level":"B1","cat":"sostantivo"},
  {"id":"w2112","it":"la galleria","nl":"de galerie","ph":"gal-le-RI-a","ex":"Visitiamo una galleria d'arte.","exNl":"We bezoeken een kunstgalerie.","lesson":233,"level":"B1","cat":"sostantivo"},
  {"id":"w2113","it":"ammirare","nl":"bewonderen","ph":"am-mi-RA-re","ex":"Ammiro i quadri di Botticelli.","exNl":"Ik bewonder de schilderijen van Botticelli.","lesson":233,"level":"B1","cat":"verbo"},
  {"id":"w2114","it":"restaurare","nl":"restaureren","ph":"res-tau-RA-re","ex":"Stanno restaurando l'affresco.","exNl":"Ze zijn het fresco aan het restaureren.","lesson":233,"level":"B1","cat":"verbo"},

  # ── Les 234: Fotografie & design ──
  {"id":"w2115","it":"scattare","nl":"(een foto) nemen","ph":"skat-TA-re","ex":"Ho scattato molte foto a Venezia.","exNl":"Ik heb veel foto's genomen in Venetië.","lesson":234,"level":"B1","cat":"verbo"},
  {"id":"w2116","it":"l'obiettivo","nl":"de lens, het objectief","ph":"o-bjet-TI-vo","ex":"Ho comprato un nuovo obiettivo per la fotocamera.","exNl":"Ik heb een nieuwe lens voor de camera gekocht.","lesson":234,"level":"B1","cat":"sostantivo"},
  {"id":"w2117","it":"lo sfondo","nl":"de achtergrond","ph":"SFON-do","ex":"Lo sfondo della foto è il mare.","exNl":"De achtergrond van de foto is de zee.","lesson":234,"level":"B1","cat":"sostantivo"},
  {"id":"w2118","it":"il design","nl":"het design, het ontwerp","ph":"di-ZAIN","ex":"Il design italiano è famoso nel mondo.","exNl":"Italiaans design is wereldberoemd.","lesson":234,"level":"B1","cat":"sostantivo"},
  {"id":"w2119","it":"l'inquadratura","nl":"het beeldkader, de kadrering","ph":"in-kwa-dra-TU-ra","ex":"L'inquadratura è perfetta.","exNl":"Het beeldkader is perfect.","lesson":234,"level":"B1","cat":"sostantivo"},
  {"id":"w2120","it":"la luce","nl":"het licht","ph":"LU-tsje","ex":"La luce del tramonto è bellissima.","exNl":"Het licht van de zonsondergang is prachtig.","lesson":234,"level":"B1","cat":"sostantivo"},
  {"id":"w2121","it":"l'immagine","nl":"het beeld, de afbeelding","ph":"im-MA-dji-ne","ex":"Questa immagine è molto suggestiva.","exNl":"Dit beeld is heel suggestief.","lesson":234,"level":"B1","cat":"sostantivo"},
  {"id":"w2122","it":"creativo","nl":"creatief","ph":"kre-a-TI-vo","ex":"È una persona molto creativa.","exNl":"Het is een heel creatief persoon.","lesson":234,"level":"B1","cat":"aggettivo"},

  # ── Les 235: Kranten & journalistiek ──
  {"id":"w2123","it":"il giornale","nl":"de krant","ph":"djor-NA-le","ex":"Leggo il giornale ogni mattina.","exNl":"Ik lees elke ochtend de krant.","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2124","it":"il giornalista","nl":"de journalist","ph":"djor-na-LIS-ta","ex":"Il giornalista ha scritto un articolo interessante.","exNl":"De journalist heeft een interessant artikel geschreven.","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2125","it":"l'articolo","nl":"het artikel","ph":"ar-TI-ko-lo","ex":"Ho letto un articolo sulla politica italiana.","exNl":"Ik heb een artikel gelezen over de Italiaanse politiek.","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2126","it":"la notizia","nl":"het nieuws, het bericht","ph":"no-TI-tsja","ex":"Hai sentito l'ultima notizia?","exNl":"Heb je het laatste nieuws gehoord?","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2127","it":"l'intervista","nl":"het interview","ph":"in-ter-VIS-ta","ex":"L'intervista al presidente è domani.","exNl":"Het interview met de president is morgen.","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2128","it":"la redazione","nl":"de redactie","ph":"re-da-TSJO-ne","ex":"Lavora nella redazione del giornale.","exNl":"Hij werkt bij de redactie van de krant.","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2129","it":"la cronaca","nl":"het verslag, de kroniek","ph":"KRO-na-ka","ex":"La cronaca locale è molto seguita.","exNl":"Het lokale nieuws wordt veel gevolgd.","lesson":235,"level":"B1","cat":"sostantivo"},
  {"id":"w2130","it":"indagare","nl":"onderzoeken, uitzoeken","ph":"in-da-GA-re","ex":"Il giornalista indaga sulla corruzione.","exNl":"De journalist onderzoekt corruptie.","lesson":235,"level":"B1","cat":"verbo"},

  # ── Les 236: Radio & televisie ──
  {"id":"w2131","it":"il telegiornale","nl":"het journaal","ph":"te-le-djor-NA-le","ex":"Guardo il telegiornale alle otto.","exNl":"Ik kijk om acht uur het journaal.","lesson":236,"level":"B1","cat":"sostantivo"},
  {"id":"w2132","it":"il canale","nl":"het kanaal, de zender","ph":"ka-NA-le","ex":"Su quale canale c'è il film?","exNl":"Op welk kanaal is de film?","lesson":236,"level":"B1","cat":"sostantivo"},
  {"id":"w2133","it":"la trasmissione","nl":"de uitzending, het programma","ph":"traz-mis-SJO-ne","ex":"È una trasmissione molto popolare.","exNl":"Het is een heel populair programma.","lesson":236,"level":"B1","cat":"sostantivo"},
  {"id":"w2134","it":"in diretta","nl":"live, rechtstreeks","ph":"in di-RET-ta","ex":"Il concerto è trasmesso in diretta.","exNl":"Het concert wordt live uitgezonden.","lesson":236,"level":"B1","cat":"espressione"},
  {"id":"w2135","it":"il conduttore","nl":"de presentator","ph":"kon-dut-TO-re","ex":"Il conduttore del programma è molto simpatico.","exNl":"De presentator van het programma is heel sympathiek.","lesson":236,"level":"B1","cat":"sostantivo"},
  {"id":"w2136","it":"la puntata","nl":"de aflevering","ph":"pun-TA-ta","ex":"Ho visto l'ultima puntata della serie.","exNl":"Ik heb de laatste aflevering van de serie gezien.","lesson":236,"level":"B1","cat":"sostantivo"},
  {"id":"w2137","it":"trasmettere","nl":"uitzenden","ph":"traz-MET-te-re","ex":"La RAI trasmette in tutta Italia.","exNl":"De RAI zendt uit in heel Italië.","lesson":236,"level":"B1","cat":"verbo"},
  {"id":"w2138","it":"il telespettatore","nl":"de kijker","ph":"te-le-spet-ta-TO-re","ex":"Il programma ha milioni di telespettatori.","exNl":"Het programma heeft miljoenen kijkers.","lesson":236,"level":"B1","cat":"sostantivo"},

  # ── Les 237: Reclame & marketing ──
  {"id":"w2139","it":"la pubblicità","nl":"de reclame","ph":"pub-bli-tsji-TA","ex":"La pubblicità in TV è troppa.","exNl":"Er is te veel reclame op TV.","lesson":237,"level":"B1","cat":"sostantivo"},
  {"id":"w2140","it":"il marchio","nl":"het merk","ph":"MAR-kjo","ex":"È un marchio italiano molto conosciuto.","exNl":"Het is een heel bekend Italiaans merk.","lesson":237,"level":"B1","cat":"sostantivo"},
  {"id":"w2141","it":"il consumatore","nl":"de consument","ph":"kon-su-ma-TO-re","ex":"I consumatori chiedono prodotti sostenibili.","exNl":"De consumenten vragen om duurzame producten.","lesson":237,"level":"B1","cat":"sostantivo"},
  {"id":"w2142","it":"lo slogan","nl":"de slogan","ph":"SLO-gan","ex":"Lo slogan è facile da ricordare.","exNl":"De slogan is makkelijk te onthouden.","lesson":237,"level":"B1","cat":"sostantivo"},
  {"id":"w2143","it":"il prodotto","nl":"het product","ph":"pro-DOT-to","ex":"Il prodotto ha un buon rapporto qualità-prezzo.","exNl":"Het product heeft een goede prijs-kwaliteitverhouding.","lesson":237,"level":"B1","cat":"sostantivo"},
  {"id":"w2144","it":"promuovere","nl":"promoten, bevorderen","ph":"pro-MWO-ve-re","ex":"L'azienda promuove il nuovo prodotto.","exNl":"Het bedrijf promoot het nieuwe product.","lesson":237,"level":"B1","cat":"verbo"},
  {"id":"w2145","it":"il target","nl":"de doelgroep","ph":"TAR-get","ex":"Il target sono i giovani.","exNl":"De doelgroep is jongeren.","lesson":237,"level":"B1","cat":"sostantivo"},
  {"id":"w2146","it":"la campagna","nl":"de campagne","ph":"kam-PA-nja","ex":"La campagna pubblicitaria è molto efficace.","exNl":"De reclamecampagne is heel effectief.","lesson":237,"level":"B1","cat":"sostantivo"},

  # ── Les 238: Mode & trends ──
  {"id":"w2147","it":"la sfilata","nl":"de modeshow","ph":"sfi-LA-ta","ex":"La sfilata si tiene a Milano.","exNl":"De modeshow vindt plaats in Milaan.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2148","it":"lo stilista","nl":"de modeontwerper","ph":"sti-LIS-ta","ex":"Armani è un famoso stilista italiano.","exNl":"Armani is een beroemde Italiaanse modeontwerper.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2149","it":"la tendenza","nl":"de trend","ph":"ten-DEN-tsa","ex":"Le tendenze cambiano ogni stagione.","exNl":"De trends veranderen elk seizoen.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2150","it":"la passerella","nl":"de catwalk","ph":"pas-se-REL-la","ex":"Le modelle sfilano sulla passerella.","exNl":"De modellen lopen over de catwalk.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2151","it":"il tessuto","nl":"de stof, het weefsel","ph":"tes-SU-to","ex":"Questo tessuto è di pura seta.","exNl":"Deze stof is van pure zijde.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2152","it":"la seta","nl":"de zijde","ph":"SE-ta","ex":"La cravatta è di seta italiana.","exNl":"De stropdas is van Italiaanse zijde.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2153","it":"il cuoio","nl":"het leer","ph":"KWO-jo","ex":"La borsa è fatta di cuoio.","exNl":"De tas is gemaakt van leer.","lesson":238,"level":"B1","cat":"sostantivo"},
  {"id":"w2154","it":"alla moda","nl":"in de mode, modieus","ph":"al-la MO-da","ex":"Questo vestito è molto alla moda.","exNl":"Deze jurk is heel modieus.","lesson":238,"level":"B1","cat":"espressione"},

  # ── Les 239: Evenementen & festivals ──
  {"id":"w2155","it":"il festival","nl":"het festival","ph":"FES-ti-val","ex":"Il Festival di Sanremo è molto seguito.","exNl":"Het Festival van Sanremo wordt veel gevolgd.","lesson":239,"level":"B1","cat":"sostantivo"},
  {"id":"w2156","it":"la fiera","nl":"de beurs, de jaarmarkt","ph":"FJE-ra","ex":"La fiera del libro è a Torino.","exNl":"De boekenbeurs is in Turijn.","lesson":239,"level":"B1","cat":"sostantivo"},
  {"id":"w2157","it":"la sagra","nl":"het dorpsfeest, het eetfestival","ph":"SA-gra","ex":"Stasera c'è la sagra della porchetta.","exNl":"Vanavond is het porchetta-festival.","lesson":239,"level":"B1","cat":"sostantivo"},
  {"id":"w2158","it":"il biglietto","nl":"het kaartje, het ticket","ph":"bi-LJET-to","ex":"I biglietti sono già esauriti.","exNl":"De kaartjes zijn al uitverkocht.","lesson":239,"level":"B1","cat":"sostantivo"},
  {"id":"w2159","it":"la folla","nl":"de menigte","ph":"FOL-la","ex":"C'era una grande folla al concerto.","exNl":"Er was een grote menigte bij het concert.","lesson":239,"level":"B1","cat":"sostantivo"},
  {"id":"w2160","it":"partecipare","nl":"deelnemen, meedoen","ph":"par-te-tsji-PA-re","ex":"Voglio partecipare al festival.","exNl":"Ik wil meedoen aan het festival.","lesson":239,"level":"B1","cat":"verbo"},
  {"id":"w2161","it":"organizzare","nl":"organiseren","ph":"or-ga-nid-ZA-re","ex":"Chi organizza l'evento?","exNl":"Wie organiseert het evenement?","lesson":239,"level":"B1","cat":"verbo"},
  {"id":"w2162","it":"esaurito","nl":"uitverkocht","ph":"e-zau-RI-to","ex":"Lo spettacolo è esaurito.","exNl":"De voorstelling is uitverkocht.","lesson":239,"level":"B1","cat":"aggettivo"},

  # ── Les 240: Toetsles Blok 12 ──
  {"id":"w2163","it":"il capolavoro","nl":"het meesterwerk","ph":"ka-po-la-VO-ro","ex":"La Divina Commedia è un capolavoro.","exNl":"De Goddelijke Komedie is een meesterwerk.","lesson":240,"level":"B1","cat":"sostantivo"},
  {"id":"w2164","it":"l'artista","nl":"de kunstenaar","ph":"ar-TIS-ta","ex":"L'artista espone al museo.","exNl":"De kunstenaar exposeert in het museum.","lesson":240,"level":"B1","cat":"sostantivo"},
  {"id":"w2165","it":"ispirare","nl":"inspireren","ph":"is-pi-RA-re","ex":"L'Italia ispira molti artisti.","exNl":"Italië inspireert veel kunstenaars.","lesson":240,"level":"B1","cat":"verbo"},
  {"id":"w2166","it":"la creatività","nl":"de creativiteit","ph":"kre-a-ti-vi-TA","ex":"La creatività italiana è rinomata.","exNl":"De Italiaanse creativiteit is vermaard.","lesson":240,"level":"B1","cat":"sostantivo"},
  {"id":"w2167","it":"il patrimonio culturale","nl":"het cultureel erfgoed","ph":"pa-tri-MO-nio kul-tu-RA-le","ex":"L'Italia ha un enorme patrimonio culturale.","exNl":"Italië heeft een enorm cultureel erfgoed.","lesson":240,"level":"B1","cat":"sostantivo"},
  {"id":"w2168","it":"il premio","nl":"de prijs (onderscheiding)","ph":"PRE-mjo","ex":"Ha vinto il premio per il miglior film.","exNl":"Hij won de prijs voor de beste film.","lesson":240,"level":"B1","cat":"sostantivo"},
  {"id":"w2169","it":"appassionato","nl":"gepassioneerd, fan","ph":"ap-pas-sjo-NA-to","ex":"Sono appassionato di cinema italiano.","exNl":"Ik ben een liefhebber van Italiaanse cinema.","lesson":240,"level":"B1","cat":"aggettivo"},
  {"id":"w2170","it":"il talento","nl":"het talent","ph":"ta-LEN-to","ex":"Ha un grande talento per la musica.","exNl":"Hij heeft een groot talent voor muziek.","lesson":240,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 13: Maatschappij & politiek (lessen 241–250)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":241,"title":"Politiek — basis","emoji":"🏛️","level":"B1",
   "description":"Leer basisbegrippen uit de politiek.",
   "grammar":{"title":"Passiva met venire",
   "body":"Naast essere + voltooid deelwoord kun je de passiva ook met venire vormen (alleen in enkelvoudige tijden):\n\nLa legge viene approvata dal parlamento. — De wet wordt goedgekeurd door het parlement.\nIl presidente viene eletto ogni sette anni. — De president wordt elke zeven jaar gekozen.\n\nVuistregel: venire + participio = actie die nu plaatsvindt; essere + participio = toestand."},
   "words":["w2171","w2172","w2173","w2174","w2175","w2176","w2177","w2178"]},

  {"id":242,"title":"Verkiezingen & democratie","emoji":"🗳️","level":"B1",
   "description":"Woorden over verkiezingen en het democratisch proces.",
   "grammar":{"title":"Over verkiezingen praten",
   "body":"Verkiezingsterminologie:\n\nvotare — stemmen\ncandidarsi — zich kandidaat stellen\neleggere (p.p.: eletto) — kiezen, verkiezen\nil seggio elettorale — het stembureau\nla scheda elettorale — het stembiljet\nla maggioranza / la minoranza — de meerderheid / de minderheid"},
   "words":["w2179","w2180","w2181","w2182","w2183","w2184","w2185","w2186"]},

  {"id":243,"title":"Rechten & plichten","emoji":"⚖️","level":"B1",
   "description":"Woorden over burgerrechten en plichten.",
   "grammar":{"title":"Rechten en plichten",
   "body":"De Italiaanse grondwet garandeert fundamentele rechten:\n\nil diritto di voto — het stemrecht\nla libertà di espressione — de vrijheid van meningsuiting\nil dovere civico — de burgerplicht\nla parità di diritti — gelijke rechten\n\nTutti i cittadini hanno pari dignità sociale. — Alle burgers hebben gelijke sociale waardigheid (Art. 3 Constituzione)."},
   "words":["w2187","w2188","w2189","w2190","w2191","w2192","w2193","w2194"]},

  {"id":244,"title":"Justitie & wetgeving","emoji":"⚖️","level":"B1",
   "description":"Woorden over recht, wetgeving en justitie.",
   "grammar":{"title":"Juridische taal",
   "body":"Basisjuridische termen:\n\nil tribunale — de rechtbank\nil giudice — de rechter\nl'avvocato — de advocaat\nla sentenza — het vonnis\nassolvere — vrijspreken\ncondannare — veroordelen"},
   "words":["w2195","w2196","w2197","w2198","w2199","w2200","w2201","w2202"]},

  {"id":245,"title":"Immigratie & integratie","emoji":"🌍","level":"B1",
   "description":"Woorden over migratie en integratie in de maatschappij.",
   "grammar":{"title":"Over migratie praten",
   "body":"Nuttige termen:\n\nl'immigrato — de immigrant\nil rifugiato — de vluchteling\nil permesso di soggiorno — de verblijfsvergunning\nintegrarsi — zich integreren\nla multiculturalità — de multiculturaliteit"},
   "words":["w2203","w2204","w2205","w2206","w2207","w2208","w2209","w2210"]},

  {"id":246,"title":"Vrijwilligerswerk & hulp","emoji":"🤲","level":"B1",
   "description":"Woorden over vrijwilligerswerk en maatschappelijke hulp.",
   "grammar":{"title":"Over vrijwilligerswerk praten",
   "body":"Fare volontariato = vrijwilligerswerk doen:\n\nFaccio volontariato in un'associazione. — Ik doe vrijwilligerswerk bij een organisatie.\nAiutiamo i senzatetto. — We helpen daklozen.\nDono il sangue regolarmente. — Ik doneer regelmatig bloed."},
   "words":["w2211","w2212","w2213","w2214","w2215","w2216","w2217","w2218"]},

  {"id":247,"title":"Religie & geloof","emoji":"⛪","level":"B1",
   "description":"Woorden over religie, geloof en spiritualiteit.",
   "grammar":{"title":"Over geloof praten",
   "body":"Italië is overwegend katholiek, maar kent ook veel diversiteit:\n\ncredere in Dio — geloven in God\nessere credente / ateo / agnostico — gelovig / atheïst / agnost zijn\nfrequentare la chiesa — naar de kerk gaan\nil Vaticano — het Vaticaan"},
   "words":["w2219","w2220","w2221","w2222","w2223","w2224","w2225","w2226"]},

  {"id":248,"title":"Gelijkheid & diversiteit","emoji":"🌈","level":"B1",
   "description":"Woorden over gelijkheid, diversiteit en inclusie.",
   "grammar":{"title":"Over gelijkheid praten",
   "body":"Nuttige uitdrukkingen:\n\nla parità di genere — gendergelijkheid\ni diritti umani — de mensenrechten\nla discriminazione — de discriminatie\nl'inclusione — de inclusie\nil rispetto — het respect\nla diversità è una ricchezza — diversiteit is een rijkdom"},
   "words":["w2227","w2228","w2229","w2230","w2231","w2232","w2233","w2234"]},

  {"id":249,"title":"Oorlog & vrede","emoji":"🕊️","level":"B1",
   "description":"Woorden over oorlog, vrede en internationale betrekkingen.",
   "grammar":{"title":"Over oorlog en vrede praten",
   "body":"Belangrijke termen:\n\nil conflitto — het conflict\nil trattato di pace — het vredesverdrag\nle Nazioni Unite — de Verenigde Naties\nil disarmo — de ontwapening\nla diplomazia — de diplomatie\nnegoziare — onderhandelen"},
   "words":["w2235","w2236","w2237","w2238","w2239","w2240","w2241","w2242"]},

  {"id":250,"title":"Toetsles B1 — Blok 13","emoji":"📋","level":"B1",
   "description":"Toets over lessen 241–250: maatschappij & politiek.",
   "grammar":{"title":"Toetsles B1 — Blok 13 (les 241–250)","body":"In dit blok heb je geleerd:\n• De passiva met venire\n• Over verkiezingen en democratie praten\n• Rechten, plichten en justitie\n• Immigratie, vrijwilligerswerk en maatschappelijke thema's"},
   "words":["w2243","w2244","w2245","w2246","w2247","w2248","w2249","w2250"]},
]

WORDS += [
  # ── Les 241: Politiek — basis ──
  {"id":"w2171","it":"la politica","nl":"de politiek","ph":"po-LI-ti-ka","ex":"La politica italiana è complessa.","exNl":"De Italiaanse politiek is complex.","lesson":241,"level":"B1","cat":"sostantivo"},
  {"id":"w2172","it":"il governo","nl":"de regering","ph":"go-VER-no","ex":"Il governo ha approvato la riforma.","exNl":"De regering heeft de hervorming goedgekeurd.","lesson":241,"level":"B1","cat":"sostantivo"},
  {"id":"w2173","it":"il parlamento","nl":"het parlement","ph":"par-la-MEN-to","ex":"Il parlamento vota la nuova legge.","exNl":"Het parlement stemt over de nieuwe wet.","lesson":241,"level":"B1","cat":"sostantivo"},
  {"id":"w2174","it":"il presidente","nl":"de president","ph":"pre-zi-DEN-te","ex":"Il Presidente della Repubblica ha firmato la legge.","exNl":"De president van de republiek heeft de wet getekend.","lesson":241,"level":"B1","cat":"sostantivo"},
  {"id":"w2175","it":"il ministro","nl":"de minister","ph":"mi-NIS-tro","ex":"Il ministro ha rilasciato una dichiarazione.","exNl":"De minister heeft een verklaring afgegeven.","lesson":241,"level":"B1","cat":"sostantivo"},
  {"id":"w2176","it":"la legge","nl":"de wet","ph":"LED-dje","ex":"La legge è uguale per tutti.","exNl":"De wet is gelijk voor iedereen.","lesson":241,"level":"B1","cat":"sostantivo"},
  {"id":"w2177","it":"approvare","nl":"goedkeuren","ph":"ap-pro-VA-re","ex":"Il parlamento ha approvato il bilancio.","exNl":"Het parlement heeft de begroting goedgekeurd.","lesson":241,"level":"B1","cat":"verbo"},
  {"id":"w2178","it":"il partito","nl":"de politieke partij","ph":"par-TI-to","ex":"A quale partito appartieni?","exNl":"Bij welke partij hoor je?","lesson":241,"level":"B1","cat":"sostantivo"},

  # ── Les 242: Verkiezingen & democratie ──
  {"id":"w2179","it":"votare","nl":"stemmen","ph":"vo-TA-re","ex":"Domani si vota per le elezioni.","exNl":"Morgen wordt er gestemd voor de verkiezingen.","lesson":242,"level":"B1","cat":"verbo"},
  {"id":"w2180","it":"le elezioni","nl":"de verkiezingen","ph":"e-le-TSJO-ni","ex":"Le elezioni politiche sono ogni cinque anni.","exNl":"De politieke verkiezingen zijn elke vijf jaar.","lesson":242,"level":"B1","cat":"sostantivo"},
  {"id":"w2181","it":"il candidato","nl":"de kandidaat","ph":"kan-di-DA-to","ex":"Ci sono tre candidati per la presidenza.","exNl":"Er zijn drie kandidaten voor het presidentschap.","lesson":242,"level":"B1","cat":"sostantivo"},
  {"id":"w2182","it":"la campagna elettorale","nl":"de verkiezingscampagne","ph":"kam-PA-nja e-let-to-RA-le","ex":"La campagna elettorale è stata intensa.","exNl":"De verkiezingscampagne was intens.","lesson":242,"level":"B1","cat":"sostantivo"},
  {"id":"w2183","it":"la democrazia","nl":"de democratie","ph":"de-mo-kra-TSI-a","ex":"La democrazia è un valore fondamentale.","exNl":"Democratie is een fundamentele waarde.","lesson":242,"level":"B1","cat":"sostantivo"},
  {"id":"w2184","it":"la maggioranza","nl":"de meerderheid","ph":"mad-djo-RAN-tsa","ex":"Il partito ha ottenuto la maggioranza.","exNl":"De partij heeft de meerderheid behaald.","lesson":242,"level":"B1","cat":"sostantivo"},
  {"id":"w2185","it":"l'opposizione","nl":"de oppositie","ph":"op-po-zi-TSJO-ne","ex":"L'opposizione ha criticato la riforma.","exNl":"De oppositie heeft de hervorming bekritiseerd.","lesson":242,"level":"B1","cat":"sostantivo"},
  {"id":"w2186","it":"eleggere","nl":"kiezen, verkiezen","ph":"e-LED-dje-re","ex":"Il popolo elegge i suoi rappresentanti.","exNl":"Het volk kiest zijn vertegenwoordigers.","lesson":242,"level":"B1","cat":"verbo"},

  # ── Les 243: Rechten & plichten ──
  {"id":"w2187","it":"il diritto","nl":"het recht","ph":"di-RIT-to","ex":"Tutti hanno il diritto alla salute.","exNl":"Iedereen heeft recht op gezondheid.","lesson":243,"level":"B1","cat":"sostantivo"},
  {"id":"w2188","it":"il dovere","nl":"de plicht","ph":"do-VE-re","ex":"Pagare le tasse è un dovere.","exNl":"Belasting betalen is een plicht.","lesson":243,"level":"B1","cat":"sostantivo"},
  {"id":"w2189","it":"la libertà","nl":"de vrijheid","ph":"li-ber-TA","ex":"La libertà di espressione è un diritto fondamentale.","exNl":"Vrijheid van meningsuiting is een grondrecht.","lesson":243,"level":"B1","cat":"sostantivo"},
  {"id":"w2190","it":"il cittadino","nl":"de burger","ph":"tshjt-ta-DI-no","ex":"I cittadini hanno diritti e doveri.","exNl":"De burgers hebben rechten en plichten.","lesson":243,"level":"B1","cat":"sostantivo"},
  {"id":"w2191","it":"la dignità","nl":"de waardigheid","ph":"di-nji-TA","ex":"Ogni persona ha diritto alla dignità.","exNl":"Ieder persoon heeft recht op waardigheid.","lesson":243,"level":"B1","cat":"sostantivo"},
  {"id":"w2192","it":"l'uguaglianza","nl":"de gelijkheid","ph":"u-gwa-LJAN-tsa","ex":"L'uguaglianza è un principio della Costituzione.","exNl":"Gelijkheid is een beginsel van de grondwet.","lesson":243,"level":"B1","cat":"sostantivo"},
  {"id":"w2193","it":"rispettare","nl":"respecteren","ph":"ris-pet-TA-re","ex":"Bisogna rispettare le regole.","exNl":"Je moet de regels respecteren.","lesson":243,"level":"B1","cat":"verbo"},
  {"id":"w2194","it":"garantire","nl":"garanderen","ph":"ga-ran-TI-re","ex":"La Costituzione garantisce i diritti fondamentali.","exNl":"De grondwet garandeert de grondrechten.","lesson":243,"level":"B1","cat":"verbo"},

  # ── Les 244: Justitie & wetgeving ──
  {"id":"w2195","it":"il tribunale","nl":"de rechtbank","ph":"tri-bu-NA-le","ex":"Il processo si svolge al tribunale.","exNl":"Het proces vindt plaats in de rechtbank.","lesson":244,"level":"B1","cat":"sostantivo"},
  {"id":"w2196","it":"il giudice","nl":"de rechter","ph":"DJU-di-tsje","ex":"Il giudice ha emesso la sentenza.","exNl":"De rechter heeft het vonnis uitgesproken.","lesson":244,"level":"B1","cat":"sostantivo"},
  {"id":"w2197","it":"l'avvocato","nl":"de advocaat","ph":"av-vo-KA-to","ex":"Ho bisogno di un avvocato.","exNl":"Ik heb een advocaat nodig.","lesson":244,"level":"B1","cat":"sostantivo"},
  {"id":"w2198","it":"la sentenza","nl":"het vonnis","ph":"sen-TEN-tsa","ex":"La sentenza è stata pronunciata.","exNl":"Het vonnis is uitgesproken.","lesson":244,"level":"B1","cat":"sostantivo"},
  {"id":"w2199","it":"il processo","nl":"het proces, de rechtszaak","ph":"pro-TSHES-so","ex":"Il processo durerà mesi.","exNl":"Het proces zal maanden duren.","lesson":244,"level":"B1","cat":"sostantivo"},
  {"id":"w2200","it":"condannare","nl":"veroordelen","ph":"kon-dan-NA-re","ex":"È stato condannato a tre anni.","exNl":"Hij is veroordeeld tot drie jaar.","lesson":244,"level":"B1","cat":"verbo"},
  {"id":"w2201","it":"assolvere","nl":"vrijspreken","ph":"as-SOL-ve-re","ex":"L'imputato è stato assolto.","exNl":"De verdachte is vrijgesproken.","lesson":244,"level":"B1","cat":"verbo"},
  {"id":"w2202","it":"il reato","nl":"het misdrijf","ph":"re-A-to","ex":"Ha commesso un reato grave.","exNl":"Hij heeft een ernstig misdrijf gepleegd.","lesson":244,"level":"B1","cat":"sostantivo"},

  # ── Les 245: Immigratie & integratie ──
  {"id":"w2203","it":"l'immigrazione","nl":"de immigratie","ph":"im-mi-gra-TSJO-ne","ex":"L'immigrazione è un tema molto discusso.","exNl":"Immigratie is een veel besproken thema.","lesson":245,"level":"B1","cat":"sostantivo"},
  {"id":"w2204","it":"il rifugiato","nl":"de vluchteling","ph":"ri-fu-DJA-to","ex":"I rifugiati cercano protezione.","exNl":"De vluchtelingen zoeken bescherming.","lesson":245,"level":"B1","cat":"sostantivo"},
  {"id":"w2205","it":"integrarsi","nl":"zich integreren","ph":"in-te-GRAR-si","ex":"Si è integrato bene nella comunità.","exNl":"Hij heeft zich goed geïntegreerd in de gemeenschap.","lesson":245,"level":"B1","cat":"verbo"},
  {"id":"w2206","it":"accogliere","nl":"ontvangen, opvangen","ph":"ak-KO-lje-re","ex":"L'Italia accoglie molti migranti.","exNl":"Italië vangt veel migranten op.","lesson":245,"level":"B1","cat":"verbo"},
  {"id":"w2207","it":"la comunità","nl":"de gemeenschap","ph":"ko-mu-ni-TA","ex":"Vive in una comunità multiculturale.","exNl":"Hij woont in een multiculturele gemeenschap.","lesson":245,"level":"B1","cat":"sostantivo"},
  {"id":"w2208","it":"lo straniero","nl":"de buitenlander, de vreemdeling","ph":"stra-NJE-ro","ex":"In Italia vivono molti stranieri.","exNl":"In Italië wonen veel buitenlanders.","lesson":245,"level":"B1","cat":"sostantivo"},
  {"id":"w2209","it":"la convivenza","nl":"het samenleven","ph":"kon-vi-VEN-tsa","ex":"La convivenza pacifica è importante.","exNl":"Vreedzaam samenleven is belangrijk.","lesson":245,"level":"B1","cat":"sostantivo"},
  {"id":"w2210","it":"il pregiudizio","nl":"het vooroordeel","ph":"pre-dju-DI-tsjo","ex":"Dobbiamo combattere i pregiudizi.","exNl":"We moeten vooroordelen bestrijden.","lesson":245,"level":"B1","cat":"sostantivo"},

  # ── Les 246: Vrijwilligerswerk & hulp ──
  {"id":"w2211","it":"il volontariato","nl":"het vrijwilligerswerk","ph":"vo-lon-ta-RJA-to","ex":"Faccio volontariato ogni weekend.","exNl":"Ik doe elke weekend vrijwilligerswerk.","lesson":246,"level":"B1","cat":"sostantivo"},
  {"id":"w2212","it":"il volontario","nl":"de vrijwilliger","ph":"vo-lon-TA-rjo","ex":"I volontari aiutano i più bisognosi.","exNl":"De vrijwilligers helpen de meest behoeftigen.","lesson":246,"level":"B1","cat":"sostantivo"},
  {"id":"w2213","it":"donare","nl":"doneren, schenken","ph":"do-NA-re","ex":"Dono il sangue due volte l'anno.","exNl":"Ik doneer twee keer per jaar bloed.","lesson":246,"level":"B1","cat":"verbo"},
  {"id":"w2214","it":"la solidarietà","nl":"de solidariteit","ph":"so-li-da-rje-TA","ex":"La solidarietà è un valore importante.","exNl":"Solidariteit is een belangrijke waarde.","lesson":246,"level":"B1","cat":"sostantivo"},
  {"id":"w2215","it":"l'associazione","nl":"de vereniging, de stichting","ph":"as-so-tsja-TSJO-ne","ex":"Lavoro per un'associazione umanitaria.","exNl":"Ik werk voor een humanitaire organisatie.","lesson":246,"level":"B1","cat":"sostantivo"},
  {"id":"w2216","it":"il senzatetto","nl":"de dakloze","ph":"sen-tsa-TET-to","ex":"Aiutiamo i senzatetto con cibo e vestiti.","exNl":"We helpen daklozen met eten en kleding.","lesson":246,"level":"B1","cat":"sostantivo"},
  {"id":"w2217","it":"raccogliere fondi","nl":"geld inzamelen","ph":"rak-KO-lje-re FON-di","ex":"Stiamo raccogliendo fondi per la scuola.","exNl":"We zamelen geld in voor de school.","lesson":246,"level":"B1","cat":"espressione"},
  {"id":"w2218","it":"la beneficenza","nl":"de liefdadigheid","ph":"be-ne-fi-TSHEN-tsa","ex":"La cena è per beneficenza.","exNl":"Het diner is voor het goede doel.","lesson":246,"level":"B1","cat":"sostantivo"},

  # ── Les 247: Religie & geloof ──
  {"id":"w2219","it":"la religione","nl":"de religie, het geloof","ph":"re-li-DJO-ne","ex":"In Italia la religione più diffusa è il cattolicesimo.","exNl":"In Italië is het katholicisme de meest verspreide religie.","lesson":247,"level":"B1","cat":"sostantivo"},
  {"id":"w2220","it":"la chiesa","nl":"de kerk","ph":"KJE-za","ex":"La chiesa del paese è molto antica.","exNl":"De dorpskerk is heel oud.","lesson":247,"level":"B1","cat":"sostantivo"},
  {"id":"w2221","it":"il Papa","nl":"de paus","ph":"PA-pa","ex":"Il Papa vive in Vaticano.","exNl":"De paus woont in het Vaticaan.","lesson":247,"level":"B1","cat":"sostantivo"},
  {"id":"w2222","it":"pregare","nl":"bidden","ph":"pre-GA-re","ex":"Molte persone pregano ogni giorno.","exNl":"Veel mensen bidden elke dag.","lesson":247,"level":"B1","cat":"verbo"},
  {"id":"w2223","it":"la fede","nl":"het geloof","ph":"FE-de","ex":"La fede è una questione personale.","exNl":"Geloof is een persoonlijke zaak.","lesson":247,"level":"B1","cat":"sostantivo"},
  {"id":"w2224","it":"sacro","nl":"heilig, sacraal","ph":"SA-kro","ex":"Questo è un luogo sacro.","exNl":"Dit is een heilige plek.","lesson":247,"level":"B1","cat":"aggettivo"},
  {"id":"w2225","it":"il santo","nl":"de heilige","ph":"SAN-to","ex":"San Francesco è il patrono d'Italia.","exNl":"Sint Franciscus is de beschermheilige van Italië.","lesson":247,"level":"B1","cat":"sostantivo"},
  {"id":"w2226","it":"la cerimonia","nl":"de ceremonie, de plechtigheid","ph":"tshe-ri-MO-nja","ex":"La cerimonia è stata molto commovente.","exNl":"De plechtigheid was heel ontroerend.","lesson":247,"level":"B1","cat":"sostantivo"},

  # ── Les 248: Gelijkheid & diversiteit ──
  {"id":"w2227","it":"la parità","nl":"de gelijkheid","ph":"pa-ri-TA","ex":"Lavoriamo per la parità di genere.","exNl":"We werken aan gendergelijkheid.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2228","it":"la discriminazione","nl":"de discriminatie","ph":"dis-kri-mi-na-TSJO-ne","ex":"La discriminazione è vietata dalla legge.","exNl":"Discriminatie is bij wet verboden.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2229","it":"i diritti umani","nl":"de mensenrechten","ph":"di-RIT-ti u-MA-ni","ex":"I diritti umani sono universali.","exNl":"Mensenrechten zijn universeel.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2230","it":"l'inclusione","nl":"de inclusie","ph":"in-klu-ZJO-ne","ex":"L'inclusione sociale è fondamentale.","exNl":"Sociale inclusie is fundamenteel.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2231","it":"il rispetto","nl":"het respect","ph":"ris-PET-to","ex":"Il rispetto reciproco è la base della convivenza.","exNl":"Wederzijds respect is de basis van samenleven.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2232","it":"la tolleranza","nl":"de tolerantie","ph":"tol-le-RAN-tsa","ex":"La tolleranza è un valore civile.","exNl":"Tolerantie is een burgerlijke waarde.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2233","it":"la minoranza","nl":"de minderheid","ph":"mi-no-RAN-tsa","ex":"I diritti delle minoranze vanno tutelati.","exNl":"De rechten van minderheden moeten beschermd worden.","lesson":248,"level":"B1","cat":"sostantivo"},
  {"id":"w2234","it":"lottare","nl":"strijden, vechten","ph":"lot-TA-re","ex":"Lottiamo per i nostri diritti.","exNl":"We strijden voor onze rechten.","lesson":248,"level":"B1","cat":"verbo"},

  # ── Les 249: Oorlog & vrede ──
  {"id":"w2235","it":"il conflitto","nl":"het conflict","ph":"kon-FLIT-to","ex":"Il conflitto è durato anni.","exNl":"Het conflict duurde jaren.","lesson":249,"level":"B1","cat":"sostantivo"},
  {"id":"w2236","it":"il trattato","nl":"het verdrag","ph":"trat-TA-to","ex":"Hanno firmato un trattato di pace.","exNl":"Ze hebben een vredesverdrag getekend.","lesson":249,"level":"B1","cat":"sostantivo"},
  {"id":"w2237","it":"la diplomazia","nl":"de diplomatie","ph":"di-plo-ma-TSI-a","ex":"La diplomazia è importante per la pace.","exNl":"Diplomatie is belangrijk voor de vrede.","lesson":249,"level":"B1","cat":"sostantivo"},
  {"id":"w2238","it":"negoziare","nl":"onderhandelen","ph":"ne-go-TSJA-re","ex":"I due paesi stanno negoziando.","exNl":"De twee landen zijn aan het onderhandelen.","lesson":249,"level":"B1","cat":"verbo"},
  {"id":"w2239","it":"l'alleato","nl":"de bondgenoot","ph":"al-le-A-to","ex":"L'Italia è un alleato della NATO.","exNl":"Italië is een bondgenoot van de NAVO.","lesson":249,"level":"B1","cat":"sostantivo"},
  {"id":"w2240","it":"il profugo","nl":"de ontheemde","ph":"PRO-fu-go","ex":"Milioni di profughi hanno lasciato il paese.","exNl":"Miljoenen ontheemden hebben het land verlaten.","lesson":249,"level":"B1","cat":"sostantivo"},
  {"id":"w2241","it":"la tregua","nl":"het bestand, de wapenstilstand","ph":"TRE-gwa","ex":"Le parti hanno concordato una tregua.","exNl":"De partijen zijn een wapenstilstand overeengekomen.","lesson":249,"level":"B1","cat":"sostantivo"},
  {"id":"w2242","it":"la cooperazione","nl":"de samenwerking","ph":"ko-o-pe-ra-TSJO-ne","ex":"La cooperazione internazionale è essenziale.","exNl":"Internationale samenwerking is essentieel.","lesson":249,"level":"B1","cat":"sostantivo"},

  # ── Les 250: Toetsles Blok 13 ──
  {"id":"w2243","it":"la società","nl":"de maatschappij, de samenleving","ph":"so-tsje-TA","ex":"La società è in continuo cambiamento.","exNl":"De samenleving verandert voortdurend.","lesson":250,"level":"B1","cat":"sostantivo"},
  {"id":"w2244","it":"il valore","nl":"de waarde","ph":"va-LO-re","ex":"La libertà è un valore fondamentale.","exNl":"Vrijheid is een fundamentele waarde.","lesson":250,"level":"B1","cat":"sostantivo"},
  {"id":"w2245","it":"il principio","nl":"het beginsel, het principe","ph":"prin-TSI-pjo","ex":"Il principio di uguaglianza è nella Costituzione.","exNl":"Het beginsel van gelijkheid staat in de grondwet.","lesson":250,"level":"B1","cat":"sostantivo"},
  {"id":"w2246","it":"la giustizia","nl":"de gerechtigheid, het recht","ph":"djus-TI-tsja","ex":"La giustizia deve essere uguale per tutti.","exNl":"Gerechtigheid moet gelijk zijn voor iedereen.","lesson":250,"level":"B1","cat":"sostantivo"},
  {"id":"w2247","it":"tutelare","nl":"beschermen (juridisch)","ph":"tu-te-LA-re","ex":"Lo Stato tutela i diritti dei cittadini.","exNl":"De staat beschermt de rechten van de burgers.","lesson":250,"level":"B1","cat":"verbo"},
  {"id":"w2248","it":"la riforma","nl":"de hervorming","ph":"ri-FOR-ma","ex":"La riforma scolastica è stata approvata.","exNl":"De onderwijshervorming is goedgekeurd.","lesson":250,"level":"B1","cat":"sostantivo"},
  {"id":"w2249","it":"il compromesso","nl":"het compromis","ph":"kom-pro-MES-so","ex":"In politica il compromesso è necessario.","exNl":"In de politiek is een compromis noodzakelijk.","lesson":250,"level":"B1","cat":"sostantivo"},
  {"id":"w2250","it":"la stabilità","nl":"de stabiliteit","ph":"sta-bi-li-TA","ex":"La stabilità politica è importante per l'economia.","exNl":"Politieke stabiliteit is belangrijk voor de economie.","lesson":250,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 14: Zakelijk Italiaans (lessen 251–260)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":251,"title":"Solliciteren — verdieping","emoji":"📝","level":"B1",
   "description":"Verdieping in sollicitatiebrieven en CV's.",
   "grammar":{"title":"Formele briefconventies",
   "body":"Een formele Italiaanse brief begint met:\n\nEgregio/a Dott./Dott.ssa… — Geachte heer/mevrouw dr. …\nSpett.le Azienda — Geachte firma\n\nEn eindigt met:\nIn attesa di un Suo cortese riscontro, porgo distinti saluti.\n— In afwachting van uw antwoord, met vriendelijke groet."},
   "words":["w2251","w2252","w2253","w2254","w2255","w2256","w2257","w2258"]},

  {"id":252,"title":"Het sollicitatiegesprek","emoji":"🤝","level":"B1",
   "description":"Woorden en zinnen voor een sollicitatiegesprek.",
   "grammar":{"title":"Sollicitatiegesprek",
   "body":"Veelgestelde vragen bij een colloquio:\n\nMi parli di sé. — Vertel eens over uzelf.\nQuali sono i Suoi punti di forza? — Wat zijn uw sterke punten?\nDove si vede tra cinque anni? — Waar ziet u zichzelf over vijf jaar?\nPerché vuole lavorare per noi? — Waarom wilt u voor ons werken?"},
   "words":["w2259","w2260","w2261","w2262","w2263","w2264","w2265","w2266"]},

  {"id":253,"title":"Vergaderen — verdieping","emoji":"📊","level":"B1",
   "description":"Verdieping in vergadertaal en presentaties.",
   "grammar":{"title":"Vergaderen in het Italiaans",
   "body":"Vergaderingen leiden:\n\nApriamo la riunione. — We openen de vergadering.\nPassiamo al punto successivo. — We gaan naar het volgende punt.\nQualcuno ha domande? — Heeft iemand vragen?\nRiassumiamo i punti principali. — We vatten de hoofdpunten samen.\nLa riunione è aggiornata a… — De vergadering is verdaagd naar…"},
   "words":["w2267","w2268","w2269","w2270","w2271","w2272","w2273","w2274"]},

  {"id":254,"title":"Presentaties geven","emoji":"📈","level":"B1",
   "description":"Woorden voor het geven van een presentatie.",
   "grammar":{"title":"Een presentatie structureren",
   "body":"Structuurzinnen voor presentaties:\n\nOggi vorrei parlare di… — Vandaag wil ik het hebben over…\nCome potete vedere dal grafico… — Zoals u kunt zien op de grafiek…\nIn conclusione… — Ter afsluiting…\nCi sono domande? — Zijn er vragen?\nGrazie per l'attenzione. — Dank voor uw aandacht."},
   "words":["w2275","w2276","w2277","w2278","w2279","w2280","w2281","w2282"]},

  {"id":255,"title":"E-mails & brieven","emoji":"✉️","level":"B1",
   "description":"Formele en informele e-mails schrijven.",
   "grammar":{"title":"Formele e-mails",
   "body":"Structuur van een formele Italiaanse e-mail:\n\nOggetto: Richiesta informazioni — Onderwerp: Informatieverzoek\n\nEgregio Dott. Rossi,\nLe scrivo per… — Ik schrijf u om…\nIn allegato troverà… — In de bijlage vindt u…\nResto a disposizione per… — Ik sta ter beschikking voor…\nCordiali saluti — Met vriendelijke groet"},
   "words":["w2283","w2284","w2285","w2286","w2287","w2288","w2289","w2290"]},

  {"id":256,"title":"Onderhandelen","emoji":"🤝","level":"B1",
   "description":"Woorden en uitdrukkingen voor onderhandeling.",
   "grammar":{"title":"Onderhandelingstaal",
   "body":"Nuttige onderhandelingsuitdrukkingen:\n\nLa nostra proposta è… — Ons voorstel is…\nSiamo disposti a… — We zijn bereid om…\nA quale prezzo? — Tegen welke prijs?\nPossiamo trovare un compromesso? — Kunnen we een compromis vinden?\nAffare fatto! — Deal!"},
   "words":["w2291","w2292","w2293","w2294","w2295","w2296","w2297","w2298"]},

  {"id":257,"title":"Bedrijfscultuur","emoji":"🏢","level":"B1",
   "description":"Woorden over Italiaanse bedrijfscultuur.",
   "grammar":{"title":"Italiaanse bedrijfscultuur",
   "body":"Kenmerken van de Italiaanse bedrijfscultuur:\n\n• Persoonlijke relaties zijn heel belangrijk\n• Formeel taalgebruik (Lei) in zakelijke context\n• La pausa pranzo — de lunchpauze is vaak langer (1–2 uur)\n• Puntualità — stiptheid wordt gewaardeerd maar flexibel toegepast\n• Il networking — zakelijke relaties opbouwen via informele contacten"},
   "words":["w2299","w2300","w2301","w2302","w2303","w2304","w2305","w2306"]},

  {"id":258,"title":"Import & export","emoji":"🚢","level":"B1",
   "description":"Woorden over internationale handel.",
   "grammar":{"title":"Handelstaal",
   "body":"'Made in Italy' is een sterk merk. Belangrijke exportsectoren:\n\nla moda — de mode\nl'alimentare — de voedingsindustrie\nil design — het design\nl'automotive — de auto-industrie\nla meccanica — de machinebouw\n\nL'Italia è il secondo paese manifatturiero d'Europa. — Italië is het tweede productieland van Europa."},
   "words":["w2307","w2308","w2309","w2310","w2311","w2312","w2313","w2314"]},

  {"id":259,"title":"Klantenservice","emoji":"📞","level":"B1",
   "description":"Woorden voor klantenservice en klachten.",
   "grammar":{"title":"Klantenservice",
   "body":"Veelgebruikte zinnen:\n\nBuongiorno, come posso aiutarLa? — Goedendag, hoe kan ik u helpen?\nVorrei fare un reclamo. — Ik wil een klacht indienen.\nIl prodotto è difettoso. — Het product is defect.\nVorrei un rimborso. — Ik wil mijn geld terug.\nPosso parlare con il responsabile? — Kan ik de verantwoordelijke spreken?"},
   "words":["w2315","w2316","w2317","w2318","w2319","w2320","w2321","w2322"]},

  {"id":260,"title":"Toetsles B1 — Blok 14","emoji":"📋","level":"B1",
   "description":"Toets over lessen 251–260: zakelijk Italiaans.",
   "grammar":{"title":"Toetsles B1 — Blok 14 (les 251–260)","body":"In dit blok heb je geleerd:\n• Formele brieven en e-mails schrijven\n• Solliciteren en presenteren\n• Onderhandelen en vergaderen\n• Bedrijfscultuur en internationale handel"},
   "words":["w2323","w2324","w2325","w2326","w2327","w2328","w2329","w2330"]},
]

WORDS += [
  # ── Les 251: Solliciteren — verdieping ──
  {"id":"w2251","it":"il curriculum vitae","nl":"het cv","ph":"kur-RI-ku-lum VI-te","ex":"Ho aggiornato il mio curriculum vitae.","exNl":"Ik heb mijn cv bijgewerkt.","lesson":251,"level":"B1","cat":"sostantivo"},
  {"id":"w2252","it":"la lettera di presentazione","nl":"de sollicitatiebrief","ph":"LET-te-ra di pre-zen-ta-TSJO-ne","ex":"La lettera di presentazione è molto importante.","exNl":"De sollicitatiebrief is heel belangrijk.","lesson":251,"level":"B1","cat":"sostantivo"},
  {"id":"w2253","it":"l'esperienza lavorativa","nl":"de werkervaring","ph":"es-pe-RJEN-tsa la-vo-ra-TI-va","ex":"Ho cinque anni di esperienza lavorativa.","exNl":"Ik heb vijf jaar werkervaring.","lesson":251,"level":"B1","cat":"sostantivo"},
  {"id":"w2254","it":"la competenza","nl":"de competentie, de vaardigheid","ph":"kom-pe-TEN-tsa","ex":"Le mie competenze includono la gestione di progetti.","exNl":"Mijn competenties omvatten projectmanagement.","lesson":251,"level":"B1","cat":"sostantivo"},
  {"id":"w2255","it":"candidarsi","nl":"solliciteren, zich kandidaat stellen","ph":"kan-di-DAR-si","ex":"Mi candido per la posizione di manager.","exNl":"Ik solliciteer naar de functie van manager.","lesson":251,"level":"B1","cat":"verbo"},
  {"id":"w2256","it":"l'annuncio di lavoro","nl":"de vacature","ph":"an-NUN-tsjo di la-VO-ro","ex":"Ho visto un annuncio di lavoro interessante.","exNl":"Ik heb een interessante vacature gezien.","lesson":251,"level":"B1","cat":"sostantivo"},
  {"id":"w2257","it":"assumere","nl":"aannemen (personeel)","ph":"as-SU-me-re","ex":"L'azienda ha assunto dieci nuovi dipendenti.","exNl":"Het bedrijf heeft tien nieuwe werknemers aangenomen.","lesson":251,"level":"B1","cat":"verbo"},
  {"id":"w2258","it":"il colloquio","nl":"het sollicitatiegesprek","ph":"kol-LO-kwjo","ex":"Ho un colloquio di lavoro domani.","exNl":"Ik heb morgen een sollicitatiegesprek.","lesson":251,"level":"B1","cat":"sostantivo"},

  # ── Les 252: Het sollicitatiegesprek ──
  {"id":"w2259","it":"il punto di forza","nl":"het sterke punt","ph":"PUN-to di FOR-tsa","ex":"Il mio punto di forza è la comunicazione.","exNl":"Mijn sterke punt is communicatie.","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2260","it":"il punto debole","nl":"het zwakke punt","ph":"PUN-to DE-bo-le","ex":"Il mio punto debole è la puntualità.","exNl":"Mijn zwakke punt is stiptheid.","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2261","it":"lo stipendio","nl":"het salaris","ph":"sti-PEN-djo","ex":"Qual è lo stipendio per questa posizione?","exNl":"Wat is het salaris voor deze functie?","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2262","it":"il contratto a tempo indeterminato","nl":"het vast contract","ph":"kon-TRAT-to in-de-ter-mi-NA-to","ex":"Spero di ottenere un contratto a tempo indeterminato.","exNl":"Ik hoop een vast contract te krijgen.","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2263","it":"la formazione","nl":"de opleiding, de training","ph":"for-ma-TSJO-ne","ex":"L'azienda offre formazione continua.","exNl":"Het bedrijf biedt doorlopende opleiding.","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2264","it":"il turno","nl":"de dienst (werk)","ph":"TUR-no","ex":"Lavoro a turni.","exNl":"Ik werk in diensten.","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2265","it":"le ferie","nl":"de vakantie(dagen)","ph":"FE-rje","ex":"Ho venti giorni di ferie all'anno.","exNl":"Ik heb twintig vakantiedagen per jaar.","lesson":252,"level":"B1","cat":"sostantivo"},
  {"id":"w2266","it":"la mansione","nl":"de taak, de functie","ph":"man-SJO-ne","ex":"Le mie mansioni includono la gestione del personale.","exNl":"Mijn taken omvatten personeelsmanagement.","lesson":252,"level":"B1","cat":"sostantivo"},

  # ── Les 253: Vergaderen — verdieping ──
  {"id":"w2267","it":"la riunione","nl":"de vergadering","ph":"ri-u-NJO-ne","ex":"La riunione è alle dieci.","exNl":"De vergadering is om tien uur.","lesson":253,"level":"B1","cat":"sostantivo"},
  {"id":"w2268","it":"l'ordine del giorno","nl":"de agenda (vergadering)","ph":"OR-di-ne del DJOR-no","ex":"Ecco l'ordine del giorno di oggi.","exNl":"Hier is de agenda van vandaag.","lesson":253,"level":"B1","cat":"sostantivo"},
  {"id":"w2269","it":"il verbale","nl":"de notulen","ph":"ver-BA-le","ex":"Chi scrive il verbale della riunione?","exNl":"Wie schrijft de notulen van de vergadering?","lesson":253,"level":"B1","cat":"sostantivo"},
  {"id":"w2270","it":"intervenire","nl":"het woord nemen, ingrijpen","ph":"in-ter-ve-NI-re","ex":"Posso intervenire su questo punto?","exNl":"Mag ik hier iets over zeggen?","lesson":253,"level":"B1","cat":"verbo"},
  {"id":"w2271","it":"la scadenza","nl":"de deadline","ph":"ska-DEN-tsa","ex":"La scadenza del progetto è venerdì.","exNl":"De deadline van het project is vrijdag.","lesson":253,"level":"B1","cat":"sostantivo"},
  {"id":"w2272","it":"il progetto","nl":"het project","ph":"pro-DJET-to","ex":"Stiamo lavorando a un nuovo progetto.","exNl":"We werken aan een nieuw project.","lesson":253,"level":"B1","cat":"sostantivo"},
  {"id":"w2273","it":"proporre","nl":"voorstellen","ph":"pro-POR-re","ex":"Propongo di posticipare la scadenza.","exNl":"Ik stel voor om de deadline uit te stellen.","lesson":253,"level":"B1","cat":"verbo"},
  {"id":"w2274","it":"approvare","nl":"goedkeuren","ph":"ap-pro-VA-re","ex":"Il direttore ha approvato il budget.","exNl":"De directeur heeft het budget goedgekeurd.","lesson":253,"level":"B1","cat":"verbo"},

  # ── Les 254: Presentaties geven ──
  {"id":"w2275","it":"la presentazione","nl":"de presentatie","ph":"pre-zen-ta-TSJO-ne","ex":"La presentazione dura venti minuti.","exNl":"De presentatie duurt twintig minuten.","lesson":254,"level":"B1","cat":"sostantivo"},
  {"id":"w2276","it":"la diapositiva","nl":"de slide, de dia","ph":"dja-po-zi-TI-va","ex":"Ho preparato venti diapositive.","exNl":"Ik heb twintig slides voorbereid.","lesson":254,"level":"B1","cat":"sostantivo"},
  {"id":"w2277","it":"il grafico","nl":"de grafiek","ph":"GRA-fi-ko","ex":"Come potete vedere dal grafico…","exNl":"Zoals u kunt zien op de grafiek…","lesson":254,"level":"B1","cat":"sostantivo"},
  {"id":"w2278","it":"i dati","nl":"de gegevens, de data","ph":"DA-ti","ex":"I dati dimostrano un aumento.","exNl":"De gegevens tonen een toename.","lesson":254,"level":"B1","cat":"sostantivo"},
  {"id":"w2279","it":"riassumere","nl":"samenvatten","ph":"rjas-SU-me-re","ex":"Riassumo i punti principali.","exNl":"Ik vat de hoofdpunten samen.","lesson":254,"level":"B1","cat":"verbo"},
  {"id":"w2280","it":"sottolineare","nl":"benadrukken, onderstrepen","ph":"sot-to-li-ne-A-re","ex":"Vorrei sottolineare l'importanza di…","exNl":"Ik wil het belang van … benadrukken.","lesson":254,"level":"B1","cat":"verbo"},
  {"id":"w2281","it":"la conclusione","nl":"de conclusie","ph":"kon-klu-ZJO-ne","ex":"In conclusione, il progetto è un successo.","exNl":"Tot slot, het project is een succes.","lesson":254,"level":"B1","cat":"sostantivo"},
  {"id":"w2282","it":"illustrare","nl":"illustreren, toelichten","ph":"il-lus-TRA-re","ex":"Il grafico illustra i risultati.","exNl":"De grafiek illustreert de resultaten.","lesson":254,"level":"B1","cat":"verbo"},

  # ── Les 255: E-mails & brieven ──
  {"id":"w2283","it":"l'allegato","nl":"de bijlage","ph":"al-le-GA-to","ex":"In allegato troverà il documento richiesto.","exNl":"In de bijlage vindt u het gevraagde document.","lesson":255,"level":"B1","cat":"sostantivo"},
  {"id":"w2284","it":"l'oggetto","nl":"het onderwerp (e-mail)","ph":"od-DJET-to","ex":"Inserisci l'oggetto dell'email.","exNl":"Vul het onderwerp van de e-mail in.","lesson":255,"level":"B1","cat":"sostantivo"},
  {"id":"w2285","it":"cordiali saluti","nl":"met vriendelijke groet","ph":"kor-DJA-li sa-LU-ti","ex":"Cordiali saluti, Marco Rossi.","exNl":"Met vriendelijke groet, Marco Rossi.","lesson":255,"level":"B1","cat":"espressione"},
  {"id":"w2286","it":"in attesa di","nl":"in afwachting van","ph":"in at-TE-za di","ex":"In attesa di una Sua risposta.","exNl":"In afwachting van uw antwoord.","lesson":255,"level":"B1","cat":"espressione"},
  {"id":"w2287","it":"la richiesta","nl":"het verzoek","ph":"ri-KJES-ta","ex":"Le scrivo in merito alla Sua richiesta.","exNl":"Ik schrijf u met betrekking tot uw verzoek.","lesson":255,"level":"B1","cat":"sostantivo"},
  {"id":"w2288","it":"confermare","nl":"bevestigen","ph":"kon-fer-MA-re","ex":"Le confermo l'appuntamento per martedì.","exNl":"Ik bevestig de afspraak voor dinsdag.","lesson":255,"level":"B1","cat":"verbo"},
  {"id":"w2289","it":"inoltrare","nl":"doorsturen","ph":"i-nol-TRA-re","ex":"Le inoltro l'email del collega.","exNl":"Ik stuur u de e-mail van de collega door.","lesson":255,"level":"B1","cat":"verbo"},
  {"id":"w2290","it":"il destinatario","nl":"de ontvanger","ph":"des-ti-na-TA-rjo","ex":"Chi è il destinatario della lettera?","exNl":"Wie is de ontvanger van de brief?","lesson":255,"level":"B1","cat":"sostantivo"},

  # ── Les 256: Onderhandelen ──
  {"id":"w2291","it":"la trattativa","nl":"de onderhandeling","ph":"trat-ta-TI-va","ex":"Le trattative sono in corso.","exNl":"De onderhandelingen zijn gaande.","lesson":256,"level":"B1","cat":"sostantivo"},
  {"id":"w2292","it":"la proposta","nl":"het voorstel","ph":"pro-POS-ta","ex":"La nostra proposta è vantaggiosa.","exNl":"Ons voorstel is voordelig.","lesson":256,"level":"B1","cat":"sostantivo"},
  {"id":"w2293","it":"l'offerta","nl":"de aanbieding, het aanbod","ph":"of-FER-ta","ex":"Abbiamo ricevuto un'offerta interessante.","exNl":"We hebben een interessant aanbod ontvangen.","lesson":256,"level":"B1","cat":"sostantivo"},
  {"id":"w2294","it":"lo sconto","nl":"de korting","ph":"SKON-to","ex":"Possiamo offrire uno sconto del 10%.","exNl":"We kunnen een korting van 10% bieden.","lesson":256,"level":"B1","cat":"sostantivo"},
  {"id":"w2295","it":"accettare","nl":"accepteren, aanvaarden","ph":"at-tshet-TA-re","ex":"Accettiamo la vostra proposta.","exNl":"We aanvaarden jullie voorstel.","lesson":256,"level":"B1","cat":"verbo"},
  {"id":"w2296","it":"rifiutare","nl":"weigeren, afwijzen","ph":"ri-fju-TA-re","ex":"Purtroppo dobbiamo rifiutare l'offerta.","exNl":"Helaas moeten we het aanbod afwijzen.","lesson":256,"level":"B1","cat":"verbo"},
  {"id":"w2297","it":"la condizione","nl":"de voorwaarde","ph":"kon-di-TSJO-ne","ex":"Accettiamo a queste condizioni.","exNl":"We accepteren onder deze voorwaarden.","lesson":256,"level":"B1","cat":"sostantivo"},
  {"id":"w2298","it":"l'accordo","nl":"de overeenkomst, het akkoord","ph":"ak-KOR-do","ex":"Abbiamo raggiunto un accordo.","exNl":"We hebben een akkoord bereikt.","lesson":256,"level":"B1","cat":"sostantivo"},

  # ── Les 257: Bedrijfscultuur ──
  {"id":"w2299","it":"l'azienda","nl":"het bedrijf","ph":"a-TSJEN-da","ex":"L'azienda ha sede a Milano.","exNl":"Het bedrijf heeft zijn hoofdkantoor in Milaan.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2300","it":"il direttore","nl":"de directeur","ph":"di-ret-TO-re","ex":"Il direttore generale dirige l'azienda.","exNl":"De algemeen directeur leidt het bedrijf.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2301","it":"il dipendente","nl":"de werknemer","ph":"di-pen-DEN-te","ex":"L'azienda ha duecento dipendenti.","exNl":"Het bedrijf heeft tweehonderd werknemers.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2302","it":"il collega","nl":"de collega","ph":"kol-LE-ga","ex":"Vado a pranzo con i colleghi.","exNl":"Ik ga lunchen met collega's.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2303","it":"la sede","nl":"het hoofdkantoor, de vestiging","ph":"SE-de","ex":"La sede centrale è a Roma.","exNl":"Het hoofdkantoor is in Rome.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2304","it":"il fatturato","nl":"de omzet","ph":"fat-tu-RA-to","ex":"Il fatturato è cresciuto del 15%.","exNl":"De omzet is met 15% gegroeid.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2305","it":"la produttività","nl":"de productiviteit","ph":"pro-dut-ti-vi-TA","ex":"La produttività è aumentata.","exNl":"De productiviteit is gestegen.","lesson":257,"level":"B1","cat":"sostantivo"},
  {"id":"w2306","it":"gestire","nl":"beheren, managen","ph":"djes-TI-re","ex":"Gestisce un team di dieci persone.","exNl":"Hij beheert een team van tien personen.","lesson":257,"level":"B1","cat":"verbo"},

  # ── Les 258: Import & export ──
  {"id":"w2307","it":"la merce","nl":"de goederen, de koopwaar","ph":"MER-tsje","ex":"La merce è stata spedita ieri.","exNl":"De goederen zijn gisteren verzonden.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2308","it":"la spedizione","nl":"de verzending","ph":"spe-di-TSJO-ne","ex":"La spedizione arriva tra tre giorni.","exNl":"De verzending komt over drie dagen aan.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2309","it":"la dogana","nl":"de douane","ph":"do-GA-na","ex":"La merce è bloccata in dogana.","exNl":"De goederen worden vastgehouden bij de douane.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2310","it":"la fattura","nl":"de factuur","ph":"fat-TU-ra","ex":"Le invio la fattura in allegato.","exNl":"Ik stuur u de factuur in de bijlage.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2311","it":"il fornitore","nl":"de leverancier","ph":"for-ni-TO-re","ex":"Abbiamo cambiato fornitore.","exNl":"We zijn van leverancier gewisseld.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2312","it":"il cliente","nl":"de klant","ph":"kli-EN-te","ex":"Il cliente ha sempre ragione.","exNl":"De klant heeft altijd gelijk.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2313","it":"l'ordine","nl":"de bestelling","ph":"OR-di-ne","ex":"Abbiamo ricevuto un grande ordine.","exNl":"We hebben een grote bestelling ontvangen.","lesson":258,"level":"B1","cat":"sostantivo"},
  {"id":"w2314","it":"consegnare","nl":"leveren, bezorgen","ph":"kon-se-NJA-re","ex":"La merce verrà consegnata lunedì.","exNl":"De goederen worden maandag geleverd.","lesson":258,"level":"B1","cat":"verbo"},

  # ── Les 259: Klantenservice ──
  {"id":"w2315","it":"il reclamo","nl":"de klacht","ph":"re-KLA-mo","ex":"Vorrei fare un reclamo.","exNl":"Ik wil een klacht indienen.","lesson":259,"level":"B1","cat":"sostantivo"},
  {"id":"w2316","it":"il rimborso","nl":"de terugbetaling","ph":"rim-BOR-so","ex":"Vorrei richiedere un rimborso.","exNl":"Ik wil een terugbetaling aanvragen.","lesson":259,"level":"B1","cat":"sostantivo"},
  {"id":"w2317","it":"difettoso","nl":"defect, gebrekkig","ph":"di-fet-TO-zo","ex":"Il prodotto è difettoso.","exNl":"Het product is defect.","lesson":259,"level":"B1","cat":"aggettivo"},
  {"id":"w2318","it":"sostituire","nl":"vervangen","ph":"sos-ti-tu-I-re","ex":"Possiamo sostituire il prodotto.","exNl":"We kunnen het product vervangen.","lesson":259,"level":"B1","cat":"verbo"},
  {"id":"w2319","it":"la garanzia","nl":"de garantie","ph":"ga-ran-TSI-a","ex":"Il prodotto è ancora in garanzia.","exNl":"Het product valt nog onder de garantie.","lesson":259,"level":"B1","cat":"sostantivo"},
  {"id":"w2320","it":"il servizio clienti","nl":"de klantenservice","ph":"ser-VI-tsjo kli-EN-ti","ex":"Chiama il servizio clienti per assistenza.","exNl":"Bel de klantenservice voor hulp.","lesson":259,"level":"B1","cat":"sostantivo"},
  {"id":"w2321","it":"risolvere","nl":"oplossen","ph":"ri-ZOL-ve-re","ex":"Cercheremo di risolvere il problema.","exNl":"We zullen proberen het probleem op te lossen.","lesson":259,"level":"B1","cat":"verbo"},
  {"id":"w2322","it":"soddisfatto","nl":"tevreden","ph":"sod-dis-FAT-to","ex":"Il cliente è soddisfatto del servizio.","exNl":"De klant is tevreden over de service.","lesson":259,"level":"B1","cat":"aggettivo"},

  # ── Les 260: Toetsles Blok 14 ──
  {"id":"w2323","it":"la strategia","nl":"de strategie","ph":"stra-te-DJI-a","ex":"La strategia aziendale è chiara.","exNl":"De bedrijfsstrategie is duidelijk.","lesson":260,"level":"B1","cat":"sostantivo"},
  {"id":"w2324","it":"l'obiettivo aziendale","nl":"de bedrijfsdoelstelling","ph":"o-bjet-TI-vo a-tsjen-DA-le","ex":"Abbiamo raggiunto i nostri obiettivi aziendali.","exNl":"We hebben onze bedrijfsdoelstellingen bereikt.","lesson":260,"level":"B1","cat":"sostantivo"},
  {"id":"w2325","it":"la concorrenza","nl":"de concurrentie","ph":"kon-kor-REN-tsa","ex":"La concorrenza è molto forte.","exNl":"De concurrentie is heel sterk.","lesson":260,"level":"B1","cat":"sostantivo"},
  {"id":"w2326","it":"il mercato","nl":"de markt","ph":"mer-KA-to","ex":"Il mercato italiano è in crescita.","exNl":"De Italiaanse markt groeit.","lesson":260,"level":"B1","cat":"sostantivo"},
  {"id":"w2327","it":"la qualità","nl":"de kwaliteit","ph":"kwa-li-TA","ex":"La qualità dei prodotti italiani è rinomata.","exNl":"De kwaliteit van Italiaanse producten is vermaard.","lesson":260,"level":"B1","cat":"sostantivo"},
  {"id":"w2328","it":"innovare","nl":"innoveren, vernieuwen","ph":"in-no-VA-re","ex":"Bisogna innovare per restare competitivi.","exNl":"Je moet innoveren om concurrerend te blijven.","lesson":260,"level":"B1","cat":"verbo"},
  {"id":"w2329","it":"la crescita","nl":"de groei","ph":"KRESH-i-ta","ex":"La crescita dell'azienda è costante.","exNl":"De groei van het bedrijf is constant.","lesson":260,"level":"B1","cat":"sostantivo"},
  {"id":"w2330","it":"efficiente","nl":"efficiënt","ph":"ef-fi-TSHEN-te","ex":"Il servizio è molto efficiente.","exNl":"De service is heel efficiënt.","lesson":260,"level":"B1","cat":"aggettivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 15: Gezondheid & wetenschap (lessen 261–270)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":261,"title":"In het ziekenhuis","emoji":"🏥","level":"B1",
   "description":"Woordenschat voor het ziekenhuis en medische situaties.",
   "grammar":{"title":"Imperativo formale voor instructies",
   "body":"Artsen en verpleegkundigen gebruiken de formele gebiedende wijs (Lei-vorm = congiuntivo presente):\n\nSi sieda, per favore. — Gaat u zitten, alstublieft.\nPrenda questa medicina. — Neem dit medicijn.\nRisposi profondamente. — Adem diep in.\nNon si preoccupi. — Maakt u zich geen zorgen."},
   "words":["w2331","w2332","w2333","w2334","w2335","w2336","w2337","w2338"]},

  {"id":262,"title":"De apotheek","emoji":"💊","level":"B1",
   "description":"Woorden voor de apotheek en medicijnen.",
   "grammar":{"title":"Bij de apotheek",
   "body":"Nuttige zinnen:\n\nHo bisogno di un farmaco per… — Ik heb een medicijn nodig voor…\nÈ senza ricetta? — Is het zonder recept?\nQuante volte al giorno? — Hoe vaak per dag?\nPrima o dopo i pasti? — Voor of na de maaltijden?\nHa qualcosa per il mal di testa? — Heeft u iets tegen hoofdpijn?"},
   "words":["w2339","w2340","w2341","w2342","w2343","w2344","w2345","w2346"]},

  {"id":263,"title":"Geestelijke gezondheid","emoji":"🧠","level":"B1",
   "description":"Woorden over geestelijke gezondheid en welzijn.",
   "grammar":{"title":"Over geestelijke gezondheid praten",
   "body":"Nuttige uitdrukkingen:\n\nSoffrire di ansia / depressione — Lijden aan angst / depressie\nAndare dallo psicologo — Naar de psycholoog gaan\nChiedere aiuto — Hulp vragen\nStare meglio / peggio — Het beter / slechter hebben\nLa salute mentale è importante quanto quella fisica. — Geestelijke gezondheid is net zo belangrijk als lichamelijke."},
   "words":["w2347","w2348","w2349","w2350","w2351","w2352","w2353","w2354"]},

  {"id":264,"title":"Eerste hulp","emoji":"🚑","level":"B1",
   "description":"Woorden en uitdrukkingen voor noodsituaties.",
   "grammar":{"title":"Noodsituaties",
   "body":"Noodgevallen in Italië:\n\nil numero di emergenza: 112 (Europees) of 118 (ambulanza)\n\nChiamate un'ambulanza! — Bel een ambulance!\nC'è stato un incidente! — Er is een ongeluk gebeurd!\nDov'è il pronto soccorso? — Waar is de eerste hulp?\nÈ urgente! — Het is dringend!"},
   "words":["w2355","w2356","w2357","w2358","w2359","w2360","w2361","w2362"]},

  {"id":265,"title":"Wetenschap — basis","emoji":"🔬","level":"B1",
   "description":"Basiswoorden over wetenschap en onderzoek.",
   "grammar":{"title":"Over wetenschap praten",
   "body":"Wetenschappelijk taalgebruik:\n\nLo studio dimostra che… — Het onderzoek toont aan dat…\nSecondo la ricerca… — Volgens het onderzoek…\nL'esperimento ha confermato… — Het experiment heeft bevestigd…\nLa teoria è stata verificata. — De theorie is geverifieerd."},
   "words":["w2363","w2364","w2365","w2366","w2367","w2368","w2369","w2370"]},

  {"id":266,"title":"Biologie & geneeskunde","emoji":"🧬","level":"B1",
   "description":"Woorden over biologie en medische wetenschap.",
   "grammar":{"title":"Biologische en medische termen",
   "body":"Basistermen uit de biologie:\n\nla cellula — de cel\nil DNA — het DNA\nil gene — het gen\nil virus / il batterio — het virus / de bacterie\nil sistema immunitario — het immuunsysteem\nil vaccino — het vaccin"},
   "words":["w2371","w2372","w2373","w2374","w2375","w2376","w2377","w2378"]},

  {"id":267,"title":"Wiskunde & natuurkunde","emoji":"🔢","level":"B1",
   "description":"Basiswoorden uit wiskunde en natuurkunde.",
   "grammar":{"title":"Wiskundige termen",
   "body":"Wiskundige bewerkingen:\n\naddizione (+) — optelling\nsottrazione (−) — aftrekking\nmoltiplicazione (×) — vermenigvuldiging\ndivisione (÷) — deling\n\nDue più tre fa cinque. — Twee plus drie is vijf.\nDieci diviso due fa cinque. — Tien gedeeld door twee is vijf."},
   "words":["w2379","w2380","w2381","w2382","w2383","w2384","w2385","w2386"]},

  {"id":268,"title":"Uitvindingen & ontdekkingen","emoji":"💡","level":"B1",
   "description":"Belangrijke uitvindingen en ontdekkingen.",
   "grammar":{"title":"Uitvindingen beschrijven",
   "body":"Gebruik de passato remoto of passato prossimo:\n\nGalilei inventò il telescopio. — Galilei vond de telescoop uit.\nMarconi ha inventato la radio. — Marconi heeft de radio uitgevonden.\nVolta scoprì la pila elettrica. — Volta ontdekte de elektrische batterij.\n\ninventare = uitvinden | scoprire = ontdekken"},
   "words":["w2387","w2388","w2389","w2390","w2391","w2392","w2393","w2394"]},

  {"id":269,"title":"Ruimtevaart & sterrenkunde","emoji":"🚀","level":"B1",
   "description":"Woorden over de ruimte en sterrenkunde.",
   "grammar":{"title":"Over de ruimte praten",
   "body":"Italiaanse ruimtevaarttermen:\n\nla stazione spaziale — het ruimtestation\nil lancio — de lancering\nl'astronauta — de astronaut\nil satellite — de satelliet\norbitare — in een baan draaien\n\nSamantha Cristoforetti è un'astronauta italiana. — Samantha Cristoforetti is een Italiaanse astronaut."},
   "words":["w2395","w2396","w2397","w2398","w2399","w2400","w2401","w2402"]},

  {"id":270,"title":"Toetsles B1 — Blok 15","emoji":"📋","level":"B1",
   "description":"Toets over lessen 261–270: gezondheid & wetenschap.",
   "grammar":{"title":"Toetsles B1 — Blok 15 (les 261–270)","body":"In dit blok heb je geleerd:\n• De formele gebiedende wijs (imperativo formale)\n• Medische en farmaceutische termen\n• Geestelijke gezondheid en eerste hulp\n• Wetenschap, biologie en ruimtevaart"},
   "words":["w2403","w2404","w2405","w2406","w2407","w2408","w2409","w2410"]},
]

WORDS += [
  # ── Les 261: In het ziekenhuis ──
  {"id":"w2331","it":"l'ospedale","nl":"het ziekenhuis","ph":"os-pe-DA-le","ex":"È stato ricoverato in ospedale.","exNl":"Hij is opgenomen in het ziekenhuis.","lesson":261,"level":"B1","cat":"sostantivo"},
  {"id":"w2332","it":"il pronto soccorso","nl":"de eerste hulp (afdeling)","ph":"PRON-to sok-KOR-so","ex":"Lo hanno portato al pronto soccorso.","exNl":"Ze hebben hem naar de eerste hulp gebracht.","lesson":261,"level":"B1","cat":"sostantivo"},
  {"id":"w2333","it":"il chirurgo","nl":"de chirurg","ph":"ki-RUR-go","ex":"Il chirurgo ha eseguito l'operazione.","exNl":"De chirurg heeft de operatie uitgevoerd.","lesson":261,"level":"B1","cat":"sostantivo"},
  {"id":"w2334","it":"l'infermiere","nl":"de verpleegkundige","ph":"in-fer-MJE-re","ex":"L'infermiera mi ha misurato la pressione.","exNl":"De verpleegkundige heeft mijn bloeddruk gemeten.","lesson":261,"level":"B1","cat":"sostantivo"},
  {"id":"w2335","it":"l'operazione","nl":"de operatie","ph":"o-pe-ra-TSJO-ne","ex":"L'operazione è andata bene.","exNl":"De operatie is goed verlopen.","lesson":261,"level":"B1","cat":"sostantivo"},
  {"id":"w2336","it":"la visita medica","nl":"het medisch onderzoek","ph":"VI-zi-ta ME-di-ka","ex":"Devo fare una visita medica.","exNl":"Ik moet een medisch onderzoek ondergaan.","lesson":261,"level":"B1","cat":"sostantivo"},
  {"id":"w2337","it":"ricoverare","nl":"opnemen (in ziekenhuis)","ph":"ri-ko-ve-RA-re","ex":"È stato ricoverato per tre giorni.","exNl":"Hij is drie dagen opgenomen geweest.","lesson":261,"level":"B1","cat":"verbo"},
  {"id":"w2338","it":"guarire","nl":"genezen","ph":"gwa-RI-re","ex":"Ci vorrà tempo per guarire.","exNl":"Het zal tijd kosten om te genezen.","lesson":261,"level":"B1","cat":"verbo"},

  # ── Les 262: De apotheek ──
  {"id":"w2339","it":"la farmacia","nl":"de apotheek","ph":"far-ma-TSI-a","ex":"La farmacia è aperta fino alle otto.","exNl":"De apotheek is open tot acht uur.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2340","it":"il farmaco","nl":"het medicijn, het geneesmiddel","ph":"FAR-ma-ko","ex":"Questo farmaco si prende due volte al giorno.","exNl":"Dit medicijn neem je twee keer per dag.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2341","it":"la ricetta","nl":"het recept (medisch)","ph":"ri-TSHET-ta","ex":"Per questo farmaco serve la ricetta medica.","exNl":"Voor dit medicijn heb je een doktersrecept nodig.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2342","it":"la pastiglia","nl":"de pil, het tablet","ph":"pas-TI-lja","ex":"Prenda una pastiglia dopo i pasti.","exNl":"Neem een tablet na de maaltijden.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2343","it":"lo sciroppo","nl":"de siroop, de drank","ph":"shi-ROP-po","ex":"Lo sciroppo per la tosse è molto efficace.","exNl":"De hoestdrank is heel effectief.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2344","it":"l'effetto collaterale","nl":"de bijwerking","ph":"ef-FET-to kol-la-te-RA-le","ex":"Questo farmaco può avere effetti collaterali.","exNl":"Dit medicijn kan bijwerkingen hebben.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2345","it":"l'allergia","nl":"de allergie","ph":"al-ler-DJI-a","ex":"Ho un'allergia ai pollini.","exNl":"Ik heb een pollenallergie.","lesson":262,"level":"B1","cat":"sostantivo"},
  {"id":"w2346","it":"il dosaggio","nl":"de dosering","ph":"do-ZAD-djo","ex":"Non superi il dosaggio consigliato.","exNl":"Overschrijd de aanbevolen dosering niet.","lesson":262,"level":"B1","cat":"sostantivo"},

  # ── Les 263: Geestelijke gezondheid ──
  {"id":"w2347","it":"lo psicologo","nl":"de psycholoog","ph":"psi-KO-lo-go","ex":"Vado dallo psicologo una volta a settimana.","exNl":"Ik ga één keer per week naar de psycholoog.","lesson":263,"level":"B1","cat":"sostantivo"},
  {"id":"w2348","it":"la terapia","nl":"de therapie","ph":"te-ra-PI-a","ex":"La terapia mi sta aiutando molto.","exNl":"De therapie helpt me heel erg.","lesson":263,"level":"B1","cat":"sostantivo"},
  {"id":"w2349","it":"il disturbo","nl":"de stoornis, de aandoening","ph":"dis-TUR-bo","ex":"Soffre di un disturbo d'ansia.","exNl":"Hij lijdt aan een angststoornis.","lesson":263,"level":"B1","cat":"sostantivo"},
  {"id":"w2350","it":"la depressione","nl":"de depressie","ph":"de-pres-SJO-ne","ex":"La depressione è una malattia seria.","exNl":"Depressie is een serieuze ziekte.","lesson":263,"level":"B1","cat":"sostantivo"},
  {"id":"w2351","it":"il benessere mentale","nl":"het geestelijk welzijn","ph":"be-nes-SE-re men-TA-le","ex":"Il benessere mentale è fondamentale.","exNl":"Geestelijk welzijn is essentieel.","lesson":263,"level":"B1","cat":"sostantivo"},
  {"id":"w2352","it":"il sostegno","nl":"de steun, de ondersteuning","ph":"sos-TE-njo","ex":"Ha bisogno di sostegno psicologico.","exNl":"Hij heeft psychologische ondersteuning nodig.","lesson":263,"level":"B1","cat":"sostantivo"},
  {"id":"w2353","it":"affrontare","nl":"onder ogen zien","ph":"af-fron-TA-re","ex":"Devi affrontare i tuoi problemi.","exNl":"Je moet je problemen onder ogen zien.","lesson":263,"level":"B1","cat":"verbo"},
  {"id":"w2354","it":"superare","nl":"overwinnen, te boven komen","ph":"su-pe-RA-re","ex":"Ha superato un periodo molto difficile.","exNl":"Hij heeft een heel moeilijke periode overwonnen.","lesson":263,"level":"B1","cat":"verbo"},

  # ── Les 264: Eerste hulp ──
  {"id":"w2355","it":"l'ambulanza","nl":"de ambulance","ph":"am-bu-LAN-tsa","ex":"Chiamate un'ambulanza!","exNl":"Bel een ambulance!","lesson":264,"level":"B1","cat":"sostantivo"},
  {"id":"w2356","it":"l'emergenza","nl":"het noodgeval","ph":"e-mer-DJEN-tsa","ex":"In caso di emergenza, chiami il 112.","exNl":"In geval van nood, bel 112.","lesson":264,"level":"B1","cat":"sostantivo"},
  {"id":"w2357","it":"la ferita","nl":"de wond","ph":"fe-RI-ta","ex":"La ferita non è grave.","exNl":"De wond is niet ernstig.","lesson":264,"level":"B1","cat":"sostantivo"},
  {"id":"w2358","it":"svenire","nl":"flauwvallen","ph":"zve-NI-re","ex":"È svenuto per il caldo.","exNl":"Hij viel flauw van de hitte.","lesson":264,"level":"B1","cat":"verbo"},
  {"id":"w2359","it":"la frattura","nl":"de breuk (bot)","ph":"frat-TU-ra","ex":"Ha una frattura al braccio.","exNl":"Hij heeft een breuk in zijn arm.","lesson":264,"level":"B1","cat":"sostantivo"},
  {"id":"w2360","it":"il bendaggio","nl":"het verband","ph":"ben-DAD-djo","ex":"L'infermiere ha applicato un bendaggio.","exNl":"De verpleegkundige heeft een verband aangelegd.","lesson":264,"level":"B1","cat":"sostantivo"},
  {"id":"w2361","it":"soccorrere","nl":"te hulp komen, bijstaan","ph":"sok-KOR-re-re","ex":"I vigili del fuoco hanno soccorso i feriti.","exNl":"De brandweerlieden hebben de gewonden geholpen.","lesson":264,"level":"B1","cat":"verbo"},
  {"id":"w2362","it":"urgente","nl":"dringend, urgent","ph":"ur-DJEN-te","ex":"È un caso urgente.","exNl":"Het is een dringend geval.","lesson":264,"level":"B1","cat":"aggettivo"},

  # ── Les 265: Wetenschap — basis ──
  {"id":"w2363","it":"la scienza","nl":"de wetenschap","ph":"SHEN-tsa","ex":"La scienza ci aiuta a capire il mondo.","exNl":"De wetenschap helpt ons de wereld te begrijpen.","lesson":265,"level":"B1","cat":"sostantivo"},
  {"id":"w2364","it":"l'esperimento","nl":"het experiment","ph":"es-pe-ri-MEN-to","ex":"L'esperimento ha dato risultati positivi.","exNl":"Het experiment gaf positieve resultaten.","lesson":265,"level":"B1","cat":"sostantivo"},
  {"id":"w2365","it":"la teoria","nl":"de theorie","ph":"te-o-RI-a","ex":"La teoria è stata confermata dai dati.","exNl":"De theorie is bevestigd door de gegevens.","lesson":265,"level":"B1","cat":"sostantivo"},
  {"id":"w2366","it":"dimostrare","nl":"aantonen, bewijzen","ph":"di-mos-TRA-re","ex":"Lo studio dimostra l'efficacia del farmaco.","exNl":"Het onderzoek toont de werkzaamheid van het medicijn aan.","lesson":265,"level":"B1","cat":"verbo"},
  {"id":"w2367","it":"il metodo","nl":"de methode","ph":"ME-to-do","ex":"Il metodo scientifico è fondamentale.","exNl":"De wetenschappelijke methode is essentieel.","lesson":265,"level":"B1","cat":"sostantivo"},
  {"id":"w2368","it":"analizzare","nl":"analyseren","ph":"a-na-lid-ZA-re","ex":"Dobbiamo analizzare i dati con attenzione.","exNl":"We moeten de gegevens zorgvuldig analyseren.","lesson":265,"level":"B1","cat":"verbo"},
  {"id":"w2369","it":"il fenomeno","nl":"het fenomeen, het verschijnsel","ph":"fe-NO-me-no","ex":"È un fenomeno naturale molto raro.","exNl":"Het is een heel zeldzaam natuurverschijnsel.","lesson":265,"level":"B1","cat":"sostantivo"},
  {"id":"w2370","it":"verificare","nl":"verifiëren, controleren","ph":"ve-ri-fi-KA-re","ex":"Bisogna verificare i risultati.","exNl":"We moeten de resultaten verifiëren.","lesson":265,"level":"B1","cat":"verbo"},

  # ── Les 266: Biologie & geneeskunde ──
  {"id":"w2371","it":"la cellula","nl":"de cel","ph":"TSHEL-lu-la","ex":"Il corpo umano è fatto di cellule.","exNl":"Het menselijk lichaam is opgebouwd uit cellen.","lesson":266,"level":"B1","cat":"sostantivo"},
  {"id":"w2372","it":"il vaccino","nl":"het vaccin","ph":"vat-TSHI-no","ex":"Il vaccino protegge dalle malattie.","exNl":"Het vaccin beschermt tegen ziekten.","lesson":266,"level":"B1","cat":"sostantivo"},
  {"id":"w2373","it":"il virus","nl":"het virus","ph":"VI-rus","ex":"Il virus si diffonde rapidamente.","exNl":"Het virus verspreidt zich snel.","lesson":266,"level":"B1","cat":"sostantivo"},
  {"id":"w2374","it":"il batterio","nl":"de bacterie","ph":"bat-TE-rjo","ex":"I batteri possono causare infezioni.","exNl":"Bacteriën kunnen infecties veroorzaken.","lesson":266,"level":"B1","cat":"sostantivo"},
  {"id":"w2375","it":"la cura","nl":"de behandeling, het geneesmiddel","ph":"KU-ra","ex":"I ricercatori cercano una cura.","exNl":"De onderzoekers zoeken een behandeling.","lesson":266,"level":"B1","cat":"sostantivo"},
  {"id":"w2376","it":"il sistema immunitario","nl":"het immuunsysteem","ph":"sis-TE-ma im-mu-ni-TA-rjo","ex":"Il sistema immunitario ci protegge.","exNl":"Het immuunsysteem beschermt ons.","lesson":266,"level":"B1","cat":"sostantivo"},
  {"id":"w2377","it":"contagioso","nl":"besmettelijk","ph":"kon-ta-DJO-zo","ex":"Questa malattia è molto contagiosa.","exNl":"Deze ziekte is heel besmettelijk.","lesson":266,"level":"B1","cat":"aggettivo"},
  {"id":"w2378","it":"prevenire","nl":"voorkomen, preventie plegen","ph":"pre-ve-NI-re","ex":"Prevenire è meglio che curare.","exNl":"Voorkomen is beter dan genezen.","lesson":266,"level":"B1","cat":"verbo"},

  # ── Les 267: Wiskunde & natuurkunde ──
  {"id":"w2379","it":"l'equazione","nl":"de vergelijking (wiskunde)","ph":"e-kwa-TSJO-ne","ex":"Risolvi questa equazione.","exNl":"Los deze vergelijking op.","lesson":267,"level":"B1","cat":"sostantivo"},
  {"id":"w2380","it":"la percentuale","nl":"het percentage","ph":"per-tshen-tu-A-le","ex":"Il 30% degli studenti è straniero.","exNl":"30% van de studenten is buitenlands.","lesson":267,"level":"B1","cat":"sostantivo"},
  {"id":"w2381","it":"calcolare","nl":"berekenen","ph":"kal-ko-LA-re","ex":"Devi calcolare la distanza.","exNl":"Je moet de afstand berekenen.","lesson":267,"level":"B1","cat":"verbo"},
  {"id":"w2382","it":"la formula","nl":"de formule","ph":"FOR-mu-la","ex":"La formula è E = mc².","exNl":"De formule is E = mc².","lesson":267,"level":"B1","cat":"sostantivo"},
  {"id":"w2383","it":"la gravità","nl":"de zwaartekracht","ph":"gra-vi-TA","ex":"Newton scoprì la legge di gravità.","exNl":"Newton ontdekte de wet van de zwaartekracht.","lesson":267,"level":"B1","cat":"sostantivo"},
  {"id":"w2384","it":"l'energia","nl":"de energie","ph":"e-ner-DJI-a","ex":"L'energia non si crea né si distrugge.","exNl":"Energie wordt niet gecreëerd noch vernietigd.","lesson":267,"level":"B1","cat":"sostantivo"},
  {"id":"w2385","it":"la velocità","nl":"de snelheid","ph":"ve-lo-tsji-TA","ex":"La velocità della luce è costante.","exNl":"De snelheid van het licht is constant.","lesson":267,"level":"B1","cat":"sostantivo"},
  {"id":"w2386","it":"misurare","nl":"meten","ph":"mi-zu-RA-re","ex":"Dobbiamo misurare la temperatura.","exNl":"We moeten de temperatuur meten.","lesson":267,"level":"B1","cat":"verbo"},

  # ── Les 268: Uitvindingen & ontdekkingen ──
  {"id":"w2387","it":"inventare","nl":"uitvinden","ph":"in-ven-TA-re","ex":"Meucci inventò il telefono.","exNl":"Meucci vond de telefoon uit.","lesson":268,"level":"B1","cat":"verbo"},
  {"id":"w2388","it":"l'invenzione","nl":"de uitvinding","ph":"in-ven-TSJO-ne","ex":"La stampa fu una grande invenzione.","exNl":"De drukpers was een grote uitvinding.","lesson":268,"level":"B1","cat":"sostantivo"},
  {"id":"w2389","it":"la scoperta","nl":"de ontdekking","ph":"sko-PER-ta","ex":"La scoperta della penicillina salvò milioni di vite.","exNl":"De ontdekking van penicilline redde miljoenen levens.","lesson":268,"level":"B1","cat":"sostantivo"},
  {"id":"w2390","it":"il brevetto","nl":"het patent","ph":"bre-VET-to","ex":"Ha ottenuto il brevetto per la sua invenzione.","exNl":"Hij heeft patent gekregen op zijn uitvinding.","lesson":268,"level":"B1","cat":"sostantivo"},
  {"id":"w2391","it":"rivoluzionare","nl":"revolutioneren","ph":"ri-vo-lu-tsjo-NA-re","ex":"Internet ha rivoluzionato la comunicazione.","exNl":"Internet heeft de communicatie gerevolutioneerd.","lesson":268,"level":"B1","cat":"verbo"},
  {"id":"w2392","it":"il progresso","nl":"de vooruitgang","ph":"pro-GRES-so","ex":"Il progresso scientifico è inarrestabile.","exNl":"De wetenschappelijke vooruitgang is onstuitbaar.","lesson":268,"level":"B1","cat":"sostantivo"},
  {"id":"w2393","it":"innovativo","nl":"innovatief, vernieuwend","ph":"in-no-va-TI-vo","ex":"È un prodotto molto innovativo.","exNl":"Het is een heel innovatief product.","lesson":268,"level":"B1","cat":"aggettivo"},
  {"id":"w2394","it":"il robot","nl":"de robot","ph":"RO-bot","ex":"I robot aiutano nella produzione industriale.","exNl":"Robots helpen bij industriële productie.","lesson":268,"level":"B1","cat":"sostantivo"},

  # ── Les 269: Ruimtevaart & sterrenkunde ──
  {"id":"w2395","it":"lo spazio","nl":"de ruimte","ph":"SPA-tsjo","ex":"L'esplorazione dello spazio affascina l'umanità.","exNl":"De verkenning van de ruimte fascineert de mensheid.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2396","it":"l'astronauta","nl":"de astronaut","ph":"as-tro-NAU-ta","ex":"Samantha Cristoforetti è un'astronauta italiana.","exNl":"Samantha Cristoforetti is een Italiaanse astronaut.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2397","it":"il pianeta","nl":"de planeet","ph":"pja-NE-ta","ex":"La Terra è il terzo pianeta dal Sole.","exNl":"De aarde is de derde planeet vanaf de zon.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2398","it":"la stella","nl":"de ster","ph":"STEL-la","ex":"Ci sono miliardi di stelle nell'universo.","exNl":"Er zijn miljarden sterren in het heelal.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2399","it":"la Luna","nl":"de maan","ph":"LU-na","ex":"L'uomo è arrivato sulla Luna nel 1969.","exNl":"De mens bereikte de maan in 1969.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2400","it":"il satellite","nl":"de satelliet","ph":"sa-TEL-li-te","ex":"Il satellite orbita intorno alla Terra.","exNl":"De satelliet draait om de aarde.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2401","it":"l'universo","nl":"het heelal, het universum","ph":"u-ni-VER-so","ex":"L'universo è in continua espansione.","exNl":"Het heelal dijt voortdurend uit.","lesson":269,"level":"B1","cat":"sostantivo"},
  {"id":"w2402","it":"il telescopio","nl":"de telescoop","ph":"te-les-KO-pjo","ex":"Galileo perfezionò il telescopio.","exNl":"Galileo perfectioneerde de telescoop.","lesson":269,"level":"B1","cat":"sostantivo"},

  # ── Les 270: Toetsles Blok 15 ──
  {"id":"w2403","it":"la salute","nl":"de gezondheid","ph":"sa-LU-te","ex":"La salute è il bene più prezioso.","exNl":"Gezondheid is het kostbaarste goed.","lesson":270,"level":"B1","cat":"sostantivo"},
  {"id":"w2404","it":"curare","nl":"behandelen, genezen","ph":"ku-RA-re","ex":"I medici curano i pazienti.","exNl":"De artsen behandelen de patiënten.","lesson":270,"level":"B1","cat":"verbo"},
  {"id":"w2405","it":"la prevenzione","nl":"de preventie","ph":"pre-ven-TSJO-ne","ex":"La prevenzione è fondamentale.","exNl":"Preventie is essentieel.","lesson":270,"level":"B1","cat":"sostantivo"},
  {"id":"w2406","it":"la diagnosi","nl":"de diagnose","ph":"DJA-njo-zi","ex":"Il medico ha fatto la diagnosi.","exNl":"De arts heeft de diagnose gesteld.","lesson":270,"level":"B1","cat":"sostantivo"},
  {"id":"w2407","it":"il sintomo","nl":"het symptoom","ph":"SIN-to-mo","ex":"I sintomi sono febbre e tosse.","exNl":"De symptomen zijn koorts en hoest.","lesson":270,"level":"B1","cat":"sostantivo"},
  {"id":"w2408","it":"cronico","nl":"chronisch","ph":"KRO-ni-ko","ex":"Soffre di una malattia cronica.","exNl":"Hij lijdt aan een chronische ziekte.","lesson":270,"level":"B1","cat":"aggettivo"},
  {"id":"w2409","it":"il microscopio","nl":"de microscoop","ph":"mi-kros-KO-pjo","ex":"Il microscopio permette di vedere le cellule.","exNl":"De microscoop maakt het mogelijk cellen te zien.","lesson":270,"level":"B1","cat":"sostantivo"},
  {"id":"w2410","it":"la scoperta scientifica","nl":"de wetenschappelijke ontdekking","ph":"sko-PER-ta sjen-TI-fi-ka","ex":"Ogni scoperta scientifica cambia il mondo.","exNl":"Elke wetenschappelijke ontdekking verandert de wereld.","lesson":270,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 16: Dagelijks leven verdieping (lessen 271–280)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":271,"title":"De kapper & schoonheid","emoji":"💇","level":"B1",
   "description":"Woordenschat voor de kapper en schoonheidssalon.",
   "grammar":{"title":"Farsi + infinito",
   "body":"Met farsi + infinito druk je uit dat je iets laat doen:\n\nfarsi tagliare i capelli — je haar laten knippen\nfarsi fare la barba — je laten scheren\nfarsi fare le unghie — je nagels laten doen\n\nMi faccio tagliare i capelli ogni mese. — Ik laat elke maand mijn haar knippen."},
   "words":["w2411","w2412","w2413","w2414","w2415","w2416","w2417","w2418"]},

  {"id":272,"title":"De auto & garage","emoji":"🚗","level":"B1",
   "description":"Woorden over de auto, onderhoud en de garage.",
   "grammar":{"title":"Bij de garage",
   "body":"Nuttige zinnen:\n\nLa macchina non parte. — De auto start niet.\nHo una gomma a terra. — Ik heb een lekke band.\nDevo fare il tagliando. — Ik moet een onderhoudsbeurt laten doen.\nIl motore fa un rumore strano. — De motor maakt een raar geluid."},
   "words":["w2419","w2420","w2421","w2422","w2423","w2424","w2425","w2426"]},

  {"id":273,"title":"Post & pakketjes","emoji":"📮","level":"B1",
   "description":"Woorden over de post, pakketjes en bezorging.",
   "grammar":{"title":"Post en bezorging",
   "body":"Nuttige zinnen:\n\nVorrei spedire un pacco. — Ik wil een pakket versturen.\nQuanto costa la spedizione? — Hoeveel kost de verzending?\nQuando arriverà? — Wanneer komt het aan?\nDevo firmare per la consegna? — Moet ik tekenen voor ontvangst?"},
   "words":["w2427","w2428","w2429","w2430","w2431","w2432","w2433","w2434"]},

  {"id":274,"title":"De bank & verzekeringen","emoji":"🏦","level":"B1",
   "description":"Bankzaken en verzekeringen regelen.",
   "grammar":{"title":"Bankzaken regelen",
   "body":"Nuttige bankzinnen:\n\nVorrei aprire un conto. — Ik wil een rekening openen.\nVorrei fare un prelievo / un versamento. — Ik wil geld opnemen / storten.\nLa mia carta è bloccata. — Mijn pas is geblokkeerd.\nVorrei sottoscrivere un'assicurazione. — Ik wil een verzekering afsluiten."},
   "words":["w2435","w2436","w2437","w2438","w2439","w2440","w2441","w2442"]},

  {"id":275,"title":"Recepten & koken verdieping","emoji":"👨‍🍳","level":"B1",
   "description":"Verdieping in kooktermen en recepten.",
   "grammar":{"title":"Een recept volgen",
   "body":"Italiaanse recepten gebruiken vaak de infinitief of imperativo:\n\nTagliare le cipolle a fettine. — De uien in plakjes snijden.\nFar bollire l'acqua. — Het water aan de kook brengen.\nMescolare gli ingredienti. — De ingrediënten mengen.\nCuocere a fuoco lento per 30 minuti. — 30 minuten op laag vuur koken."},
   "words":["w2443","w2444","w2445","w2446","w2447","w2448","w2449","w2450"]},

  {"id":276,"title":"Huishouden & schoonmaken","emoji":"🧹","level":"B1",
   "description":"Woorden over huishoudelijke taken.",
   "grammar":{"title":"Huishoudelijke taken",
   "body":"Veelgebruikte werkwoorden:\n\npulire — schoonmaken\nlavare i piatti — de afwas doen\nfare il bucato — de was doen\npassare l'aspirapolvere — stofzuigen\nstirare — strijken\nsparecchiare — de tafel afruimen"},
   "words":["w2451","w2452","w2453","w2454","w2455","w2456","w2457","w2458"]},

  {"id":277,"title":"Doe-het-zelf & reparatie","emoji":"🔧","level":"B1",
   "description":"Woorden over klussen en reparaties.",
   "grammar":{"title":"Reparaties beschrijven",
   "body":"Nuttige zinnen:\n\nDevo riparare il rubinetto. — Ik moet de kraan repareren.\nLa lampadina è fulminata. — De gloeilamp is doorgebrand.\nHo bisogno di un cacciavite / un martello. — Ik heb een schroevendraaier / hamer nodig.\nChiamo l'idraulico / l'elettricista. — Ik bel de loodgieter / elektricien."},
   "words":["w2459","w2460","w2461","w2462","w2463","w2464","w2465","w2466"]},

  {"id":278,"title":"Tuinieren & buitenleven","emoji":"🌻","level":"B1",
   "description":"Woorden over tuinieren en het buitenleven.",
   "grammar":{"title":"Over de tuin praten",
   "body":"Tuinactiviteiten:\n\npiantare — planten\npotare — snoeien\ntagliare l'erba — het gras maaien\nraccogliere i frutti — de vruchten oogsten\nil prato — het gazon\nl'aiuola — het bloembed"},
   "words":["w2467","w2468","w2469","w2470","w2471","w2472","w2473","w2474"]},

  {"id":279,"title":"Feest & vieren","emoji":"🎉","level":"B1",
   "description":"Woorden voor feesten, uitnodigingen en vieringen.",
   "grammar":{"title":"Feesten en uitnodigen",
   "body":"Uitnodigingen:\n\nSei invitato/a alla mia festa! — Je bent uitgenodigd op mijn feest!\nVuoi venire alla cena? — Wil je naar het diner komen?\nFesteggiamo il mio compleanno sabato. — We vieren zaterdag mijn verjaardag.\nPorto una bottiglia di vino. — Ik neem een fles wijn mee."},
   "words":["w2475","w2476","w2477","w2478","w2479","w2480","w2481","w2482"]},

  {"id":280,"title":"Toetsles B1 — Blok 16","emoji":"📋","level":"B1",
   "description":"Toets over lessen 271–280: dagelijks leven verdieping.",
   "grammar":{"title":"Toetsles B1 — Blok 16 (les 271–280)","body":"In dit blok heb je geleerd:\n• Farsi + infinito (iets laten doen)\n• Bij de kapper, garage, post en bank\n• Koken, huishouden en klussen\n• Feesten en uitnodigen"},
   "words":["w2483","w2484","w2485","w2486","w2487","w2488","w2489","w2490"]},
]

WORDS += [
  # ── Les 271: De kapper & schoonheid ──
  {"id":"w2411","it":"il parrucchiere","nl":"de kapper","ph":"par-ruk-KJE-re","ex":"Vado dal parrucchiere ogni sei settimane.","exNl":"Ik ga elke zes weken naar de kapper.","lesson":271,"level":"B1","cat":"sostantivo"},
  {"id":"w2412","it":"tagliare","nl":"knippen, snijden","ph":"ta-LJA-re","ex":"Mi tagli solo le punte, per favore.","exNl":"Knip alleen de punten, alstublieft.","lesson":271,"level":"B1","cat":"verbo"},
  {"id":"w2413","it":"la piega","nl":"de föhnbeurt","ph":"PJE-ga","ex":"Vorrei un taglio e una piega.","exNl":"Ik wil een knipbeurt en een föhnbeurt.","lesson":271,"level":"B1","cat":"sostantivo"},
  {"id":"w2414","it":"tingere","nl":"verven (haar)","ph":"TIN-dje-re","ex":"Voglio tingermi i capelli di biondo.","exNl":"Ik wil mijn haar blond verven.","lesson":271,"level":"B1","cat":"verbo"},
  {"id":"w2415","it":"la frangia","nl":"de pony (haar)","ph":"FRAN-dja","ex":"Vorrei accorciare la frangia.","exNl":"Ik wil de pony korter.","lesson":271,"level":"B1","cat":"sostantivo"},
  {"id":"w2416","it":"l'asciugacapelli","nl":"de föhn","ph":"a-shu-ga-ka-PEL-li","ex":"Usa l'asciugacapelli per asciugare i capelli.","exNl":"Gebruik de föhn om je haar te drogen.","lesson":271,"level":"B1","cat":"sostantivo"},
  {"id":"w2417","it":"la barba","nl":"de baard","ph":"BAR-ba","ex":"Mi faccio la barba ogni mattina.","exNl":"Ik scheer me elke ochtend.","lesson":271,"level":"B1","cat":"sostantivo"},
  {"id":"w2418","it":"il trucco","nl":"de make-up","ph":"TRUK-ko","ex":"Non metto molto trucco.","exNl":"Ik draag niet veel make-up.","lesson":271,"level":"B1","cat":"sostantivo"},

  # ── Les 272: De auto & garage ──
  {"id":"w2419","it":"il motore","nl":"de motor","ph":"mo-TO-re","ex":"Il motore non funziona bene.","exNl":"De motor werkt niet goed.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2420","it":"la gomma","nl":"de band (auto)","ph":"GOM-ma","ex":"Devo cambiare le gomme invernali.","exNl":"Ik moet de winterbanden verwisselen.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2421","it":"il meccanico","nl":"de monteur","ph":"mek-KA-ni-ko","ex":"Porto la macchina dal meccanico.","exNl":"Ik breng de auto naar de monteur.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2422","it":"il freno","nl":"de rem","ph":"FRE-no","ex":"I freni devono essere controllati.","exNl":"De remmen moeten gecontroleerd worden.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2423","it":"la patente","nl":"het rijbewijs","ph":"pa-TEN-te","ex":"Ho preso la patente a diciotto anni.","exNl":"Ik heb mijn rijbewijs gehaald op mijn achttiende.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2424","it":"il carburante","nl":"de brandstof","ph":"kar-bu-RAN-te","ex":"Il prezzo del carburante è aumentato.","exNl":"De brandstofprijs is gestegen.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2425","it":"il cofano","nl":"de motorkap","ph":"KO-fa-no","ex":"Apri il cofano per controllare l'olio.","exNl":"Open de motorkap om de olie te controleren.","lesson":272,"level":"B1","cat":"sostantivo"},
  {"id":"w2426","it":"la revisione","nl":"de APK, de keuring","ph":"re-vi-ZJO-ne","ex":"La macchina deve fare la revisione.","exNl":"De auto moet gekeurd worden.","lesson":272,"level":"B1","cat":"sostantivo"},

  # ── Les 273: Post & pakketjes ──
  {"id":"w2427","it":"l'ufficio postale","nl":"het postkantoor","ph":"uf-FI-tsjo pos-TA-le","ex":"Vado all'ufficio postale a spedire un pacco.","exNl":"Ik ga naar het postkantoor om een pakket te versturen.","lesson":273,"level":"B1","cat":"sostantivo"},
  {"id":"w2428","it":"il pacco","nl":"het pakket","ph":"PAK-ko","ex":"Il pacco è arrivato questa mattina.","exNl":"Het pakket is vanochtend aangekomen.","lesson":273,"level":"B1","cat":"sostantivo"},
  {"id":"w2429","it":"la busta","nl":"de envelop","ph":"BUS-ta","ex":"Metti la lettera nella busta.","exNl":"Doe de brief in de envelop.","lesson":273,"level":"B1","cat":"sostantivo"},
  {"id":"w2430","it":"il francobollo","nl":"de postzegel","ph":"fran-ko-BOL-lo","ex":"Devo comprare dei francobolli.","exNl":"Ik moet postzegels kopen.","lesson":273,"level":"B1","cat":"sostantivo"},
  {"id":"w2431","it":"spedire","nl":"versturen, verzenden","ph":"spe-DI-re","ex":"Ho spedito il pacco ieri.","exNl":"Ik heb het pakket gisteren verstuurd.","lesson":273,"level":"B1","cat":"verbo"},
  {"id":"w2432","it":"il corriere","nl":"de koerier","ph":"kor-RJE-re","ex":"Il corriere consegna domani.","exNl":"De koerier bezorgt morgen.","lesson":273,"level":"B1","cat":"sostantivo"},
  {"id":"w2433","it":"la consegna","nl":"de bezorging, de levering","ph":"kon-SE-nja","ex":"La consegna è prevista per lunedì.","exNl":"De bezorging staat gepland voor maandag.","lesson":273,"level":"B1","cat":"sostantivo"},
  {"id":"w2434","it":"il mittente","nl":"de afzender","ph":"mit-TEN-te","ex":"Il mittente è scritto sulla busta.","exNl":"De afzender staat op de envelop.","lesson":273,"level":"B1","cat":"sostantivo"},

  # ── Les 274: De bank & verzekeringen ──
  {"id":"w2435","it":"il bancomat","nl":"de pinautomaat","ph":"BAN-ko-mat","ex":"Devo prelevare al bancomat.","exNl":"Ik moet pinnen bij de pinautomaat.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2436","it":"il prelievo","nl":"de opname (geld)","ph":"pre-LJE-vo","ex":"Ho fatto un prelievo di 200 euro.","exNl":"Ik heb 200 euro opgenomen.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2437","it":"il versamento","nl":"de storting","ph":"ver-sa-MEN-to","ex":"Devo fare un versamento sul conto.","exNl":"Ik moet geld storten op de rekening.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2438","it":"l'assicurazione","nl":"de verzekering","ph":"as-si-ku-ra-TSJO-ne","ex":"Ho un'assicurazione sulla vita.","exNl":"Ik heb een levensverzekering.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2439","it":"la polizza","nl":"de polis","ph":"PO-lid-za","ex":"La polizza copre i danni da incendio.","exNl":"De polis dekt brandschade.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2440","it":"il premio assicurativo","nl":"de verzekeringspremie","ph":"PRE-mjo as-si-ku-ra-TI-vo","ex":"Il premio assicurativo è aumentato.","exNl":"De verzekeringspremie is gestegen.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2441","it":"il danno","nl":"de schade","ph":"DAN-no","ex":"L'assicurazione copre i danni.","exNl":"De verzekering dekt de schade.","lesson":274,"level":"B1","cat":"sostantivo"},
  {"id":"w2442","it":"il pagamento","nl":"de betaling","ph":"pa-ga-MEN-to","ex":"Il pagamento può essere fatto online.","exNl":"De betaling kan online gedaan worden.","lesson":274,"level":"B1","cat":"sostantivo"},

  # ── Les 275: Recepten & koken verdieping ──
  {"id":"w2443","it":"mescolare","nl":"mengen, roeren","ph":"mes-ko-LA-re","ex":"Mescola gli ingredienti con cura.","exNl":"Meng de ingrediënten zorgvuldig.","lesson":275,"level":"B1","cat":"verbo"},
  {"id":"w2444","it":"bollire","nl":"koken (water)","ph":"bol-LI-re","ex":"Fai bollire l'acqua per la pasta.","exNl":"Breng het water aan de kook voor de pasta.","lesson":275,"level":"B1","cat":"verbo"},
  {"id":"w2445","it":"il forno","nl":"de oven","ph":"FOR-no","ex":"Preriscalda il forno a 180 gradi.","exNl":"Verwarm de oven voor op 180 graden.","lesson":275,"level":"B1","cat":"sostantivo"},
  {"id":"w2446","it":"la padella","nl":"de koekenpan","ph":"pa-DEL-la","ex":"Rosola la cipolla in padella.","exNl":"Bak de ui aan in de koekenpan.","lesson":275,"level":"B1","cat":"sostantivo"},
  {"id":"w2447","it":"l'ingrediente","nl":"het ingrediënt","ph":"in-gre-DJEN-te","ex":"Quali sono gli ingredienti di questa ricetta?","exNl":"Wat zijn de ingrediënten van dit recept?","lesson":275,"level":"B1","cat":"sostantivo"},
  {"id":"w2448","it":"grattugiare","nl":"raspen","ph":"grat-tu-DJA-re","ex":"Grattugia il parmigiano sulla pasta.","exNl":"Rasp de parmezaan over de pasta.","lesson":275,"level":"B1","cat":"verbo"},
  {"id":"w2449","it":"la porzione","nl":"de portie","ph":"por-TSJO-ne","ex":"Questa ricetta è per quattro porzioni.","exNl":"Dit recept is voor vier porties.","lesson":275,"level":"B1","cat":"sostantivo"},
  {"id":"w2450","it":"condire","nl":"kruiden, op smaak brengen","ph":"kon-DI-re","ex":"Condisci l'insalata con olio e sale.","exNl":"Maak de salade op smaak met olie en zout.","lesson":275,"level":"B1","cat":"verbo"},

  # ── Les 276: Huishouden & schoonmaken ──
  {"id":"w2451","it":"l'aspirapolvere","nl":"de stofzuiger","ph":"as-pi-ra-POL-ve-re","ex":"Passo l'aspirapolvere ogni giorno.","exNl":"Ik stofzuig elke dag.","lesson":276,"level":"B1","cat":"sostantivo"},
  {"id":"w2452","it":"lo straccio","nl":"de dweil, de lap","ph":"STRAT-tsho","ex":"Pulisci il pavimento con lo straccio.","exNl":"Maak de vloer schoon met de dweil.","lesson":276,"level":"B1","cat":"sostantivo"},
  {"id":"w2453","it":"il detersivo","nl":"het schoonmaakmiddel","ph":"de-ter-SI-vo","ex":"Compra il detersivo per i piatti.","exNl":"Koop afwasmiddel.","lesson":276,"level":"B1","cat":"sostantivo"},
  {"id":"w2454","it":"stirare","nl":"strijken","ph":"sti-RA-re","ex":"Odio stirare le camicie.","exNl":"Ik haat het om overhemden te strijken.","lesson":276,"level":"B1","cat":"verbo"},
  {"id":"w2455","it":"la lavatrice","nl":"de wasmachine","ph":"la-va-TRI-tshe","ex":"La lavatrice è rotta.","exNl":"De wasmachine is kapot.","lesson":276,"level":"B1","cat":"sostantivo"},
  {"id":"w2456","it":"il bucato","nl":"de was","ph":"bu-KA-to","ex":"Devo fare il bucato oggi.","exNl":"Ik moet vandaag de was doen.","lesson":276,"level":"B1","cat":"sostantivo"},
  {"id":"w2457","it":"spolverare","nl":"afstoffen","ph":"spol-ve-RA-re","ex":"Spolvera i mobili del soggiorno.","exNl":"Stof de meubels in de woonkamer af.","lesson":276,"level":"B1","cat":"verbo"},
  {"id":"w2458","it":"riordinare","nl":"opruimen","ph":"ri-or-di-NA-re","ex":"Riordina la tua camera!","exNl":"Ruim je kamer op!","lesson":276,"level":"B1","cat":"verbo"},

  # ── Les 277: Doe-het-zelf & reparatie ──
  {"id":"w2459","it":"il cacciavite","nl":"de schroevendraaier","ph":"kat-sha-VI-te","ex":"Passami il cacciavite, per favore.","exNl":"Geef me de schroevendraaier, alsjeblieft.","lesson":277,"level":"B1","cat":"sostantivo"},
  {"id":"w2460","it":"il martello","nl":"de hamer","ph":"mar-TEL-lo","ex":"Ho bisogno di un martello e dei chiodi.","exNl":"Ik heb een hamer en spijkers nodig.","lesson":277,"level":"B1","cat":"sostantivo"},
  {"id":"w2461","it":"il chiodo","nl":"de spijker","ph":"KJO-do","ex":"Ho piantato un chiodo nel muro.","exNl":"Ik heb een spijker in de muur geslagen.","lesson":277,"level":"B1","cat":"sostantivo"},
  {"id":"w2462","it":"la vite","nl":"de schroef","ph":"VI-te","ex":"Stringe la vite con il cacciavite.","exNl":"Draai de schroef vast met de schroevendraaier.","lesson":277,"level":"B1","cat":"sostantivo"},
  {"id":"w2463","it":"riparare","nl":"repareren","ph":"ri-pa-RA-re","ex":"Devo riparare la porta.","exNl":"Ik moet de deur repareren.","lesson":277,"level":"B1","cat":"verbo"},
  {"id":"w2464","it":"l'idraulico","nl":"de loodgieter","ph":"i-DRAU-li-ko","ex":"Chiamo l'idraulico per il rubinetto.","exNl":"Ik bel de loodgieter voor de kraan.","lesson":277,"level":"B1","cat":"sostantivo"},
  {"id":"w2465","it":"l'elettricista","nl":"de elektricien","ph":"e-let-tri-TSHIS-ta","ex":"L'elettricista ha riparato l'impianto.","exNl":"De elektricien heeft de installatie gerepareerd.","lesson":277,"level":"B1","cat":"sostantivo"},
  {"id":"w2466","it":"il rubinetto","nl":"de kraan","ph":"ru-bi-NET-to","ex":"Il rubinetto perde acqua.","exNl":"De kraan lekt.","lesson":277,"level":"B1","cat":"sostantivo"},

  # ── Les 278: Tuinieren & buitenleven ──
  {"id":"w2467","it":"il prato","nl":"het gazon, de weide","ph":"PRA-to","ex":"Il prato ha bisogno di essere tagliato.","exNl":"Het gazon moet gemaaid worden.","lesson":278,"level":"B1","cat":"sostantivo"},
  {"id":"w2468","it":"potare","nl":"snoeien","ph":"po-TA-re","ex":"Devo potare le rose.","exNl":"Ik moet de rozen snoeien.","lesson":278,"level":"B1","cat":"verbo"},
  {"id":"w2469","it":"il vaso","nl":"de bloempot","ph":"VA-zo","ex":"Ho messo la pianta in un vaso nuovo.","exNl":"Ik heb de plant in een nieuwe pot gezet.","lesson":278,"level":"B1","cat":"sostantivo"},
  {"id":"w2470","it":"la siepe","nl":"de haag","ph":"SJE-pe","ex":"La siepe divide i due giardini.","exNl":"De haag scheidt de twee tuinen.","lesson":278,"level":"B1","cat":"sostantivo"},
  {"id":"w2471","it":"il girasole","nl":"de zonnebloem","ph":"dji-ra-SO-le","ex":"I girasoli seguono il sole.","exNl":"Zonnebloemen volgen de zon.","lesson":278,"level":"B1","cat":"sostantivo"},
  {"id":"w2472","it":"la rosa","nl":"de roos","ph":"RO-za","ex":"Le rose del giardino sono bellissime.","exNl":"De rozen in de tuin zijn prachtig.","lesson":278,"level":"B1","cat":"sostantivo"},
  {"id":"w2473","it":"il concime","nl":"de mest, de kunstmest","ph":"kon-TSI-me","ex":"Aggiungi il concime alla terra.","exNl":"Voeg mest toe aan de aarde.","lesson":278,"level":"B1","cat":"sostantivo"},
  {"id":"w2474","it":"seminare","nl":"zaaien","ph":"se-mi-NA-re","ex":"In primavera seminiamo i fiori.","exNl":"In de lente zaaien we bloemen.","lesson":278,"level":"B1","cat":"verbo"},

  # ── Les 279: Feest & vieren ──
  {"id":"w2475","it":"l'invito","nl":"de uitnodiging","ph":"in-VI-to","ex":"Ho ricevuto un invito alla festa.","exNl":"Ik heb een uitnodiging voor het feest ontvangen.","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2476","it":"il brindisi","nl":"de toast (drinken)","ph":"BRIN-di-zi","ex":"Facciamo un brindisi! Cin cin!","exNl":"Laten we een toast uitbrengen! Proost!","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2477","it":"i fuochi d'artificio","nl":"het vuurwerk","ph":"FWO-ki dar-ti-FI-tsjo","ex":"A Capodanno ci sono i fuochi d'artificio.","exNl":"Met Oud en Nieuw is er vuurwerk.","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2478","it":"la sorpresa","nl":"de verrassing","ph":"sor-PRE-za","ex":"Abbiamo organizzato una festa a sorpresa.","exNl":"We hebben een verrassingsfeest georganiseerd.","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2479","it":"il palloncino","nl":"de ballon","ph":"pal-lon-TSI-no","ex":"La sala è decorata con palloncini colorati.","exNl":"De zaal is versierd met gekleurde ballonnen.","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2480","it":"la torta","nl":"de taart","ph":"TOR-ta","ex":"La torta di compleanno ha dieci candeline.","exNl":"De verjaardagstaart heeft tien kaarsjes.","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2481","it":"la candelina","nl":"het verjaardagskaarsje","ph":"kan-de-LI-na","ex":"Soffia sulle candeline!","exNl":"Blaas de kaarsjes uit!","lesson":279,"level":"B1","cat":"sostantivo"},
  {"id":"w2482","it":"augurare","nl":"wensen","ph":"au-gu-RA-re","ex":"Ti auguro buon compleanno!","exNl":"Ik wens je een fijne verjaardag!","lesson":279,"level":"B1","cat":"verbo"},

  # ── Les 280: Toetsles Blok 16 ──
  {"id":"w2483","it":"il fai da te","nl":"het doe-het-zelven","ph":"FAI da TE","ex":"Mi piace il fai da te.","exNl":"Ik hou van doe-het-zelven.","lesson":280,"level":"B1","cat":"sostantivo"},
  {"id":"w2484","it":"l'attrezzo","nl":"het gereedschap","ph":"at-TRET-tso","ex":"Ho comprato nuovi attrezzi.","exNl":"Ik heb nieuw gereedschap gekocht.","lesson":280,"level":"B1","cat":"sostantivo"},
  {"id":"w2485","it":"il giardinaggio","nl":"het tuinieren","ph":"djar-di-NAD-djo","ex":"Il giardinaggio è il mio hobby preferito.","exNl":"Tuinieren is mijn favoriete hobby.","lesson":280,"level":"B1","cat":"sostantivo"},
  {"id":"w2486","it":"la colla","nl":"de lijm","ph":"KOL-la","ex":"Usa la colla per incollare i pezzi.","exNl":"Gebruik lijm om de stukken te plakken.","lesson":280,"level":"B1","cat":"sostantivo"},
  {"id":"w2487","it":"verniciare","nl":"verven, schilderen (muur)","ph":"ver-ni-TSHA-re","ex":"Domani vernicio la camera da letto.","exNl":"Morgen verf ik de slaapkamer.","lesson":280,"level":"B1","cat":"verbo"},
  {"id":"w2488","it":"montare","nl":"monteren, in elkaar zetten","ph":"mon-TA-re","ex":"Devo montare l'armadio nuovo.","exNl":"Ik moet de nieuwe kast in elkaar zetten.","lesson":280,"level":"B1","cat":"verbo"},
  {"id":"w2489","it":"la festa di compleanno","nl":"het verjaardagsfeest","ph":"FES-ta di kom-ple-AN-no","ex":"Organizzo una festa di compleanno sabato.","exNl":"Ik organiseer zaterdag een verjaardagsfeest.","lesson":280,"level":"B1","cat":"sostantivo"},
  {"id":"w2490","it":"il regalo","nl":"het cadeau","ph":"re-GA-lo","ex":"Che bel regalo, grazie!","exNl":"Wat een mooi cadeau, dank je!","lesson":280,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 17: Idioom & uitdrukkingen (lessen 281–290)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":281,"title":"Uitdrukkingen — deel 1","emoji":"💬","level":"B1",
   "description":"Veelgebruikte Italiaanse uitdrukkingen met lichaamsdelen.",
   "grammar":{"title":"Idioom met lichaamsdelen",
   "body":"Italiaanse uitdrukkingen met lichaamsdelen:\n\navere le mani in pasta — overal bij betrokken zijn\nessere in gamba — capabel zijn, pienter zijn\ncostare un occhio della testa — heel duur zijn\nnon vedere l'ora — ergens naar uitkijken\navere la testa fra le nuvole — in de wolken zijn, dromerig zijn"},
   "words":["w2491","w2492","w2493","w2494","w2495","w2496","w2497","w2498"]},

  {"id":282,"title":"Uitdrukkingen — deel 2","emoji":"💬","level":"B1",
   "description":"Meer Italiaanse uitdrukkingen voor dagelijks gebruik.",
   "grammar":{"title":"Dagelijkse uitdrukkingen",
   "body":"Uitdrukkingen voor elke dag:\n\nIn bocca al lupo! — Succes! (antwoord: Crepi!)\nAcqua in bocca! — Mond dicht! (geheim houden)\nNon c'è due senza tre. — Alle goede dingen bestaan in drieën.\nChi dorme non piglia pesci. — Wie slaapt, vangt geen vis.\nMeglio tardi che mai. — Beter laat dan nooit."},
   "words":["w2499","w2500","w2501","w2502","w2503","w2504","w2505","w2506"]},

  {"id":283,"title":"Spreekwoorden","emoji":"📜","level":"B1",
   "description":"Bekende Italiaanse spreekwoorden en gezegden.",
   "grammar":{"title":"Italiaanse spreekwoorden",
   "body":"Spreekwoorden zijn wijsheden die van generatie op generatie worden doorgegeven:\n\nChi va piano, va sano e va lontano. — Wie langzaam gaat, gaat gezond en komt ver.\nL'appetito vien mangiando. — De eetlust komt al etend.\nTutti i gusti son gusti. — Over smaak valt niet te twisten.\nTra il dire e il fare c'è di mezzo il mare. — Tussen zeggen en doen ligt de zee."},
   "words":["w2507","w2508","w2509","w2510","w2511","w2512","w2513","w2514"]},

  {"id":284,"title":"Vaste werkwoordcombinaties","emoji":"🔗","level":"B1",
   "description":"Verbi pronominali en vaste combinaties.",
   "grammar":{"title":"Verbi pronominali",
   "body":"Verbi pronominali zijn werkwoorden met een vast voornaamwoord dat de betekenis verandert:\n\nfarcela — het redden (Ce la fai? — Red je het?)\nandarsene — weggaan (Me ne vado. — Ik ga weg.)\ncavarsela — zich redden (Me la cavo bene. — Ik red me goed.)\nprendersela — het kwalijk nemen (Non te la prendere! — Neem het niet kwalijk!)\nvolerci — nodig zijn (Ci vogliono due ore. — Er zijn twee uur nodig.)"},
   "words":["w2515","w2516","w2517","w2518","w2519","w2520","w2521","w2522"]},

  {"id":285,"title":"Formeel schrijven","emoji":"✍️","level":"B1",
   "description":"Formele schrijfconventies en briefstijl.",
   "grammar":{"title":"Formeel schrijven",
   "body":"Formele schrijfconventies:\n\nSpett.le — Geachte (voor bedrijven)\nEgregio/a — Geachte (voor personen)\nLa presente per comunicarLe che… — Hierbij deel ik u mede dat…\nIn fede — Hoogachtend\nDistinti saluti — Met onderscheiden groet\n\nLet op: Lei/Suo/La worden met hoofdletter geschreven uit respect."},
   "words":["w2523","w2524","w2525","w2526","w2527","w2528","w2529","w2530"]},

  {"id":286,"title":"Informeel taalgebruik","emoji":"😄","level":"B1",
   "description":"Informeel Italiaans en veelgebruikte slang.",
   "grammar":{"title":"Informele taal",
   "body":"Informeel Italiaans:\n\nDai! — Kom op! / Toe maar!\nBoh! — Geen idee!\nMagari! — Was het maar zo!\nFigata! — Gaaf! Cool!\nChe palle! — Wat vervelend! (grof)\nBasta! — Genoeg!\nMica male! — Niet slecht!"},
   "words":["w2531","w2532","w2533","w2534","w2535","w2536","w2537","w2538"]},

  {"id":287,"title":"Telefoneren","emoji":"📱","level":"B1",
   "description":"Woorden en uitdrukkingen voor telefoongesprekken.",
   "grammar":{"title":"Telefoneren in het Italiaans",
   "body":"Telefoongesprekken:\n\nProonto? — Hallo? (bij het opnemen)\nVorrei parlare con… — Ik zou graag spreken met…\nChi parla? — Met wie spreek ik?\nUn momento, glielo/gliela passo. — Een moment, ik verbind u door.\nPosso lasciare un messaggio? — Kan ik een bericht achterlaten?\nLa linea è disturbata. — De verbinding is slecht."},
   "words":["w2539","w2540","w2541","w2542","w2543","w2544","w2545","w2546"]},

  {"id":288,"title":"Klachten & problemen","emoji":"😤","level":"B1",
   "description":"Woorden voor het uiten van klachten en problemen.",
   "grammar":{"title":"Klachten uiten",
   "body":"Beleefde manieren om te klagen:\n\nMi scusi, c'è un problema con… — Neemt u me niet kwalijk, er is een probleem met…\nNon sono soddisfatto del servizio. — Ik ben niet tevreden over de service.\nVorrei parlare con il responsabile. — Ik wil de verantwoordelijke spreken.\nÈ inaccettabile. — Dit is onacceptabel.\nChiedo un rimborso. — Ik eis mijn geld terug."},
   "words":["w2547","w2548","w2549","w2550","w2551","w2552","w2553","w2554"]},

  {"id":289,"title":"Complimenten & bedankjes","emoji":"🙏","level":"B1",
   "description":"Complimenten geven en ontvangen, bedanken.",
   "grammar":{"title":"Complimenten & bedankjes",
   "body":"Complimenten geven:\n\nComplimenti! — Gefeliciteerd! Goed gedaan!\nChe bel vestito! — Wat een mooie jurk!\nSei molto bravo/a! — Je bent heel goed!\n\nBedanken:\nGrazie mille / Grazie di cuore — Heel hartelijk bedankt\nTi sono molto grato/a — Ik ben je heel dankbaar\nNon c'è di che / Di niente — Graag gedaan"},
   "words":["w2555","w2556","w2557","w2558","w2559","w2560","w2561","w2562"]},

  {"id":290,"title":"Toetsles B1 — Blok 17","emoji":"📋","level":"B1",
   "description":"Toets over lessen 281–290: idioom & uitdrukkingen.",
   "grammar":{"title":"Toetsles B1 — Blok 17 (les 281–290)","body":"In dit blok heb je geleerd:\n• Italiaanse uitdrukkingen en spreekwoorden\n• Verbi pronominali (farcela, andarsene, etc.)\n• Formeel en informeel schrijven\n• Telefoneren, klagen en complimenteren"},
   "words":["w2563","w2564","w2565","w2566","w2567","w2568","w2569","w2570"]},
]

WORDS += [
  # ── Les 281: Uitdrukkingen — deel 1 ──
  {"id":"w2491","it":"in gamba","nl":"capabel, pienter","ph":"in GAM-ba","ex":"È una ragazza molto in gamba.","exNl":"Ze is een heel capabel meisje.","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2492","it":"costare un occhio della testa","nl":"een fortuin kosten","ph":"kos-TA-re un OK-kjo","ex":"Questa borsa costa un occhio della testa.","exNl":"Deze tas kost een fortuin.","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2493","it":"non vedere l'ora","nl":"ergens naar uitkijken","ph":"non ve-DE-re LO-ra","ex":"Non vedo l'ora di partire!","exNl":"Ik kijk ernaar uit om te vertrekken!","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2494","it":"avere la testa fra le nuvole","nl":"met het hoofd in de wolken","ph":"a-VE-re la TES-ta","ex":"Oggi hai la testa fra le nuvole.","exNl":"Je bent vandaag met je hoofd in de wolken.","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2495","it":"prendere in giro","nl":"voor de gek houden","ph":"PREN-de-re in DJI-ro","ex":"Non mi prendere in giro!","exNl":"Hou me niet voor de gek!","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2496","it":"dare una mano","nl":"een handje helpen","ph":"DA-re u-na MA-no","ex":"Mi dai una mano con i bagagli?","exNl":"Help je me met de koffers?","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2497","it":"rompere le scatole","nl":"lastigvallen, irriteren","ph":"ROM-pe-re le SKA-to-le","ex":"Smetti di rompermi le scatole!","exNl":"Stop met me lastig te vallen!","lesson":281,"level":"B1","cat":"espressione"},
  {"id":"w2498","it":"avere il pollice verde","nl":"groene vingers hebben","ph":"a-VE-re il POL-li-tsje","ex":"Mia nonna ha il pollice verde.","exNl":"Mijn oma heeft groene vingers.","lesson":281,"level":"B1","cat":"espressione"},

  # ── Les 282: Uitdrukkingen — deel 2 ──
  {"id":"w2499","it":"in bocca al lupo","nl":"succes! (lett.: in de bek van de wolf)","ph":"in BOK-ka al LU-po","ex":"In bocca al lupo per l'esame!","exNl":"Succes met het examen!","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2500","it":"acqua in bocca","nl":"mondje dicht!","ph":"AK-kwa in BOK-ka","ex":"Ti dico un segreto, ma acqua in bocca!","exNl":"Ik vertel je een geheim, maar mondje dicht!","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2501","it":"meglio tardi che mai","nl":"beter laat dan nooit","ph":"ME-ljo TAR-di ke MAI","ex":"Sei arrivato! Meglio tardi che mai.","exNl":"Je bent er! Beter laat dan nooit.","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2502","it":"non c'è due senza tre","nl":"alle goede dingen bestaan in drieën","ph":"non tshe DU-e SEN-tsa TRE","ex":"Hai vinto di nuovo? Non c'è due senza tre!","exNl":"Je hebt weer gewonnen? Alle goede dingen bestaan in drieën!","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2503","it":"fare le ore piccole","nl":"tot diep in de nacht opblijven","ph":"FA-re le O-re PIK-ko-le","ex":"Ieri sera abbiamo fatto le ore piccole.","exNl":"Gisteravond zijn we tot diep in de nacht opgebleven.","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2504","it":"prendere due piccioni con una fava","nl":"twee vliegen in één klap","ph":"PREN-de-re DU-e","ex":"Così prendiamo due piccioni con una fava.","exNl":"Zo slaan we twee vliegen in één klap.","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2505","it":"essere al verde","nl":"blut zijn","ph":"ES-se-re al VER-de","ex":"Sono al verde, non posso uscire stasera.","exNl":"Ik ben blut, ik kan vanavond niet uit.","lesson":282,"level":"B1","cat":"espressione"},
  {"id":"w2506","it":"vuotare il sacco","nl":"het hele verhaal vertellen, opbiechten","ph":"vwo-TA-re il SAK-ko","ex":"Dai, vuota il sacco! Cosa è successo?","exNl":"Kom op, vertel het hele verhaal! Wat is er gebeurd?","lesson":282,"level":"B1","cat":"espressione"},

  # ── Les 283: Spreekwoorden ──
  {"id":"w2507","it":"chi va piano va sano e va lontano","nl":"wie langzaam gaat, komt ver","ph":"ki va PJA-no","ex":"Non avere fretta: chi va piano va sano e va lontano.","exNl":"Heb geen haast: wie langzaam gaat, komt ver.","lesson":283,"level":"B1","cat":"espressione"},
  {"id":"w2508","it":"l'appetito vien mangiando","nl":"de eetlust komt al etend","ph":"lap-pe-TI-to vjen","ex":"Prova, l'appetito vien mangiando!","exNl":"Probeer het, de eetlust komt al etend!","lesson":283,"level":"B1","cat":"espressione"},
  {"id":"w2509","it":"il proverbio","nl":"het spreekwoord","ph":"pro-VER-bjo","ex":"Questo proverbio è molto saggio.","exNl":"Dit spreekwoord is heel wijs.","lesson":283,"level":"B1","cat":"sostantivo"},
  {"id":"w2510","it":"la saggezza","nl":"de wijsheid","ph":"sad-DJET-tsa","ex":"I proverbi contengono molta saggezza.","exNl":"Spreekwoorden bevatten veel wijsheid.","lesson":283,"level":"B1","cat":"sostantivo"},
  {"id":"w2511","it":"sbagliando si impara","nl":"van fouten leer je","ph":"zba-LJAN-do si im-PA-ra","ex":"Non preoccuparti: sbagliando si impara.","exNl":"Maak je geen zorgen: van fouten leer je.","lesson":283,"level":"B1","cat":"espressione"},
  {"id":"w2512","it":"ogni lasciata è persa","nl":"elke gemiste kans is verloren","ph":"O-nji la-SHA-ta e PER-sa","ex":"Prendi l'occasione: ogni lasciata è persa.","exNl":"Grijp de kans: elke gemiste kans is verloren.","lesson":283,"level":"B1","cat":"espressione"},
  {"id":"w2513","it":"il detto","nl":"het gezegde","ph":"DET-to","ex":"C'è un detto che dice…","exNl":"Er is een gezegde dat zegt…","lesson":283,"level":"B1","cat":"sostantivo"},
  {"id":"w2514","it":"la morale","nl":"de moraal, de les","ph":"mo-RA-le","ex":"Qual è la morale della storia?","exNl":"Wat is de moraal van het verhaal?","lesson":283,"level":"B1","cat":"sostantivo"},

  # ── Les 284: Vaste werkwoordcombinaties ──
  {"id":"w2515","it":"farcela","nl":"het redden, het klaarspelen","ph":"far-TSHE-la","ex":"Ce la fai da solo?","exNl":"Red je het alleen?","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2516","it":"andarsene","nl":"weggaan, vertrekken","ph":"an-DAR-se-ne","ex":"Me ne vado, è troppo tardi.","exNl":"Ik ga weg, het is te laat.","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2517","it":"cavarsela","nl":"zich er doorheen slaan","ph":"ka-VAR-se-la","ex":"Me la cavo abbastanza bene.","exNl":"Ik red me redelijk goed.","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2518","it":"prendersela","nl":"het kwalijk nemen, boos worden","ph":"PREN-der-se-la","ex":"Non te la prendere, stavo scherzando.","exNl":"Neem het niet kwalijk, ik maakte een grapje.","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2519","it":"volerci","nl":"nodig zijn (tijd/moeite)","ph":"vo-LER-tsji","ex":"Ci vogliono due ore per arrivare.","exNl":"Er zijn twee uur nodig om er te komen.","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2520","it":"metterci","nl":"erover doen (tijd)","ph":"MET-ter-tsji","ex":"Quanto ci metti ad arrivare?","exNl":"Hoe lang doe je erover om er te komen?","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2521","it":"entrarci","nl":"ermee te maken hebben","ph":"en-TRAR-tsji","ex":"Io non c'entro niente!","exNl":"Ik heb er niets mee te maken!","lesson":284,"level":"B1","cat":"verbo"},
  {"id":"w2522","it":"starci","nl":"akkoord gaan, meedoen","ph":"STAR-tsji","ex":"Ci stai a venire al cinema?","exNl":"Ga je mee naar de bioscoop?","lesson":284,"level":"B1","cat":"verbo"},

  # ── Les 285: Formeel schrijven ──
  {"id":"w2523","it":"Egregio","nl":"Geachte (formeel, man)","ph":"e-GRE-djo","ex":"Egregio Dottor Rossi, Le scrivo per…","exNl":"Geachte heer dr. Rossi, ik schrijf u om…","lesson":285,"level":"B1","cat":"espressione"},
  {"id":"w2524","it":"Spettabile","nl":"Geachte (formeel, bedrijf)","ph":"spet-TA-bi-le","ex":"Spettabile Ditta, con la presente…","exNl":"Geacht bedrijf, hierbij…","lesson":285,"level":"B1","cat":"espressione"},
  {"id":"w2525","it":"distinti saluti","nl":"met onderscheiden groet","ph":"dis-TIN-ti sa-LU-ti","ex":"In attesa di riscontro, distinti saluti.","exNl":"In afwachting van uw antwoord, met onderscheiden groet.","lesson":285,"level":"B1","cat":"espressione"},
  {"id":"w2526","it":"la presente","nl":"dit schrijven (formeel)","ph":"pre-ZEN-te","ex":"La presente per comunicarLe che…","exNl":"Hierbij deel ik u mede dat…","lesson":285,"level":"B1","cat":"espressione"},
  {"id":"w2527","it":"in merito a","nl":"met betrekking tot","ph":"in ME-ri-to a","ex":"In merito alla Sua richiesta del 10 marzo…","exNl":"Met betrekking tot uw verzoek van 10 maart…","lesson":285,"level":"B1","cat":"espressione"},
  {"id":"w2528","it":"pregiarsi","nl":"de eer hebben (formeel)","ph":"pre-DJAR-si","ex":"Mi pregio di informarLa che…","exNl":"Ik heb de eer u te informeren dat…","lesson":285,"level":"B1","cat":"verbo"},
  {"id":"w2529","it":"la comunicazione","nl":"de mededeling","ph":"ko-mu-ni-ka-TSJO-ne","ex":"La comunicazione ufficiale è stata inviata.","exNl":"De officiële mededeling is verstuurd.","lesson":285,"level":"B1","cat":"sostantivo"},
  {"id":"w2530","it":"la cortese attenzione","nl":"uw welwillende aandacht","ph":"kor-TE-ze at-ten-TSJO-ne","ex":"RingraziandoLa per la cortese attenzione.","exNl":"U dankend voor uw welwillende aandacht.","lesson":285,"level":"B1","cat":"espressione"},

  # ── Les 286: Informeel taalgebruik ──
  {"id":"w2531","it":"dai","nl":"kom op!, toe maar!","ph":"DAI","ex":"Dai, andiamo al cinema!","exNl":"Kom op, we gaan naar de bioscoop!","lesson":286,"level":"B1","cat":"espressione"},
  {"id":"w2532","it":"boh","nl":"geen idee, weet niet","ph":"BO","ex":"Boh, non so cosa fare stasera.","exNl":"Geen idee, ik weet niet wat ik vanavond moet doen.","lesson":286,"level":"B1","cat":"espressione"},
  {"id":"w2533","it":"figurati","nl":"graag gedaan, maakt niet uit","ph":"fi-GU-ra-ti","ex":"Grazie! — Figurati!","exNl":"Bedankt! — Graag gedaan!","lesson":286,"level":"B1","cat":"espressione"},
  {"id":"w2534","it":"mica","nl":"helemaal niet, toch niet","ph":"MI-ka","ex":"Non è mica facile!","exNl":"Het is helemaal niet makkelijk!","lesson":286,"level":"B1","cat":"avverbio"},
  {"id":"w2535","it":"roba da matti","nl":"te gek voor woorden","ph":"RO-ba da MAT-ti","ex":"Questa è roba da matti!","exNl":"Dit is te gek voor woorden!","lesson":286,"level":"B1","cat":"espressione"},
  {"id":"w2536","it":"che figata","nl":"wat gaaf!, wat cool!","ph":"ke fi-GA-ta","ex":"Che figata questo posto!","exNl":"Wat een gave plek!","lesson":286,"level":"B1","cat":"espressione"},
  {"id":"w2537","it":"tipo","nl":"zoiets als, een soort van","ph":"TI-po","ex":"È tipo un bar, ma più elegante.","exNl":"Het is zoiets als een bar, maar chiquer.","lesson":286,"level":"B1","cat":"avverbio"},
  {"id":"w2538","it":"scherzare","nl":"grappen maken","ph":"sker-TSA-re","ex":"Stavo solo scherzando!","exNl":"Ik maakte maar een grapje!","lesson":286,"level":"B1","cat":"verbo"},

  # ── Les 287: Telefoneren ──
  {"id":"w2539","it":"pronto","nl":"hallo (telefoon)","ph":"PRON-to","ex":"Pronto? Chi parla?","exNl":"Hallo? Met wie spreek ik?","lesson":287,"level":"B1","cat":"espressione"},
  {"id":"w2540","it":"richiamare","nl":"terugbellen","ph":"ri-kja-MA-re","ex":"Posso richiamarLa più tardi?","exNl":"Kan ik u later terugbellen?","lesson":287,"level":"B1","cat":"verbo"},
  {"id":"w2541","it":"la segreteria telefonica","nl":"het antwoordapparaat, de voicemail","ph":"se-gre-te-RI-a","ex":"Lasci un messaggio in segreteria.","exNl":"Spreek een bericht in op de voicemail.","lesson":287,"level":"B1","cat":"sostantivo"},
  {"id":"w2542","it":"il prefisso","nl":"het netnummer","ph":"pre-FIS-so","ex":"Il prefisso di Roma è 06.","exNl":"Het netnummer van Rome is 06.","lesson":287,"level":"B1","cat":"sostantivo"},
  {"id":"w2543","it":"la chiamata","nl":"het telefoongesprek","ph":"kja-MA-ta","ex":"Ho ricevuto una chiamata importante.","exNl":"Ik heb een belangrijk telefoongesprek ontvangen.","lesson":287,"level":"B1","cat":"sostantivo"},
  {"id":"w2544","it":"passare","nl":"doorverbinden","ph":"pas-SA-re","ex":"Le passo il mio collega.","exNl":"Ik verbind u door met mijn collega.","lesson":287,"level":"B1","cat":"verbo"},
  {"id":"w2545","it":"attendere","nl":"wachten (formeel)","ph":"at-TEN-de-re","ex":"Attenda in linea, per favore.","exNl":"Blijft u aan de lijn, alstublieft.","lesson":287,"level":"B1","cat":"verbo"},
  {"id":"w2546","it":"il messaggio vocale","nl":"het spraakbericht","ph":"mes-SAD-djo vo-KA-le","ex":"Ti ho lasciato un messaggio vocale.","exNl":"Ik heb je een spraakbericht achtergelaten.","lesson":287,"level":"B1","cat":"sostantivo"},

  # ── Les 288: Klachten & problemen ──
  {"id":"w2547","it":"lamentarsi","nl":"klagen, zich beklagen","ph":"la-men-TAR-si","ex":"Si lamenta sempre del cibo.","exNl":"Hij klaagt altijd over het eten.","lesson":288,"level":"B1","cat":"verbo"},
  {"id":"w2548","it":"il disguido","nl":"het misverstand, de fout","ph":"dis-GWI-do","ex":"C'è stato un disguido con la prenotazione.","exNl":"Er was een fout met de reservering.","lesson":288,"level":"B1","cat":"sostantivo"},
  {"id":"w2549","it":"il disservizio","nl":"de slechte dienstverlening","ph":"dis-ser-VI-tsjo","ex":"Questo disservizio è inaccettabile.","exNl":"Deze slechte dienstverlening is onacceptabel.","lesson":288,"level":"B1","cat":"sostantivo"},
  {"id":"w2550","it":"pretendere","nl":"eisen, verlangen","ph":"pre-TEN-de-re","ex":"Pretendo una spiegazione!","exNl":"Ik eis een verklaring!","lesson":288,"level":"B1","cat":"verbo"},
  {"id":"w2551","it":"il difetto","nl":"het gebrek, het defect","ph":"di-FET-to","ex":"Il prodotto ha un difetto di fabbricazione.","exNl":"Het product heeft een fabricagefout.","lesson":288,"level":"B1","cat":"sostantivo"},
  {"id":"w2552","it":"reclamare","nl":"reclameren, een klacht indienen","ph":"re-kla-MA-re","ex":"Ho reclamato per il ritardo.","exNl":"Ik heb gereclameerd vanwege de vertraging.","lesson":288,"level":"B1","cat":"verbo"},
  {"id":"w2553","it":"la soluzione","nl":"de oplossing","ph":"so-lu-TSJO-ne","ex":"Dobbiamo trovare una soluzione.","exNl":"We moeten een oplossing vinden.","lesson":288,"level":"B1","cat":"sostantivo"},
  {"id":"w2554","it":"inaccettabile","nl":"onacceptabel","ph":"i-nat-tshet-TA-bi-le","ex":"Questo comportamento è inaccettabile.","exNl":"Dit gedrag is onacceptabel.","lesson":288,"level":"B1","cat":"aggettivo"},

  # ── Les 289: Complimenten & bedankjes ──
  {"id":"w2555","it":"complimenti","nl":"gefeliciteerd, goed gedaan","ph":"kom-pli-MEN-ti","ex":"Complimenti per il tuo lavoro!","exNl":"Goed gedaan met je werk!","lesson":289,"level":"B1","cat":"espressione"},
  {"id":"w2556","it":"grazie mille","nl":"heel erg bedankt","ph":"GRA-tsje MIL-le","ex":"Grazie mille per l'aiuto!","exNl":"Heel erg bedankt voor de hulp!","lesson":289,"level":"B1","cat":"espressione"},
  {"id":"w2557","it":"di niente","nl":"graag gedaan, niets te danken","ph":"di NJEN-te","ex":"Grazie! — Di niente!","exNl":"Bedankt! — Graag gedaan!","lesson":289,"level":"B1","cat":"espressione"},
  {"id":"w2558","it":"ringraziare","nl":"bedanken","ph":"rin-gra-TSJA-re","ex":"Ti ringrazio di cuore.","exNl":"Ik bedank je uit de grond van mijn hart.","lesson":289,"level":"B1","cat":"verbo"},
  {"id":"w2559","it":"apprezzare","nl":"waarderen","ph":"ap-pret-TSA-re","ex":"Apprezzo molto il tuo gesto.","exNl":"Ik waardeer je gebaar heel erg.","lesson":289,"level":"B1","cat":"verbo"},
  {"id":"w2560","it":"che gentile","nl":"wat aardig","ph":"ke djen-TI-le","ex":"Che gentile da parte tua!","exNl":"Wat aardig van je!","lesson":289,"level":"B1","cat":"espressione"},
  {"id":"w2561","it":"fare un complimento","nl":"een compliment maken","ph":"FA-re un kom-pli-MEN-to","ex":"Mi ha fatto un bel complimento.","exNl":"Hij gaf me een mooi compliment.","lesson":289,"level":"B1","cat":"espressione"},
  {"id":"w2562","it":"meritare","nl":"verdienen","ph":"me-ri-TA-re","ex":"Te lo meriti!","exNl":"Je verdient het!","lesson":289,"level":"B1","cat":"verbo"},

  # ── Les 290: Toetsles Blok 17 ──
  {"id":"w2563","it":"l'espressione","nl":"de uitdrukking","ph":"es-pres-SJO-ne","ex":"Questa espressione è molto usata.","exNl":"Deze uitdrukking wordt veel gebruikt.","lesson":290,"level":"B1","cat":"sostantivo"},
  {"id":"w2564","it":"il modo di dire","nl":"het gezegde, de uitdrukking","ph":"MO-do di DI-re","ex":"È un modo di dire italiano.","exNl":"Het is een Italiaans gezegde.","lesson":290,"level":"B1","cat":"sostantivo"},
  {"id":"w2565","it":"colloquiale","nl":"spreektaal-, informeel","ph":"kol-lo-KWJA-le","ex":"È un termine colloquiale.","exNl":"Het is een informeel woord.","lesson":290,"level":"B1","cat":"aggettivo"},
  {"id":"w2566","it":"letterale","nl":"letterlijk","ph":"let-te-RA-le","ex":"Non prendere tutto in senso letterale.","exNl":"Neem niet alles letterlijk.","lesson":290,"level":"B1","cat":"aggettivo"},
  {"id":"w2567","it":"figurato","nl":"figuurlijk","ph":"fi-gu-RA-to","ex":"In senso figurato significa…","exNl":"In figuurlijke zin betekent het…","lesson":290,"level":"B1","cat":"aggettivo"},
  {"id":"w2568","it":"comunicare","nl":"communiceren","ph":"ko-mu-ni-KA-re","ex":"È importante comunicare bene.","exNl":"Het is belangrijk om goed te communiceren.","lesson":290,"level":"B1","cat":"verbo"},
  {"id":"w2569","it":"esprimere","nl":"uitdrukken","ph":"es-PRI-me-re","ex":"Non riesco a esprimere quello che sento.","exNl":"Ik kan niet uitdrukken wat ik voel.","lesson":290,"level":"B1","cat":"verbo"},
  {"id":"w2570","it":"il significato","nl":"de betekenis","ph":"si-nji-fi-KA-to","ex":"Qual è il significato di questa parola?","exNl":"Wat is de betekenis van dit woord?","lesson":290,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# BLOK 18: Herhaling & afsluiting (lessen 291–300)
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS += [
  {"id":291,"title":"Verleden tijden — herhaling","emoji":"⏳","level":"B1",
   "description":"Herhaling van alle verleden tijden: passato prossimo, imperfetto, passato remoto.",
   "grammar":{"title":"Alle verleden tijden",
   "body":"Overzicht verleden tijden:\n\n• Passato prossimo: afgesloten handeling met link naar heden (Ho mangiato la pizza.)\n• Imperfetto: beschrijving, gewoonte, achtergrond (Quando ero piccolo, giocavo.)\n• Passato remoto: afgesloten handeling in ver verleden (Dante scrisse la Divina Commedia.)\n• Trapassato prossimo: voltooid verleden (Quando arrivai, era già partito.)\n\nVuistregel: gebruik passato prossimo in gesproken taal, passato remoto in geschreven taal en Zuid-Italië."},
   "words":["w2571","w2572","w2573","w2574","w2575","w2576","w2577","w2578"]},

  {"id":292,"title":"Congiuntivo — herhaling","emoji":"🧠","level":"B1",
   "description":"Herhaling van de congiuntivo in al zijn vormen.",
   "grammar":{"title":"Congiuntivo overzicht",
   "body":"De congiuntivo heeft vier tijden:\n\n• Presente: Penso che sia vero. (Ik denk dat het waar is.)\n• Passato: Credo che abbia parlato. (Ik geloof dat hij gesproken heeft.)\n• Imperfetto: Pensavo che fosse vero. (Ik dacht dat het waar was.)\n• Trapassato: Credevo che avesse parlato. (Ik dacht dat hij had gesproken.)\n\nGebruik na: che + mening/emotie/twijfel/wens, conjuncties (prima che, sebbene, affinché)."},
   "words":["w2579","w2580","w2581","w2582","w2583","w2584","w2585","w2586"]},

  {"id":293,"title":"Condizionale — herhaling","emoji":"💭","level":"B1",
   "description":"Herhaling van condizionale presente en passato.",
   "grammar":{"title":"Condizionale overzicht",
   "body":"Twee vormen:\n\n• Presente: Vorrei un caffè. (Ik zou graag een koffie willen.)\n• Passato: Avrei voluto venire. (Ik had willen komen.)\n\nGebruik:\n1. Beleefde verzoeken (vorrei, potrebbe)\n2. Wensen en verlangens (Mi piacerebbe…)\n3. Spijt (Avrei dovuto…)\n4. Hypothesen (Se avessi tempo, viaggerei.)"},
   "words":["w2587","w2588","w2589","w2590","w2591","w2592","w2593","w2594"]},

  {"id":294,"title":"Periodo ipotetico — alle types","emoji":"🔀","level":"B1",
   "description":"Alle drie de conditionele types vergeleken.",
   "grammar":{"title":"Periodo ipotetico — alle types",
   "body":"Drie types conditionele zinnen:\n\n• Type 1 (realis): Se piove, resto a casa. — Als het regent, blijf ik thuis. (indicativo + indicativo)\n• Type 2 (irrealis heden): Se avessi tempo, viaggerei. — Als ik tijd had, zou ik reizen. (congiuntivo imperfetto + condizionale presente)\n• Type 3 (irrealis verleden): Se avessi studiato, avrei superato l'esame. — Als ik had gestudeerd, had ik het examen gehaald. (congiuntivo trapassato + condizionale passato)"},
   "words":["w2595","w2596","w2597","w2598","w2599","w2600","w2601","w2602"]},

  {"id":295,"title":"Indirecte rede — verdieping","emoji":"🗣️","level":"B1",
   "description":"Verdieping in de indirecte rede en tijdverschuiving.",
   "grammar":{"title":"Indirecte rede verdieping",
   "body":"Bij de omzetting naar indirecte rede verschuiven tijden:\n\nDirect: \"Vengo domani.\" — Ik kom morgen.\nIndirect: Ha detto che sarebbe venuto il giorno dopo. — Hij zei dat hij de volgende dag zou komen.\n\nVerschuivingen:\npresente → imperfetto\npassato prossimo → trapassato prossimo\nfuturo → condizionale passato\ndomani → il giorno dopo\nieri → il giorno prima"},
   "words":["w2603","w2604","w2605","w2606","w2607","w2608","w2609","w2610"]},

  {"id":296,"title":"Connettivi & tekststructuur","emoji":"📝","level":"B1",
   "description":"Verbindingswoorden voor samenhangende teksten.",
   "grammar":{"title":"Connettivi testuali",
   "body":"Verbindingswoorden voor structuur:\n\nInnanzitutto / In primo luogo — In de eerste plaats\nInoltre / Per di più — Bovendien\nTuttavia / Nonostante ciò — Echter / Desondanks\nQuindi / Perciò / Di conseguenza — Dus / Daarom\nIn conclusione / Per concludere — Tot slot\nIn sintesi — Samengevat"},
   "words":["w2611","w2612","w2613","w2614","w2615","w2616","w2617","w2618"]},

  {"id":297,"title":"Woordvorming & afleidingen","emoji":"🔤","level":"B1",
   "description":"Leer hoe Italiaanse woorden worden gevormd.",
   "grammar":{"title":"Woordvorming",
   "body":"Italiaanse prefixen en suffixen:\n\nPrefixen:\nri- = opnieuw (riscrivere = herschrijven)\ns- = ontkenning (scontento = ontevreden)\nin-/im- = niet (impossibile = onmogelijk)\n\nSuffixen:\n-mente = bijwoord (velocemente = snel)\n-zione = actie/resultaat (educazione = onderwijs)\n-ista = beoefenaar (giornalista = journalist)\n-abile/-ibile = mogelijkheid (possibile = mogelijk)"},
   "words":["w2619","w2620","w2621","w2622","w2623","w2624","w2625","w2626"]},

  {"id":298,"title":"Valse vrienden NL-IT","emoji":"⚠️","level":"B1",
   "description":"Woorden die lijken op Nederlands maar iets anders betekenen.",
   "grammar":{"title":"Valse vrienden",
   "body":"Pas op voor deze valse vrienden:\n\nbravo = goed/knap (NIET braaf)\nsimpatico = sympathiek/leuk (NIET simpel)\neventualmente = eventueel (NIET per ongeluk)\ncamera = kamer (NIET camera → macchina fotografica)\nfirma = handtekening (NIET bedrijf → azienda/ditta)\nnoioso = saai (NIET naïef)\nfatto = feit/gedaan (NIET vet)"},
   "words":["w2627","w2628","w2629","w2630","w2631","w2632","w2633","w2634"]},

  {"id":299,"title":"Formeel register — verdieping","emoji":"👔","level":"B1",
   "description":"Verdieping in het formele register.",
   "grammar":{"title":"Formeel vs. informeel",
   "body":"Het formele register (Lei) is in Italië veel gebruikelijker dan in Nederland:\n\n• Winkels: il commesso zegt Lei tegen klanten\n• Kantoor: collegae gebruiken vaak Lei bij eerste contact\n• E-mails: altijd Lei tenzij je elkaar goed kent\n\nTu → Lei verschuivingen:\nCome stai? → Come sta?\nPuoi…? → Può…? / Potrebbe…?\nDimmi → Mi dica"},
   "words":["w2635","w2636","w2637","w2638","w2639","w2640","w2641","w2642"]},

  {"id":300,"title":"🎓 B1 volledig afgerond!","emoji":"🎓","level":"B1",
   "description":"Gefeliciteerd! Je hebt alle B1-lessen voltooid. Je beheerst nu meer dan 1400 Italiaanse woorden en de belangrijkste grammaticale structuren van het B1-niveau.",
   "grammar":{"title":"🎓 B1 — Complimenti!",
   "body":"Wat je nu kunt:\n\n✓ Verleden tijden gebruiken (passato prossimo, imperfetto, passato remoto)\n✓ De congiuntivo (presente, imperfetto)\n✓ De condizionale (presente en passato)\n✓ Hypothetische zinnen (periodo ipotetico)\n✓ Indirecte rede\n✓ Formeel en informeel register\n✓ Over kunst, wetenschap, politiek en dagelijks leven praten\n✓ Italiaanse uitdrukkingen en spreekwoorden\n\nJe bent nu op B1-niveau. Complimenti e in bocca al lupo per il tuo viaggio linguistico! 🇮🇹"},
   "words":["w2643","w2644","w2645","w2646","w2647","w2648","w2649","w2650"]},
]

WORDS += [
  # ── Les 291: Verleden tijden — herhaling ──
  {"id":"w2571","it":"raccontare","nl":"vertellen","ph":"rak-kon-TA-re","ex":"Mi racconti cosa è successo?","exNl":"Vertel me wat er gebeurd is?","lesson":291,"level":"B1","cat":"verbo"},
  {"id":"w2572","it":"accadere","nl":"gebeuren, plaatsvinden","ph":"ak-ka-DE-re","ex":"Cosa è accaduto ieri sera?","exNl":"Wat is er gisteravond gebeurd?","lesson":291,"level":"B1","cat":"verbo"},
  {"id":"w2573","it":"il ricordo","nl":"de herinnering","ph":"ri-KOR-do","ex":"Ho bei ricordi dell'infanzia.","exNl":"Ik heb mooie herinneringen aan mijn jeugd.","lesson":291,"level":"B1","cat":"sostantivo"},
  {"id":"w2574","it":"il passato","nl":"het verleden","ph":"pas-SA-to","ex":"Non possiamo cambiare il passato.","exNl":"We kunnen het verleden niet veranderen.","lesson":291,"level":"B1","cat":"sostantivo"},
  {"id":"w2575","it":"il presente","nl":"het heden","ph":"pre-ZEN-te","ex":"Vivi nel presente!","exNl":"Leef in het heden!","lesson":291,"level":"B1","cat":"sostantivo"},
  {"id":"w2576","it":"il futuro","nl":"de toekomst","ph":"fu-TU-ro","ex":"Il futuro è pieno di possibilità.","exNl":"De toekomst is vol mogelijkheden.","lesson":291,"level":"B1","cat":"sostantivo"},
  {"id":"w2577","it":"nel frattempo","nl":"intussen, ondertussen","ph":"nel frat-TEM-po","ex":"Nel frattempo ho imparato molto.","exNl":"Intussen heb ik veel geleerd.","lesson":291,"level":"B1","cat":"avverbio"},
  {"id":"w2578","it":"all'improvviso","nl":"plotseling","ph":"al-lim-prov-VI-zo","ex":"All'improvviso cominciò a piovere.","exNl":"Plotseling begon het te regenen.","lesson":291,"level":"B1","cat":"avverbio"},

  # ── Les 292: Congiuntivo — herhaling ──
  {"id":"w2579","it":"benché","nl":"hoewel","ph":"ben-KE","ex":"Benché sia stanco, continuo a studiare.","exNl":"Hoewel ik moe ben, ga ik door met studeren.","lesson":292,"level":"B1","cat":"congiunzione"},
  {"id":"w2580","it":"affinché","nl":"opdat","ph":"af-fin-KE","ex":"Studio affinché possa superare l'esame.","exNl":"Ik studeer opdat ik het examen kan halen.","lesson":292,"level":"B1","cat":"congiunzione"},
  {"id":"w2581","it":"purché","nl":"mits, op voorwaarde dat","ph":"pur-KE","ex":"Vengo purché tu venga anche.","exNl":"Ik kom mits jij ook komt.","lesson":292,"level":"B1","cat":"congiunzione"},
  {"id":"w2582","it":"è necessario che","nl":"het is noodzakelijk dat","ph":"e ne-tshes-SA-rjo ke","ex":"È necessario che tu venga subito.","exNl":"Het is noodzakelijk dat je meteen komt.","lesson":292,"level":"B1","cat":"espressione"},
  {"id":"w2583","it":"è probabile che","nl":"het is waarschijnlijk dat","ph":"e pro-BA-bi-le ke","ex":"È probabile che piova domani.","exNl":"Het is waarschijnlijk dat het morgen regent.","lesson":292,"level":"B1","cat":"espressione"},
  {"id":"w2584","it":"desiderare","nl":"wensen, verlangen","ph":"de-zi-de-RA-re","ex":"Desidero che tutto vada bene.","exNl":"Ik wens dat alles goed gaat.","lesson":292,"level":"B1","cat":"verbo"},
  {"id":"w2585","it":"sperare","nl":"hopen","ph":"spe-RA-re","ex":"Spero che tu stia bene.","exNl":"Ik hoop dat het goed met je gaat.","lesson":292,"level":"B1","cat":"verbo"},
  {"id":"w2586","it":"temere","nl":"vrezen","ph":"te-ME-re","ex":"Temo che sia troppo tardi.","exNl":"Ik vrees dat het te laat is.","lesson":292,"level":"B1","cat":"verbo"},

  # ── Les 293: Condizionale — herhaling ──
  {"id":"w2587","it":"potrebbe","nl":"u/hij zou kunnen","ph":"po-TREB-be","ex":"Potrebbe aiutarmi, per favore?","exNl":"Zou u me kunnen helpen, alstublieft?","lesson":293,"level":"B1","cat":"verbo"},
  {"id":"w2588","it":"mi piacerebbe","nl":"ik zou graag willen","ph":"mi pja-tshe-REB-be","ex":"Mi piacerebbe visitare la Sicilia.","exNl":"Ik zou graag Sicilië willen bezoeken.","lesson":293,"level":"B1","cat":"espressione"},
  {"id":"w2589","it":"sarebbe","nl":"het zou zijn","ph":"sa-REB-be","ex":"Sarebbe bello andare in vacanza.","exNl":"Het zou leuk zijn om op vakantie te gaan.","lesson":293,"level":"B1","cat":"verbo"},
  {"id":"w2590","it":"dovrebbe","nl":"hij/u zou moeten","ph":"dov-REB-be","ex":"Dovrebbe riposarsi di più.","exNl":"U zou meer moeten rusten.","lesson":293,"level":"B1","cat":"verbo"},
  {"id":"w2591","it":"al posto tuo","nl":"in jouw plaats","ph":"al POS-to TU-o","ex":"Al posto tuo, accetterei l'offerta.","exNl":"In jouw plaats zou ik het aanbod accepteren.","lesson":293,"level":"B1","cat":"espressione"},
  {"id":"w2592","it":"volentieri","nl":"graag, met plezier","ph":"vo-len-TJE-ri","ex":"Verrei volentieri alla tua festa.","exNl":"Ik zou graag naar je feest komen.","lesson":293,"level":"B1","cat":"avverbio"},
  {"id":"w2593","it":"nel caso","nl":"voor het geval","ph":"nel KA-zo","ex":"Prendi l'ombrello, nel caso piova.","exNl":"Neem de paraplu mee, voor het geval het regent.","lesson":293,"level":"B1","cat":"espressione"},
  {"id":"w2594","it":"altrimenti","nl":"anders, zo niet","ph":"al-tri-MEN-ti","ex":"Sbrigati, altrimenti perdiamo il treno.","exNl":"Schiet op, anders missen we de trein.","lesson":293,"level":"B1","cat":"avverbio"},

  # ── Les 294: Periodo ipotetico — alle types ──
  {"id":"w2595","it":"se","nl":"als, indien","ph":"SE","ex":"Se studi, impari.","exNl":"Als je studeert, leer je.","lesson":294,"level":"B1","cat":"congiunzione"},
  {"id":"w2596","it":"l'ipotesi","nl":"de hypothese, de veronderstelling","ph":"i-PO-te-zi","ex":"È solo un'ipotesi.","exNl":"Het is slechts een hypothese.","lesson":294,"level":"B1","cat":"sostantivo"},
  {"id":"w2597","it":"immaginare","nl":"je voorstellen, verbeelden","ph":"im-ma-dji-NA-re","ex":"Immagina di essere in Italia.","exNl":"Stel je voor dat je in Italië bent.","lesson":294,"level":"B1","cat":"verbo"},
  {"id":"w2598","it":"supponiamo che","nl":"stel dat","ph":"sup-po-NJA-mo ke","ex":"Supponiamo che tu abbia ragione.","exNl":"Stel dat je gelijk hebt.","lesson":294,"level":"B1","cat":"espressione"},
  {"id":"w2599","it":"realistico","nl":"realistisch","ph":"re-a-LIS-ti-ko","ex":"Il tuo piano non è molto realistico.","exNl":"Je plan is niet erg realistisch.","lesson":294,"level":"B1","cat":"aggettivo"},
  {"id":"w2600","it":"irreale","nl":"onwerkelijk, irreëel","ph":"ir-re-A-le","ex":"È una situazione completamente irreale.","exNl":"Het is een volkomen onwerkelijke situatie.","lesson":294,"level":"B1","cat":"aggettivo"},
  {"id":"w2601","it":"la conseguenza","nl":"het gevolg","ph":"kon-se-GWEN-tsa","ex":"Ogni scelta ha le sue conseguenze.","exNl":"Elke keuze heeft zijn gevolgen.","lesson":294,"level":"B1","cat":"sostantivo"},
  {"id":"w2602","it":"la possibilità","nl":"de mogelijkheid","ph":"pos-si-bi-li-TA","ex":"Ci sono molte possibilità.","exNl":"Er zijn veel mogelijkheden.","lesson":294,"level":"B1","cat":"sostantivo"},

  # ── Les 295: Indirecte rede — verdieping ──
  {"id":"w2603","it":"riferire","nl":"melden, rapporteren","ph":"ri-fe-RI-re","ex":"Gli ho riferito la notizia.","exNl":"Ik heb hem het nieuws gemeld.","lesson":295,"level":"B1","cat":"verbo"},
  {"id":"w2604","it":"sostenere","nl":"beweren, volhouden","ph":"sos-te-NE-re","ex":"Sostiene di non sapere nulla.","exNl":"Hij beweert niets te weten.","lesson":295,"level":"B1","cat":"verbo"},
  {"id":"w2605","it":"affermare","nl":"bevestigen, verklaren","ph":"af-fer-MA-re","ex":"Ha affermato di essere innocente.","exNl":"Hij verklaarde onschuldig te zijn.","lesson":295,"level":"B1","cat":"verbo"},
  {"id":"w2606","it":"negare","nl":"ontkennen","ph":"ne-GA-re","ex":"Ha negato ogni coinvolgimento.","exNl":"Hij ontkende elke betrokkenheid.","lesson":295,"level":"B1","cat":"verbo"},
  {"id":"w2607","it":"chiedere se","nl":"vragen of","ph":"KJE-de-re se","ex":"Mi ha chiesto se volevo venire.","exNl":"Hij vroeg me of ik wilde komen.","lesson":295,"level":"B1","cat":"espressione"},
  {"id":"w2608","it":"rispondere che","nl":"antwoorden dat","ph":"ris-PON-de-re ke","ex":"Ha risposto che non era possibile.","exNl":"Hij antwoordde dat het niet mogelijk was.","lesson":295,"level":"B1","cat":"espressione"},
  {"id":"w2609","it":"il giorno prima","nl":"de dag ervoor","ph":"il DJOR-no PRI-ma","ex":"Ha detto che il giorno prima era a Roma.","exNl":"Hij zei dat hij de dag ervoor in Rome was.","lesson":295,"level":"B1","cat":"espressione"},
  {"id":"w2610","it":"il giorno dopo","nl":"de dag erna","ph":"il DJOR-no DO-po","ex":"Ha promesso che sarebbe venuto il giorno dopo.","exNl":"Hij beloofde dat hij de dag erna zou komen.","lesson":295,"level":"B1","cat":"espressione"},

  # ── Les 296: Connettivi & tekststructuur ──
  {"id":"w2611","it":"innanzitutto","nl":"in de eerste plaats, allereerst","ph":"in-nan-tsi-TUT-to","ex":"Innanzitutto vorrei ringraziarvi.","exNl":"Allereerst wil ik jullie bedanken.","lesson":296,"level":"B1","cat":"avverbio"},
  {"id":"w2612","it":"inoltre","nl":"bovendien","ph":"i-NOL-tre","ex":"Inoltre, vorrei aggiungere che…","exNl":"Bovendien wil ik toevoegen dat…","lesson":296,"level":"B1","cat":"avverbio"},
  {"id":"w2613","it":"pertanto","nl":"daarom, derhalve","ph":"per-TAN-to","ex":"Pertanto propongo di cambiare piano.","exNl":"Daarom stel ik voor om van plan te veranderen.","lesson":296,"level":"B1","cat":"avverbio"},
  {"id":"w2614","it":"nonostante","nl":"ondanks, desondanks","ph":"no-nos-TAN-te","ex":"Nonostante la pioggia, siamo usciti.","exNl":"Ondanks de regen zijn we naar buiten gegaan.","lesson":296,"level":"B1","cat":"congiunzione"},
  {"id":"w2615","it":"di conseguenza","nl":"als gevolg daarvan","ph":"di kon-se-GWEN-tsa","ex":"Ha piovuto molto, di conseguenza il fiume è straripato.","exNl":"Het heeft veel geregend, als gevolg daarvan is de rivier overstroomd.","lesson":296,"level":"B1","cat":"espressione"},
  {"id":"w2616","it":"in sintesi","nl":"samengevat, kortom","ph":"in SIN-te-zi","ex":"In sintesi, il progetto è un successo.","exNl":"Samengevat, het project is een succes.","lesson":296,"level":"B1","cat":"espressione"},
  {"id":"w2617","it":"vale a dire","nl":"dat wil zeggen","ph":"VA-le a DI-re","ex":"È bilingue, vale a dire parla due lingue.","exNl":"Hij is tweetalig, dat wil zeggen hij spreekt twee talen.","lesson":296,"level":"B1","cat":"espressione"},
  {"id":"w2618","it":"in altre parole","nl":"met andere woorden","ph":"in AL-tre pa-RO-le","ex":"In altre parole, non è d'accordo.","exNl":"Met andere woorden, hij is het niet eens.","lesson":296,"level":"B1","cat":"espressione"},

  # ── Les 297: Woordvorming & afleidingen ──
  {"id":"w2619","it":"riscrivere","nl":"herschrijven","ph":"ri-SKRI-ve-re","ex":"Devo riscrivere l'intero testo.","exNl":"Ik moet de hele tekst herschrijven.","lesson":297,"level":"B1","cat":"verbo"},
  {"id":"w2620","it":"scontento","nl":"ontevreden","ph":"skon-TEN-to","ex":"Il cliente è scontento del servizio.","exNl":"De klant is ontevreden over de service.","lesson":297,"level":"B1","cat":"aggettivo"},
  {"id":"w2621","it":"impossibile","nl":"onmogelijk","ph":"im-pos-SI-bi-le","ex":"Niente è impossibile!","exNl":"Niets is onmogelijk!","lesson":297,"level":"B1","cat":"aggettivo"},
  {"id":"w2622","it":"velocemente","nl":"snel (bijwoord)","ph":"ve-lo-tshe-MEN-te","ex":"Il treno va velocemente.","exNl":"De trein gaat snel.","lesson":297,"level":"B1","cat":"avverbio"},
  {"id":"w2623","it":"l'educazione","nl":"het onderwijs, de opvoeding","ph":"e-du-ka-TSJO-ne","ex":"L'educazione è un diritto fondamentale.","exNl":"Onderwijs is een grondrecht.","lesson":297,"level":"B1","cat":"sostantivo"},
  {"id":"w2624","it":"giornaliero","nl":"dagelijks","ph":"djor-na-LJE-ro","ex":"È un'attività giornaliera.","exNl":"Het is een dagelijkse activiteit.","lesson":297,"level":"B1","cat":"aggettivo"},
  {"id":"w2625","it":"incredibile","nl":"ongelooflijk","ph":"in-kre-DI-bi-le","ex":"È una storia incredibile!","exNl":"Het is een ongelooflijk verhaal!","lesson":297,"level":"B1","cat":"aggettivo"},
  {"id":"w2626","it":"riutilizzabile","nl":"herbruikbaar","ph":"ri-u-ti-lid-ZA-bi-le","ex":"Questa borsa è riutilizzabile.","exNl":"Deze tas is herbruikbaar.","lesson":297,"level":"B1","cat":"aggettivo"},

  # ── Les 298: Valse vrienden NL-IT ──
  {"id":"w2627","it":"bravo","nl":"goed, knap (NIET braaf)","ph":"BRA-vo","ex":"Sei stato molto bravo all'esame.","exNl":"Je was heel goed op het examen.","lesson":298,"level":"B1","cat":"aggettivo"},
  {"id":"w2628","it":"la camera","nl":"de kamer (NIET camera)","ph":"KA-me-ra","ex":"La camera da letto è al primo piano.","exNl":"De slaapkamer is op de eerste verdieping.","lesson":298,"level":"B1","cat":"sostantivo"},
  {"id":"w2629","it":"la firma","nl":"de handtekening (NIET bedrijf)","ph":"FIR-ma","ex":"Metta la firma qui.","exNl":"Zet hier uw handtekening.","lesson":298,"level":"B1","cat":"sostantivo"},
  {"id":"w2630","it":"noioso","nl":"saai, vervelend (NIET naïef)","ph":"no-JO-zo","ex":"Il film era molto noioso.","exNl":"De film was heel saai.","lesson":298,"level":"B1","cat":"aggettivo"},
  {"id":"w2631","it":"il fatto","nl":"het feit (NIET vet)","ph":"FAT-to","ex":"Il fatto è che hai ragione.","exNl":"Het feit is dat je gelijk hebt.","lesson":298,"level":"B1","cat":"sostantivo"},
  {"id":"w2632","it":"la cantina","nl":"de kelder (NIET kantine)","ph":"kan-TI-na","ex":"Il vino è in cantina.","exNl":"De wijn staat in de kelder.","lesson":298,"level":"B1","cat":"sostantivo"},
  {"id":"w2633","it":"il burro","nl":"de boter (NIET bureau)","ph":"BUR-ro","ex":"Metti il burro nella padella.","exNl":"Doe de boter in de pan.","lesson":298,"level":"B1","cat":"sostantivo"},
  {"id":"w2634","it":"largo","nl":"breed, wijd (NIET lang)","ph":"LAR-go","ex":"La strada è molto larga.","exNl":"De straat is heel breed.","lesson":298,"level":"B1","cat":"aggettivo"},

  # ── Les 299: Formeel register — verdieping ──
  {"id":"w2635","it":"Le comunico che","nl":"ik deel u mede dat","ph":"le ko-MU-ni-ko ke","ex":"Le comunico che la Sua richiesta è stata approvata.","exNl":"Ik deel u mede dat uw verzoek is goedgekeurd.","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2636","it":"La prego di","nl":"ik verzoek u om","ph":"la PRE-go di","ex":"La prego di rispondere al più presto.","exNl":"Ik verzoek u zo snel mogelijk te antwoorden.","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2637","it":"mi permetta di","nl":"staat u mij toe om","ph":"mi per-MET-ta di","ex":"Mi permetta di presentarmi.","exNl":"Staat u mij toe me voor te stellen.","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2638","it":"a tale proposito","nl":"in dit verband","ph":"a TA-le pro-PO-zi-to","ex":"A tale proposito vorrei aggiungere…","exNl":"In dit verband wil ik toevoegen…","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2639","it":"per quanto riguarda","nl":"wat betreft","ph":"per KWAN-to ri-GWAR-da","ex":"Per quanto riguarda il prezzo, possiamo trattare.","exNl":"Wat de prijs betreft, we kunnen onderhandelen.","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2640","it":"resto a disposizione","nl":"ik sta ter beschikking","ph":"RES-to a dis-po-zi-TSJO-ne","ex":"Resto a Sua completa disposizione.","exNl":"Ik sta geheel ter uw beschikking.","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2641","it":"con i migliori saluti","nl":"met de beste groeten","ph":"kon i mi-LJO-ri sa-LU-ti","ex":"Con i migliori saluti, dott. Bianchi.","exNl":"Met de beste groeten, dr. Bianchi.","lesson":299,"level":"B1","cat":"espressione"},
  {"id":"w2642","it":"gradire","nl":"op prijs stellen (formeel)","ph":"gra-DI-re","ex":"Gradirei ricevere una risposta.","exNl":"Ik zou het op prijs stellen een antwoord te ontvangen.","lesson":299,"level":"B1","cat":"verbo"},

  # ── Les 300: 🎓 B1 volledig afgerond! ──
  {"id":"w2643","it":"il traguardo","nl":"de finish, het einddoel","ph":"tra-GWAR-do","ex":"Hai raggiunto un grande traguardo!","exNl":"Je hebt een groot doel bereikt!","lesson":300,"level":"B1","cat":"sostantivo"},
  {"id":"w2644","it":"la padronanza","nl":"de beheersing","ph":"pa-dro-NAN-tsa","ex":"Hai una buona padronanza dell'italiano.","exNl":"Je hebt een goede beheersing van het Italiaans.","lesson":300,"level":"B1","cat":"sostantivo"},
  {"id":"w2645","it":"il percorso","nl":"het traject, de route","ph":"per-KOR-so","ex":"Il percorso di apprendimento è stato lungo.","exNl":"Het leertraject was lang.","lesson":300,"level":"B1","cat":"sostantivo"},
  {"id":"w2646","it":"la soddisfazione","nl":"de voldoening","ph":"sod-dis-fa-TSJO-ne","ex":"Che soddisfazione aver completato il B1!","exNl":"Wat een voldoening om het B1-niveau te hebben afgerond!","lesson":300,"level":"B1","cat":"sostantivo"},
  {"id":"w2647","it":"proseguire","nl":"doorgaan, vervolgen","ph":"pro-se-GWI-re","ex":"Prosegui con lo studio dell'italiano!","exNl":"Ga door met het studeren van Italiaans!","lesson":300,"level":"B1","cat":"verbo"},
  {"id":"w2648","it":"arricchire","nl":"verrijken","ph":"ar-rik-KI-re","ex":"Studiare le lingue arricchisce la mente.","exNl":"Talen leren verrijkt de geest.","lesson":300,"level":"B1","cat":"verbo"},
  {"id":"w2649","it":"la costanza","nl":"de volharding","ph":"kos-TAN-tsa","ex":"La costanza è la chiave del successo.","exNl":"Volharding is de sleutel tot succes.","lesson":300,"level":"B1","cat":"sostantivo"},
  {"id":"w2650","it":"il successo","nl":"het succes","ph":"sut-TSJES-so","ex":"Il tuo successo è meritato. Complimenti!","exNl":"Je succes is verdiend. Gefeliciteerd!","lesson":300,"level":"B1","cat":"sostantivo"},
]

# ═══════════════════════════════════════════════════════════════════════════════
# SAMENVOEGEN MET BESTAANDE DATA
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    curr_path = os.path.join(DATA_DIR, 'curriculum.json')
    voc_path  = os.path.join(DATA_DIR, 'vocabulary.json')

    with open(curr_path, 'r', encoding='utf-8') as f:
        curriculum = json.load(f)
    with open(voc_path, 'r', encoding='utf-8') as f:
        vocabulary = json.load(f)

    existing_lesson_ids = {l['id'] for l in curriculum}
    existing_word_ids   = {w['id'] for w in vocabulary}

    new_lessons = [l for l in LESSONS if l['id'] not in existing_lesson_ids]
    new_words   = [w for w in WORDS   if w['id'] not in existing_word_ids]

    if not new_lessons:
        print("⚠️  Geen nieuwe lessen om toe te voegen (al aanwezig).")
    else:
        curriculum.extend(new_lessons)
        curriculum.sort(key=lambda l: l['id'])
        with open(curr_path, 'w', encoding='utf-8') as f:
            json.dump(curriculum, f, ensure_ascii=False, indent=2)
        print(f"✅ {len(new_lessons)} lessen toegevoegd → totaal {len(curriculum)}")

    if not new_words:
        print("⚠️  Geen nieuwe woorden om toe te voegen (al aanwezig).")
    else:
        vocabulary.extend(new_words)
        vocabulary.sort(key=lambda w: w['id'])
        with open(voc_path, 'w', encoding='utf-8') as f:
            json.dump(vocabulary, f, ensure_ascii=False, indent=2)
        print(f"✅ {len(new_words)} woorden toegevoegd → totaal {len(vocabulary)}")

    print(f"\n📊 Samenvatting:")
    print(f"   Lessen: {len(curriculum)}")
    print(f"   Woorden: {len(vocabulary)}")
    a1 = sum(1 for w in vocabulary if w['level'] == 'A1')
    a2 = sum(1 for w in vocabulary if w['level'] == 'A2')
    b1 = sum(1 for w in vocabulary if w['level'] == 'B1')
    print(f"   A1={a1}, A2={a2}, B1={b1}")
