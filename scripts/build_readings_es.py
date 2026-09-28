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
]
for r in READINGS:
    n = len(r['text'].split()); assert 35 <= n <= 80, (r['id'], n)
    assert all(len(q['options']) == 4 and 0 <= q['answer'] < 4 for q in r['questions'])
OUT.write_text(json.dumps(READINGS, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'{len(READINGS)} Spaanse leesteksten → {OUT.name}')
