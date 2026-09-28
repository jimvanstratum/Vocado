#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_readings_es.py — Spaanse leesteksten A1 (v1.48): één per blok, in de toetsles. Zelfde formaat als build_readings.py."""
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
]
for r in READINGS:
    n = len(r['text'].split()); lo, hi = (35, 80) if r['level'] == 'A1' else (80, 140); assert lo <= n <= hi, (r['id'], n)
    assert all(len(q['options']) == 4 and 0 <= q['answer'] < 4 for q in r['questions'])
OUT.write_text(json.dumps(READINGS, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(READINGS)} Spaanse leesteksten → {OUT.name}')
