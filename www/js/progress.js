/**
 * Progress — beheer van voortgang, XP, streak en voltooide lessen.
 */

const PROG_KEY = 'italiano_progress_v2';

const PROG_DEFAULTS = {
  xp: 0,
  level: 1,
  streak: 0,
  lastActiveDate: null,
  completedLessons: [],   // array van lesson id's (echt voltooid)
  skippedLessons: [],     // array van lesson id's (overgeslagen via plaatsingstoets)
  lessonXP: {},           // lessonId -> xp verdiend in die les
  totalCorrect: 0,
  totalAnswered: 0,
  achievements: [],
  todayXP: 0,             // XP verdiend vandaag (reset elke dag)
  lastXPDate: null,       // datum van laatste dag-XP-reset (YYYY-MM-DD)
  activityLog: {},        // { 'YYYY-MM-DD': true } voor activiteitslog
  passedMilestones: [],   // array van checkpoint-nummers (10, 20, … 90)
  skippedMilestones: [],  // Sprint 14: milestones die via plaatsingstoets overgeslagen zijn
  xpMigratedV10: false,   // Sprint 10: XP herschaald naar nieuwe waarden
  partialLessons: {}       // Sprint 12: { lessonId: pct } voor afgebroken lessen
};

function load() {
  try {
    const raw = localStorage.getItem(PROG_KEY);
    return raw ? { ...PROG_DEFAULTS, ...JSON.parse(raw) } : { ...PROG_DEFAULTS };
  } catch { return { ...PROG_DEFAULTS }; }
}

function save(data) {
  try { localStorage.setItem(PROG_KEY, JSON.stringify(data)); } catch {}
}

export function getProgress() { return load(); }

export function addXP(amount) {
  const p = load();
  p.xp += amount;
  p.level = xpToLevel(p.xp);
  save(p);
  return { xp: p.xp, level: p.level, gained: amount };
}

/** Voeg XP toe aan het dagelijkse tegoed (reset bij nieuwe dag). */
export function addTodayXP(amount) {
  const p = load();
  const today = new Date().toISOString().split('T')[0]; // YYYY-MM-DD
  if (p.lastXPDate !== today) {
    p.todayXP = 0;
    p.lastXPDate = today;
  }
  p.todayXP = (p.todayXP || 0) + amount;
  save(p);
  return p.todayXP;
}

export function getTodayXP() {
  const p = load();
  const today = new Date().toISOString().split('T')[0];
  return p.lastXPDate === today ? (p.todayXP || 0) : 0;
}

export function xpToLevel(xp) {
  // Elke 200 XP = 1 level, max level 30
  return Math.min(30, Math.floor(xp / 200) + 1);
}

export function xpForNextLevel(currentXP) {
  const currentLevel = xpToLevel(currentXP);
  return currentLevel * 200 - currentXP;
}

export function recordAnswer(correct) {
  const p = load();
  p.totalAnswered = (p.totalAnswered || 0) + 1;
  if (correct) p.totalCorrect = (p.totalCorrect || 0) + 1;
  save(p);
}

export function completeLesson(lessonId, xpEarned) {
  const p = load();
  if (!p.completedLessons.includes(lessonId)) {
    p.completedLessons.push(lessonId);
  }
  // Sprint 9: als een les eerder overgeslagen was maar nu echt gemaakt is, verwijder de skip-status
  p.skippedLessons = (p.skippedLessons || []).filter(id => id !== lessonId);
  p.lessonXP = p.lessonXP || {};
  p.lessonXP[lessonId] = (p.lessonXP[lessonId] || 0) + xpEarned;
  save(p);
  addXP(xpEarned);
  checkAchievements();
}

export function isLessonCompleted(lessonId) {
  return load().completedLessons.includes(lessonId);
}

/** Markeer een les als overgeslagen (via plaatsingstoets). Geen XP, geen achievements. */
export function skipLesson(lessonId) {
  const p = load();
  p.skippedLessons = p.skippedLessons || [];
  if (!p.skippedLessons.includes(lessonId) && !p.completedLessons.includes(lessonId)) {
    p.skippedLessons.push(lessonId);
  }
  save(p);
}

export function isLessonSkipped(lessonId) {
  const p = load();
  return (p.skippedLessons || []).includes(lessonId);
}

export function getSkippedLessons() {
  return load().skippedLessons || [];
}

export function getAccuracy() {
  const p = load();
  if (!p.totalAnswered) return 0;
  return Math.round(p.totalCorrect / p.totalAnswered * 100);
}

/** Streak bijhouden — bel dit elke keer als de gebruiker iets doet. */
export function updateStreak() {
  const p = load();
  const today = new Date().toDateString();
  const todayISO = new Date().toISOString().split('T')[0];
  const yesterday = new Date(Date.now() - 86400000).toDateString();

  // Activiteitslog bijhouden voor heatmap
  p.activityLog = p.activityLog || {};
  p.activityLog[todayISO] = true;

  if (p.lastActiveDate === today) {
    save(p);
    return p.streak;
  }

  if (p.lastActiveDate === yesterday) {
    p.streak = (p.streak || 0) + 1;
  } else {
    p.streak = 1;
  }
  p.lastActiveDate = today;
  save(p);
  return p.streak;
}

export function getActivityLog() {
  return load().activityLog || {};
}

export function getStreak() {
  return load().streak || 0;
}

/** Achievement-systeem */
const ACHIEVEMENT_DEFS = [
  { id: 'first_lesson',  label: 'Eerste les!',        emoji: '🎓', condition: p => p.completedLessons.length >= 1 },
  { id: 'five_lessons',  label: '5 lessen gedaan',    emoji: '📚', condition: p => p.completedLessons.length >= 5 },
  { id: 'ten_lessons',   label: '10 lessen gedaan',   emoji: '🏆', condition: p => p.completedLessons.length >= 10 },
  { id: 'all_a1',        label: 'A1 module voltooid', emoji: '🇮🇹', condition: p => p.completedLessons.length >= 20 },
  { id: 'all_a2',        label: 'A2 module voltooid', emoji: '🌟', condition: p => p.completedLessons.length >= 40 },
  { id: 'all_b1',        label: 'B1 module voltooid', emoji: '🏅', condition: p => p.completedLessons.length >= 60 },
  { id: 'streak_3',      label: '3 dagen op rij',     emoji: '🔥', condition: p => p.streak >= 3 },
  { id: 'streak_7',      label: 'Week vol!',          emoji: '💎', condition: p => p.streak >= 7 },
  { id: 'streak_30',     label: 'Maand vol!',         emoji: '👑', condition: p => p.streak >= 30 },
  { id: 'xp_500',        label: '500 XP verdiend',    emoji: '⭐', condition: p => p.xp >= 500 },
  { id: 'xp_1000',       label: '1000 XP verdiend',   emoji: '💫', condition: p => p.xp >= 1000 },
  { id: 'xp_2000',       label: '2000 XP verdiend',   emoji: '🚀', condition: p => p.xp >= 2000 },
  { id: 'accurate',      label: '90% nauwkeurig',     emoji: '🎯', condition: p => p.totalAnswered >= 20 && getAccuracy() >= 90 }
];

export function checkAchievements() {
  const p = load();
  p.achievements = p.achievements || [];
  const newOnes = [];

  ACHIEVEMENT_DEFS.forEach(def => {
    if (!p.achievements.includes(def.id) && def.condition(p)) {
      p.achievements.push(def.id);
      newOnes.push(def);
    }
  });

  if (newOnes.length) save(p);
  return newOnes;
}

export function getAchievements() {
  const p = load();
  const earned = p.achievements || [];
  return ACHIEVEMENT_DEFS.map(def => ({
    ...def,
    earned: earned.includes(def.id)
  }));
}

export function resetProgress() {
  localStorage.removeItem(PROG_KEY);
}

export function getSkippedCount() {
  return (load().skippedLessons || []).length;
}

/** Milestone-systeem — toetslessen na elke 10 voltooide lessen */
export function passMilestone(checkpoint) {
  const p = load();
  p.passedMilestones = p.passedMilestones || [];
  if (!p.passedMilestones.includes(checkpoint)) {
    p.passedMilestones.push(checkpoint);
  }
  save(p);
}

export function isMilestonePassed(checkpoint) {
  return (load().passedMilestones || []).includes(checkpoint);
}

/** Sprint 9.1: Verwijder een milestone-pass (bijv. als deze incorrect auto-passed was). */
export function unpassMilestone(checkpoint) {
  const p = load();
  p.passedMilestones = (p.passedMilestones || []).filter(cp => cp !== checkpoint);
  save(p);
}

/** Sprint 14: Markeer een milestone als overgeslagen (via plaatsingstoets). */
export function skipMilestone(id) {
  const p = load();
  p.passedMilestones  = [...new Set([...(p.passedMilestones  || []), id])];
  p.skippedMilestones = [...new Set([...(p.skippedMilestones || []), id])];
  save(p);
}

export function isMilestoneSkipped(id) {
  return ((load().skippedMilestones) || []).includes(id);
}

export function getPassedMilestones() {
  return load().passedMilestones || [];
}

/**
 * Sprint 9.1: Herstel — verwijder lessen uit skippedLessons die ook in completedLessons
 * staan. Veilig om meerdere keren te draaien.
 */
export function cleanupSkippedCompleted() {
  const p = load();
  const completed = new Set(p.completedLessons || []);
  const before = (p.skippedLessons || []).length;
  p.skippedLessons = (p.skippedLessons || []).filter(id => !completed.has(id));
  if ((p.skippedLessons || []).length !== before) save(p);
}

/**
 * Migreer lessen die door de OUDE plaatsingstoets als "voltooid" met 0 XP zijn
 * opgeslagen naar "overgeslagen". Eenmalig — veilig om meerdere keren aan te roepen.
 */
export function migrateOldSkipped() {
  const p = load();
  const lessonXP = p.lessonXP || {};
  p.completedLessons = p.completedLessons || [];
  p.skippedLessons   = p.skippedLessons   || [];

  // Lessen met 0 XP in completedLessons zijn altijd door de oude plaatsingstoets gezet
  const toMove = p.completedLessons.filter(id => (lessonXP[id] ?? 0) === 0);
  if (toMove.length === 0) return;

  p.completedLessons = p.completedLessons.filter(id => !toMove.includes(id));
  toMove.forEach(id => {
    if (!p.skippedLessons.includes(id)) p.skippedLessons.push(id);
  });
  save(p);
}

/**
 * Sprint 12: Gedeeltelijke lesvoortgang opslaan / ophalen / wissen.
 * Wordt gebruikt om de voortgangsbalk correct te tonen na een afgebroken les.
 */
export function savePartialLesson(lessonId, pct, index, serializedQueue) {
  const p = load();
  p.partialLessons = p.partialLessons || {};
  p.partialLessons[lessonId] = { pct, index, queue: serializedQueue };
  save(p);
}

export function getPartialLesson(lessonId) {
  return ((load().partialLessons) || {})[lessonId] ?? null;
}

export function clearPartialLesson(lessonId) {
  const p = load();
  if (p.partialLessons) {
    delete p.partialLessons[lessonId];
    save(p);
  }
}

/**
 * Sprint 14: Hernummer les-IDs en milestone-IDs na uitbreiding 60 → 90 lessen.
 * A2: oud 21–40 → nieuw 31–50 (+10). B1: oud 41–60 → nieuw 61–80 (+20).
 * Milestones: 30→40, 40→50, 50→70, 60→80. Eenmalig — veilig meerdere keren.
 */
export function migrateToV14() {
  const p = load();
  if ((p.schemaV || 0) >= 14) return;

  const mapLesson = id => id >= 41 ? id + 20 : id >= 21 ? id + 10 : id;
  const mapMs     = id => ({30:40, 40:50, 50:70, 60:80}[id] ?? id);

  if (p.completedLessons) p.completedLessons = p.completedLessons.map(mapLesson);
  if (p.skippedLessons)   p.skippedLessons   = p.skippedLessons.map(mapLesson);
  if (p.passedMilestones) p.passedMilestones = p.passedMilestones.map(mapMs);
  if (p.skippedMilestones) p.skippedMilestones = p.skippedMilestones.map(mapMs);
  if (p.partialLessons) {
    const np = {};
    for (const [k, v] of Object.entries(p.partialLessons)) np[mapLesson(+k)] = v;
    p.partialLessons = np;
  }
  if (p.lessonXP) {
    const nx = {};
    for (const [k, v] of Object.entries(p.lessonXP)) nx[mapLesson(+k)] = v;
    p.lessonXP = nx;
  }

  p.schemaV = 14;
  save(p);
}

/**
 * Sprint 10: Herschaal alle opgeslagen XP naar de nieuwe waarden (factor 0.4).
 * Eenmalig — veilig om meerdere keren aan te roepen.
 */
export function migrateXPToV10() {
  const p = load();
  if (p.xpMigratedV10) return;

  const scale = 0.4;
  p.xp      = Math.round((p.xp      || 0) * scale);
  p.todayXP = Math.round((p.todayXP || 0) * scale);
  p.level   = xpToLevel(p.xp);

  const lessonXP = p.lessonXP || {};
  Object.keys(lessonXP).forEach(key => {
    lessonXP[key] = Math.round((lessonXP[key] || 0) * scale);
  });
  p.lessonXP = lessonXP;

  p.xpMigratedV10 = true;
  save(p);
}
