#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_readings_es.py — Spaanse leesteksten A1/A2/B1 (v1.48–v1.59): één per blok, in de toetsles. Zelfde formaat als build_readings.py."""
import json
from pathlib import Path
OUT = Path(__file__).parent.parent / 'www' / 'data' / 'es' / 'readings.json'
def R(milestone, level, title, text, *qs):
    return {'id': f'r{milestone}', 'milestone': milestone, 'level': level, 'title': title, 'text': text.strip(),
            'questions': [{'q': q, 'options': list(opts), 'answer': ans} for q, opts, ans in qs]}
READINGS = [
R(10, 'A1', 'Me llamo Carlos', """
¡Hola! Me llamo Carlos y tengo treinta años. Soy español, de Sevilla. Vivo en una casa pequeña con mi mujer Laura y nuestro hijo Pablo. Pablo tiene cuatro años.
Por la mañana tomo un café con leche y como pan con tomate. Al mediodía comemos en casa. Por la noche vamos al restaurante con los amigos. ¡Buenas noches y buen provecho!
""",
  ('Waar woont Carlos?', ['In Madrid', 'In Sevilla', 'In Barcelona', 'In Valencia'], 1),
  ('Hoe oud is Pablo?', ['Drie jaar', 'Vier jaar', 'Dertig jaar', 'Veertien jaar'], 1),
  ("Wat eet Carlos 's ochtends?", ['Paella', 'Tortilla', 'Brood met tomaat', 'Fruit'], 2)),
R(20, 'A1', 'Un sábado en Madrid', """
Hoy es sábado. Hace buen tiempo: hay sol y no llueve. Tomo el metro y voy al centro.
En el mercado compro una camisa azul y unos zapatos. Cuestan cuarenta euros. Después visito el museo con mi hermana. A las seis volvemos a casa en autobús. El domingo jugamos al fútbol en el parque.
""",
  ('Hoe is het weer?', ['Het regent', 'Het sneeuwt', 'Het is zonnig', 'Het is bewolkt'], 2),
  ('Wat koopt de schrijver op de markt?', ['Een rok en een hoed', 'Een blauw overhemd en schoenen', 'Een jas', 'Een fiets'], 1),
  ('Hoe gaan ze naar huis?', ['Met de metro', 'Met de bus', 'Te voet', 'Met de taxi'], 1)),
R(30, 'A1', 'La casa de Ana', """
Ana vive en un piso en Valencia. La casa tiene una cocina, un baño, un salón y dos dormitorios. El salón es grande y tiene un sofá verde y una ventana grande.
Ana está contenta: su cumpleaños es el viernes. Invita a sus amigos a cenar. Compra fruta, verdura y un postre en el mercado. El fin de semana es siempre tranquilo.
""",
  ('Hoeveel slaapkamers heeft de woning?', ['Eén', 'Twee', 'Drie', 'Vier'], 1),
  ('Welke kleur heeft de bank?', ['Rood', 'Blauw', 'Groen', 'Wit'], 2),
  ('Wanneer is de verjaardag van Ana?', ['Maandag', 'Woensdag', 'Vrijdag', 'Zondag'], 2)),
R(40, 'A1', 'En el hotel', """
¡Buenos días! Tengo una reserva para dos noches. La habitación está en el tercer piso, cerca del ascensor. Es pequeña pero bonita, con vistas al mar.
Tengo dolor de cabeza. Pregunto en recepción: "¿Dónde está la farmacia?" "Todo recto y después a la izquierda, al lado de la iglesia." ¡Muchas gracias! Mañana salimos temprano: tengo hambre y tengo sed, pero estoy contento.
""",
  ('Hoeveel nachten blijft de gast?', ['Eén nacht', 'Twee nachten', 'Drie nachten', 'Een week'], 1),
  ('Wat is het probleem van de gast?', ['Hoofdpijn', 'Koorts', 'Buikpijn', 'Een verkoudheid'], 0),
  ('Waar is de apotheek?', ['Rechts, naast het station', 'Rechtdoor en dan links, bij de kerk', 'In het hotel', 'Aan zee'], 1)),
R(50, 'A1', 'En el bar con Luis', """
Cada mañana voy al bar con mi amigo Luis. Yo tomo un café con leche y un churro, él toma un té. El camarero es simpático y siempre habla del tiempo: hoy está nublado.
Después del bar, Luis va al trabajo en bicicleta. Yo tomo el tren a las ocho y media. El sábado hacemos una excursión a la montaña con la familia. ¡Por fin un poco de deporte!
""",
  ('Wat drinkt Luis?', ['Een koffie met melk', 'Een espresso', 'Thee', 'Water'], 2),
  ('Hoe gaat Luis naar zijn werk?', ['Met de trein', 'Met de auto', 'Op de fiets', 'Te voet'], 2),
  ('Wat doen ze zaterdag?', ['Een uitstapje naar de bergen', 'Naar de bioscoop', 'Voetballen', 'Zwemmen'], 0)),
R(60, 'A1', 'El viaje de Sofía', """
Sofía es profesora en Bilbao. Mañana viaja a Mallorca. En el aeropuerto enseña el pasaporte y el billete en el móvil. El avión despega a las diez.
En Mallorca quiere ver el mar, la naturaleza y un concierto de flamenco. También compra un recuerdo para su abuelo: un pequeño castillo de cerámica. "¡Qué bonito!", dice el abuelo.
""",
  ('Wat is het beroep van Sofía?', ['Dokter', 'Lerares', 'Kok', 'Ingenieur'], 1),
  ('Hoe laat stijgt het vliegtuig op?', ['Om acht uur', 'Om tien uur', 'Om twaalf uur', 'Om zes uur'], 1),
  ('Wat koopt Sofía voor haar opa?', ['Een boek', 'Een keramisch kasteel', 'Een fles wijn', 'Een T-shirt'], 1)),
R(70, 'A2', 'El primer día de trabajo', """
Ayer fue mi primer día de trabajo en una empresa de Barcelona. Estaba nerviosa, pero mis compañeros fueron muy amables. Mi compañera Marta me explicó el proyecto: tenemos que terminar todo antes de la reunión del viernes.
En mi opinión, el trabajo es interesante, pero la reunión fue demasiado larga. El jefe es simpático y muy paciente. Cuando era estudiante, trabajaba en un bar: era más cansado, aunque menos complicado.
Mañana será un día largo. Probablemente empezaré pronto y terminaré tarde. De todos modos, estoy contenta: creo que este trabajo es mejor que el anterior.
""",
  ('Waar werkt de schrijfster?', ['In een bar in Madrid', 'Bij een bedrijf in Barcelona', 'Op een school', 'In een ziekenhuis'], 1),
  ('Wanneer moet het project klaar zijn?', ['Maandag', 'Woensdag', 'Voor de vergadering van vrijdag', 'Volgende maand'], 2),
  ('Hoe vergelijkt ze het oude werk met het nieuwe?', ['Het oude was vermoeiender maar minder ingewikkeld', 'Het oude was makkelijker en leuker', 'Het nieuwe is saaier', 'Er is geen verschil'], 0)),
R(80, 'A2', 'Un domingo en familia', """
El domingo en España es el día de la familia. En mi casa cocinamos juntos: mi madre prepara la paella con ingredientes frescos del mercado y mi padre abre una botella de vino de la casa. Después de comer viene la sobremesa: charlamos durante dos horas y luego todos hacen la siesta.
Por la tarde damos un paseo por el centro y tomamos el aperitivo en la plaza. Mis hermanos hablan de fútbol: su equipo ganó el partido y marcó tres goles.
Por la noche veo una película en el sofá. Me encantan estos días tranquilos: sin estrés, solo la buena vida.
""",
  ('Wie maakt de paella?', ['De vader', 'De moeder', 'De broers', 'De schrijver'], 1),
  ('Wat gebeurt er na het eten?', ['Iedereen gaat voetballen', 'Ze gaan winkelen', 'Natafelen en dan siësta', 'Ze gaan naar de bioscoop'], 2),
  ('Waarover praten de broers?', ['Over politiek', 'Over voetbal', 'Over werk', 'Over muziek'], 1)),
R(90, 'A2', 'El futuro de Lucía', """
Lucía tiene dieciocho años y tiene que elegir carrera. Le gustan las ciencias y quiere estudiar biología en Valencia. Su padre, sin embargo, cree que la economía es más útil.
"El mundo cambia", dice Lucía. "El clima, la contaminación, las energías renovables: necesitamos científicos". Lee las noticias cada día y no se fía de las noticias falsas.
Su meta está clara: sacar el título y después trabajar en un laboratorio. Quizás un día haga un gran descubrimiento. Al final su padre sonríe: "Confía en tu sueño".
""",
  ('Wat wil Lucía studeren?', ['Economie', 'Biologie', 'Rechten', 'Geschiedenis'], 1),
  ('Wat vindt haar vader nuttiger?', ['Biologie', 'Geneeskunde', 'Economie', 'Kunst'], 2),
  ('Wat is het doel van Lucía?', ['Een eigen bedrijf', 'Werken in een laboratorium', 'Journalist worden', 'Politica worden'], 1)),
R(100, 'A2', 'Un piso nuevo', """
El mes pasado busqué un piso de alquiler en Madrid. No fue fácil: los gastos eran altos y el alquiler casi siempre demasiado caro. Por fin encontré un piso amueblado cerca del centro y pagué la fianza.
Mi rutina ha cambiado. Me despierto a las siete, desayuno y voy al trabajo andando. Por la noche cocino: ayer hice una tortilla con patatas del mercado.
El sábado invité a mis amigos a ver una película. Por desgracia, Carlos tuvo que cancelar en el último momento, pero nos divertimos igual.
""",
  ('Wat voor woning heeft de schrijver gevonden?', ['Een groot huis met tuin', 'Een gemeubileerd appartement bij het centrum', 'Een kamer bij een familie', 'Een villa buiten de stad'], 1),
  ('Hoe gaat de schrijver naar het werk?', ['Met de bus', 'Op de fiets', 'Te voet', 'Met de auto'], 2),
  ('Waarom was Carlos er zaterdag niet?', ['Hij was ziek', 'Hij moest op het laatste moment afzeggen', 'Hij was op reis', 'Hij was het vergeten'], 1)),
R(110, 'A2', 'La fiesta de cumpleaños', """
El sábado pasado celebramos el cumpleaños de mi abuela: ¡ochenta años! Lo organizamos todo en secreto. Mi tío reservó un restaurante de cocina gallega, con marisco fresco.
Saqué dinero del cajero para el regalo: un viaje a Sevilla. Cuando llegó, la abuela llevaba el pelo recién arreglado y gafas nuevas. "¡Felicidades!", gritamos todos juntos.
Solo hubo un problema: el horno del restaurante tenía una avería y la tarta llegó tarde. Pero la abuela se rio y dijo: "¡Salud, y que cumplas muchos más!"
""",
  ('Hoe oud wordt de oma?', ['Zeventig', 'Vijfenzeventig', 'Tachtig', 'Negentig'], 2),
  ('Wat is het cadeau?', ['Een bril', 'Een reis naar Sevilla', 'Een taart', 'Een boek'], 1),
  ('Wat was het probleem in het restaurant?', ['Het eten was koud', 'De oven was kapot', 'Er was geen tafel', 'De ober was onbeleefd'], 1)),
R(120, 'A2', 'Las Fallas de Valencia', """
Cada año en marzo, Valencia se transforma. Las Fallas son una tradición muy antigua: los vecinos construyen enormes figuras de cartón y madera, y la última noche las queman en la calle. Hay fuegos artificiales, música y mucha gente en la plaza mayor.
Este año subí muchas fotos a las redes sociales. Un periodista escribió un reportaje sobre la fiesta: según él, el turismo es importante para la economía, pero hay que reducir la basura y proteger el medio ambiente.
He aprendido una cosa: para entender España, hay que vivir sus tradiciones. Ahora comprendo las noticias, me expreso mejor y estoy listo para el siguiente paso: el B1.
""",
  ('Wanneer zijn de Fallas?', ['In augustus', 'In maart', 'In december', 'In mei'], 1),
  ("Wat gebeurt er met de figuren op de laatste avond?", ['Ze worden verkocht', 'Ze worden verbrand', 'Ze gaan naar een museum', 'Ze worden weggegooid'], 1),
  ('Waar moet volgens de journalist op gelet worden?', ['Op de toeristen', 'Op afval en het milieu', 'Op de muziek', 'Op het verkeer'], 1)),
R(130, 'B1', 'Una mudanza inesperada', """
Hace dos años, Elena vivía en Madrid y trabajaba en una oficina del centro. Cada mañana cogía el metro a las ocho, tomaba un café en el mismo bar y llegaba al trabajo siempre puntual. Tenía una vida cómoda, pero sentía que le faltaba algo.
Un día, su empresa le ofreció un puesto en Sevilla. Al principio dudó: no conocía a nadie allí y su familia estaba en Madrid. Sin embargo, aceptó. "Si no lo intento ahora, nunca lo haré", pensó.
Hoy Elena vive en un piso con balcón cerca del río. Dice que fue la mejor decisión de su vida: ha hecho nuevos amigos, ha aprendido a bailar sevillanas y ya no echa de menos el metro. Solo echa de menos el bar de siempre.
""",
  ('Wat deed Elena elke ochtend in Madrid?', ['Ze fietste naar kantoor', 'Ze nam de metro en dronk koffie in dezelfde bar', 'Ze werkte thuis', 'Ze ging naar het zwembad'], 1),
  ('Waarom twijfelde ze over het aanbod?', ['Het salaris was te laag', 'Ze kende niemand in Sevilla en haar familie was in Madrid', 'Ze hield niet van warmte', 'Haar baas was tegen'], 1),
  ('Wat mist ze nog uit Madrid?', ['De metro', 'Haar kantoor', 'De bar van altijd', 'Niets'], 2)),
R(140, 'B1', 'Si pudiera elegir', """
El otro día mi amiga Nuria me preguntó qué haría si me tocara la lotería. Le dije que dejaría de trabajar, viajaría por Sudamérica y compraría una casa junto al mar. Ella se rio: "Te aburrirías en un mes".
Quizá tenga razón. Me gusta mi trabajo, aunque a veces sea estresante. Lo que de verdad cambiaría sería el tiempo: trabajaría menos horas para poder leer, cocinar y ver a mis padres más a menudo.
Nuria, en cambio, no cambiaría casi nada. Solo le gustaría que su jefe la escuchara más. Es curioso: cuando imaginamos otra vida, casi siempre deseamos cosas pequeñas. Ojalá fuera tan fácil conseguirlas sin necesidad de un premio.
""",
  ('Wat zou de schrijver doen met een loterijprijs?', ['Een bedrijf beginnen', 'Stoppen met werken, reizen en een huis aan zee kopen', 'Alles sparen', 'Naar Madrid verhuizen'], 1),
  ('Wat zou de schrijver écht willen veranderen?', ['Zijn baan', 'Zijn stad', 'De tijd: minder uren werken', 'Zijn vrienden'], 2),
  ('Wat zou Nuria graag willen?', ['Een nieuw huis', 'Dat haar baas beter naar haar luistert', 'Een lange reis', 'Meer geld'], 1)),
R(150, 'B1', 'Teletrabajo: ¿sí o no?', """
Desde hace un año, Javier trabaja desde casa tres días a la semana. Al principio le encantaba: no perdía tiempo en el tráfico, comía mejor y podía recoger a sus hijos del colegio. Su jefa, sin embargo, no estaba convencida de que el equipo rindiera igual.
Con el tiempo aparecieron los problemas. Javier tenía la sensación de que nunca desconectaba: contestaba correos por la noche y las reuniones por videollamada eran interminables. Además, echaba de menos las charlas con los compañeros en la cafetería.
Ahora la empresa ha encontrado un equilibrio: dos días en la oficina para reunirse y planificar, y el resto en casa para concentrarse. Javier cree que es lo mejor de los dos mundos, siempre que todos respeten los horarios. "El teletrabajo funciona si la confianza es mutua", dice.
""",
  ('Wat vond Javier aanvankelijk prettig aan thuiswerken?', ['Hij verdiende meer', 'Geen verkeer, beter eten en de kinderen ophalen', 'Hij hoefde niet te vergaderen', 'Hij kon later opstaan'], 1),
  ('Welk probleem ontstond na verloop van tijd?', ['Slechte internetverbinding', 'Hij kon nooit loskoppelen van het werk', 'Hij werd ontslagen', 'Zijn kinderen stoorden hem'], 1),
  ('Wat is de oplossing van het bedrijf?', ['Iedereen weer volledig naar kantoor', 'Twee dagen kantoor, de rest thuis', 'Alleen nog thuiswerken', 'Kortere werkdagen'], 1)),
R(160, 'B1', 'La ciudad sin coches', """
Hace unos años, el ayuntamiento de mi ciudad decidió cerrar el centro al tráfico. Muchos comerciantes protestaron: temían que los clientes dejaran de venir. Los vecinos, en cambio, estaban divididos. Algunos querían menos ruido y aire más limpio; otros pensaban que sería imposible llegar al trabajo.
El primer año fue difícil. Faltaban aparcamientos en las afueras y el transporte público no era suficiente. Pero poco a poco la ciudad cambió: se plantaron árboles, se ampliaron las aceras y aparecieron terrazas donde antes había atascos.
Hoy nadie quiere volver atrás. Las tiendas venden más que antes, los niños juegan en las plazas y el nivel de contaminación ha bajado mucho. Según un estudio reciente, es una de las ciudades más saludables del país. A veces, para mejorar, hay que atreverse a cambiar.
""",
  ('Waar waren de winkeliers bang voor?', ['Hogere belastingen', 'Dat klanten zouden wegblijven', 'Meer lawaai', 'Minder parkeerplaatsen voor henzelf'], 1),
  ('Wat ontbrak er het eerste jaar?', ['Bomen en terrassen', 'Parkeerplaatsen en voldoende openbaar vervoer', 'Fietspaden', 'Winkels'], 1),
  ('Hoe is de situatie nu?', ['De winkels verkopen minder', 'Niemand wil terug naar vroeger', 'De vervuiling is toegenomen', 'Het centrum is weer open voor auto\'s'], 1)),
R(170, 'B1', 'Una entrevista con la abuela', """
Para un trabajo de clase, entrevisté a mi abuela sobre su juventud. Me contó que había nacido en un pueblo pequeño de Extremadura y que de niña ayudaba en el campo mientras sus hermanos iban a la escuela. Me dijo que no había tenido la oportunidad de estudiar, aunque siempre le había gustado leer.
Le pregunté si se había arrepentido de algo. Me respondió que no, porque cada época tiene sus dificultades. A los veinte años se casó y se fue a Barcelona, donde trabajó en una fábrica textil durante treinta años. "Estábamos cansadas, pero éramos jóvenes y nos reíamos mucho", recordó.
Al final me preguntó qué quería ser yo de mayor. Le contesté que todavía no lo sabía. Ella sonrió y me dijo que eso no importaba, siempre que siguiera aprendiendo. Creo que fue la mejor entrevista que he hecho nunca.
""",
  ('Waar werd de oma geboren?', ['In Barcelona', 'In een klein dorp in Extremadura', 'In Madrid', 'In Sevilla'], 1),
  ('Waarom kon zij niet studeren?', ['Ze wilde niet', 'Ze hielp op het land terwijl haar broers naar school gingen', 'Er was geen school', 'Ze was ziek'], 1),
  ('Wat antwoordde de oma op de vraag naar spijt?', ['Dat ze veel spijt had', 'Dat ze geen spijt had, elke tijd heeft zijn moeilijkheden', 'Dat ze liever in het dorp was gebleven', 'Dat ze niet wilde antwoorden'], 1)),
R(180, 'B1', 'Aprender un idioma es un viaje', """
Cuando empecé a estudiar español, pensaba que sería cuestión de aprender listas de palabras. Pronto descubrí que un idioma es mucho más: es una forma de mirar el mundo. Si hubiera sabido lo largo que sería el camino, quizá me habría asustado. Pero cada paso valió la pena.
Al principio entendía poco y hablaba con miedo. Con el tiempo aprendí a pedir en un restaurante, a contar lo que había hecho el fin de semana y a expresar lo que haría si tuviera más tiempo. Descubrí el subjuntivo, que al principio parecía imposible y ahora me parece casi natural.
Hoy leo noticias, sigo series sin subtítulos y tengo amigos con los que solo hablo español. Todavía cometo errores, pero ya no me importan: forman parte del viaje. Si tú también has llegado hasta aquí, enhorabuena. El siguiente bloque te espera. ¡Sigue adelante!
""",
  ('Wat dacht de schrijver aan het begin over een taal leren?', ['Dat het een kwestie van woordenlijsten was', 'Dat het onmogelijk was', 'Dat het snel zou gaan', 'Dat het saai zou zijn'], 0),
  ('Hoe kijkt de schrijver nu tegen de subjuntivo aan?', ['Nog steeds onmogelijk', 'Bijna natuurlijk', 'Onbelangrijk', 'Te moeilijk om te gebruiken'], 1),
  ('Wat vindt de schrijver van fouten maken?', ['Het is beschamend', 'Ze horen bij de reis', 'Het moet vermeden worden', 'Het betekent dat je opnieuw moet beginnen'], 1)),
R(190, 'B1', 'Las tres culturas de Toledo', """
El verano pasado visité Toledo con mi hermano. Antes de ir, había leído que durante la Edad Media convivieron allí cristianos, musulmanes y judíos, y quería comprobarlo con mis propios ojos.
Nada más llegar entendí por qué la llaman la ciudad de las tres culturas. En pocos metros pasamos de una mezquita del siglo X a una sinagoga y después a la catedral gótica. Nuestra guía nos explicó que, cuando el rey Alfonso X fundó la Escuela de Traductores, los sabios de las tres religiones ya habían trabajado juntos durante décadas para traducir textos árabes al latín.
Lo que más me impresionó fue una pequeña iglesia que antes había sido mezquita. Mi hermano, que nunca había mostrado interés por la historia, se quedó callado un buen rato. "Ojalá hubiéramos venido antes", me dijo al salir.
""",
  ('Wat had de schrijver vóór de reis gelezen?', ['Dat Toledo de hoofdstad van Spanje was', 'Dat drie culturen er in de middeleeuwen samenleefden', 'Dat de kathedraal gesloten was', 'Dat er geen gidsen waren'], 1),
  ('Wat vertelde de gids over de Escuela de Traductores?', ['Dat Alfonso X haar sloot', 'Dat geleerden van drie religies al decennia samenwerkten', 'Dat er alleen Latijn werd gesproken', 'Dat ze in de kathedraal zat'], 1),
  ('Hoe reageerde de broer?', ['Hij verveelde zich', 'Hij wilde snel weg', 'Hij werd stil en wenste dat ze eerder waren gekomen', 'Hij kocht een boek'], 2)),
R(200, 'B1', 'El piso que no alquilamos', """
Cuando Marta y yo decidimos vivir juntos, pensábamos que encontrar piso sería fácil. Nos equivocamos. En tres semanas vimos doce pisos: unos eran oscuros, otros estaban mal comunicados y el único que nos gustó costaba casi todo nuestro sueldo.
Al final encontramos uno céntrico, reformado y con gastos incluidos. El casero parecía amable, pero el contrato tenía una cláusula extraña: la fianza no se devolvería si nos íbamos antes de dos años. Marta quería firmar de todos modos. Yo le pedí que esperara un día.
Esa noche llamé a un amigo abogado. Me dijo que, de haber firmado, habríamos perdido más de dos mil euros. Al día siguiente rechazamos el piso. Ahora vivimos en las afueras, en un barrio tranquilo, y pagamos la mitad. Debería haber confiado antes en mi intuición, pero al menos aprendimos a leer la letra pequeña.
""",
  ('Wat was het probleem met de meeste appartementen?', ['Ze waren te groot', 'Ze waren donker, slecht bereikbaar of te duur', 'Ze lagen te ver van het werk van Marta', 'Ze waren al verhuurd'], 1),
  ('Wat stond er in de vreemde clausule?', ['De huur zou elk jaar stijgen', 'Huisdieren waren verboden', 'De borg werd niet terugbetaald bij vertrek binnen twee jaar', 'De huisbaas mocht altijd binnenkomen'], 2),
  ('Hoeveel betalen ze nu?', ['Hetzelfde', 'Het dubbele', 'De helft', 'Niets, ze wonen bij familie'], 2)),
R(210, 'B1', 'La profesora que cambió mi vida', """
En el instituto yo era un alumno mediocre. Sacaba notas justas, no entregaba los deberes a tiempo y mis padres ya no sabían qué hacer conmigo. Nadie creía que fuera a terminar el bachillerato.
Entonces llegó Carmen, la nueva profesora de literatura. El primer día nos pidió que escribiéramos una página sobre algo que nos importara de verdad. Yo escribí sobre mi abuelo, que había sido pastor en los Pirineos. Al devolverme el texto, me dijo que tenía talento y que sería una pena que no lo aprovechara.
No fue magia. Seguí suspendiendo matemáticas y tuve que ir a la recuperación de septiembre. Pero por primera vez alguien esperaba algo de mí, y eso lo cambió todo. Hoy soy periodista. Hace poco escribí a Carmen para darle las gracias. Me contestó que no recordaba aquel texto, pero que se alegraba mucho de que yo sí.
""",
  ('Hoe was de schrijver als leerling?', ['Uitstekend', 'Middelmatig, met matige cijfers en te laat huiswerk', 'Afwezig', 'De beste van de klas in wiskunde'], 1),
  ('Wat vroeg Carmen op de eerste dag?', ['Een toets te maken', 'Een gedicht uit het hoofd te leren', 'Een pagina te schrijven over iets dat echt belangrijk voor hen was', 'Een boek samen te vatten'], 2),
  ('Wat antwoordde Carmen op zijn bedankje?', ['Dat ze de tekst nog precies wist', 'Dat ze het niet meer wist, maar blij was dat hij het wel wist', 'Dat ze geen tijd had', 'Dat hij beter wiskunde had kunnen studeren'], 1)),
R(220, 'B1', 'Dos amigos y una discusión', """
Pablo y yo somos amigos desde la escuela primaria. Siempre nos habíamos llevado bien, hasta que el año pasado discutimos por una tontería: él había olvidado mi cumpleaños y yo le dije cosas que no sentía. Él se ofendió, yo también, y durante cuatro meses no nos hablamos.
Durante ese tiempo me di cuenta de lo mucho que lo echaba de menos. Varias veces quise llamarlo, pero el orgullo me lo impedía. Mi hermana, que es muy sensata, me dijo que si yo no daba el primer paso, quizá lo perdería para siempre.
Al final le escribí un mensaje largo pidiéndole perdón. Me contestó en cinco minutos: él también se arrepentía y no sabía cómo acercarse. Hicimos las paces en el bar de siempre. Ahora, cuando uno de los dos se enfada, respiramos hondo y hablamos antes de que el malentendido crezca. Aprendimos que la amistad vale más que tener razón.
""",
  ('Waarom kregen de vrienden ruzie?', ['Over geld', 'Omdat Pablo de verjaardag vergat en de schrijver te harde dingen zei', 'Omdat ze voor verschillende clubs waren', 'Over een meisje'], 1),
  ('Wat hield de schrijver tegen om te bellen?', ['Hij had geen telefoon', 'Zijn zus verbood het', 'Zijn trots', 'Hij was verhuisd'], 2),
  ('Wat doen ze nu als een van beiden boos wordt?', ['Ze praten een maand niet', 'Ze halen diep adem en praten voordat het misverstand groeit', 'Ze bellen de zus', 'Ze schrijven lange berichten'], 1)),
R(230, 'B1', 'El pueblo que recuperó su río', """
Hace veinte años, el río que pasa por mi pueblo estaba prácticamente muerto. Una fábrica de papel vertía sus residuos sin control, el agua olía mal y hacía décadas que nadie se bañaba en él. Los mayores contaban que, de jóvenes, habían pescado truchas allí, pero a nosotros nos parecía una leyenda.
Todo cambió cuando un grupo de vecinos, entre ellos mi madre, empezó a recoger firmas y a denunciar la situación. Al principio nadie les hacía caso. La fábrica daba trabajo a medio pueblo y muchos temían que cerrara si se endurecían las normas.
Con el tiempo consiguieron que la empresa instalara una depuradora y que el ayuntamiento plantara árboles en las orillas. El agua tardó años en limpiarse, pero hoy el río vuelve a tener vida: hay garzas, nutrias y, sí, truchas. Cada verano los niños se bañan donde antes nadie se atrevía a acercarse. Si aquellos vecinos no hubieran insistido, el río seguiría siendo una cloaca.
""",
  ('Waarom was de rivier twintig jaar geleden bijna dood?', ['Door droogte', 'Door een papierfabriek die ongecontroleerd afval loosde', 'Door toeristen', 'Door een dam'], 1),
  ('Waarom luisterde niemand aanvankelijk naar de buurtbewoners?', ['Ze hadden geen handtekeningen', 'De fabriek gaf werk aan het halve dorp en men vreesde sluiting', 'De burgemeester was op vakantie', 'Het water was al schoon'], 1),
  ('Wat is er nu in de rivier te zien?', ['Alleen algen', 'Reigers, otters en forellen', 'Boten van de fabriek', 'Niets, hij is drooggevallen'], 1)),
R(240, 'B1', 'Una noche de cine en versión original', """
Durante años vi todas las películas dobladas al español. Me parecía lo normal: en España casi todo se dobla, y las voces de los actores de doblaje me resultaban tan familiares como las de mis amigos. Hasta que una amiga me arrastró a un pequeño cine del centro que solo proyecta películas en versión original subtitulada.
La primera media hora fue incómoda. Leía los subtítulos tan deprisa que me perdía los gestos de los actores y, para colmo, el protagonista hablaba con un acento que me costaba entender. Pero poco a poco algo cambió: empecé a escuchar la música de la lengua, los silencios, la ironía que el doblaje a veces borra.
Al salir, mi amiga me preguntó qué me había parecido. Le dije que, si me lo hubiera propuesto un año antes, habría dicho que no. Ahora voy casi todas las semanas. He descubierto que ver cine en versión original es también una forma de viajar: por un par de horas vives en otra lengua sin salir de tu ciudad.
""",
  ('Waarom keek de schrijver jarenlang nagesynchroniseerde films?', ['Omdat ondertitels verboden waren', 'Omdat dat in Spanje normaal is en de stemmen vertrouwd klonken', 'Omdat hij geen Engels sprak', 'Omdat de bioscoop goedkoper was'], 1),
  ('Wat was moeilijk in het eerste halfuur?', ['De zaal was te koud', 'Hij las de ondertitels te snel en miste de gebaren; het accent was lastig', 'De film had geen geluid', 'Zijn vriendin praatte de hele tijd'], 1),
  ('Hoe vaak gaat de schrijver nu naar die bioscoop?', ['Nooit meer', 'Een keer per jaar', 'Bijna elke week', 'Alleen met vakantie'], 2)),
]
for r in READINGS:
    n = len(r['text'].split()); lo, hi = {'A1': (35, 80), 'A2': (80, 140), 'B1': (110, 200)}[r['level']]; assert lo <= n <= hi, (r['id'], n)
    assert all(len(q['options']) == 4 and 0 <= q['answer'] < 4 for q in r['questions'])
OUT.write_text(json.dumps(READINGS, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(READINGS)} Spaanse leesteksten → {OUT.name}')
