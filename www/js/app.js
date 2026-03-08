/**
 * App — Hoofd-router en lifecycle.
 * Sprint 10: segment-locking, thema, XP-migratie, vorige-knop fix.
 */

import { initAudio, setTTSRate, stopSpeech } from './audio.js?v=16';
import { isWordSeen, isWordLearned, getDueWordIds, getLearnedPercent, isWordDue } from './srs.js?v=16';
import { getProgress, addXP, completeLesson, isLessonCompleted, isLessonSkipped, skipLesson, getSkippedCount, getStreak, updateStreak, getAccuracy, getAchievements, checkAchievements, resetProgress, addTodayXP, getTodayXP, passMilestone, isMilestonePassed, skipMilestone, isMilestoneSkipped, unpassMilestone, migrateOldSkipped, cleanupSkippedCompleted, migrateXPToV10, migrateToV14, savePartialLesson, getPartialLesson, clearPartialLesson } from './progress.js?v=16';
import { buildExerciseQueue, renderLessonIntro, renderFlashcard, renderMultipleChoice, renderListenChoose, renderListenType, renderTypeExercise, renderWordOrder, renderGrammarCard, cancelAdvanceTimer } from './exercises.js?v=16';
import { getSettings, saveSettings, isPlacementDone, markPlacementDone, migrateSettingsV10 } from './settings.js?v=16';

// ─── CONSTANTEN ───────────────────────────────────────────────────────────────
const MILESTONE_POINTS = [10, 20, 30, 40, 50, 60, 70, 80, 90];
const MILESTONE_NAMES  = {
  10: 'Toetsles A1 — Blok 1 (les 1–10)',
  20: 'Toetsles A1 — Blok 2 (les 11–20)',
  30: 'Toetsles A1 — Blok 3 (les 21–30)',
  40: 'Toetsles A2 — Blok 1 (les 31–40)',
  50: 'Toetsles A2 — Blok 2 (les 41–50)',
  60: 'Toetsles A2 — Blok 3 (les 51–60)',
  70: 'Toetsles B1 — Blok 1 (les 61–70)',
  80: 'Toetsles B1 — Blok 2 (les 71–80)',
  90: 'Toetsles B1 — Blok 3 (les 81–90)',
};

// Kleuren en bereiken per niveau (voor sectie-headers)
const LEVEL_COLORS = { A1: '#009246', A2: '#f5a623', B1: '#8b5cf6' };
const LEVEL_RANGES = { A1: 'lessen 1–30', A2: 'lessen 31–60', B1: 'lessen 61–90' };

// ─── SEGMENT-HELPERS (Sprint 10) ─────────────────────────────────────────────
/** Segmentnummer van een les-id: 1=les1-10, 2=11-20, ..., 6=51-60 */
function getSegmentNum(lessonId) { return Math.ceil(lessonId / 10); }

/** Is segment segNum ontgrendeld? Segment 1 altijd; hogere segmenten na vorige milestone. */
function isSegmentUnlocked(segNum) {
  if (segNum <= 1) return true;
  const requiredMilestone = (segNum - 1) * 10;
  return isMilestonePassed(requiredMilestone);
}

/** Zijn alle lessen in segment segNum voltooid of overgeslagen? */
function isSegmentComplete(segNum) {
  const start = (segNum - 1) * 10 + 1;
  const end   = segNum * 10;
  const segLessons = CURRICULUM.filter(l => l.id >= start && l.id <= end);
  if (segLessons.length === 0) return false;
  return segLessons.every(l => isLessonCompleted(l.id) || isLessonSkipped(l.id));
}

/** Sprint 13: zijn alle lessen én alle milestones van een niveau afgerond? */
function isLevelComplete(level) {
  const levelLessons = CURRICULUM.filter(l => l.level === level);
  if (levelLessons.length === 0) return false;
  if (!levelLessons.every(l => isLessonCompleted(l.id) || isLessonSkipped(l.id))) return false;
  const segNums = [...new Set(levelLessons.map(l => getSegmentNum(l.id)))];
  return segNums.every(sn => isMilestonePassed(sn * 10));
}

// ─── DATA ────────────────────────────────────────────────────────────────────
let VOCAB = [];
let CURRICULUM = [];

async function loadData() {
  const [vocabRes, currRes] = await Promise.all([
    fetch('./data/vocabulary.json'),
    fetch('./data/curriculum.json')
  ]);
  VOCAB = await vocabRes.json();
  CURRICULUM = await currRes.json();
}

function getWordById(id)    { return VOCAB.find(w => w.id === id); }
function getLessonById(id)  { return CURRICULUM.find(l => l.id === id); }
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// ─── SESSIESTATUS ─────────────────────────────────────────────────────────────
let currentLesson   = null;
let isReviewMode    = false;
let isMilestoneMode = false;
let currentMilestone = null;
let exerciseQueue   = [];
let exerciseIndex   = 0;
let sessionXP       = 0;
let sessionCorrect  = 0;
let sessionTotal    = 0;
let sessionErrors   = [];  // { it, nl } — foutgemaakte woorden deze sessie
let exerciseHistory = [];  // Sprint 9: stack van { xp, correct } voor terug-knop
// Sprint 13: bijhouden welke afgeronde niveaus zijn uitgevouwen (reset bij app-reload)
const expandedLevels = new Set();

// Plaatsingstoets staat
let placementQuestions = [];
let placementIndex     = 0;
let placementScore     = 0;

// ─── HELPERS ─────────────────────────────────────────────────────────────────
function $id(id)            { return document.getElementById(id); }
function getExContainer()   { return $id('exercise-container'); }
function getProgressBar()   { return $id('lesson-progress-bar'); }
function getProgressText()  { return $id('lesson-progress-text'); }
function getSessionXP()     { return $id('session-xp'); }
function getLessonTitle()   { return $id('lesson-title'); }
function getLevelBadge()    { return $id('lesson-level-badge'); }

// ─── ROUTER ──────────────────────────────────────────────────────────────────
export function navigate(screen, data = {}) {
  stopSpeech();

  // Sprint 12/16: sla gedeeltelijke lesvoortgang + queue op bij verlaten van een actieve les
  if (currentLesson && !isMilestoneMode && exerciseIndex > 0
      && exerciseQueue.length > 0 && exerciseIndex < exerciseQueue.length) {
    const pct = Math.round(exerciseIndex / exerciseQueue.length * 100);
    const serializedQ = exerciseQueue.map(item => {
      if (item.type === 'intro' || item.type === 'grammar')
        return { type: item.type, lessonId: currentLesson.id };
      if (!item.word) return null;
      return { type: item.type, wordId: item.word.id };
    }).filter(Boolean);
    savePartialLesson(currentLesson.id, pct, exerciseIndex, serializedQ);
  }

  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));

  const screenId = (screen === 'review') ? 'screen-lesson' : `screen-${screen}`;
  const el = document.getElementById(screenId);
  if (el) el.classList.add('active');

  // Bottom nav: settings en placement zijn "overlay-schermen" zonder nav highlight
  const navScreen = (['review','lesson'].includes(screen))     ? 'home'
                  : (['settings','placement'].includes(screen)) ? ''
                  : screen;  // 'home', 'stats', 'achievements', 'dictionary'
  document.querySelectorAll('.nav-btn[data-screen]').forEach(b =>
    b.classList.toggle('active', navScreen !== '' && b.dataset.screen === navScreen)
  );

  if (screen === 'home')         renderHome();
  if (screen === 'lesson')       startLesson(data.lessonId);
  if (screen === 'review')       startReview();
  if (screen === 'stats')        renderStats();
  if (screen === 'achievements') renderAchievements();
  if (screen === 'settings')     renderSettings();
  if (screen === 'placement')    renderPlacement();
  if (screen === 'dictionary')   renderDictionary();
}

// ─── HOME ─────────────────────────────────────────────────────────────────────
function renderHome() {
  // Sprint 9.1: Eenmalige opruiming van datastatus-bugs
  cleanupSkippedCompleted();   // verwijder lessen die zowel completed als skipped zijn

  const prog     = getProgress();
  const streak   = getStreak();
  const accuracy = getAccuracy();

  // Sprint 9.1: Cursus-voortgangsbalk (vervangt XP/level balk op home)
  const totalLessons    = CURRICULUM.length;
  const completedCount  = (prog.completedLessons || []).length;
  const coursePct       = totalLessons > 0 ? Math.round(completedCount / totalLessons * 100) : 0;
  const cpLabel = $id('cp-label');
  const cpPct   = $id('cp-pct');
  const cpFill  = $id('cp-fill');
  if (cpLabel) cpLabel.textContent = `${completedCount} van ${totalLessons} lessen afgerond`;
  if (cpPct)   cpPct.textContent   = `${coursePct}%`;
  if (cpFill)  cpFill.style.width  = coursePct + '%';

  $id('home-streak').textContent = streak === 0 ? 'Begin vandaag!' : `${streak} dag${streak !== 1 ? 'en' : ''} op rij 🔥`;
  // Sprint 12: quick-stats verwijderd van homescreen (verplaatst naar Voortgang)

  // ── Dagdoel-voortgang ──────────────────────────────────────────────────────
  const settings  = getSettings();
  const dagdoel   = settings.dagdoel || 30;
  const todayXP   = getTodayXP();
  const goalPct   = Math.min(100, Math.round(todayXP / dagdoel * 100));
  const goalDone  = todayXP >= dagdoel;
  const dgSection = $id('daily-goal-section');
  if (dgSection) {
    dgSection.innerHTML = `
      <div class="dg-row">
        <span class="dg-label">Dagdoel</span>
        <span class="dg-val">${todayXP} / ${dagdoel} XP${goalDone ? ' ✅' : ''}</span>
      </div>
      <div class="dg-track"><div class="dg-fill${goalDone ? ' done' : ''}" style="width:${goalPct}%"></div></div>
    `;
  }

  // ── Review-badge ───────────────────────────────────────────────────────────
  const dueIds    = getDueWordIds(VOCAB.map(w => w.id));
  const badge     = $id('review-badge');
  const reviewBtn = $id('review-btn');
  if (dueIds.length > 0) {
    badge.textContent = dueIds.length;
    badge.style.display = 'flex';
    reviewBtn.classList.add('has-due');
  } else {
    badge.style.display = 'none';
    reviewBtn.classList.remove('has-due');
  }

  // ── Soft-lock: aanbevolen volgende les (milestone-aware) ───────────────────
  // Sprint 11: auto-pass milestones in drie gevallen:
  // 1. Alle lessen overgeslagen (plaatsingstoets → A1 overslaan) → unblock hogere niveaus
  // 2. Voltooide lessen voorbij dit milestone (voortgang van vóór segment-locking, Sprint 10)
  // 3. 80%+ écht voltooid in blok en daarna nog lessen gedaan
  MILESTONE_POINTS.forEach(cp => {
    if (isMilestonePassed(cp)) return;
    const segStart   = cp - 9;
    const segLessons = CURRICULUM.filter(l => l.id >= segStart && l.id <= cp);
    if (segLessons.length === 0) return;
    const allSkipped         = segLessons.every(l => isLessonSkipped(l.id));
    const hasCompletedBeyond = CURRICULUM.some(l => l.id > cp && isLessonCompleted(l.id));
    const completedInBlock   = segLessons.filter(l => isLessonCompleted(l.id)).length;
    const lastCompleted      = CURRICULUM.reduce((max, l) => isLessonCompleted(l.id) ? Math.max(max, l.id) : max, 0);
    if (allSkipped || hasCompletedBeyond || (completedInBlock / segLessons.length >= 0.8 && lastCompleted > cp)) {
      if (allSkipped) skipMilestone(cp);
      else passMilestone(cp);
    }
  });

  // Sprint 10: eerste beschikbare milestone (segment volledig + ontgrendeld + niet gehaald)
  const firstAvailableMilestone = MILESTONE_POINTS.find(cp => {
    if (isMilestonePassed(cp)) return false;
    const segNum = getSegmentNum(cp);
    return isSegmentUnlocked(segNum) && isSegmentComplete(segNum);
  });

  // Aanbevolen les: eerste milestone of eerste openstaande les in ontgrendeld segment
  const firstUndoneLesson = CURRICULUM.find(l => {
    if (isLessonCompleted(l.id) || isLessonSkipped(l.id)) return false;
    return isSegmentUnlocked(getSegmentNum(l.id));
  });
  const nextRecommendedId = firstAvailableMilestone !== undefined
    ? null
    : (firstUndoneLesson ? firstUndoneLesson.id : null);

  // ── Lessenlijst — gegroepeerd per niveau ───────────────────────────────────
  const grid = $id('lesson-list');
  grid.innerHTML = '';

  const levels = [...new Set(CURRICULUM.map(l => l.level))];
  levels.forEach(level => {
    const levelLessons = CURRICULUM.filter(l => l.level === level);

    // Sprint 9: tweede en volgende secties krijgen visuele scheidingslijn bovenaan
    const isFirstLevel = levels.indexOf(level) === 0;

    // Sprint 13: volledig afgeronde niveaus → compacte banner; anders normale header
    let target; // grid (normaal) of content-div (compact banner)
    let header; // alleen voor actieve niveaus (voor ↓-knop)
    let hasDoneGroups = false;
    let firstActiveEl = null;

    if (isLevelComplete(level)) {
      const isExpanded = expandedLevels.has(level);
      const segNums13 = [...new Set(levelLessons.map(l => getSegmentNum(l.id)))].sort((a, b) => a - b);
      const banner = document.createElement('div');
      banner.className = 'level-complete-banner' + (isFirstLevel ? '' : ' level-sep');
      banner.innerHTML = `
        <span class="lcb-icon">✅</span>
        <span class="lcb-name">${level} Italiaans</span>
        <span class="lcb-stats">${levelLessons.length} lessen · ${segNums13.length} toetsen</span>
        <span class="lcb-arrow">${isExpanded ? '▾' : '▸'}</span>
      `;
      const content = document.createElement('div');
      content.className = 'level-complete-content' + (isExpanded ? ' open' : '');
      banner.addEventListener('click', () => {
        const open = content.classList.toggle('open');
        banner.querySelector('.lcb-arrow').textContent = open ? '▾' : '▸';
        if (open) expandedLevels.add(level); else expandedLevels.delete(level);
      });
      grid.appendChild(banner);
      grid.appendChild(content);
      target = content;
    } else {
      // ─ Sectie-header met niveau-kleur ────────────────────────────────────
      header = document.createElement('div');
      header.className = 'section-label section-label-list level-section-header' + (isFirstLevel ? '' : ' level-sep');
      header.style.borderLeftColor = LEVEL_COLORS[level] || 'var(--accent)';
      header.innerHTML = `<span class="level-header-name" style="color:${LEVEL_COLORS[level] || 'var(--accent)'}">${level}</span> Italiaans <span class="level-header-range">${LEVEL_RANGES[level] || ''}</span>`;
      grid.appendChild(header);
      target = grid;
    }

    // ─ Sprint 11/12: per segment renderen — segmenttitel + done-group + lessen + milestone inline ─
    const segNums = [...new Set(levelLessons.map(l => getSegmentNum(l.id)))].sort((a, b) => a - b);
    segNums.forEach(segNum => {
      const segStart    = (segNum - 1) * 10 + 1;
      const segEnd      = segNum * 10;
      const segLessons  = levelLessons.filter(l => l.id >= segStart && l.id <= segEnd);
      const cp          = segEnd;   // milestone-ID voor dit segment (10, 20, 30…)
      const segUnlocked  = isSegmentUnlocked(segNum);
      const milestonePassed = isMilestonePassed(cp);

      const doneLessons   = segLessons.filter(l => isLessonCompleted(l.id) || isLessonSkipped(l.id));
      const activeLessons = segLessons.filter(l => !isLessonCompleted(l.id) && !isLessonSkipped(l.id));
      const segComplete   = activeLessons.length === 0;

      // Sprint 12 Item 1: waren alle lessen in dit segment overgeslagen?
      const allSegSkipped = doneLessons.length > 0 && doneLessons.every(l => isLessonSkipped(l.id));

      // Sprint 12 Item 2: segmenttitel ("Deel 1", "Deel 2") boven elk segment
      const localSegIndex = segNums.indexOf(segNum);
      const segHeader = document.createElement('div');
      segHeader.className = 'segment-header';
      segHeader.textContent = `Deel ${localSegIndex + 1}`;
      target.appendChild(segHeader);

      // ── Done-group voor voltooide/overgeslagen lessen in dit segment ───────
      if (doneLessons.length > 0) {
        hasDoneGroups = true;
        const doneCount = doneLessons.filter(l => isLessonCompleted(l.id)).length;
        const skipCount = doneLessons.filter(l => isLessonSkipped(l.id)).length;
        let toggleParts = [];
        if (doneCount > 0) toggleParts.push(`✓ ${doneCount} voltooid`);
        if (skipCount > 0) toggleParts.push(`↷ ${skipCount} overgeslagen`);
        // Sprint 12 Item 1: toon "overgeslagen" i.p.v. "gehaald" als alle lessen overgeslagen zijn
        if (milestonePassed) toggleParts.push((isMilestoneSkipped(cp) || allSegSkipped) ? '↷ toetsles overgeslagen' : '🎖️ toetsles gehaald');

        const toggle = document.createElement('div');
        toggle.className = 'done-group-toggle';
        toggle.innerHTML = `<span class="done-group-text">${toggleParts.join(' · ')}</span><span class="done-group-arrow">▸</span>`;

        const doneContainer = document.createElement('div');
        doneContainer.className = 'done-group-container';

        doneLessons.forEach(lesson => {
          const completed = isLessonCompleted(lesson.id);
          const skipped   = isLessonSkipped(lesson.id);
          const card = document.createElement('div');
          card.className = ['lesson-card', completed ? 'done' : '', skipped ? 'skipped' : ''].filter(Boolean).join(' ');
          card.innerHTML = `
            <div class="lesson-num">${completed ? '✓' : '↷'}</div>
            <div class="lesson-card-mid">
              <div class="lesson-emoji-title">
                <span class="lesson-emoji">${lesson.emoji}</span>
                <span class="lesson-title">${lesson.title}</span>
                ${skipped ? '<span class="lesson-skip-badge">Overgeslagen</span>' : ''}
              </div>
              <div class="lesson-meta">${lesson.level} · ${lesson.words.length} woorden</div>
            </div>
            <div class="lesson-card-right"><div class="lesson-pct">${completed ? '✓' : ''}</div></div>
          `;
          card.addEventListener('click', () => navigate('lesson', { lessonId: lesson.id }));
          doneContainer.appendChild(card);
        });

        // Gehaalde milestone BINNEN done-group (herhaling mogelijk)
        if (milestonePassed) {
          const mCard = document.createElement('div');
          mCard.className = 'milestone-card passed';
          mCard.style.cursor = 'pointer';
          // Sprint 14: badge en subtekst afhankelijk van skipMilestone of allSegSkipped
          const msOvergeslagen = isMilestoneSkipped(cp) || allSegSkipped;
          const badgeClass = msOvergeslagen ? 'overgeslagen' : 'passed';
          const badgeText  = msOvergeslagen ? 'Overgeslagen ↷' : 'Gehaald ✓';
          const subText    = msOvergeslagen
            ? 'Overgeslagen via plaatsingstoets · tikken om alsnog te doen'
            : 'Toetsles · tikken om opnieuw te doen';
          mCard.innerHTML = `
            <div class="milestone-icon">${msOvergeslagen ? '↷' : '🎖️'}</div>
            <div class="milestone-mid">
              <div class="milestone-title">${MILESTONE_NAMES[cp] || `Toetsles ${cp}`}</div>
              <div class="milestone-sub">${subText}</div>
            </div>
            <div class="milestone-right"><span class="milestone-badge ${badgeClass}">${badgeText}</span></div>
          `;
          mCard.addEventListener('click', () => startMilestoneQuiz(cp));
          doneContainer.appendChild(mCard);
        }

        toggle.addEventListener('click', () => {
          const isOpen = doneContainer.classList.toggle('open');
          toggle.querySelector('.done-group-arrow').textContent = isOpen ? '▾' : '▸';
        });
        target.appendChild(toggle);
        target.appendChild(doneContainer);
      }

      // ── Openstaande lessen in dit segment ────────────────────────────────────
      activeLessons.forEach(lesson => {
        const isLocked  = !segUnlocked;
        const isNext    = !isLocked && lesson.id === nextRecommendedId;
        // Sprint 12 Item 5: gebruik opgeslagen gedeeltelijke voortgang indien beschikbaar
        const partialData = getPartialLesson(lesson.id);
        const hasPartial  = partialData !== null;
        // Nieuw formaat: object met .pct; oud formaat: getal (backward-compat)
        const partialPct  = hasPartial ? (typeof partialData === 'object' ? partialData.pct : partialData) : null;
        const pct         = partialPct ?? getLearnedPercent(lesson.words);
        const card = document.createElement('div');
        card.className = ['lesson-card', isNext ? 'recommended' : '', isLocked ? 'locked' : ''].filter(Boolean).join(' ');
        card.innerHTML = `
          <div class="lesson-num">${isLocked ? '🔒' : lesson.id}</div>
          <div class="lesson-card-mid">
            <div class="lesson-emoji-title">
              <span class="lesson-emoji">${lesson.emoji}</span>
              <span class="lesson-title">${lesson.title}</span>
              ${isNext && !hasPartial ? '<span class="lesson-next-badge">Aanbevolen</span>' : ''}
              ${hasPartial && !isLocked ? '<span class="lesson-inprogress-badge">In voortgang</span>' : ''}
            </div>
            <div class="lesson-meta">${lesson.level} · ${lesson.words.length} woorden</div>
            <div class="lesson-bar-wrap"><div class="lesson-bar-fill" style="width:${pct}%"></div></div>
          </div>
          <div class="lesson-card-right"><div class="lesson-pct">${isLocked ? '–' : pct + '%'}</div></div>
        `;
        if (isLocked) {
          const reqMilestone = (segNum - 1) * 10;
          card.addEventListener('click', () => showToast(`Haal eerst de toetsles na les ${reqMilestone} 🎯`));
        } else {
          card.addEventListener('click', () => navigate('lesson', { lessonId: lesson.id }));
        }
        // Sprint 13: bijhoud eerste actieve (niet-locked) les voor ↓-knop
        if (!firstActiveEl && !isLocked) firstActiveEl = card;
        target.appendChild(card);
      });

      // Sprint 12 Item 3: milestone altijd tonen (ook voor locked/onvoltooide segmenten)
      if (!milestonePassed) {
        const isNext        = firstAvailableMilestone === cp;
        const allSkipped    = doneLessons.length > 0 && doneLessons.every(l => isLessonSkipped(l.id));
        const noneCompleted = doneLessons.length > 0 && doneLessons.every(l => !isLessonCompleted(l.id));

        let subText, iconEl, cardOpacity, isClickable;
        if (!segUnlocked) {
          // Toekomstig locked segment
          subText      = 'Beschikbaar na de vorige toets';
          iconEl       = '🔒';
          cardOpacity  = '0.45';
          isClickable  = false;
        } else if (!segComplete) {
          // Segment ontgrendeld maar nog niet volledig gedaan
          const remaining = activeLessons.length;
          subText      = `Nog ${remaining} les${remaining !== 1 ? 'sen' : ''} te gaan in dit deel`;
          iconEl       = '📋';
          cardOpacity  = '0.65';
          isClickable  = false;
        } else {
          // Segment volledig — klaar voor toets
          subText      = (allSkipped && noneCompleted)
            ? '⚠️ Lessen overgeslagen — toets vereist!'
            : '20 vragen · Minimaal 70% om te slagen';
          iconEl       = '📋';
          cardOpacity  = null;
          isClickable  = true;
        }

        const mCard = document.createElement('div');
        mCard.className = `milestone-card${isNext ? ' recommended' : ''}`;
        if (cardOpacity) { mCard.style.opacity = cardOpacity; mCard.style.cursor = 'default'; }
        mCard.innerHTML = `
          <div class="milestone-icon">${iconEl}</div>
          <div class="milestone-mid">
            <div class="milestone-title">${MILESTONE_NAMES[cp] || `Toetsles ${cp}`}</div>
            <div class="milestone-sub">${subText}</div>
          </div>
          <div class="milestone-right">
            ${isNext && isClickable ? '<span class="milestone-badge aanbevolen">Nu doen</span>' : ''}
            ${(allSkipped && noneCompleted && isClickable) ? '<span class="milestone-badge skipped-req">Vereist ⚠️</span>' : ''}
          </div>
        `;
        if (isClickable) {
          mCard.addEventListener('click', () => startMilestoneQuiz(cp));
          // Sprint 13: clickbare milestone telt ook als eerste actieve element
          if (!firstActiveEl) firstActiveEl = mCard;
        }
        target.appendChild(mCard);
      }
    });

    // Sprint 13: ↓ Mijn positie knop toevoegen aan actieve niveauheader
    if (!isLevelComplete(level) && hasDoneGroups && firstActiveEl && header) {
      const btn = document.createElement('button');
      btn.className = 'level-jump-btn';
      btn.textContent = '↓ Mijn positie';
      btn.addEventListener('click', e => {
        e.stopPropagation();
        firstActiveEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      header.appendChild(btn);
    }
  });
}

// ─── LES ──────────────────────────────────────────────────────────────────────
function startLesson(lessonId) {
  isReviewMode  = false;
  currentLesson = getLessonById(lessonId);
  if (!currentLesson) { navigate('home'); return; }

  getLessonTitle().textContent = `${currentLesson.emoji} ${currentLesson.title}`;
  getLevelBadge().textContent  = currentLesson.level;
  getSessionXP().textContent   = '+0 XP';

  // Voltooide les: toon eerst recap-scherm
  if (isLessonCompleted(currentLesson.id)) {
    const prog = getProgress();
    const earnedXP = (prog.lessonXP || {})[currentLesson.id] || 0;
    const lessonWords = currentLesson.words.map(getWordById).filter(Boolean);
    const learnedCount = lessonWords.filter(w => isWordLearned(w.id)).length;

    getProgressBar().style.width = '100%';
    getProgressText().textContent = '';
    getExContainer().innerHTML = `
      <div class="lesson-complete">
        <div class="lc-emoji">✅</div>
        <div class="lc-title">${currentLesson.emoji} ${currentLesson.title}</div>
        <div class="lc-stats">
          <div class="lc-stat"><div class="lc-stat-val">${earnedXP}</div><div class="lc-stat-label">XP verdiend</div></div>
          <div class="lc-stat"><div class="lc-stat-val">${learnedCount}/${lessonWords.length}</div><div class="lc-stat-label">Geleerd</div></div>
          <div class="lc-stat"><div class="lc-stat-val">${currentLesson.level}</div><div class="lc-stat-label">Niveau</div></div>
        </div>
        <div class="lc-grammar-recap">
          <div class="lc-grammar-title">📖 ${currentLesson.grammar.title}</div>
          <div class="lc-grammar-body">${currentLesson.grammar.body}</div>
        </div>
        <button class="lc-btn primary" id="lc-redo">🔄 Opnieuw doen</button>
        <button class="lc-btn secondary" id="lc-home">↩ Terug naar home</button>
      </div>
    `;
    $id('lc-redo').addEventListener('click', () => beginLesson(lessonId, true));
    $id('lc-home').addEventListener('click', () => navigate('home'));
    return;
  }

  // Sprint 14/16: gedeeltelijk gemaakte les — bied keuze aan
  const partial = getPartialLesson(lessonId);
  if (partial !== null) {
    // Backward-compat: oud formaat was een getal, clear en begin opnieuw
    if (typeof partial !== 'object' || !partial.queue) {
      clearPartialLesson(lessonId);
      beginLesson(lessonId);
      return;
    }
    showLessonResumeChoice(lessonId, partial);
    return;
  }

  beginLesson(lessonId);
}

function showLessonResumeChoice(lessonId, partial) {
  // Geen navigate() hier — we zijn al op het les-scherm (aangeroepen vanuit startLesson).
  // navigate() zou startLesson() opnieuw aanroepen → oneindige recursie → blanco scherm.
  const pct = partial.pct;
  getProgressBar().style.width = `${pct}%`;
  getExContainer().innerHTML = `
    <div class="lesson-resume">
      <div class="lr-emoji">📖</div>
      <div class="lr-title">Les in voortgang</div>
      <div class="lr-pct">${pct}% voltooid in vorige sessie</div>
      <button class="lc-btn primary" id="lr-continue">▶ Ga verder</button>
      <button class="lc-btn secondary" id="lr-restart">↩ Begin opnieuw</button>
    </div>
  `;
  $id('lr-continue').addEventListener('click', () => {
    clearPartialLesson(lessonId);
    resumeLesson(lessonId, partial);
  });
  $id('lr-restart').addEventListener('click', () => {
    clearPartialLesson(lessonId);
    beginLesson(lessonId, true);
  });
}

function resumeLesson(lessonId, partial) {
  currentLesson   = getLessonById(lessonId);
  isMilestoneMode = false;
  isReviewMode    = false;
  sessionXP = 0; sessionCorrect = 0; sessionTotal = 0; sessionErrors = []; exerciseHistory = [];

  const lessonWords = currentLesson.words.map(getWordById).filter(Boolean);

  // Herstel de exacte queue vanuit geserialiseerde items
  exerciseQueue = partial.queue.map(item => {
    if (item.type === 'intro')    return { type: 'intro', lesson: currentLesson, words: lessonWords };
    if (item.type === 'grammar')  return { type: 'grammar', grammarNote: currentLesson.grammar };
    const word = getWordById(item.wordId);
    if (!word) return null;
    return { type: item.type, word };
  }).filter(Boolean);

  // Herstel index (klamp tot geldige grens)
  exerciseIndex = Math.min(partial.index, exerciseQueue.length - 1);

  getLessonTitle().textContent = `${currentLesson.emoji} ${currentLesson.title}`;
  getLevelBadge().textContent  = currentLesson.level;
  getSessionXP().textContent   = '+0 XP';
  getProgressBar().style.width = `${partial.pct}%`;
  const backBtn = $id('ex-back-btn');
  if (backBtn) { backBtn.style.display = 'none'; backBtn.onclick = goBack; }
  updateStreak();
  renderExercise();
}

function beginLesson(lessonId, forceAll = false) {
  currentLesson   = getLessonById(lessonId);
  isMilestoneMode = false;
  isReviewMode    = false;
  sessionXP = 0; sessionCorrect = 0; sessionTotal = 0; sessionErrors = []; exerciseHistory = [];

  const lessonWords = currentLesson.words.map(getWordById).filter(Boolean);
  // forceAll=true (opnieuw doen): negeer SRS, alle woorden als nieuw behandelen
  const newWords    = forceAll ? lessonWords : lessonWords.filter(w => !isWordSeen(w.id));
  const reviewWords = forceAll ? []          : lessonWords.filter(w => isWordSeen(w.id) && isWordDue(w.id));

  exerciseQueue = buildExerciseQueue(newWords, reviewWords, VOCAB);
  const grammarSlot = Math.min(3, exerciseQueue.length);
  exerciseQueue.splice(grammarSlot, 0, { type: 'grammar', grammarNote: currentLesson.grammar });
  exerciseQueue.unshift({ type: 'intro', lesson: currentLesson, words: lessonWords });
  exerciseIndex = 0;

  getLessonTitle().textContent = `${currentLesson.emoji} ${currentLesson.title}`;
  getLevelBadge().textContent  = currentLesson.level;
  getSessionXP().textContent   = '+0 XP';
  getProgressBar().style.width = '0%';
  // Sprint 9: terug-knop verbergen bij start
  const backBtn = $id('ex-back-btn');
  if (backBtn) { backBtn.style.display = 'none'; backBtn.onclick = goBack; }
  updateStreak();
  renderExercise();
}

// ─── REVIEW ───────────────────────────────────────────────────────────────────
function startReview() {
  isReviewMode  = true;
  currentLesson = null;
  sessionXP = 0; sessionCorrect = 0; sessionTotal = 0; sessionErrors = []; exerciseHistory = [];

  const dueWords = getDueWordIds(VOCAB.map(w => w.id))
    .map(getWordById).filter(Boolean).slice(0, 20);

  getLessonTitle().textContent  = '🔄 Dagelijkse herhaling';
  getLevelBadge().textContent   = `${dueWords.length} woorden`;
  getSessionXP().textContent    = '+0 XP';
  getProgressBar().style.width  = '0%';
  getProgressText().textContent = '0/0';

  if (dueWords.length === 0) {
    getExContainer().innerHTML = `
      <div class="empty-state">
        <div style="font-size:56px">🎉</div>
        <div class="empty-title">Niets te herhalen!</div>
        <div class="empty-sub">Alle woorden zijn up-to-date.<br>Kom morgen terug voor nieuwe herhaling.</div>
        <button class="lc-btn primary" style="margin-top:20px" onclick="window.app.navigate('home')">Terug naar home</button>
      </div>
    `;
    return;
  }

  sessionXP = 0; sessionCorrect = 0; sessionTotal = 0; exerciseHistory = [];
  exerciseQueue = buildExerciseQueue([], dueWords, VOCAB);
  exerciseIndex = 0;
  renderExercise();
}

// ─── OEFENING RENDEREN ────────────────────────────────────────────────────────
function updateProgress() {
  const total = exerciseQueue.length;
  const pct   = total > 0 ? Math.round(exerciseIndex / total * 100) : 0;
  getProgressBar().style.width  = pct + '%';
  getProgressText().textContent = `${exerciseIndex}/${total}`;
  // Sprint 9: toon/verberg terug-knop op basis van geschiedenis
  const backBtn = $id('ex-back-btn');
  if (backBtn) backBtn.style.display = exerciseHistory.length > 0 ? 'flex' : 'none';
}

function renderExercise() {
  if (exerciseIndex >= exerciseQueue.length) {
    if (isMilestoneMode) {
      const acc = sessionTotal > 0 ? Math.round(sessionCorrect / sessionTotal * 100) : 100;
      showMilestoneComplete(currentMilestone, acc, sessionXP);
    } else if (isReviewMode) {
      showReviewComplete();
    } else {
      showLessonComplete();
    }
    return;
  }

  updateProgress();
  const exercise  = exerciseQueue[exerciseIndex];
  const container = getExContainer();
  container.innerHTML = '';
  container.classList.remove('slide-in');
  void container.offsetWidth;
  container.classList.add('slide-in');
  getSessionXP().textContent = `+${sessionXP} XP`;

  if      (exercise.type === 'intro')           renderLessonIntro(exercise, container, onDone);
  else if (exercise.type === 'flashcard')       renderFlashcard(exercise, container, onDone);
  else if (exercise.type === 'multiple-choice') renderMultipleChoice(exercise, container, VOCAB, onDone);
  else if (exercise.type === 'listen-choose')   renderListenChoose(exercise, container, VOCAB, onDone);
  else if (exercise.type === 'listen-type')     renderListenType(exercise, container, onDone);
  else if (exercise.type === 'type')            renderTypeExercise(exercise, container, onDone);
  else if (exercise.type === 'word-order')      renderWordOrder(exercise, container, onDone);
  else if (exercise.type === 'grammar')         renderGrammarCard(exercise.grammarNote, container, onDone);
}

function onDone(result) {
  const xpEarned   = result.xp || 0;
  const isMetaCard = result.result === 'grammar' || result.result === 'intro';
  sessionXP += xpEarned;

  if (!isMetaCard) {
    sessionTotal++;
    const wasCorrect = result.result === 'correct';
    if (wasCorrect) {
      sessionCorrect++;
    } else if (result.result === 'wrong' && result.word) {
      // Foutgemaakte woorden bijhouden (max 10, uniek)
      const already = sessionErrors.some(e => e.it === result.word.it);
      if (!already && sessionErrors.length < 10) {
        sessionErrors.push({ it: result.word.it, nl: result.word.nl });
      }
    }
    // Sprint 9: sla op voor terug-knop (max 20 stappen in geheugen)
    exerciseHistory.push({ xp: xpEarned, correct: wasCorrect });
    if (exerciseHistory.length > 20) exerciseHistory.shift();
  }

  exerciseIndex++;
  getSessionXP().textContent = `+${sessionXP} XP`;
  setTimeout(renderExercise, isMetaCard ? 0 : 250);
}

// Sprint 10: Ga één oefening terug (annuleer ook een lopende auto-advance timer)
function goBack() {
  cancelAdvanceTimer();   // stop pending auto-advance zodat de timer niet achteraf afvuurt
  if (exerciseHistory.length === 0 || exerciseIndex === 0) return;
  const last = exerciseHistory.pop();
  sessionXP      = Math.max(0, sessionXP - last.xp);
  sessionTotal   = Math.max(0, sessionTotal - 1);
  if (last.correct) sessionCorrect = Math.max(0, sessionCorrect - 1);
  exerciseIndex--;
  getSessionXP().textContent = `+${sessionXP} XP`;
  renderExercise();
}

// ─── LES AFGEROND ─────────────────────────────────────────────────────────────
function showLessonComplete() {
  const accuracy = sessionTotal > 0 ? Math.round(sessionCorrect / sessionTotal * 100) : 100;
  const { emoji, medal } = resultMedal(accuracy);

  completeLesson(currentLesson.id, sessionXP);
  clearPartialLesson(currentLesson.id);  // Sprint 12: wis gedeeltelijke voortgang na afronden
  addTodayXP(sessionXP);
  const newAch = checkAchievements();
  const hasNext = CURRICULUM.some(l => l.id === currentLesson.id + 1);
  getProgressBar().style.width = '100%';

  const errorsHtml = sessionErrors.length > 0 ? `
    <div class="lc-errors">
      <div class="lc-errors-title">📝 Nog iets aan werken</div>
      <div class="lc-errors-list">
        ${sessionErrors.slice(0, 5).map(e => `
          <div class="lc-error-item">
            <span class="lc-error-it">${e.it}</span>
            <span class="lc-error-nl">${e.nl}</span>
          </div>
        `).join('')}
      </div>
    </div>
  ` : '';

  getExContainer().innerHTML = `
    <div class="lesson-complete">
      <div class="lc-emoji">${emoji}</div>
      <div class="lc-title">${medal}</div>
      <div class="lc-stats">
        <div class="lc-stat"><div class="lc-stat-val">+${sessionXP}</div><div class="lc-stat-label">XP verdiend</div></div>
        <div class="lc-stat"><div class="lc-stat-val">${accuracy}%</div><div class="lc-stat-label">Nauwkeurig</div></div>
        <div class="lc-stat"><div class="lc-stat-val">${sessionCorrect}/${sessionTotal}</div><div class="lc-stat-label">Correct</div></div>
      </div>
      ${newAch.length ? `<div class="lc-achievements">${newAch.map(a => `<div class="lc-achievement">${a.emoji} <strong>${a.label}</strong> behaald!</div>`).join('')}</div>` : ''}
      ${errorsHtml}
      <div class="lc-grammar-recap">
        <div class="lc-grammar-title">📖 ${currentLesson.grammar.title}</div>
        <div class="lc-grammar-body">${currentLesson.grammar.body}</div>
      </div>
      <button class="lc-btn primary" id="lc-home">↩ Terug naar home</button>
      ${hasNext ? `<button class="lc-btn secondary" id="lc-next">Volgende les →</button>` : ''}
    </div>
  `;

  $id('lc-home').addEventListener('click', () => navigate('home'));
  $id('lc-next')?.addEventListener('click', () => navigate('lesson', { lessonId: currentLesson.id + 1 }));
}

function showReviewComplete() {
  const accuracy = sessionTotal > 0 ? Math.round(sessionCorrect / sessionTotal * 100) : 100;
  const { emoji, medal } = resultMedal(accuracy);
  addTodayXP(sessionXP);
  getProgressBar().style.width = '100%';

  const errorsHtml = sessionErrors.length > 0 ? `
    <div class="lc-errors">
      <div class="lc-errors-title">📝 Nog iets aan werken</div>
      <div class="lc-errors-list">
        ${sessionErrors.slice(0, 5).map(e => `
          <div class="lc-error-item">
            <span class="lc-error-it">${e.it}</span>
            <span class="lc-error-nl">${e.nl}</span>
          </div>
        `).join('')}
      </div>
    </div>
  ` : '';

  getExContainer().innerHTML = `
    <div class="lesson-complete">
      <div class="lc-emoji">${emoji}</div>
      <div class="lc-title">${medal}</div>
      <div class="lc-stats">
        <div class="lc-stat"><div class="lc-stat-val">+${sessionXP}</div><div class="lc-stat-label">XP verdiend</div></div>
        <div class="lc-stat"><div class="lc-stat-val">${accuracy}%</div><div class="lc-stat-label">Nauwkeurig</div></div>
        <div class="lc-stat"><div class="lc-stat-val">${sessionTotal}</div><div class="lc-stat-label">Herhaald</div></div>
      </div>
      ${errorsHtml}
      <div class="lc-grammar-recap">
        <div class="lc-grammar-title">🔄 Herhaling voltooid!</div>
        <div class="lc-grammar-body">Goed gedaan — de woorden die je moeilijk vond komen sneller terug. Woorden die je goed kent zie je minder vaak. Zo werkt het SM-2 algoritme.</div>
      </div>
      <button class="lc-btn primary" id="lc-home">↩ Terug naar home</button>
    </div>
  `;
  $id('lc-home').addEventListener('click', () => navigate('home'));
}

// ─── TOETSLES (MILESTONE QUIZ) ────────────────────────────────────────────────
function startMilestoneQuiz(checkpoint) {
  isMilestoneMode  = true;
  currentMilestone = checkpoint;
  isReviewMode     = false;
  currentLesson    = null;
  sessionXP = 0; sessionCorrect = 0; sessionTotal = 0; sessionErrors = []; exerciseHistory = [];

  // Woorden uit de specifieke batch (bijv. lessen 1-10 voor M10, 11-20 voor M20)
  const lessonStart = checkpoint - 9;
  const quizWords   = shuffle(VOCAB.filter(w => w.lesson >= lessonStart && w.lesson <= checkpoint)).slice(0, 20);

  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById('screen-lesson').classList.add('active');
  document.querySelectorAll('.nav-btn[data-screen]').forEach(b => b.classList.remove('active'));

  getLessonTitle().textContent = `📋 ${MILESTONE_NAMES[checkpoint] || 'Toetsles'}`;
  getLevelBadge().textContent  = '20 vragen';
  getSessionXP().textContent   = '+0 XP';
  getProgressBar().style.width = '0%';
  getProgressText().textContent = '0/0';

  exerciseQueue = buildExerciseQueue([], quizWords, VOCAB);
  exerciseIndex = 0;
  updateStreak();
  renderExercise();
}

function showMilestoneComplete(checkpoint, accuracy, xpEarned) {
  const passed = accuracy >= 70;
  isMilestoneMode = false;

  if (passed) {
    passMilestone(checkpoint);
    addXP(xpEarned);
    addTodayXP(xpEarned);
  } else {
    const consolationXP = Math.min(xpEarned, 10);
    addXP(consolationXP);
    addTodayXP(consolationXP);
  }

  getProgressBar().style.width = '100%';

  getExContainer().innerHTML = `
    <div class="lesson-complete">
      <div class="lc-emoji">${passed ? '🎖️' : '💪'}</div>
      <div class="lc-title">${MILESTONE_NAMES[checkpoint] || `Toetsles ${checkpoint}`}</div>
      <div class="lc-stats">
        <div class="lc-stat"><div class="lc-stat-val">${accuracy}%</div><div class="lc-stat-label">Nauwkeurig</div></div>
        <div class="lc-stat"><div class="lc-stat-val">${sessionCorrect}/${sessionTotal}</div><div class="lc-stat-label">Correct</div></div>
        <div class="lc-stat"><div class="lc-stat-val">+${passed ? xpEarned : Math.min(xpEarned, 10)}</div><div class="lc-stat-label">XP verdiend</div></div>
      </div>
      <div class="lc-grammar-recap">
        <div class="lc-grammar-title">${passed ? '✅ Gehaald!' : '❌ Niet gehaald'}</div>
        <div class="lc-grammar-body">${passed
          ? 'Goed gedaan! De volgende lessen zijn nu ontgrendeld. Ga zo door!'
          : `Je scoorde ${accuracy}% maar je hebt minimaal 70% nodig. Oefen de woorden nog even en probeer het opnieuw.`
        }</div>
      </div>
      ${!passed ? `<button class="lc-btn primary" id="lc-retry">🔄 Opnieuw proberen</button>` : ''}
      <button class="lc-btn ${passed ? 'primary' : 'secondary'}" id="lc-home">↩ Terug naar home</button>
    </div>
  `;

  $id('lc-retry')?.addEventListener('click', () => startMilestoneQuiz(checkpoint));
  $id('lc-home').addEventListener('click', () => navigate('home'));
}

function resultMedal(accuracy) {
  if (accuracy >= 90) return { emoji: '🏆', medal: 'Uitstekend!' };
  if (accuracy >= 70) return { emoji: '🌟', medal: 'Goed gedaan!' };
  if (accuracy >= 50) return { emoji: '👍', medal: 'Redelijk goed!' };
  return { emoji: '💪', medal: 'Blijf oefenen!' };
}

// ─── INSTELLINGEN ─────────────────────────────────────────────────────────────
function renderSettings() {
  const settings = getSettings();

  // Dagdoel-knoppen activeren (Sprint 10: waarden in minuten)
  document.querySelectorAll('.dagdoel-btn').forEach(btn => {
    const val = parseInt(btn.dataset.xp, 10);
    btn.classList.toggle('active', val === settings.dagdoel);
    const newBtn = btn.cloneNode(true);
    btn.parentNode.replaceChild(newBtn, btn);
    newBtn.addEventListener('click', () => {
      saveSettings({ dagdoel: val });
      renderSettings();
    });
  });

  // TTS-snelheid knoppen activeren
  document.querySelectorAll('.tts-rate-btn').forEach(btn => {
    const val = parseFloat(btn.dataset.rate);
    btn.classList.toggle('active', Math.abs(val - settings.ttsRate) < 0.05);
    const newBtn = btn.cloneNode(true);
    btn.parentNode.replaceChild(newBtn, btn);
    newBtn.addEventListener('click', () => {
      saveSettings({ ttsRate: val });
      setTTSRate(val);
      renderSettings();
    });
  });

  // Sprint 10: Thema-knoppen activeren
  document.querySelectorAll('.theme-btn').forEach(btn => {
    const val = btn.dataset.theme;
    btn.classList.toggle('active', val === (settings.theme || 'auto'));
    const newBtn = btn.cloneNode(true);
    btn.parentNode.replaceChild(newBtn, btn);
    newBtn.addEventListener('click', () => {
      saveSettings({ theme: val });
      applyTheme(val);
      renderSettings();
    });
  });
}

/** Sprint 10: Pas het thema toe via data-attribuut op <html>. */
function applyTheme(theme) {
  const html = document.documentElement;
  if (theme === 'light') html.dataset.theme = 'light';
  else if (theme === 'dark') html.dataset.theme = 'dark';
  else delete html.dataset.theme; // 'auto' = geen class, volgt systeem
}

// ─── PLAATSINGSTOETS ──────────────────────────────────────────────────────────
function renderPlacement() {
  const container = $id('placement-container');
  container.innerHTML = `
    <div class="placement-intro">
      <div class="placement-flag">🇮🇹</div>
      <h2 class="placement-title">Hoe goed is jouw Italiaans?</h2>
      <p class="placement-desc">Wij zoeken de beste startplek voor jou. Sla lessen over die je al kent, of begin gewoon bij het begin.</p>
      <div class="placement-choices">
        <button class="pl-choice-btn" id="pl-new">
          <span class="pl-choice-emoji">🐣</span>
          <div>
            <div class="pl-choice-title">Helemaal nieuw</div>
            <div class="pl-choice-sub">Begin bij les 1 — de basis</div>
          </div>
        </button>
        <button class="pl-choice-btn" id="pl-some">
          <span class="pl-choice-emoji">📖</span>
          <div>
            <div class="pl-choice-title">Ik ken wat basiswoorden</div>
            <div class="pl-choice-sub">Doe de korte toets (15 vragen)</div>
          </div>
        </button>
        <button class="pl-choice-btn" id="pl-exp">
          <span class="pl-choice-emoji">🎓</span>
          <div>
            <div class="pl-choice-title">Ik spreek al wat Italiaans</div>
            <div class="pl-choice-sub">Doe de korte toets (15 vragen)</div>
          </div>
        </button>
      </div>
    </div>
  `;

  $id('pl-new').addEventListener('click', () => {
    markPlacementDone();
    navigate('home');
  });
  $id('pl-some').addEventListener('click', startPlacementQuiz);
  $id('pl-exp').addEventListener('click',  startPlacementQuiz);
}

function startPlacementQuiz() {
  // 15 woorden verspreid over 5 groepen van 6 A1-lessen (3 per groep)
  const a1Words = VOCAB.filter(w => w.level === 'A1');
  const groups  = [
    a1Words.filter(w => w.lesson >= 1  && w.lesson <= 6),
    a1Words.filter(w => w.lesson >= 7  && w.lesson <= 12),
    a1Words.filter(w => w.lesson >= 13 && w.lesson <= 18),
    a1Words.filter(w => w.lesson >= 19 && w.lesson <= 24),
    a1Words.filter(w => w.lesson >= 25 && w.lesson <= 30),
  ];
  placementQuestions = groups.flatMap(g => shuffle(g).slice(0, 3)).slice(0, 15);
  placementIndex = 0;
  placementScore = 0;
  renderPlacementQuestion();
}

function renderPlacementQuestion() {
  if (placementIndex >= placementQuestions.length) {
    showPlacementResult();
    return;
  }

  const word    = placementQuestions[placementIndex];
  const pool    = VOCAB.filter(w => w.id !== word.id && w.level === 'A1');
  const wrongs  = shuffle(pool).slice(0, 3);
  const options = shuffle([word, ...wrongs]);
  const container = $id('placement-container');

  container.innerHTML = `
    <div class="pq-wrap">
      <div class="pq-top">
        <div class="pq-progress-bar"><div class="pq-progress-fill" style="width:${placementIndex / 15 * 100}%"></div></div>
        <div class="pq-count">${placementIndex + 1} <span>/ 15</span></div>
      </div>
      <div class="pq-question">
        <div class="pq-label">Wat betekent dit woord?</div>
        <div class="pq-word">${word.it}</div>
        ${word.ph ? `<div class="pq-ph">[${word.ph}]</div>` : ''}
      </div>
      <div class="pq-options">
        ${options.map((opt, i) => `
          <button class="pq-option" data-id="${opt.id}" data-correct="${opt.id === word.id}">
            <span class="pq-letter">${['A','B','C','D'][i]}</span>
            <span class="pq-text">${opt.nl}</span>
          </button>
        `).join('')}
      </div>
    </div>
  `;

  container.querySelectorAll('.pq-option').forEach(btn => {
    btn.addEventListener('click', () => {
      const isCorrect = btn.dataset.correct === 'true';
      if (isCorrect) placementScore++;
      container.querySelectorAll('.pq-option').forEach(b => {
        b.disabled = true;
        if (b.dataset.correct === 'true') b.classList.add('pq-correct');
        else if (b === btn && !isCorrect) b.classList.add('pq-wrong');
      });
      setTimeout(() => { placementIndex++; renderPlacementQuestion(); }, 700);
    });
  });
}

function showPlacementResult() {
  let skipTo = 0, startAt = 1, msg = '', detail = '';

  if      (placementScore >= 13) { skipTo = 30; startAt = 31; msg = 'Uitstekend!';          detail = 'Je kent al heel wat Italiaans.'; }
  else if (placementScore >= 10) { skipTo = 19; startAt = 20; msg = 'Goed gedaan!';         detail = 'Je hebt een stevige basis.'; }
  else if (placementScore >= 5)  { skipTo = 9;  startAt = 10; msg = 'Mooi begin!';          detail = 'Je kent al wat woorden.'; }
  else                            { skipTo = 0;  startAt = 1;  msg = 'Begin bij de basis!';  detail = 'Geen zorgen — solide fundamenten zijn goud waard.'; }

  const container = $id('placement-container');
  container.innerHTML = `
    <div class="pr-wrap">
      <div class="pr-ring">
        <svg viewBox="0 0 100 100" class="pr-svg">
          <circle cx="50" cy="50" r="40" fill="none" stroke="var(--surface2)" stroke-width="10"/>
          <circle cx="50" cy="50" r="40" fill="none" stroke="var(--accent)" stroke-width="10"
            stroke-dasharray="${2 * Math.PI * 40}"
            stroke-dashoffset="${2 * Math.PI * 40 * (1 - placementScore / 15)}"
            stroke-linecap="round" transform="rotate(-90 50 50)"/>
        </svg>
        <div class="pr-score-inner">
          <div class="pr-score-num">${placementScore}</div>
          <div class="pr-score-denom">/ 15</div>
        </div>
      </div>
      <div class="pr-msg">${msg}</div>
      <div class="pr-detail">${detail}</div>
      <div class="pr-rec-box">
        <div class="pr-rec-label">Aanbevolen startpunt</div>
        <div class="pr-rec-lesson">Les ${startAt}</div>
        ${skipTo > 0 ? `<div class="pr-rec-skip">Lessen 1–${skipTo} worden overgeslagen — je kunt ze altijd nog doen</div>` : ''}
      </div>
      <button class="lc-btn primary" id="pr-start">Start bij les ${startAt} →</button>
      <button class="lc-btn secondary" id="pr-begin">Toch beginnen bij les 1</button>
    </div>
  `;

  $id('pr-start').addEventListener('click', () => {
    for (let i = 1; i <= skipTo; i++) {
      skipLesson(i);  // overgeslagen, NIET voltooid — geen XP, geen achievements
    }
    markPlacementDone();
    navigate('lesson', { lessonId: startAt });
  });
  $id('pr-begin').addEventListener('click', () => {
    markPlacementDone();
    navigate('home');
  });
}

// ─── STATS ────────────────────────────────────────────────────────────────────
function renderStats() {
  const prog = getProgress();
  $id('stat-seen').textContent     = VOCAB.filter(w => isWordSeen(w.id)).length;
  $id('stat-learned').textContent  = VOCAB.filter(w => isWordLearned(w.id)).length;
  $id('stat-lessons').textContent  = prog.completedLessons.length;
  $id('stat-skipped').textContent  = getSkippedCount();
  $id('stat-streak').textContent   = getStreak();
  $id('stat-xp').textContent       = prog.xp;
  $id('stat-accuracy').textContent = getAccuracy() + '%';

  // ── Lessen-lijst ────────────────────────────────────────────────────────────
  const list = $id('stats-lesson-list');
  list.innerHTML = '';
  CURRICULUM.forEach(lesson => {
    const pct      = getLearnedPercent(lesson.words);
    const done     = isLessonCompleted(lesson.id);
    const skipped  = isLessonSkipped(lesson.id);
    const item = document.createElement('div');
    item.className = 'stats-lesson-item';
    item.innerHTML = `
      <div class="sli-header">
        <span>${lesson.emoji} ${lesson.title}</span>
        <span class="sli-pct">${done ? '✓' : skipped ? '↷' : pct + '%'}</span>
      </div>
      <div class="sli-bar"><div class="sli-fill${skipped ? ' skipped' : ''}" style="width:${skipped ? '100' : pct}%"></div></div>
    `;
    list.appendChild(item);
  });
}

// ─── WOORDENBOEK ──────────────────────────────────────────────────────────────
function renderDictionary() {
  const searchInput = $id('dict-search');
  const dictList    = $id('dict-list');
  const filterBtns  = document.querySelectorAll('.dict-filter-btn');
  let activeLevel   = 'all';

  function getStatusBadge(wordId) {
    if (isWordLearned(wordId))  return '<span class="dict-badge learned">Geleerd</span>';
    if (isWordSeen(wordId))     return '<span class="dict-badge seen">Gezien</span>';
    return '<span class="dict-badge new">Nieuw</span>';
  }

  function render() {
    const query = (searchInput?.value || '').toLowerCase().trim();
    const filtered = VOCAB.filter(w => {
      const matchLevel = activeLevel === 'all' || w.level === activeLevel;
      const matchQuery = !query || w.it.toLowerCase().includes(query) || w.nl.toLowerCase().includes(query);
      return matchLevel && matchQuery;
    });

    dictList.innerHTML = filtered.length === 0
      ? '<div class="dict-empty">Geen woorden gevonden</div>'
      : filtered.map(w => `
          <div class="dict-item">
            <div class="dict-item-top">
              <span class="dict-it">${w.it}</span>
              ${getStatusBadge(w.id)}
            </div>
            <div class="dict-nl">${w.nl}</div>
            ${w.ph ? `<div class="dict-ph">[${w.ph}]</div>` : ''}
          </div>
        `).join('');
  }

  render();
  searchInput?.addEventListener('input', render);
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeLevel = btn.dataset.level;
      render();
    });
  });
}

// ─── ACHIEVEMENTS ─────────────────────────────────────────────────────────────
function renderAchievements() {
  $id('achievements-list').innerHTML = getAchievements().map(a => `
    <div class="achievement-item ${a.earned ? 'earned' : 'locked'}">
      <div class="ach-emoji">${a.earned ? a.emoji : '🔒'}</div>
      <div class="ach-info">
        <div class="ach-label">${a.label}</div>
        <div class="ach-status">${a.earned ? '✓ Behaald!' : 'Nog niet behaald'}</div>
      </div>
    </div>
  `).join('');
}

// ─── TOAST ────────────────────────────────────────────────────────────────────
let toastTimer;
export function showToast(msg) {
  const t = $id('toast');
  t.textContent = msg;
  t.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 2500);
}

// ─── INIT ─────────────────────────────────────────────────────────────────────
async function init() {
  await loadData();
  migrateOldSkipped();    // eenmalige migratie: 0-XP completed → skipped
  migrateXPToV10();       // Sprint 10: herschaal XP naar nieuwe waarden
  migrateToV14();         // Sprint 14: hernummer les-IDs 21-60 naar nieuwe structuur
  migrateSettingsV10();   // Sprint 10: migreer dagdoel (10/20/30/50 → 50/100/150/200)
  const settings = getSettings();
  applyTheme(settings.theme || 'auto');  // Sprint 10: thema toepassen
  initAudio();
  setTTSRate(settings.ttsRate);
  updateStreak();

  window.app = { navigate, showToast };

  // Nav-knoppen
  document.querySelectorAll('.nav-btn[data-screen]').forEach(btn =>
    btn.addEventListener('click', () => navigate(btn.dataset.screen))
  );

  // Terug-knoppen — les-terugknop toont bevestigingsdialog
  document.querySelectorAll('[data-back]').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.back;
      const inLesson = document.getElementById('screen-lesson')?.classList.contains('active');
      if (inLesson && target === 'home' && exerciseQueue.length > 0 && exerciseIndex > 0) {
        $id('exit-lesson-modal')?.classList.add('active');
      } else {
        navigate(target);
      }
    });
  });

  // Les-verlaten modal knoppen
  $id('exit-lesson-stay')?.addEventListener('click', () => {
    $id('exit-lesson-modal')?.classList.remove('active');
  });
  $id('exit-lesson-leave')?.addEventListener('click', () => {
    $id('exit-lesson-modal')?.classList.remove('active');
    navigate('home');
  });

  // Review-knop
  $id('review-btn')?.addEventListener('click', () => navigate('review'));

  // Instellingen-knop (gear icon in home header)
  $id('settings-btn')?.addEventListener('click', () => navigate('settings'));

  // Reset-knop
  $id('reset-btn')?.addEventListener('click', () => {
    if (confirm('Weet je zeker dat je alle voortgang wilt resetten? Dit kan niet ongedaan worden.')) {
      resetProgress();
      localStorage.removeItem('italiano_srs_v2');
      navigate('home');
      showToast('Voortgang gereset');
    }
  });

  // Plaatsingstoets opnieuw doen (vanuit instellingen)
  $id('redo-placement-btn')?.addEventListener('click', () => {
    saveSettings({ placementDone: false });
    navigate('placement');
  });

  // ── Voortgang delen via herstellink ────────────────────────────────────────
  $id('share-progress-btn')?.addEventListener('click', async () => {
    const prog = getProgress();
    const compactData = {
      v: 2,
      completedLessons: prog.completedLessons,
      skippedLessons:   prog.skippedLessons  || [],
      passedMilestones: prog.passedMilestones || [],
      xp:               prog.xp,
      streak:           prog.streak,
      achievements:     prog.achievements    || []
    };
    const encoded = btoa(unescape(encodeURIComponent(JSON.stringify(compactData))));
    const url     = `${location.origin}${location.pathname}?herstel=${encoded}`;

    if (navigator.share) {
      try {
        await navigator.share({
          title: 'Italiaans voor op vakantie — mijn voortgang',
          text:  `Ik heb ${prog.completedLessons.length} lessen voltooid en ${prog.xp} XP verdiend!`,
          url
        });
      } catch (e) { /* gebruiker heeft geannuleerd */ }
    } else {
      try {
        await navigator.clipboard.writeText(url);
        showToast('Herstellink gekopieerd! 📋');
      } catch (e) {
        showToast('Kon link niet kopiëren');
      }
    }
  });

  // ── Exporteer voortgang als back-upcode ────────────────────────────────────
  $id('export-progress-btn')?.addEventListener('click', async () => {
    const raw  = localStorage.getItem('italiano_progress_v2') || '{}';
    const code = btoa(unescape(encodeURIComponent(raw)));
    const out  = $id('export-code-output');
    try {
      await navigator.clipboard.writeText(code);
      showToast('✅ Back-upcode gekopieerd naar klembord!');
      if (out) out.style.display = 'none';
    } catch {
      // Klembord niet beschikbaar — toon de code in het tekstveld
      if (out) {
        out.style.display = 'block';
        out.value = code;
        out.select();
        showToast('Kopieer de code handmatig uit het veld hieronder');
      }
    }
  });

  // ── Importeer voortgang via geplakte code ──────────────────────────────────
  $id('import-progress-btn')?.addEventListener('click', () => {
    const code = $id('import-code-input')?.value?.trim();
    if (!code) { showToast('Plak eerst een back-upcode in het veld'); return; }
    try {
      const json = decodeURIComponent(escape(atob(code)));
      const data = JSON.parse(json);
      // Minimale validatie: moet een object zijn met bekende sleutels
      if (typeof data !== 'object' || data === null) throw new Error('Ongeldig');
      const lessen = data.completedLessons?.length ?? '?';
      const xp     = data.xp ?? '?';
      const ok = window.confirm(
        `Voortgang herstellen?\n\n${lessen} lessen voltooid · ${xp} XP\n\nJe huidige voortgang wordt overschreven.`
      );
      if (ok) {
        localStorage.setItem('italiano_progress_v2', json);
        showToast('✅ Voortgang hersteld!');
        setTimeout(() => location.reload(), 800);
      }
    } catch {
      showToast('❌ Ongeldige code — controleer of je de volledige code hebt geplakt');
    }
  });

  // ── Herstellink detecteren (?herstel=...) ─────────────────────────────────
  const herstelParam = new URLSearchParams(location.search).get('herstel');
  if (herstelParam) {
    try {
      const data = JSON.parse(decodeURIComponent(escape(atob(herstelParam))));
      if (data.v === 2 && Array.isArray(data.completedLessons)) {
        const modal = $id('restore-modal');
        if (modal) {
          const el = $id('restore-info');
          if (el) el.textContent = `${data.completedLessons.length} lessen voltooid · ${data.xp || 0} XP`;
          modal.classList.add('active');
          $id('restore-confirm')?.addEventListener('click', () => {
            localStorage.setItem('italiano_progress_v2', JSON.stringify(data));
            history.replaceState(null, '', location.pathname);
            location.reload();
          });
          $id('restore-cancel')?.addEventListener('click', () => {
            modal.classList.remove('active');
            history.replaceState(null, '', location.pathname);
          });
        }
      }
    } catch (e) {
      history.replaceState(null, '', location.pathname);
    }
  }

  // Eerste keer: plaatsingstoets tonen
  if (!isPlacementDone()) {
    navigate('placement');
  } else {
    navigate('home');
  }
}

init().catch(err => {
  console.error('App kon niet laden:', err);
  const screen = document.getElementById('screen-home');
  if (screen) {
    screen.classList.add('active');
    screen.innerHTML = `
      <div class="empty-state" style="height:100dvh">
        <div style="font-size:48px">⚠️</div>
        <div class="empty-title">App kon niet laden</div>
        <div class="empty-sub">${err.message}<br><br>Ververs de pagina.</div>
      </div>
    `;
  }
  document.getElementById('loading')?.classList.add('hidden');
});
