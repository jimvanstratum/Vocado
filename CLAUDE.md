# Vocado — projectdossier voor Claude

Dit bestand is de vaste context voor Claude Code. Lees dit altijd eerst voordat je een sprint begint.
Update dit bestand aan het einde van elke sprint.

---

## Wat is Vocado?

Vocado is een Nederlandse PWA (Progressive Web App) waarmee gebruikers Italiaans leren via gestructureerde lessen, flashcards en oefeningen. De app is volledig offline bruikbaar via een Service Worker en werkt als geïnstalleerde app op iOS (Safari → "Zet op beginscherm").

De doelgroep is Nederlandssprekend. Alle UI-tekst is in het Nederlands.

---

## Technische architectuur

- **Geen framework** — vanilla JS + CSS, geen build-tooling buiten `build.py`
- **Bronbestanden**: `www/` (index.html, js/, data/)
- **Productie-build**: `vocado.html` — gegenereerd door `python3 build.py`, alles in één bestand
- **Service Worker**: `www/sw.js` — CACHE_NAME wordt automatisch bijgewerkt bij elke `build.py`-run
- **Hosting**: GitHub Pages
- **Data**: twee JSON-bestanden, geladen via `fetch()` bij opstarten
- **Opslag**: `localStorage` voor voortgang (`italiano_progress_v2`) en SRS (`italiano_srs_v2`)

### Sleutelbestanden

| Bestand | Inhoud |
|---|---|
| `www/index.html` | HTML-structuur + alle CSS + versiestring + cache buster |
| `www/js/app.js` | App-logica: navigatie, lesweergave, SRS, statistieken, plaatsingstoets |
| `www/js/exercises.js` | Alle oefentypes (rendering + interactie) |
| `www/data/curriculum.json` | Array van les-objecten |
| `www/data/vocabulary.json` | Array van woord-objecten |
| `www/sw.js` | Service Worker |
| `build.py` | Bouwscript: concat → vocado.html |
| `scripts/generate_a2.py` | Script dat A2-lessen 91–120 heeft gegenereerd (al uitgevoerd) |
| `vocado.html` | Productie-build — nooit handmatig bewerken |

### Versie & cache buster

- Versiestring in `www/index.html`: `Vocado · v1.XX · Italiaans · N lessen · M woorden`
- Cache buster: `import './js/app.js?v=N';` — verhoog N bij elke release
- Huidige versie: **v1.38**, cache buster **?v=29**

### Build & deploy

```bash
python3 build.py          # genereert vocado.html + update sw.js CACHE_NAME
git add ...
git commit -m "vX.XX — ..."
# git push (handmatig — credential-fout op dit apparaat)
```

---

## Datastructuur

### curriculum.json

Array van les-objecten:

```json
{
  "id": 1,
  "title": "Begroetingen",
  "emoji": "👋",
  "level": "A1",
  "description": "Korte beschrijving.",
  "grammar": {
    "title": "Grammatica-onderwerp",
    "body": "Uitleg in het Nederlands."
  },
  "words": ["w001", "w002", "w003", "w004", "w005", "w006", "w007", "w008"]
}
```

### vocabulary.json

Array van woord-objecten:

```json
{
  "id": "w001",
  "it": "ciao",
  "nl": "hallo",
  "ph": "TSJA-o",
  "ex": "Ciao, come stai?",
  "exNl": "Hallo, hoe gaat het?",
  "lesson": 1,
  "level": "A1",
  "cat": "begroeting"
}
```

### Conventies

- **Word-IDs**: `wNNN` (driecijferig, nul-padded: w001–w960, gaps mogelijk door deduplicatie)
- **Lesson-IDs**: integers 1–120
- **Levels**: `"A1"` (lessen 1–60) of `"A2"` (lessen 61–120)
- **Elke les**: exact 8 woorden (uitzondering: les 3 heeft 10 vanwege cijferreeks)
- **Zelfstandige naamwoorden**: altijd met lidwoord (`il/la/lo/l'/i/le/gli`)
- **Grammatica**: A1-niveau = herkenning, geen productie van complexe constructies

---

## Huidige staat (v1.35)

### Inhoud
- **120 lessen**: A1 = lessen 1–60, A2 = lessen 61–120
- **1000 unieke woorden**: A1 = 500, A2 = 500
- **Woordtelling per les**: 8 (les 3: 10)

### Niveau-indeling (CEFR)
| Niveau | Lessen | Woorden | CEFR-doel |
|--------|--------|---------|-----------|
| A1 | 1–60 | 500 | 500–700 ✓ |
| A2 | 61–120 | 500 | +500–800 ✓ |
| B1 | 121+ | 0 | +1500 (niet gestart) |

### Milestone-namen (MILESTONE_NAMES in app.js)

```javascript
10: 'Toetsles A1 — Blok 1 (les 1–10)'  ...t/m...  60: 'Toetsles A1 — Blok 6 (les 51–60)'
70: 'Toetsles A2 — Blok 1 (les 61–70)' ...t/m... 120: 'Toetsles A2 — Blok 6 (les 111–120)'
```

---

## Geïmplementeerde features (volledig werkend)

Controleer deze lijst vóór je een feature voorstelt — stel niets voor dat er al in zit.

### Oefentypes (exercises.js)
| Type | Beschrijving |
|---|---|
| `flashcard` | Toon Italiaans woord, flip voor vertaling |
| `multiple-choice` | Kies de juiste Nederlandse vertaling (4 opties) |
| `listen-choose` | TTS spreekt Italiaans woord uit, kies Nederlandse vertaling |
| `listen-type` | TTS spreekt woord uit, typ het Italiaans (dictee) |
| `type` | Toon Nederlandse vertaling, typ het Italiaans |
| `word-order` | Rangschik losse woorden tot een juiste Italiaanse zin |
| `sentence-choice` | Kies de juiste Nederlandse vertaling van een volledige zin |
| `grammar` | Grammaticakaart met uitleg (tussen oefeningen) |
| `intro` | Les-introductiekaart (eerste kaart van elke les) |

**Oefeningenrij-logica** (buildExerciseQueue in exercises.js):
- Nieuw woord: flashcard → MC of listen-choose → type of listen-type (30% dictee als TTS beschikbaar)
- Review-woord: random type incl. word-order, sentence-choice

### App-schermen
- **Home**: lessenlijst met niveau-headers, voortgangsbadges, "Mijn positie"-knop, review-badge
- **Lesson**: oefeningen met voortgangsbalk, terug-bevestiging, XP-beloning na afloop
- **Review**: SRS-sessie met vervallen woorden (SM-2 algoritme)
- **Stats**: leerstatistieken (woorden geleerd, XP, streak)
- **Dictionary**: woordenboek — zoekbaar op Italiaans of Nederlands
- **Achievements**: badge-systeem met vergrendelde/behaalde badges
- **Settings**: thema, TTS-snelheid, dagdoel, data-reset
- **Placement**: plaatsingstoets (15 vragen, 5 groepen van A1-lessen)
- **Lang**: taalinstelling (alleen Italiaans momenteel)

### Overige features
- **Dark mode**: handmatig (donker/licht/auto) + systeem-voorkeur (`prefers-color-scheme`)
- **Streak-teller**: aaneengesloten leerdagen, zichtbaar op homescherm
- **SRS (SM-2)**: spaced repetition via `srs.js`. Quality-scores per antwoord:
  | Actie | Quality | Gevolg |
  |---|---|---|
  | Flashcard "Moeilijk" | 1 | interval → 1 dag, repetitions reset, easeFactor daalt |
  | MC/type fout | 0 | interval → 1 dag, repetitions reset, easeFactor daalt sterk |
  | MC/type bijna | 2 | interval → 1 dag, easeFactor daalt licht |
  | Flashcard "Goed" / antwoord correct | 3–4 | interval × easeFactor (1d→6d→15d→…) |
  | Flashcard "Makkelijk" | 5 | interval groeit snel, easeFactor stijgt |
  - Dagelijkse herhaling (`getDueWordIds`) = alle woorden met `nextReview <= vandaag`, max 20
  - De review is automatisch gevuld met foute/moeilijke woorden — geen extra logica nodig
  - `sessionErrors[]` = foute woorden deze sessie (max 10, uniek op `it`-veld)
- **Directe herhaalronde** (`startErrorRetry`): knop "🔁 Oefen foute woorden (N)" op afsluitscherm van les én review, zichtbaar als `sessionErrors.length > 0`. Start mini-sessie via `buildExerciseQueue([], errorWords, VOCAB)` met `isReviewMode = true`. Recursief: nieuwe fouten → knop verschijnt opnieuw.
- **TTS**: Web Speech API, Italiaanse stem, accenten genormaliseerd (é → e)
- **Milestone-quiz**: elke 10 lessen, 20 willekeurige woorden uit de voorgaande lessen
- **Les overslaan**: gebruiker kan lessen markeren als overgeslagen
- **Opnieuw doen**: les herhalen met `forceAll=true`
- **iOS PWA install prompt**: instructie-overlay voor "Zet op beginscherm"
- **iOS safe-area fix**: `--app-height` via `window.innerHeight` (v1.31)
- **"Mijn positie"-knop**: springt naar eerste actieve les, met offset van één kaardhoogte

---

## Versiegeschiedenis (samenvatting)

| Versie | Sprint |
|--------|--------|
| v1.31 | iOS safe-area fix + TTS-accenten normalisatie |
| v1.32 | Niveau-herindeling: A1=1–60, A2=61–90, B1 verwijderd |
| v1.33 | A2 uitgebreid: 30 nieuwe lessen (91–120) |
| v1.34 | Opschonen: deduplicatie, mijn-positie scroll-fix |
| v1.35 | Grammar 57/58/60 herschreven, artikel-uniformering lessen 1–20, 51 dubbele artikel-versies verwijderd |
| v1.36 | Directe herhaalronde: "🔁 Oefen foute woorden" knop na les en review |
| v1.37 | Sprint 1: Grammar herschreven lessen 61, 79, 80, 81, 85, 87, 88, 90; "B1 bereikt!"-bug les 80 opgelost |
| v1.38 | Sprint 2: Vocabulaire aangevuld tot A1=500 + A2=500 (totaal 1000 woorden) |

---

## CEFR-referentie (Common European Framework of Reference)

Gebruik dit als maatlat bij het plannen van content en features.

### Woordenschat per niveau

| Niveau | Totale woordenschat | Nieuwe woorden | Vocado nu |
|--------|--------------------|--------------------|-----------|
| A1 | ±500–700 | 500–700 | 500 ✓ |
| A2 | ±1.000–1.500 | +500–800 | 500 ✓ |
| B1 | ±2.500–3.000 | +1.500 | 0 |
| B2+ | ±5.000 | +2.000 | 0 |

### Grammatica per niveau

| Niveau | Kernonderwerpen |
|--------|----------------|
| **A1** | Tegenwoordige tijd, lidwoorden, meervoud, basiszinnen, vraagzinnen, persoonlijke voornaamwoorden |
| **A2** | Verleden tijd (basis), toekomende tijd, vergelijkingen, bijzinnen, reflexieve werkwoorden, voorkeur uitdrukken |
| **B1** | Onvoltooid verleden tijd, perfectum, conditionele zinnen (als…dan), bijzinnen (omdat/hoewel/terwijl), indirecte rede |
| **B2** | Subjonctief, passief productief, geavanceerde conditionalis, nuances en register |

### Vaardigheden die een volledige app dekt

| Vaardigheid | Vocado nu | Doel |
|---|---|---|
| **Lezen** | Voorbeeldzinnen per woord | Leesteksten per niveau (A1: 20–50w, A2: 50–120w, B1: 150–300w) |
| **Luisteren** | TTS per woord/zin | Dialogen (doel: 100–200 stuks) |
| **Schrijven** | Type-oefening (los woord) | Zinnen typen, e-mails, meningen |
| **Spreken** | — | Uitspraakfeedback, rollenspellen |

### Studietijd per niveau (Council of Europe)

| Niveau | Uren studie |
|--------|------------|
| A1 | 80–100 uur |
| A2 | +100 uur |
| B1 | +200 uur |
| B2 | +200 uur |
| C1 | +200 uur |

Tot B2 = circa **600–800 uur** totale studie.

### Implicaties voor Vocado

- **A1 woordtekort**: 432 vs. 500–700 doel → ~70 woorden toe te voegen
- **A2 woordtekort**: 435 vs. 500–800 doel → ~65–365 woorden toe te voegen
- **B1 ontbreekt volledig**: eerste prioriteit na A2-aanvulling
- **Spreken**: buiten scope van huidige app (Web Speech API biedt geen beoordelingsfunctie)
- **Leesteksten**: zinvolle uitbreiding voor A2/B1 — korte dialogen of paragrafen als los oefentype

---

## Bekende issues

- **git push credentials**: werkt niet automatisch op dit apparaat — altijd handmatig pushen
- **Woordtekort A1**: 432 woorden is aan de onderkant van CEFR A1 (doel: 500–700)

---

## Gepland / toekomstige sprints

| Prioriteit | Sprint | Toelichting |
|---|---|---|
| Hoog | **B1-content** | Lessen 121–180, ~500 nieuwe woorden, grammatica: subjonctief, indirecte rede |
| Middel | **Foutanalyse** | Na een les tonen welke woorden fout gingen, gerichte herhaling |
| Middel | **Voortgangsgrafiek** | Woorden per week in stats-scherm |
| Laag | **Push-notificaties** | "Je hebt vandaag nog niet geoefend" (PWA ondersteunt dit) |
| Laag | **Geluidseffecten** | Subtiel geluid bij goed/fout |

---

## Spelregels voor Claude

1. **Controleer altijd dit bestand** voordat je een feature voorstelt of implementeert
2. **Stel nooit features voor die al bestaan** (zie geïmplementeerde features hierboven)
3. **Update dit bestand aan het einde van elke sprint** (versie, woordtelling, nieuwe features, geplande items)
4. **Nieuwe woord-IDs**: controleer het hoogste bestaande ID en ga verder vanaf daar
5. **Taal**: alle code-commentaar en gebruikersgerichte tekst in het **Nederlands**
6. **Grammar-niveau**: A1 = herkenning, nooit productie van congiuntivo/passief/stare+gerundio
7. **Commit-formaat**: `vX.XX — Korte beschrijving van wat er veranderd is`
