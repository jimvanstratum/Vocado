# Vocado — projectdossier voor Claude

Dit bestand is de vaste context voor Claude Code. Lees dit altijd eerst voordat je een sprint begint.
Update dit bestand aan het einde van elke sprint.

---

## Wat is Vocado?

Vocado is een Nederlandse PWA (Progressive Web App) waarmee gebruikers Italiaans en (sinds v1.48) Spaans leren via gestructureerde lessen, flashcards en oefeningen. De app is volledig offline bruikbaar via een Service Worker en werkt als geïnstalleerde app op iOS (Safari → "Zet op beginscherm").

De doelgroep is Nederlandssprekend. Alle UI-tekst is in het Nederlands.

---

## Technische architectuur

- **Geen framework** — vanilla JS + CSS, geen build-tooling buiten `build.py`
- **Bronbestanden**: `www/` (index.html, js/, data/)
- **Productie-build**: `vocado.html` — gegenereerd door `python3 build.py`, alles in één bestand
- **Service Worker**: `www/sw.js` — CACHE_NAME wordt automatisch bijgewerkt bij elke `build.py`-run
- **Hosting**: GitHub Pages
- **Data**: per taal drie JSON-bestanden in `www/data/<code>/` (vocabulary, curriculum, readings) + gedeelde `changelog.json`, geladen via `fetch()` bij opstarten en door `build.py` inline gezet
- **Opslag**: `localStorage` per taal — Italiaans: `italiano_progress_v2` / `italiano_srs_v2` (ongewijzigd), Spaans: `vocado_es_progress_v1` / `vocado_es_srs_v1`; actieve taal in `vocado_active_lang`; instellingen gedeeld (`italiano_settings_v1`, plaatsingstoets per taal)

### Sleutelbestanden

| Bestand | Inhoud |
|---|---|
| `www/index.html` | HTML-structuur + alle CSS + versiestring + cache buster |
| `www/js/app.js` | App-logica: navigatie, lesweergave, SRS, statistieken, plaatsingstoets, taalkeuze |
| `www/js/lang.js` | Taalconfiguratie `LANGS` (naam, vlag, TTS-code, lidwoorden, opslagsleutels) + actieve taal |
| `www/js/conjugation_es.js` | Spaanse vervoegingsmotor (presente, perfecto, imperfecto, futuro) |
| `www/js/exercises.js` | Alle oefentypes (rendering + interactie) |
| `www/data/it/curriculum.json` | Array van les-objecten (Italiaans) |
| `www/data/es/…` | Spaanse data: 60 A1-lessen, 482 woorden (IDs `e001`…), 6 leesteksten — gegenereerd door `scripts/generate_es_a1.py` en `build_readings_es.py` |
| `www/data/it/vocabulary.json` | Array van woord-objecten (Italiaans) |
| `www/data/changelog.json` | Gebruikersgerichte wijzigingen per versie, nieuwste eerst; `build.py` faalt als de bovenste versie niet gelijk is aan de versiestring |
| `www/data/it/readings.json` | 30 leesteksten (één per blok van 10 lessen), gegenereerd door `scripts/build_readings.py` |
| `www/sw.js` | Service Worker |
| `build.py` | Bouwscript: concat → vocado.html; bundelt beide talen inline (`DATA_BY_LANG`); faalt bij dubbele `it`-waarden, dubbele IDs, lessen met onbekend woord-ID of ontbrekende changelog-entry |
| `scripts/generate_a2.py` | Script dat A2-lessen 91–120 heeft gegenereerd (al uitgevoerd) |
| `scripts/generate_b1*.py` | Scripts die B1-lessen 121–300 hebben gegenereerd (al uitgevoerd) |
| `scripts/add_b1_extra.py` | Script dat 60 extra B1-woorden (w2651–w2710) heeft toegevoegd (al uitgevoerd) |
| `scripts/dedupe_b1.py` + `dedupe_b1_data.py` | Deduplicatie v1.44: 451 dubbels verwijderd, 451 gaten gevuld (w2711–w3161), genereert `www/js/idmap.js` (al uitgevoerd) |
| `www/js/idmap.js` | Gegenereerd: verwijderd woord-ID → behouden ID, voor de eenmalige SRS-migratie |
| `scripts/rebalance_a1.py` | A1/A2-herbalancering v1.44: 99 kernwoorden van B1 naar A1/A2 geruild met zeldzame woorden (al uitgevoerd) |
| `scripts/build_readings.py` | Bron van de leesteksten; bewerk hier en draai opnieuw om `readings.json` te genereren |
| `vocado.html` | Productie-build — nooit handmatig bewerken |

### Versie & cache buster

- Versiestring in `www/index.html`: `Vocado · v1.XX · Italiaans · N lessen · M woorden`
- Cache buster: `import './js/app.js?v=N';` — verhoog N bij elke release
- Huidige versie: **v1.49**, cache buster **?v=43**

### Build & deploy

```bash
python3 build.py          # genereert vocado.html + update sw.js CACHE_NAME
git add ...
git commit -m "vX.XX — ..."
# git push: zie 'Bekende issues' voor de juiste credential helper
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

### Meertaligheid (v1.48)

- Het veld `it` in vocabulary.json bevat het doeltaalwoord, ook voor Spaans (veldnaam is historisch)
- Alle UI-teksten halen taalnaam/vlag uit `getLang()`; nooit meer 'Italiaans' hardcoden
- Taal wisselen = `setActiveLangCode()` + `location.reload()`; data en opslag worden dan opnieuw geladen
- Vervoegen: `conjEngine()` in exercises.js kiest de Italiaanse of Spaanse motor; tijd-sleutels zijn gedeeld (`presente`, `passato`, `imperfetto`, `futuro`)
- Spaans A1 spiegelt de Italiaanse A1-thema's (les 1–60), zodat plaatsingstoets en toetslessen zonder aanpassing werken
- Toetsles-punten en niveaubereiken worden uit het actieve curriculum afgeleid (`activeMilestonePoints()`, `levelRange()`)

### Conventies

- **Word-IDs**: `wNNN` (w001–w3161, gaps door deduplicatie)
- **Uniciteit**: elke `it`-waarde komt precies één keer voor (afgedwongen door `build.py` sinds v1.44)
- **Lesson-IDs**: integers 1–300
- **Levels**: `"A1"` (lessen 1–60), `"A2"` (lessen 61–120), `"B1"` (lessen 121–300)
- **Elke les**: exact 8 woorden (uitzondering: les 3 heeft 10 vanwege cijferreeks)
- **Gedeelde woorden**: sommige A1/A2-lessen delen een woord-ID (bijv. `la schiena` in les 7 en 24); het `lesson`/`level`-veld van zo'n woord wijst naar één van beide. Dit is historisch en ongewijzigd
- **Extra woorden buiten lessen**: 193 woorden (133 A1/A2 + 60 B1) staan niet in een `words`-lijst maar hebben wel een `lesson`-nummer; ze draaien mee in de toetsles van dat blok (quizselectie op `w.lesson`) en in het woordenboek. 60 A1/A2-woorden hebben `lesson: 0` en zijn alleen in het woordenboek zichtbaar
- **Zelfstandige naamwoorden**: altijd met lidwoord (`il/la/lo/l'/i/le/gli`)
- **Grammatica**: A1-niveau = herkenning, geen productie van complexe constructies

---

## Huidige staat (v1.49)

### Inhoud
- **300 lessen**: A1 = lessen 1–60, A2 = lessen 61–120, B1 = lessen 121–300
- **2500 woorden**: A1 = 500, A2 = 500, B1 = 1500
- **Woordtelling per les**: 8 (les 3: 10)

### Niveau-indeling (CEFR)
| Niveau | Lessen | Woorden | CEFR-doel |
|--------|--------|---------|-----------|
| A1 | 1–60 | 500 | 500–700 ✓ |
| A2 | 61–120 | 500 | +500–800 ✓ |
| B1 | 121–300 | 1500 | +1500 ✓ |

### Milestone-namen (MILESTONE_NAMES in app.js)

```javascript
10: 'Toetsles A1 — Blok 1 (les 1–10)'  ...t/m...  60: 'Toetsles A1 — Blok 6 (les 51–60)'
70: 'Toetsles A2 — Blok 1 (les 61–70)' ...t/m... 120: 'Toetsles A2 — Blok 6 (les 111–120)'
130: 'Toetsles B1 — Blok 1 (les 121–130)' ...t/m... 300: 'Toetsles B1 — Blok 18 (les 291–300)'
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
| `fill-in-blank-mc` | Zin met gat, kies het juiste woord (4 opties) |
| `fill-in-blank-type` | Zin met gat, typ het ontbrekende woord |
| `matching` | Koppel 4 Italiaanse woorden aan hun Nederlandse vertaling |
| `find-error` | Fout zoeken: Italiaanse zin met één fout woord, tik op het foute woord (v1.42) |
| `sentence-dictation` | Zinsdictee: TTS spreekt een hele zin uit, typ de zin (Levenshtein-tolerantie per woord); zonder TTS fallback naar word-order (v1.42) |
| `category-sort` | Categorie sorteren: 6 woorden (2 categorieën × 3) aan de juiste categorie toewijzen (v1.42) |
| `conjugation` | Vervoegen: infinitief + persoon + tijd, kies (MC) of typ de vorm; bij fout het volledige schema (v1.45) |
| `reading` | Leestekst: tekst van het blok met 3 meerkeuze-begripsvragen (NL), alleen in de toetsles (v1.45) |
| `grammar` | Grammaticakaart met uitleg (tussen oefeningen) |
| `intro` | Les-introductiekaart (eerste kaart van elke les) |

**Oefeningenrij-logica** (buildExerciseQueue in exercises.js):
- Nieuw woord: flashcard → MC of listen-choose → type of listen-type (30% dictee als TTS beschikbaar)
- Per les extra: max 3 word-order, max 2 sentence-choice, max 3 fill-in-blank-mc, 1 matching, max 2 find-error, max 2 sentence-dictation (alleen met TTS), 1 category-sort (als de les 2+ categorieën met elk 2+ woorden heeft)
- Per les extra (v1.45): max 2 conjugation voor vervoegbare werkwoorden (eerst MC, dan typen)
- Review-woord: random type incl. word-order, sentence-choice, fill-in-blank-type, find-error, sentence-dictation, conjugation; plus 1 matching en 1 category-sort per review-sessie als er genoeg woorden zijn
- MC-afleiders komen bij voorkeur uit dezelfde categorie, daarna dezelfde les, daarna hetzelfde niveau (v1.41c)

**Vervoegingsmotor** (exercises.js, v1.45/v1.46): `conjugate(inf, persoon 0–5, tijd)` voor presente, passato prossimo, imperfetto en futuro.
- Regelmatig -are/-ere/-ire incl. spelling (-care/-gare → -chi/-ghi, -ciare/-giare → tu/noi zonder i, -isc- lijst `ISC_VERBS`), wederkerend (`mi/ti/si…`)
- Onregelmatig: tabel `IRREG_PRES` (essere, avere, andare, dire, bere, potere, sapere, …) + families `PRES_FAMILIES` (-tenere, -venire, -porre, -durre, -trarre, -gliere, -parire, -piacere, -uscire); stammen `IRREG_IMPF_STEM`, `IRREG_FUT_STEM`
- `CONJ_EXCLUDE`: onpersoonlijke of niet-werkwoorden (piovere, succedere, benessere, …). `isConjugatable(it)` = enkelvoudige infinitief, niet uitgesloten
- Passato prossimo (v1.46): deelwoord via `PARTICIPLES` (tabel) → `PART_FAMILIES` (achtervoegsel, bijv. -prendere → -preso) → regelmatig; -ere alleen regelmatig als in `REGULAR_ERE`. Hulpwerkwoord: wederkerend → essere, `ESSERE_VERBS` → essere, anders avere; `AMBIG_AUX` (passare, finire, vivere, …) krijgt geen passato. Overeenstemming bij essere: canoniek mannelijk, vrouwelijke vorm telt ook goed (`conjugateAccepted`). `canUseTense(inf, tijd)` bewaakt dit
- Tijdkeuze: A1 presente; A2 presente, passato vanaf les 62 (30%), futuro vanaf les 64 (20%); B1 presente 35% / passato 25% / imperfetto 20% / futuro 20%
- Bij twijfel over een nieuw onregelmatig werkwoord: toevoegen aan tabel of aan `CONJ_EXCLUDE`, nooit stilzwijgend regelmatig laten vervoegen

**Leesteksten** (readings.json, v1.45): `{ id, milestone, level, title, text, questions[3] }`. Wordt als eerste oefening in de toetsles van dat blok gezet (`startMilestoneQuiz`). Richtlengte A1 40–60, A2 80–120, B1 120–200 woorden. Vragen en opties in het Nederlands. Resultaat correct bij ≥ 2 van 3, XP = 3 per goed antwoord.

### App-schermen
- **Home**: lessenlijst met niveau-headers, voortgangsbadges, "Mijn positie"-knop, review-badge
- **Lesson**: oefeningen met voortgangsbalk, terug-bevestiging, XP-beloning na afloop
- **Review**: SRS-sessie met vervallen woorden (SM-2 algoritme)
- **Stats**: leerstatistieken (woorden geleerd, XP, streak)
- **Dictionary**: woordenboek — zoekbaar op Italiaans of Nederlands
- **Achievements**: badge-systeem met vergrendelde/behaalde badges
- **Settings**: thema, TTS-snelheid, dagdoel, data-reset
- **Placement**: plaatsingstoets (15 vragen, 5 groepen van A1-lessen)
- **Lang**: taalkeuze bij eerste start (Italiaans, Spaans; Frans 'binnenkort'); wisselen via de vlagknop op het homescherm of Instellingen › Taal

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
  - Overflow (>20 vervallen woorden) wordt na de sessie met `snoozeWordUntilTomorrow` naar morgen verschoven zodat de review-badge leeg is (v1.41c)
  - De review is automatisch gevuld met foute/moeilijke woorden — geen extra logica nodig
  - `sessionErrors[]` = foute woorden deze sessie (max 10, uniek op `it`-veld)
- **Directe herhaalronde** (`startErrorRetry`): knop "🔁 Oefen foute woorden (N)" op afsluitscherm van les én review, zichtbaar als `sessionErrors.length > 0`. Start mini-sessie via `buildExerciseQueue([], errorWords, VOCAB)` met `isReviewMode = true`. Recursief: nieuwe fouten → knop verschijnt opnieuw.
- **TTS**: Web Speech API, Italiaanse stem, accenten genormaliseerd (é → e)
- **Milestone-quiz**: elke 10 lessen, leestekst van het blok + 20 willekeurige woorden uit de voorgaande lessen
- **Les overslaan**: gebruiker kan lessen markeren als overgeslagen
- **Opnieuw doen**: les herhalen met `forceAll=true`
- **iOS PWA install prompt**: instructie-overlay voor "Zet op beginscherm"
- **iOS viewport**: in de browser volgt `--app-height` de `visualViewport` (v1.31); in de geïnstalleerde app (standalone) krijgt `<html>` de class `standalone` en vult `#app` het scherm via `bottom:0` zonder JS-meting (v1.49, fix voor lege ruimte onder de menubalk na herladen)
- **Wat is er nieuw?** (v1.47): modal met `changelog.json`, te openen via Instellingen › Over Vocado of door op de versieregel te tikken. De homescherm-kaart is in v1.48 op verzoek verwijderd
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
| v1.39 | Sprint 3: UI-fixes (terugnavigatie vergrendeld, kleurthema's, Doorgaan-kaart, SW-update-banner) |
| v1.40 | Sprint 4: B1-content — 60 nieuwe lessen (121–180), 480 woorden, 6 grammaticablokken |
| v1.41 | Sprint 5: B1-uitbreiding (120 extra lessen 181–300, 960 woorden) + 2 nieuwe oefenvormen (gat-invullen, koppelen) |
| v1.41b | Doorgaan-kaart toont toetsles; MILESTONE_POINTS uitgebreid tot 300 |
| v1.41c | Android PWA fix (manifest id/scope), review-badge leeg na sessie (overflow gesnoozed), MC-afleiders uit zelfde categorie, logo offline gecached |
| v1.42 | Sprint 6: drie nieuwe oefenvormen — fout zoeken, zinsdictee, categorie sorteren |
| v1.42b | Fix: buildCategoryGroups geëxporteerd voor category-sort |
| v1.42c | Fix terug-knop: meta-kaarten in history opgeslagen zodat de lock altijd werkt |
| v1.43 | Sprint 7: 60 extra B1-woorden (B1 = 1500, CEFR-doel gehaald) + CLAUDE.md bijgewerkt |
| v1.49 | Taalknop op het homescherm (modal), standalone-hoogtefix iPhone, Vocado-laadscherm i.p.v. Italiaanse vlag, laatste 'Italiano'-teksten weg |
| v1.48 | Sprint 11: Spaans toegevoegd (A1: 60 lessen, 482 woorden, 6 leesteksten, eigen vervoegingsmotor); app meertalig (data, opslag, TTS, teksten per taal); update-kaart op homescherm verwijderd |
| v1.47 | Wat is er nieuw?-overzicht in de interface + update-kaart op het homescherm |
| v1.46 | Sprint 10: passato prossimo in de vervoegingsmotor (deelwoorden, essere/avere, overeenstemming) |
| v1.45 | Sprint 9: twee nieuwe oefenvormen — vervoegen (presente/imperfetto/futuro, MC + typen) en leestekst (30 teksten, in de toetsles); root opgeruimd (oude index.html, italiano-per-vacanza.html, sw.js, manifest.json verwijderd) |
| v1.44 | Sprint 8: deduplicatie — 451 dubbele woorden verwijderd, 451 gaten gevuld met frequente ontbrekende woorden (frequentie-analyse OpenSubtitles + simplemma); SRS-migratie oude→nieuwe IDs; uniciteitscheck in build.py. Plus A1/A2-herbalancering: 99 kernwoorden (uomo, donna, libro, dire, solo, mai, ...) van B1 naar thematisch passende A1/A2-lessen geruild met zeldzame woorden (IDs ongewijzigd) |

---

## CEFR-referentie (Common European Framework of Reference)

Gebruik dit als maatlat bij het plannen van content en features.

### Woordenschat per niveau

| Niveau | Totale woordenschat | Nieuwe woorden | Vocado nu |
|--------|--------------------|--------------------|-----------|
| A1 | ±500–700 | 500–700 | 500 ✓ |
| A2 | ±1.000–1.500 | +500–800 | 500 ✓ |
| B1 | ±2.500–3.000 | +1.500 | 1500 ✓ |
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
| **Lezen** | 30 leesteksten in de toetslessen (v1.45) + voorbeeldzinnen | Meer teksten per les, dialogen |
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

- **Woordenschat A1/A2/B1**: alle drie op CEFR-doel (500 / 500 / 1500), sinds v1.44 zonder dubbels
- **Frequentiedekking** (v1.44-analyse, OpenSubtitles-lemma's zonder functiewoorden): top-500 85%, top-1000 75%, top-2000 59%. Vóór v1.44 was dat 50 / 46 / 37%. Na de herbalancering zitten 99 van de meest frequente kernwoorden in A1/A2-lessen; de overige frequente woorden uit de v1.44-aanvulling (bijv. `potere`, `bastare`, `capitare`) staan bewust in B1-grammaticalessen als vervoegingsmateriaal, omdat de A1-vorm (`posso`) al bestaat
- **B2**: niet aanwezig; pas zinvol na Spaans en leesteksten
- **Spreken**: buiten scope van huidige app (Web Speech API biedt geen beoordelingsfunctie)
- **Leesteksten**: sinds v1.45 één tekst per blok in de toetsles; uitbreiding naar meerdere teksten per blok of dialogen is mogelijk
- **Schrijven**: zinsdictee (v1.42) dekt nu het typen van hele zinnen; vrije schrijfopdrachten blijven buiten scope

---

## Bekende issues

- **git push credentials**: de macOS-keychain levert het token van het GitHub-account `jimvanstratumbcs`, dat geen rechten heeft op `jimvanstratum/Vocado` (403). Beide accounts zijn in `gh` ingelogd. Pushen werkt zonder configuratie te wijzigen met een eenmalige credential helper:
  ```bash
  git -c credential.helper= -c credential.helper='!f() { echo "username=jimvanstratum"; echo "password=$(gh auth token --user jimvanstratum)"; }; f' push
  ```
---

## Gepland / toekomstige sprints

| Prioriteit | Sprint | Toelichting |
|---|---|---|
| Hoog | **Spaans A2 en B1** | A1 is af (v1.48). A2 (les 61–120) en B1 volgen; zelfde aanpak als Italiaans: generatiescript per blok, leesteksten per toetsles |
| Middel | **Meer leesteksten** | Nu 1 per blok (30). Optie: 1 per les of dialogen met TTS per spreker |
| Laag | **Vervoegen uitbreiden** | Condizionale en congiuntivo presente ontbreken nog in de motor (passato prossimo sinds v1.46) |

---

## Spelregels voor Claude

1. **Controleer altijd dit bestand** voordat je een feature voorstelt of implementeert
2. **Stel nooit features voor die al bestaan** (zie geïmplementeerde features hierboven)
3. **Update dit bestand aan het einde van elke sprint** (versie, woordtelling, nieuwe features, geplande items)
4. **Nieuwe woord-IDs**: controleer het hoogste bestaande ID en ga verder vanaf daar
5. **Taal**: alle code-commentaar en gebruikersgerichte tekst in het **Nederlands**
6. **Grammar-niveau**: A1 = herkenning, nooit productie van congiuntivo/passief/stare+gerundio
7. **Commit-formaat**: `vX.XX — Korte beschrijving van wat er veranderd is`
8. **Changelog**: voeg bij elke release bovenaan `www/data/changelog.json` een entry toe in gebruikerstaal (geen technische termen); de build controleert dat de versie overeenkomt
