/**
 * SRS — Spaced Repetition System (SM-2 algoritme)
 * Bepaalt wanneer een woord herhaald moet worden op basis van hoe goed je het kent.
 * Quality: 0=totaal fout, 1=fout maar herkend, 2=fout maar makkelijk, 3=goed met moeite, 4=goed, 5=perfect
 */

const SRS_KEY = 'italiano_srs_v2';

function loadSRSData() {
  try {
    return JSON.parse(localStorage.getItem(SRS_KEY) || '{}');
  } catch { return {}; }
}

function saveSRSData(data) {
  try { localStorage.setItem(SRS_KEY, JSON.stringify(data)); } catch {}
}

/** Geeft de huidige SRS-staat van een woord. */
export function getWordState(wordId) {
  const data = loadSRSData();
  return data[wordId] || {
    interval: 0,
    easeFactor: 2.5,
    repetitions: 0,
    nextReview: null,
    totalReviews: 0,
    correctStreak: 0
  };
}

/** Berekent nieuwe SRS-staat na een antwoord (quality 0-5). */
export function updateWordState(wordId, quality) {
  const data = loadSRSData();
  let state = data[wordId] || {
    interval: 0, easeFactor: 2.5, repetitions: 0,
    nextReview: null, totalReviews: 0, correctStreak: 0
  };

  state.totalReviews = (state.totalReviews || 0) + 1;

  if (quality >= 3) {
    // Correct antwoord
    state.correctStreak = (state.correctStreak || 0) + 1;
    if (state.repetitions === 0) {
      state.interval = 1;
    } else if (state.repetitions === 1) {
      state.interval = 6;
    } else {
      state.interval = Math.round(state.interval * state.easeFactor);
    }
    state.repetitions++;
  } else {
    // Fout antwoord — reset
    state.correctStreak = 0;
    state.repetitions = 0;
    state.interval = 1;
  }

  // Ease factor aanpassen (minimaal 1.3)
  state.easeFactor = Math.max(
    1.3,
    state.easeFactor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
  );

  // Volgende review datum instellen
  const nextDate = new Date();
  nextDate.setDate(nextDate.getDate() + state.interval);
  state.nextReview = nextDate.toISOString();

  data[wordId] = state;
  saveSRSData(data);
  return state;
}

/** Geeft true als een woord vandaag herhaald moet worden. */
export function isWordDue(wordId) {
  const state = getWordState(wordId);
  if (!state.nextReview) return false;
  return new Date(state.nextReview) <= new Date();
}

/** Geeft true als een woord al minstens één keer is gezien. */
export function isWordSeen(wordId) {
  const state = getWordState(wordId);
  return state.totalReviews > 0;
}

/** Geeft true als een woord 'geleerd' is (3+ correcte herhalingen). */
export function isWordLearned(wordId) {
  const state = getWordState(wordId);
  return state.repetitions >= 3;
}

/** Geeft alle woord-IDs die vandaag herhaald moeten worden. */
export function getDueWordIds(allWordIds) {
  return allWordIds.filter(id => isWordDue(id));
}

/** Geeft het percentage geleerd voor een set woord-IDs. */
export function getLearnedPercent(wordIds) {
  if (!wordIds.length) return 0;
  const learned = wordIds.filter(id => isWordSeen(id)).length;
  return Math.round(learned / wordIds.length * 100);
}

/** Reset alle SRS-data. */
export function resetSRS() {
  localStorage.removeItem(SRS_KEY);
}

/**
 * Mapt een antwoordkwaliteit (correct/fout/bijna) naar een SM-2 quality score.
 * correct = 4, bijna = 2, fout = 0
 */
export function qualityFromResult(result) {
  if (result === 'correct') return 4;
  if (result === 'close')   return 2;
  return 0;
}
