/**
 * Exercises — Sprint 10
 * Types: flashcard, multiple-choice, listen-choose, listen-type, type, word-order, sentence-choice,
 * fill-in-blank-mc/-type, matching, find-error, sentence-dictation, category-sort, conjugation, reading, grammar, intro
 */

import { speak, isTTSAvailable, getTTSRate } from './audio.js?v=10';
import { updateWordState, qualityFromResult } from './srs.js?v=17';
import { recordAnswer } from './progress.js?v=10';
import { getLang } from './lang.js?v=1';
import { ES_PRONOUNS, ES_TENSE_LABELS, esIsConjugatable, esCanUseTense, esConjugateAccepted, esPickTense } from './conjugation_es.js?v=2';

// ─── Auto-advance timer (annuleerbaar via goBack) ─────────────────────────────
let _pendingAdvanceTimer = null;

/** Annuleer een lopende auto-advance timer (aangeroepen door goBack in app.js). */
export function cancelAdvanceTimer() {
  if (_pendingAdvanceTimer !== null) {
    clearTimeout(_pendingAdvanceTimer);
    _pendingAdvanceTimer = null;
  }
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function normalize(str) {
  return str.toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/['']/g, "'")
    .replace(/[.,!?;:]/g, '')
    .trim();
}

function levenshtein(a, b) {
  const m = a.length, n = b.length;
  const dp = Array.from({ length: m + 1 }, (_, i) => [i, ...Array(n).fill(0)]);
  for (let j = 0; j <= n; j++) dp[0][j] = j;
  for (let i = 1; i <= m; i++)
    for (let j = 1; j <= n; j++)
      dp[i][j] = a[i-1] === b[j-1] ? dp[i-1][j-1]
        : 1 + Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
  return dp[m][n];
}

function checkTypedAnswer(typed, correct) {
  const t = normalize(typed);
  const c = normalize(correct);
  if (!t) return 'empty';
  if (t === c) return 'correct';
  if (levenshtein(t, c) <= Math.max(1, Math.floor(c.length / 6))) return 'close';
  return 'wrong';
}

function getDistractors(word, allWords, count = 3) {
  const notTarget = allWords.filter(w => w.id !== word.id && w.nl !== word.nl);

  // Voorkeur: zelfde categorie → zelfde les → zelfde niveau → alles
  // Zo zijn afleidende antwoorden altijd realistisch (geen 'dolfijn' bij getallen)
  const sameCat    = word.cat ? notTarget.filter(w => w.cat === word.cat) : [];
  const sameLesson = notTarget.filter(w => w.lesson === word.lesson);
  const sameLevel  = notTarget.filter(w => w.level === word.level);

  const pool = sameCat.length    >= count ? sameCat
             : sameLesson.length >= count ? sameLesson
             : sameLevel.length  >= count ? sameLevel
             : notTarget;

  return shuffleEx(pool).slice(0, count);
}

function shuffleEx(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** Splits een zin in word-tokens, behoudt leestekens. */
function sentenceToTokens(sentence) {
  return (sentence || '').split(/\s+/).filter(w => w.length > 0);
}

/**
 * Sprint 9: Stel de volgende-knop in.
 * Bij correcte antwoorden: automatisch verder na 2 seconden (countdown zichtbaar).
 * Gebruiker kan ook direct klikken om sneller te gaan.
 * Bij foute antwoorden: gewoon klikken vereist (geen timer).
 */
// SVG-ring die in 4 seconden leegloopt (r=7 → omtrek ≈ 44px)
const ADV_RING_SVG = `<svg class="adv-ring" viewBox="0 0 18 18" width="16" height="16" aria-hidden="true">
  <circle cx="9" cy="9" r="7" class="adv-ring-bg"/>
  <circle cx="9" cy="9" r="7" class="adv-ring-fill"/>
</svg>`;

function setupNextBtn(btn, callback, autoAdvance = false) {
  btn.style.display = 'block';
  if (autoAdvance) {
    btn.innerHTML = `Volgende ${ADV_RING_SVG}`;
    _pendingAdvanceTimer = setTimeout(() => {
      _pendingAdvanceTimer = null;
      callback();
    }, 4000);
    btn.addEventListener('click', () => {
      if (_pendingAdvanceTimer) { clearTimeout(_pendingAdvanceTimer); _pendingAdvanceTimer = null; }
      callback();
    }, { once: true });
  } else {
    btn.textContent = 'Volgende →';
    btn.addEventListener('click', callback, { once: true });
  }
}


// ─── Hulpfuncties ─────────────────────────────────────────────────────────────

function capitalize(str) {
  return str ? str.charAt(0).toUpperCase() + str.slice(1) : '';
}

/**
 * Vergelijk getypte zin met correcte zin op woordniveau.
 * Geeft 'correct', 'close' of 'wrong'.
 */
function checkSentenceAnswer(typed, correct) {
  const t = normalize(typed);
  const c = normalize(correct);
  if (t === c) return 'correct';
  const tW = t.split(/\s+/).filter(Boolean);
  const cW = c.split(/\s+/).filter(Boolean);
  const lenDiff = Math.abs(tW.length - cW.length);
  if (lenDiff > 2) return 'wrong';
  const minLen = Math.min(tW.length, cW.length);
  let errors = lenDiff;
  for (let i = 0; i < minLen; i++) {
    const maxErr = Math.max(1, Math.floor(cW[i].length / 5));
    if (levenshtein(tW[i], cW[i]) > maxErr) errors++;
  }
  if (errors === 0) return 'correct';
  if (errors <= Math.ceil(cW.length / 4)) return 'close';
  return 'wrong';
}

/**
 * Groepeer woorden per categorie. Geeft null als er geen 2 categorieën met elk 2+ woorden zijn.
 */
export function buildCategoryGroups(words) {
  const groups = {};
  words.forEach(w => {
    if (w.cat) (groups[w.cat] = groups[w.cat] || []).push(w);
  });
  const valid = Object.values(groups).filter(g => g.length >= 2);
  if (valid.length < 2) return null;
  valid.sort((a, b) => b.length - a.length);
  return [shuffleEx(valid[0]).slice(0, 3), shuffleEx(valid[1]).slice(0, 3)];
}

// ─── Gat-invullen helpers ─────────────────────────────────────────────────────

/** Strip lidwoord van een Italiaans woord (il gatto → gatto). */
function stripArticle(it) {
  return it.replace(getLang().articleRe, '').trim();
}

/**
 * Zoek het doelwoord in de voorbeeldzin en geef de zin terug met ___ op die plek.
 * Geeft null als het woord niet gevonden wordt.
 */
function makeGapSentence(word) {
  if (!word.ex) return null;
  const stemNorm = normalize(stripArticle(word.it));
  if (!stemNorm) return null;
  // Token-gebaseerd zoeken (werkt ook met geaccentueerde tekens zoals sì, è, ecc.)
  const tokens = word.ex.match(/\S+/g) || [];
  const idx = tokens.findIndex(t => normalize(t.replace(/[.,!?;:]/g, '')) === stemNorm);
  if (idx === -1) return null;
  const punct = tokens[idx].match(/[.,!?;:]+$/)?.[0] || '';
  const result = [...tokens];
  result[idx] = '___' + punct;
  return result.join(' ');
}

/**
 * Gat-invullen (MC) — toon een zin met ___, kies het juiste woord.
 */
export function renderFillBlankMC(exercise, container, allWords, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();
  const gapped = makeGapSentence(word);
  if (!gapped) {
    // Fallback: gebruik gewone MC als gat niet gemaakt kan worden
    renderMultipleChoice(exercise, container, allWords, onComplete);
    return;
  }

  const stem = stripArticle(word.it);
  // Afleiders: woorden uit dezelfde les, anders willekeurig
  const sameLesson = allWords.filter(w => w.lesson === word.lesson && w.id !== word.id);
  const pool = sameLesson.length >= 3 ? sameLesson : allWords.filter(w => w.id !== word.id);
  const distractorWords = shuffleEx(pool).slice(0, 3);
  const distractors = distractorWords.map(w => stripArticle(w.it));

  const options = shuffleEx([{ text: stem, correct: true }, ...distractors.map(d => ({ text: d, correct: false }))]);

  container.innerHTML = `
    <div class="ex-label">Vul het ontbrekende woord in</div>
    <div class="fib-hint">${word.nl}</div>
    <div class="fib-sentence">${gapped}</div>
    <div class="mc-options" id="fib-options">
      ${options.map((opt, i) => `
        <button class="mc-option" data-correct="${opt.correct}">
          <span class="mc-letter">${['A','B','C','D'][i]}</span>
          <span class="mc-text">${opt.text}</span>
        </button>
      `).join('')}
    </div>
    <div class="mc-feedback" id="fib-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  let answered = false;
  container.querySelectorAll('.mc-option').forEach(btn => {
    btn.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const isCorrect = btn.dataset.correct === 'true';
      const result = isCorrect ? 'correct' : 'wrong';

      container.querySelectorAll('.mc-option').forEach(b => {
        b.classList.add('disabled');
        if (b.dataset.correct === 'true') b.classList.add('correct');
        else if (b === btn) b.classList.add('wrong');
      });

      const fb = container.querySelector('#fib-feedback');
      if (isCorrect) {
        fb.className = 'mc-feedback correct show';
        fb.innerHTML = `✓ Correct! <em>"${word.ex}"</em>`;
        if (hasTTS) setTimeout(() => speak(word.ex), 400);
      } else {
        fb.className = 'mc-feedback wrong show';
        fb.innerHTML = `✗ Fout. Het juiste woord is: <strong>${stem}</strong> — "${word.ex}"`;
        if (hasTTS) setTimeout(() => speak(word.ex), 500);
      }

      updateWordState(word.id, qualityFromResult(result));
      recordAnswer(isCorrect);

      const nextBtn = container.querySelector('#ex-next');
      setupNextBtn(nextBtn, () => onComplete({ result, word, xp: isCorrect ? 4 : 1 }), isCorrect);
    });
  });
}

/**
 * Gat-invullen (type) — toon een zin met ___, typ het juiste woord.
 */
export function renderFillBlankType(exercise, container, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();
  const gapped = makeGapSentence(word);
  if (!gapped) {
    renderTypeExercise(exercise, container, onComplete);
    return;
  }

  const stem = stripArticle(word.it);

  container.innerHTML = `
    <div class="ex-label">Vul het ontbrekende woord in</div>
    <div class="fib-hint">${word.nl}</div>
    <div class="fib-sentence">${gapped}</div>
    <div class="type-input-wrap">
      <input
        type="text"
        class="type-input"
        id="fib-input"
        placeholder="Typ het ontbrekende woord..."
        autocomplete="off"
        autocorrect="off"
        autocapitalize="none"
        spellcheck="false"
      >
      <button class="type-submit-btn" id="fib-submit">✓</button>
    </div>
    <button class="type-skip-btn" id="fib-skip">Weet ik niet →</button>
    <div class="type-feedback" id="fib-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  const input     = container.querySelector('#fib-input');
  const submitBtn = container.querySelector('#fib-submit');
  const feedback  = container.querySelector('#fib-feedback');
  const skipBtn   = container.querySelector('#fib-skip');
  let answered = false;

  setTimeout(() => input.focus(), 100);

  const checkAnswer = () => {
    if (answered) return;
    const typed = input.value.trim();
    if (!typed) {
      input.classList.add('shake');
      setTimeout(() => input.classList.remove('shake'), 400);
      return;
    }

    answered = true;
    input.disabled = true;
    submitBtn.disabled = true;

    const result  = checkTypedAnswer(typed, stem);
    const nextBtn = container.querySelector('#ex-next');

    if (result === 'correct') {
      input.classList.add('input-correct');
      feedback.className = 'type-feedback correct show';
      feedback.innerHTML = `✓ Correct! <em>"${word.ex}"</em>`;
      if (hasTTS) setTimeout(() => speak(word.ex), 400);
      updateWordState(word.id, 4);
      recordAnswer(true);
      setupNextBtn(nextBtn, () => onComplete({ result: 'correct', word, xp: 4 }), true);
    } else if (result === 'close') {
      input.classList.add('input-close');
      feedback.className = 'type-feedback close show';
      feedback.innerHTML = `≈ Bijna! Je schreef "<strong>${typed}</strong>", het is <strong>${stem}</strong> — "${word.ex}"`;
      if (hasTTS) setTimeout(() => speak(word.ex), 500);
      updateWordState(word.id, qualityFromResult('close'));
      recordAnswer(false);
      setupNextBtn(nextBtn, () => onComplete({ result: 'close', word, xp: 2 }), false);
    } else {
      input.classList.add('input-wrong');
      feedback.className = 'type-feedback wrong show';
      feedback.innerHTML = `✗ Het juiste woord is: <strong>${stem}</strong> — "${word.ex}"`;
      if (hasTTS) setTimeout(() => speak(word.ex), 600);
      updateWordState(word.id, 0);
      recordAnswer(false);
      setupNextBtn(nextBtn, () => onComplete({ result: 'wrong', word, xp: 1 }), false);
    }
  };

  submitBtn.addEventListener('click', checkAnswer);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') checkAnswer(); });

  skipBtn.addEventListener('click', () => {
    if (answered) return;
    answered = true;
    input.disabled = true;
    submitBtn.disabled = true;
    skipBtn.style.display = 'none';
    input.classList.add('input-wrong');
    feedback.className = 'type-feedback wrong show';
    feedback.innerHTML = `Het antwoord is: <strong>${stem}</strong> — "${word.ex}"`;
    if (hasTTS) setTimeout(() => speak(word.ex), 400);
    updateWordState(word.id, 0);
    recordAnswer(false);
    const nextBtn = container.querySelector('#ex-next');
    nextBtn.style.display = 'block';
    nextBtn.addEventListener('click', () => onComplete({ result: 'wrong', word, xp: 0 }));
  });
}


/**
 * Koppelen (matching) — koppel 4 Italiaanse woorden aan hun Nederlandse vertaling.
 * exercise.words = array van 4 woordobjecten (geselecteerd in buildExerciseQueue).
 */
export function renderMatching(exercise, container, onComplete) {
  const pairs = exercise.words;
  const hasTTS = isTTSAvailable();

  const leftItems  = shuffleEx(pairs.map(w => ({ id: w.id, text: stripArticle(w.it), full: w.it })));
  const rightItems = shuffleEx(pairs.map(w => ({ id: w.id, text: w.nl })));

  let selectedLeft = null;
  let matched = new Set();
  let attempts = 0;
  let errors = 0;

  const rebuild = () => {
    const leftCol  = container.querySelector('#match-left');
    const rightCol = container.querySelector('#match-right');

    leftCol.innerHTML = leftItems.map(item => {
      const done = matched.has(item.id);
      const sel  = selectedLeft === item.id;
      return `<button class="match-chip ${done ? 'match-done' : ''} ${sel ? 'match-selected' : ''}" data-id="${item.id}" data-side="left" ${done ? 'disabled' : ''}>${item.text}</button>`;
    }).join('');

    rightCol.innerHTML = rightItems.map(item => {
      const done = matched.has(item.id);
      return `<button class="match-chip ${done ? 'match-done' : ''}" data-id="${item.id}" data-side="right" ${done ? 'disabled' : ''}>${item.text}</button>`;
    }).join('');

    // Event listeners
    leftCol.querySelectorAll('.match-chip:not([disabled])').forEach(btn => {
      btn.addEventListener('click', () => {
        selectedLeft = btn.dataset.id;
        if (hasTTS) {
          const item = leftItems.find(i => i.id === btn.dataset.id);
          if (item) speak(item.full);
        }
        rebuild();
      });
    });

    rightCol.querySelectorAll('.match-chip:not([disabled])').forEach(btn => {
      btn.addEventListener('click', () => {
        if (!selectedLeft) return;
        attempts++;
        const isMatch = btn.dataset.id === selectedLeft;

        if (isMatch) {
          matched.add(selectedLeft);
          // Flash groen
          const leftBtn = leftCol.querySelector(`[data-id="${selectedLeft}"]`);
          if (leftBtn) leftBtn.classList.add('match-correct');
          btn.classList.add('match-correct');
          selectedLeft = null;

          if (matched.size === pairs.length) {
            // Alle paren gekoppeld
            setTimeout(() => {
              const allCorrect = errors === 0;
              const fb = container.querySelector('#match-feedback');
              fb.className = 'mc-feedback correct show';
              fb.innerHTML = allCorrect
                ? '✓ Perfect! Alle paren correct gekoppeld.'
                : `✓ Klaar! ${errors} fout${errors > 1 ? 'en' : ''} gemaakt.`;

              const result = allCorrect ? 'correct' : 'wrong';
              pairs.forEach(w => {
                updateWordState(w.id, allCorrect ? 4 : 2);
              });
              recordAnswer(allCorrect);

              const nextBtn = container.querySelector('#ex-next');
              setupNextBtn(nextBtn, () => onComplete({ result, word: pairs[0], xp: allCorrect ? 6 : 2 }), allCorrect);
            }, 400);
          } else {
            setTimeout(rebuild, 400);
          }
        } else {
          errors++;
          // Flash rood
          const leftBtn = leftCol.querySelector(`[data-id="${selectedLeft}"]`);
          if (leftBtn) leftBtn.classList.add('match-wrong');
          btn.classList.add('match-wrong');
          selectedLeft = null;
          setTimeout(() => {
            leftCol.querySelectorAll('.match-wrong').forEach(b => b.classList.remove('match-wrong'));
            rightCol.querySelectorAll('.match-wrong').forEach(b => b.classList.remove('match-wrong'));
            rebuild();
          }, 600);
        }
      });
    });
  };

  container.innerHTML = `
    <div class="ex-label">Koppel de woorden</div>
    <div class="match-grid">
      <div class="match-col" id="match-left"></div>
      <div class="match-col" id="match-right"></div>
    </div>
    <div class="mc-feedback" id="match-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  rebuild();
}


/**
 * Fout zoeken — toon een Italiaanse zin met één fout woord; tik op het foute woord.
 */
export function renderFindError(exercise, container, allWords, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();

  // Kies een afleider voor het doelwoord
  const [distractor] = getDistractors(word, allWords, 1);
  if (!distractor || !word.ex) {
    renderMultipleChoice(exercise, container, allWords, onComplete);
    return;
  }

  const stem = stripArticle(word.it);
  const distractorStem = stripArticle(distractor.it);
  const stemNorm = normalize(stem);

  // Tokenize op spaties en vind het doelwoord via normalize (werkt ook met accenten)
  const tokens = (word.ex.match(/\S+/g) || []);
  const targetIdx = tokens.findIndex(t => normalize(t.replace(/[.,!?;:]/g, '')) === stemNorm);
  if (targetIdx === -1) {
    renderMultipleChoice(exercise, container, allWords, onComplete);
    return;
  }

  // Bouw fout-zin: vervang doelwoord door afleider, behoud leestekens
  const punct = tokens[targetIdx].match(/[.,!?;:]+$/)?.[0] || '';
  const isCapital = /^[A-Z]/.test(tokens[targetIdx]);
  const errorWord = (isCapital
    ? distractorStem.charAt(0).toUpperCase() + distractorStem.slice(1)
    : distractorStem) + punct;
  const errorTokens = [...tokens];
  errorTokens[targetIdx] = errorWord;
  const wrongIdx = targetIdx;

  let answered = false;

  container.innerHTML = `
    <div class="ex-label">Tik op het foute woord</div>
    ${hasTTS ? `<button class="fe-tts-btn" id="fe-tts">🔊</button>` : ''}
    <div class="fe-sentence" id="fe-sentence">
      ${errorTokens.map((t, i) => `<button class="fe-chip" data-idx="${i}">${t}</button>`).join('')}
    </div>
    <div class="mc-feedback" id="fe-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  if (hasTTS) {
    container.querySelector('#fe-tts').addEventListener('click', () => speak(errorSentence));
    setTimeout(() => speak(errorSentence), 400);
  }

  container.querySelectorAll('.fe-chip').forEach(btn => {
    btn.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const idx = parseInt(btn.dataset.idx);
      const isCorrect = idx === wrongIdx;
      const result = isCorrect ? 'correct' : 'wrong';

      container.querySelectorAll('.fe-chip').forEach((b, i) => {
        b.classList.add('disabled');
        if (i === wrongIdx) b.classList.add('correct');
        else if (b === btn && !isCorrect) b.classList.add('wrong');
      });

      const fb = container.querySelector('#fe-feedback');
      fb.className = `mc-feedback ${result} show`;
      if (isCorrect) {
        fb.innerHTML = `✓ Goed! De juiste zin is: <em>"${word.ex}"</em>`;
      } else {
        fb.innerHTML = `✗ Het foute woord was <strong>${distractorStem}</strong>. Juiste zin: <em>"${word.ex}"</em>`;
      }
      if (hasTTS) setTimeout(() => speak(word.ex), 600);

      updateWordState(word.id, qualityFromResult(result));
      recordAnswer(isCorrect);
      setupNextBtn(container.querySelector('#ex-next'), () => onComplete({ result, word, xp: isCorrect ? 3 : 1 }), isCorrect);
    });
  });
}


/**
 * Zinsdictee — TTS spreekt een volledige zin; typ de Italiaanse zin.
 * Vereist TTS; fallback naar word-order als TTS niet beschikbaar.
 */
export function renderSentenceDictation(exercise, container, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();

  if (!hasTTS || !word.ex) {
    renderWordOrder(exercise, container, onComplete);
    return;
  }

  container.innerHTML = `
    <div class="ex-label">Typ de zin die je hoort</div>
    <button class="sd-play-btn" id="sd-tts">🔊 Speel zin af</button>
    <div class="sd-hint">Tip: tik nogmaals op 🔊 om opnieuw te luisteren</div>
    <div class="type-input-wrap">
      <input class="type-input" id="sd-input" type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" placeholder="Typ de ${getLang().adj} zin...">
    </div>
    <button class="type-check-btn" id="sd-check">Controleer</button>
    <div class="type-feedback" id="sd-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  setTimeout(() => speak(word.ex), 400);
  container.querySelector('#sd-tts').addEventListener('click', () => speak(word.ex));

  let answered = false;
  const input = container.querySelector('#sd-input');
  const checkBtn = container.querySelector('#sd-check');
  const feedback = container.querySelector('#sd-feedback');

  const check = () => {
    if (answered || !input.value.trim()) return;
    answered = true;
    input.disabled = true;
    checkBtn.disabled = true;

    const result = checkSentenceAnswer(input.value.trim(), word.ex);
    const isCorrect = result === 'correct';
    const isClose = result === 'close';

    input.classList.add(isCorrect ? 'input-correct' : isClose ? 'input-close' : 'input-wrong');
    feedback.className = `type-feedback ${result} show`;
    if (isCorrect) {
      feedback.innerHTML = `✓ Correct! <em>"${word.ex}"</em>`;
    } else if (isClose) {
      feedback.innerHTML = `≈ Bijna! De juiste zin is: <strong>"${word.ex}"</strong>`;
      setTimeout(() => speak(word.ex), 500);
    } else {
      feedback.innerHTML = `✗ De juiste zin is: <strong>"${word.ex}"</strong>`;
      setTimeout(() => speak(word.ex), 600);
    }

    updateWordState(word.id, qualityFromResult(result));
    recordAnswer(isCorrect || isClose);
    setupNextBtn(container.querySelector('#ex-next'), () => onComplete({ result, word, xp: isCorrect ? 5 : isClose ? 2 : 1 }), isCorrect);
  };

  checkBtn.addEventListener('click', check);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
  setTimeout(() => input.focus(), 100);
}


/**
 * Categorie sorteren — wijs 6 woorden (2 categorieën × 3) toe aan de juiste categorie.
 */
export function renderCategorySort(exercise, container, onComplete) {
  const { words } = exercise;
  const cats = [...new Set(words.map(w => w.cat))].slice(0, 2);
  if (cats.length < 2) {
    onComplete({ result: 'correct', word: words[0], xp: 2 });
    return;
  }

  const shuffled = shuffleEx([...words]);
  const assignments = {};
  let selectedId = null;

  container.innerHTML = `
    <div class="ex-label">Sorteer de woorden in de juiste categorie</div>
    <div class="cs-pool" id="cs-pool">
      ${shuffled.map(w => `
        <button class="cs-chip" data-id="${w.id}">
          ${w.it}<span class="cs-chip-nl">${w.nl}</span>
        </button>`).join('')}
    </div>
    <div class="cs-buckets">
      <div class="cs-bucket" id="cs-b0" data-cat="${cats[0]}">
        <div class="cs-bucket-label">${capitalize(cats[0])}</div>
        <div class="cs-bucket-words" id="cs-bw0"></div>
      </div>
      <div class="cs-bucket" id="cs-b1" data-cat="${cats[1]}">
        <div class="cs-bucket-label">${capitalize(cats[1])}</div>
        <div class="cs-bucket-words" id="cs-bw1"></div>
      </div>
    </div>
    <div class="mc-feedback" id="cs-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  const refreshChips = () => {
    container.querySelectorAll('.cs-chip').forEach(c => {
      c.classList.toggle('cs-selected', c.dataset.id === selectedId);
    });
    container.querySelectorAll('.cs-bucket').forEach(b => {
      b.classList.toggle('cs-bucket-active', !!selectedId);
    });
  };

  // Stap 1: selecteer een woord
  container.querySelectorAll('.cs-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      selectedId = selectedId === chip.dataset.id ? null : chip.dataset.id;
      refreshChips();
    });
  });

  // Stap 2: tik op een categorie om het woord te plaatsen
  container.querySelectorAll('.cs-bucket').forEach((bucket, bIdx) => {
    bucket.addEventListener('click', () => {
      if (!selectedId) return;
      const cat = bucket.dataset.cat;
      const w = words.find(x => x.id === selectedId);
      if (!w) return;

      assignments[selectedId] = cat;
      selectedId = null;

      // Verplaats chip naar bucket
      const chip = container.querySelector(`.cs-chip[data-id="${w.id}"]`);
      chip.classList.remove('cs-selected');
      container.querySelector(`#cs-bw${bIdx}`).appendChild(chip);
      refreshChips();

      // Zijn alle woorden geplaatst?
      if (Object.keys(assignments).length === words.length) {
        let correct = 0;
        words.forEach(x => {
          const c = container.querySelector(`.cs-chip[data-id="${x.id}"]`);
          if (assignments[x.id] === x.cat) { correct++; c.classList.add('cs-correct'); }
          else c.classList.add('cs-wrong');
        });

        const allCorrect = correct === words.length;
        const fb = container.querySelector('#cs-feedback');
        fb.className = `mc-feedback ${allCorrect ? 'correct' : 'wrong'} show`;
        fb.innerHTML = allCorrect
          ? `✓ Perfect! Alle woorden correct gesorteerd.`
          : `${correct} van ${words.length} correct gesorteerd.`;

        words.forEach(x => updateWordState(x.id, allCorrect ? 4 : 2));
        recordAnswer(allCorrect);
        const result = allCorrect ? 'correct' : correct >= words.length / 2 ? 'close' : 'wrong';
        setupNextBtn(container.querySelector('#ex-next'), () => onComplete({ result, word: words[0], xp: allCorrect ? 6 : 2 }), allCorrect);
      }
    });
  });
}


// ─── Queue builder ─────────────────────────────────────────────────────────────

/**
 * Genereer een oefenwachtrij.
 * Nieuwe woorden: flashcard → recognition (MC of listen-choose) → type
 * Plus word-order voor woorden met zinnen van 3+ tokens (max 3 per les)
 * Review-woorden: 1 oefening, random type
 */
export function buildExerciseQueue(newWords, reviewWords, allWords) {
  const queue = [];
  const ttsOk = isTTSAvailable();

  newWords.forEach(word => {
    queue.push({ type: 'flashcard', word, isNew: true });

    // Erkenning: MC of listen-choose (listen-choose alleen als TTS beschikbaar)
    const useListenChoose = ttsOk && Math.random() < 0.5;
    queue.push({ type: useListenChoose ? 'listen-choose' : 'multiple-choice', word, isNew: true });

    // Productie: type of listen-type (dictee) — 30% kans op dictee als TTS beschikbaar
    const useListenType = ttsOk && Math.random() < 0.30;
    queue.push({ type: useListenType ? 'listen-type' : 'type', word, isNew: false });
  });

  // Word-order: voor woorden met 3+ token-zinnen, max 3 per les
  const woWords = newWords
    .filter(w => sentenceToTokens(w.ex).length >= 3)
    .slice(0, 3);
  woWords.forEach(word => {
    queue.push({ type: 'word-order', word, isNew: false });
  });

  // Zinsoefening: max 2 per les, aangeboden nadat woord al geproduceerd is
  const scWords = newWords.filter(w => w.ex && w.exNl).slice(0, 2);
  scWords.forEach(word => {
    queue.push({ type: 'sentence-choice', word, isNew: false });
  });

  // Gat-invullen (MC): max 3 per les, alleen voor woorden waar een gat gemaakt kan worden
  const fibWords = newWords.filter(w => makeGapSentence(w) !== null).slice(0, 3);
  fibWords.forEach(word => {
    queue.push({ type: 'fill-in-blank-mc', word, isNew: false });
  });

  // Koppelen: 1 groepsoefening per les met 4 willekeurige woorden uit de les
  if (newWords.length >= 4) {
    const matchWords = shuffleEx([...newWords]).slice(0, 4);
    queue.push({ type: 'matching', words: matchWords, isNew: false });
  }

  // Fout zoeken: max 2 per les, voor woorden met een vindbaar doelwoord in de zin
  const feWords = newWords.filter(w => makeGapSentence(w) !== null).slice(0, 2);
  feWords.forEach(word => queue.push({ type: 'find-error', word, isNew: false }));

  // Zinsdictee: max 2 per les, alleen als TTS beschikbaar
  if (ttsOk) {
    const sdWords = newWords.filter(w => w.ex).slice(0, 2);
    sdWords.forEach(word => queue.push({ type: 'sentence-dictation', word, isNew: false }));
  }

  // Categorie sorteren: 1 per les als er 2+ categorieën zijn
  const csGroups = buildCategoryGroups(newWords);
  if (csGroups) queue.push({ type: 'category-sort', words: [...csGroups[0], ...csGroups[1]], isNew: false });

  // Vervoegen (v1.45): max 2 per les voor vervoegbare werkwoorden — eerst kiezen, dan typen
  const conjWords = newWords.filter(w => conjEngine().is(w.it)).slice(0, 2);
  conjWords.forEach((word, i) => queue.push({ type: 'conjugation', word, isNew: false, mode: i === 0 ? 'mc' : 'type' }));

  // Review: random type, inclusief alle oefenvormen
  reviewWords.forEach(word => {
    const types = ['multiple-choice', 'type'];
    if (ttsOk) {
      types.push('listen-choose');
      types.push('listen-type');
      if (word.ex) types.push('sentence-dictation');
    }
    if (sentenceToTokens(word.ex).length >= 3) types.push('word-order');
    if (word.ex && word.exNl) types.push('sentence-choice');
    if (makeGapSentence(word) !== null) {
      types.push('fill-in-blank-type');
      types.push('find-error');
    }
    if (conjEngine().is(word.it)) types.push('conjugation');
    const type = types[Math.floor(Math.random() * types.length)];
    queue.push({ type, word, isNew: false });
  });

  // Koppelen review: als er 4+ review-woorden zijn
  if (reviewWords.length >= 4) {
    const matchReview = shuffleEx([...reviewWords]).slice(0, 4);
    queue.push({ type: 'matching', words: matchReview, isNew: false });
  }

  // Categorie sorteren review: als review-woorden 2+ categorieën bevatten
  const csReview = buildCategoryGroups(reviewWords);
  if (csReview) queue.push({ type: 'category-sort', words: [...csReview[0], ...csReview[1]], isNew: false });

  // Flashcards eerst (introductie), rest geshuffled
  const flashcards = queue.filter(e => e.type === 'flashcard');
  const rest = shuffleEx(queue.filter(e => e.type !== 'flashcard'));
  return [...flashcards, ...rest];
}


// ─── Renderers ─────────────────────────────────────────────────────────────────

/**
 * Les-intro kaart — toont voor de eerste oefening.
 * Geeft de gebruiker context: onderwerp, woordpreview, grammatica-hint.
 */
export function renderLessonIntro(exercise, container, onComplete) {
  const { lesson, words } = exercise;
  const preview = words.slice(0, 3);
  const estMin  = Math.max(2, Math.round(words.length * 0.5));

  container.innerHTML = `
    <div class="intro-card">
      <div class="intro-emoji">${lesson.emoji}</div>
      <div class="intro-title">${lesson.title}</div>
      <div class="intro-desc">${lesson.description}</div>

      <div class="intro-words-label">In deze les leer je:</div>
      <div class="intro-words">
        ${preview.map(w => `
          <div class="intro-word-row">
            <span class="intro-it">${w.it}</span>
            <span class="intro-arrow">→</span>
            <span class="intro-nl">${w.nl}</span>
          </div>
        `).join('')}
        ${words.length > 3 ? `<div class="intro-more">+ ${words.length - 3} meer woorden</div>` : ''}
      </div>

      <div class="intro-grammar-hint">
        📖 <strong>${lesson.grammar.title}</strong>
      </div>

      <div class="intro-meta">
        <span>⏱️ ~${estMin} min</span>
        <span>·</span>
        <span>${words.length} woorden</span>
        <span>·</span>
        <span>${lesson.level}</span>
      </div>

      <button class="ex-next-btn intro-start-btn" id="intro-start">Start les →</button>
    </div>
  `;

  container.querySelector('#intro-start')
    .addEventListener('click', () => onComplete({ result: 'intro', xp: 0 }));
}


/**
 * Flashcard oefening.
 */
export function renderFlashcard(exercise, container, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();

  container.innerHTML = `
    <div class="ex-label">Vertaal naar ${getLang().name}</div>
    <div class="flashcard-ex" id="fc-scene">
      <div class="fc-card" id="fc-card">
        <div class="fc-front">
          <div class="fc-lang">Nederlands</div>
          <div class="fc-word">${word.nl}</div>
          <div class="fc-tap-hint">Tik om te onthullen</div>
        </div>
        <div class="fc-back">
          <div class="fc-lang">${getLang().name}</div>
          <div class="fc-it">${word.it}</div>
          <div class="fc-ph">[${word.ph}]</div>
          <div class="fc-ex">"${word.ex}"</div>
          ${hasTTS ? `<button class="fc-audio-btn" id="fc-audio">🔊 Uitspreken</button>` : ''}
        </div>
      </div>
    </div>
    <div class="fc-actions" id="fc-actions" style="display:none">
      <button class="fc-btn fc-hard" data-q="1">😓<span>Moeilijk</span></button>
      <button class="fc-btn fc-ok"   data-q="3">🙂<span>Goed</span></button>
      <button class="fc-btn fc-easy" data-q="5">😄<span>Makkelijk</span></button>
    </div>
  `;

  const card    = container.querySelector('#fc-card');
  const scene   = container.querySelector('#fc-scene');
  const actions = container.querySelector('#fc-actions');
  let revealed = false;
  let flipped  = false;

  scene.addEventListener('click', () => {
    if (!revealed) {
      // Eerste klik: onthul Italiaanse kant
      revealed = true;
      flipped  = true;
      card.classList.add('flipped');
      actions.style.display = 'flex';
      if (hasTTS) speak(word.it);
    } else {
      // Volgende klikken: toggle terug/heen
      flipped = !flipped;
      card.classList.toggle('flipped', flipped);
    }
  });

  const audioBtn = container.querySelector('#fc-audio');
  if (audioBtn) audioBtn.addEventListener('click', e => { e.stopPropagation(); speak(word.it); });

  container.querySelectorAll('.fc-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const quality = parseInt(btn.dataset.q);
      const result  = quality >= 3 ? 'correct' : 'wrong';
      updateWordState(word.id, quality);
      recordAnswer(result === 'correct');
      onComplete({ result, word, xp: quality >= 3 ? 2 : 1 });
    });
  });
}


/**
 * Multiple-choice — Nederlands → kies het Italiaanse woord.
 */
export function renderMultipleChoice(exercise, container, allWords, onComplete) {
  const { word } = exercise;
  const distractors = getDistractors(word, allWords, 3);
  const options  = shuffleEx([word, ...distractors]);
  const hasTTS   = isTTSAvailable();

  container.innerHTML = `
    <div class="ex-label">Wat is de ${getLang().adj} vertaling?</div>
    <div class="mc-question">
      <div class="mc-nl">${word.nl}</div>
      ${word.exNl ? `<div class="mc-context">"${word.exNl}"</div>` : ''}
    </div>
    <div class="mc-options" id="mc-options">
      ${options.map((opt, i) => `
        <button class="mc-option" data-id="${opt.id}" data-correct="${opt.id === word.id}">
          <span class="mc-letter">${['A','B','C','D'][i]}</span>
          <span class="mc-text">${opt.it}</span>
          ${hasTTS ? `<span class="mc-play" data-word="${opt.it}">🔊</span>` : ''}
        </button>
      `).join('')}
    </div>
    <div class="mc-feedback" id="mc-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  if (hasTTS) {
    container.querySelectorAll('.mc-play').forEach(btn => {
      btn.addEventListener('click', e => { e.stopPropagation(); speak(btn.dataset.word); });
    });
  }

  let answered = false;
  container.querySelectorAll('.mc-option').forEach(btn => {
    btn.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const isCorrect = btn.dataset.correct === 'true';
      const result = isCorrect ? 'correct' : 'wrong';

      container.querySelectorAll('.mc-option').forEach(b => {
        b.classList.add('disabled');
        if (b.dataset.correct === 'true') b.classList.add('correct');
        else if (b === btn) b.classList.add('wrong');
      });

      const fb = container.querySelector('#mc-feedback');
      if (isCorrect) {
        fb.className = 'mc-feedback correct show';
        fb.innerHTML = `✓ Correct! <em>[${word.ph}]</em>`;

        if (hasTTS) setTimeout(() => speak(word.it), 400);
      } else {
        fb.className = 'mc-feedback wrong show';
        fb.innerHTML = `✗ Fout. Het antwoord is: <strong>${word.it}</strong> <em>[${word.ph}]</em>`;
        if (hasTTS) setTimeout(() => speak(word.it), 500);
      }

      updateWordState(word.id, qualityFromResult(result));
      recordAnswer(isCorrect);

      const nextBtn = container.querySelector('#ex-next');
      setupNextBtn(nextBtn, () => onComplete({ result, word, xp: isCorrect ? 4 : 1 }), isCorrect);
    });
  });
}


/**
 * Zinsoefening — Kies de juiste Italiaanse zin bij een Nederlandse zin.
 * Aangeboden nadat een woord al eens gezien is (isNew: false).
 */
export function renderSentenceChoice(exercise, container, allWords, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();

  const distractors = allWords
    .filter(w => w.id !== word.id && w.ex)
    .sort(() => Math.random() - 0.5)
    .slice(0, 3);
  const options = shuffleEx([word, ...distractors]);

  container.innerHTML = `
    <div class="ex-label">Welke zin klopt?</div>
    <div class="sc-nl-sentence">"${word.exNl}"</div>
    <div class="mc-options" id="sc-options">
      ${options.map((opt, i) => `
        <button class="mc-option sc-option" data-id="${opt.id}" data-correct="${opt.id === word.id}">
          <span class="mc-letter">${['A','B','C','D'][i]}</span>
          <span class="mc-text">${opt.ex}</span>
        </button>
      `).join('')}
    </div>
    <div class="mc-feedback" id="sc-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  let answered = false;
  container.querySelectorAll('.mc-option').forEach(btn => {
    btn.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const isCorrect = btn.dataset.correct === 'true';
      const result = isCorrect ? 'correct' : 'wrong';

      container.querySelectorAll('.mc-option').forEach(b => {
        b.classList.add('disabled');
        if (b.dataset.correct === 'true') b.classList.add('correct');
        else if (b === btn) b.classList.add('wrong');
      });

      const fb = container.querySelector('#sc-feedback');
      if (isCorrect) {
        fb.className = 'mc-feedback correct show';
        fb.innerHTML = `✓ Correct! <em>${word.it}</em> — "${word.ex}"`;
        if (hasTTS) setTimeout(() => speak(word.ex), 400);
      } else {
        fb.className = 'mc-feedback wrong show';
        fb.innerHTML = `✗ Fout. De vertaling is: <strong>"${word.ex}"</strong>`;
        if (hasTTS) setTimeout(() => speak(word.ex), 500);
      }

      updateWordState(word.id, qualityFromResult(result));
      recordAnswer(isCorrect);

      const nextBtn = container.querySelector('#ex-next');
      setupNextBtn(nextBtn, () => onComplete({ result, word, xp: isCorrect ? 4 : 1 }), isCorrect);
    });
  });
}


/**
 * Luister & kies — TTS speelt het Italiaanse woord af, kies de Nederlandse vertaling.
 * Doel: auditief herkennen van Italiaans.
 */
export function renderListenChoose(exercise, container, allWords, onComplete) {
  const { word } = exercise;
  const distractors = getDistractors(word, allWords, 3);
  const options  = shuffleEx([word, ...distractors]);
  const hasTTS   = isTTSAvailable();

  container.innerHTML = `
    <div class="ex-label">Welk woord hoor je?</div>

    <div class="lc-audio-section">
      <button class="lc-play-btn" id="lc-play">🔊 Afspelen</button>
      <div class="lc-word-reveal" id="lc-reveal" style="visibility:hidden">
        <span class="lc-it">${word.it}</span>
        <span class="lc-ph">[${word.ph}]</span>
      </div>
    </div>

    <div class="mc-options" id="lc-options">
      ${options.map((opt, i) => `
        <button class="mc-option" data-id="${opt.id}" data-correct="${opt.id === word.id}">
          <span class="mc-letter">${['A','B','C','D'][i]}</span>
          <span class="mc-text">${opt.nl}</span>
        </button>
      `).join('')}
    </div>
    <div class="mc-feedback" id="lc-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  let hasPlayed = false;
  const playBtn  = container.querySelector('#lc-play');
  const revealEl = container.querySelector('#lc-reveal');

  const playWord = () => {
    if (hasTTS) speak(word.it);
    hasPlayed = true;
  };

  playBtn.addEventListener('click', playWord);

  // Auto-play na 2000ms — knoptekst blijft stabiel
  if (hasTTS) setTimeout(playWord, 2000);

  let answered = false;
  container.querySelectorAll('.mc-option').forEach(btn => {
    btn.addEventListener('click', () => {
      if (answered) return;
      if (!hasPlayed) {
        // Speel eerst af — forceer de gebruiker te luisteren
        playWord();
        playBtn.classList.add('shake');
        setTimeout(() => playBtn.classList.remove('shake'), 400);
        return;
      }
      answered = true;
      const isCorrect = btn.dataset.correct === 'true';
      const result = isCorrect ? 'correct' : 'wrong';

      container.querySelectorAll('.mc-option').forEach(b => {
        b.classList.add('disabled');
        if (b.dataset.correct === 'true') b.classList.add('correct');
        else if (b === btn) b.classList.add('wrong');
      });

      // Onthul het Italiaanse woord
      revealEl.style.visibility = 'visible';
      revealEl.style.animation = 'slideIn 0.3s ease';

      const fb = container.querySelector('#lc-feedback');
      if (isCorrect) {
        fb.className = 'mc-feedback correct show';
        fb.innerHTML = `✓ Correct! <strong>${word.it}</strong> = ${word.nl}`;

      } else {
        fb.className = 'mc-feedback wrong show';
        fb.innerHTML = `✗ Fout. Het juiste antwoord was: <strong>${word.nl}</strong>`;
        if (hasTTS) setTimeout(() => speak(word.it), 600);
      }

      updateWordState(word.id, qualityFromResult(result));
      recordAnswer(isCorrect);

      const nextBtn = container.querySelector('#ex-next');
      setupNextBtn(nextBtn, () => onComplete({ result, word, xp: isCorrect ? 4 : 1 }), isCorrect);
    });
  });
}


/**
 * Typ-het-woord oefening.
 */
export function renderTypeExercise(exercise, container, onComplete) {
  const { word } = exercise;
  const hasTTS = isTTSAvailable();

  container.innerHTML = `
    <div class="ex-label">Typ het ${getLang().adj} woord</div>
    <div class="type-question">
      <div class="type-nl">${word.nl}</div>
      ${word.exNl ? `<div class="type-context">"${word.exNl}"</div>` : ''}
    </div>
    <div class="type-input-wrap">
      <input
        type="text"
        class="type-input"
        id="type-input"
        placeholder="Typ hier in het ${getLang().name}..."
        autocomplete="off"
        autocorrect="off"
        autocapitalize="none"
        spellcheck="false"
      >
      <button class="type-submit-btn" id="type-submit">✓</button>
    </div>
    <div class="type-hint" id="type-hint"></div>
    <button class="type-skip-btn" id="type-skip">Weet ik niet →</button>
    <div class="type-feedback" id="type-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  const input     = container.querySelector('#type-input');
  const submitBtn = container.querySelector('#type-submit');
  const feedback  = container.querySelector('#type-feedback');
  const hint      = container.querySelector('#type-hint');
  const skipBtn   = container.querySelector('#type-skip');
  let answered  = false;
  let hintShown = false;

  setTimeout(() => input.focus(), 100);

  // Hint: gehusselde letterpanelen
  const showHint = () => {
    hintShown = true;
    const tiles = word.it.split('').map(l => l === ' ' ? null : l);
    const nonSpaces = tiles.filter(Boolean);
    const shuffled = shuffleEx([...nonSpaces]);
    let si = 0;
    const tileHtml = word.it.split('').map(l => {
      if (l === ' ') return '<span class="hint-space"> </span>';
      return `<span class="hint-tile">${shuffled[si++]}</span>`;
    }).join('');
    hint.innerHTML = `<div class="hint-label">💡 Hint — zet de letters op volgorde:</div><div class="hint-tiles">${tileHtml}</div>`;
  };

  const hintTimer = setTimeout(() => {
    if (!answered) {
      hint.innerHTML = `<button class="hint-btn" id="hint-btn">💡 Hint tonen</button>`;
      container.querySelector('#hint-btn')?.addEventListener('click', showHint);
    }
  }, 5000);

  const checkAnswer = () => {
    if (answered) return;
    const typed = input.value.trim();
    if (!typed) {
      input.classList.add('shake');
      setTimeout(() => input.classList.remove('shake'), 400);
      return;
    }

    clearTimeout(hintTimer);
    answered = true;
    input.disabled = true;
    submitBtn.disabled = true;
    hint.innerHTML = '';

    const result  = checkTypedAnswer(typed, word.it);
    const nextBtn = container.querySelector('#ex-next');

    if (result === 'correct') {
      input.classList.add('input-correct');
      feedback.className = 'type-feedback correct show';
      feedback.innerHTML = `✓ Perfect! <em>[${word.ph}]</em>`;
      if (hasTTS) setTimeout(() => speak(word.it), 400);
      updateWordState(word.id, hintShown ? 3 : 5);
      recordAnswer(true);
      setupNextBtn(nextBtn, () => onComplete({ result: 'correct', word, xp: hintShown ? 3 : 5 }), true);
    } else if (result === 'close') {
      input.classList.add('input-close');
      feedback.className = 'type-feedback close show';
      feedback.innerHTML = `≈ Bijna! Je schreef "<strong>${typed}</strong>", het is <strong>${word.it}</strong> <em>[${word.ph}]</em>`;
      if (hasTTS) setTimeout(() => speak(word.it), 500);
      updateWordState(word.id, qualityFromResult('close'));
      recordAnswer(false);
      setupNextBtn(nextBtn, () => onComplete({ result: 'close', word, xp: 2 }), false);
    } else {
      input.classList.add('input-wrong');
      feedback.className = 'type-feedback wrong show';
      feedback.innerHTML = `✗ Het juiste antwoord is: <strong>${word.it}</strong> <em>[${word.ph}]</em>`;
      if (hasTTS) setTimeout(() => speak(word.it), 600);
      updateWordState(word.id, 0);
      recordAnswer(false);
      setupNextBtn(nextBtn, () => onComplete({ result: 'wrong', word, xp: 1 }), false);
    }
  };

  submitBtn.addEventListener('click', checkAnswer);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') checkAnswer(); });

  // Skip: antwoord onthullen als wrong
  skipBtn.addEventListener('click', () => {
    if (answered) return;
    clearTimeout(hintTimer);
    answered = true;
    input.disabled = true;
    submitBtn.disabled = true;
    skipBtn.style.display = 'none';
    hint.innerHTML = '';
    input.classList.add('input-wrong');
    feedback.className = 'type-feedback wrong show';
    feedback.innerHTML = `Het antwoord is: <strong>${word.it}</strong> <em>[${word.ph}]</em>`;
    if (hasTTS) setTimeout(() => speak(word.it), 400);
    updateWordState(word.id, 0);
    recordAnswer(false);
    const nextBtn = container.querySelector('#ex-next');
    nextBtn.style.display = 'block';
    nextBtn.addEventListener('click', () => onComplete({ result: 'wrong', word, xp: 0 }));
  });
}


/**
 * Woordvolgorde — tik chips om de Italiaanse zin in de juiste volgorde te zetten.
 * De Nederlandse vertaling staat als context bovenaan.
 */
export function renderWordOrder(exercise, container, onComplete) {
  const { word } = exercise;
  const tokens   = sentenceToTokens(word.ex);
  const hasTTS   = isTTSAvailable();

  if (tokens.length < 2) {
    // Valgback: te kort voor word-order, gebruik type
    renderTypeExercise(exercise, container, onComplete);
    return;
  }

  let available = shuffleEx([...tokens]);
  let assembled = [];
  let answered  = false;

  const rebuildUI = () => {
    const answerEl = container.querySelector('#wo-answer');
    const chipsEl  = container.querySelector('#wo-chips');
    const checkBtn = container.querySelector('#wo-check');

    // Answer area
    if (assembled.length === 0) {
      answerEl.innerHTML = `<span class="wo-placeholder">Tik woorden hieronder om ze toe te voegen</span>`;
    } else {
      answerEl.innerHTML = assembled.map((tok, i) =>
        `<button class="wo-chip wo-chip-placed" data-idx="${i}">${tok}</button>`
      ).join('');
      answerEl.querySelectorAll('.wo-chip-placed').forEach(btn => {
        btn.addEventListener('click', () => {
          if (answered) return;
          const idx = parseInt(btn.dataset.idx);
          available.push(assembled.splice(idx, 1)[0]);
          rebuildUI();
        });
      });
    }

    // Available chips
    chipsEl.innerHTML = available.map((tok, i) =>
      `<button class="wo-chip" data-idx="${i}">${tok}</button>`
    ).join('');
    chipsEl.querySelectorAll('.wo-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        if (answered) return;
        const idx  = parseInt(btn.dataset.idx);
        const tok  = available[idx];
        assembled.push(available.splice(idx, 1)[0]);
        // Spreek chip uit; sla alleen leestekens over (pure punctuatie heeft geen uitspraak).
        // Normaliseer voor TTS: kleine letters + strip accenten (voorkomt "e-acuut" e.d. bij
        // losse klinkers met leesteken, en "hoofdletter X" bij beginhoofdletters).
        const ttsTok = tok.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        if (hasTTS && ttsTok.replace(/[.,!?;:'"«»\-]/g, '').length > 0) speak(ttsTok);
        rebuildUI();
        // Als alle chips geplaatst: toon controleer-knop
        if (available.length === 0 && checkBtn) {
          checkBtn.style.display = 'block';
        }
      });
    });

    // Controleer-knop: verberg als er nog chips beschikbaar zijn
    if (checkBtn && available.length > 0) checkBtn.style.display = 'none';
  };

  container.innerHTML = `
    <div class="ex-label">Zet de woorden in de juiste volgorde</div>
    <div class="wo-context">"${word.exNl}"</div>
    <div class="wo-answer-area" id="wo-answer">
      <span class="wo-placeholder">Tik woorden hieronder om ze toe te voegen</span>
    </div>
    <div class="wo-divider"></div>
    <div class="wo-chips" id="wo-chips"></div>
    <div class="mc-feedback" id="wo-feedback"></div>
    <button class="ex-next-btn" id="wo-check" style="display:none">Controleer →</button>
    <button class="ex-next-btn" id="ex-next"  style="display:none">Volgende →</button>
  `;

  rebuildUI();

  const checkAnswer = () => {
    if (answered) return;
    answered = true;

    const isCorrect = assembled.length === tokens.length &&
      assembled.every((t, i) => normalize(t) === normalize(tokens[i]));
    const result = isCorrect ? 'correct' : 'wrong';

    // Kleur de geplaatste chips
    container.querySelectorAll('.wo-chip-placed').forEach(c => {
      c.classList.add(isCorrect ? 'wo-correct' : 'wo-wrong');
      c.disabled = true;
    });
    container.querySelectorAll('.wo-chip').forEach(c => c.disabled = true);

    const fb      = container.querySelector('#wo-feedback');
    const nextBtn = container.querySelector('#ex-next');
    const checkBtn = container.querySelector('#wo-check');
    if (checkBtn) checkBtn.style.display = 'none';

    if (isCorrect) {
      fb.className = 'mc-feedback correct show';
      fb.innerHTML = `✓ Correct! <em>"${word.ex}"</em>`;
      // Lees de hele zin iets langzamer voor (0.75× gebruikersinstelling)
      if (hasTTS) setTimeout(() => speak(word.ex, Math.max(0.4, getTTSRate() * 0.75)), 400);
    } else {
      fb.className = 'mc-feedback wrong show';
      fb.innerHTML = `✗ De juiste volgorde: <strong>"${word.ex}"</strong>`;
      if (hasTTS) setTimeout(() => speak(word.ex), 600);
    }

    updateWordState(word.id, qualityFromResult(result));
    recordAnswer(isCorrect);

    setupNextBtn(nextBtn, () => onComplete({ result, word, xp: isCorrect ? 5 : 1 }), isCorrect);
  };

  container.querySelector('#wo-check').addEventListener('click', checkAnswer);
}


/**
 * Luister & typ — TTS spreekt het Italiaanse woord uit, typ wat je hoort (dictee).
 * Sprint 8: combineert luistervaardigheid met spelling.
 */
export function renderListenType(exercise, container, onComplete) {
  const { word } = exercise;
  const hasTTS   = isTTSAvailable();

  container.innerHTML = `
    <div class="ex-label">Wat hoor je? Typ het ${getLang().adj} woord</div>

    <div class="lc-audio-section">
      <button class="lc-play-btn" id="lt-play">🔊 Afspelen</button>
    </div>

    <div class="type-input-wrap">
      <input
        type="text"
        class="type-input"
        id="lt-input"
        placeholder="Typ wat je hoort..."
        autocomplete="off"
        autocorrect="off"
        autocapitalize="none"
        spellcheck="false"
      >
      <button class="type-submit-btn" id="lt-submit">✓</button>
    </div>
    <button class="type-skip-btn" id="lt-skip">Weet ik niet →</button>
    <div class="type-feedback" id="lt-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>
  `;

  const playBtn   = container.querySelector('#lt-play');
  const input     = container.querySelector('#lt-input');
  const submitBtn = container.querySelector('#lt-submit');
  const feedback  = container.querySelector('#lt-feedback');
  const skipBtn   = container.querySelector('#lt-skip');
  let answered  = false;
  let hasPlayed = false;

  const playWord = () => {
    if (hasTTS) speak(word.it);
    hasPlayed = true;
  };

  playBtn.addEventListener('click', playWord);
  if (hasTTS) setTimeout(playWord, 400);
  setTimeout(() => input.focus(), 600);

  const checkAnswer = () => {
    if (answered) return;
    if (!hasPlayed) { playWord(); return; }
    const typed = input.value.trim();
    if (!typed) {
      input.classList.add('shake');
      setTimeout(() => input.classList.remove('shake'), 400);
      return;
    }
    answered = true;
    input.disabled = true;
    submitBtn.disabled = true;

    const result  = checkTypedAnswer(typed, word.it);
    const nextBtn = container.querySelector('#ex-next');

    if (result === 'correct') {
      input.classList.add('input-correct');
      feedback.className = 'type-feedback correct show';
      feedback.innerHTML = `✓ Correct! <strong>${word.it}</strong> = ${word.nl} <em>[${word.ph}]</em>`;
      if (hasTTS) setTimeout(() => speak(word.it), 400);
      updateWordState(word.id, 5);
      recordAnswer(true);
      setupNextBtn(nextBtn, () => onComplete({ result: 'correct', word, xp: 5 }), true);
    } else if (result === 'close') {
      input.classList.add('input-close');
      feedback.className = 'type-feedback close show';
      feedback.innerHTML = `≈ Bijna! Je schreef "<strong>${typed}</strong>", het is <strong>${word.it}</strong> = ${word.nl} <em>[${word.ph}]</em>`;
      if (hasTTS) setTimeout(() => speak(word.it), 500);
      updateWordState(word.id, qualityFromResult('close'));
      recordAnswer(false);
      setupNextBtn(nextBtn, () => onComplete({ result: 'close', word, xp: 2 }), false);
    } else {
      input.classList.add('input-wrong');
      feedback.className = 'type-feedback wrong show';
      feedback.innerHTML = `✗ Het is: <strong>${word.it}</strong> = ${word.nl} <em>[${word.ph}]</em>`;
      if (hasTTS) setTimeout(() => speak(word.it), 600);
      updateWordState(word.id, 0);
      recordAnswer(false);
      setupNextBtn(nextBtn, () => onComplete({ result: 'wrong', word, xp: 1 }), false);
    }
  };

  submitBtn.addEventListener('click', checkAnswer);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') checkAnswer(); });

  skipBtn.addEventListener('click', () => {
    if (answered) return;
    answered = true;
    input.disabled = true;
    submitBtn.disabled = true;
    input.classList.add('input-wrong');
    feedback.className = 'type-feedback wrong show';
    feedback.innerHTML = `Het antwoord is: <strong>${word.it}</strong> = ${word.nl} <em>[${word.ph}]</em>`;
    if (hasTTS) setTimeout(() => speak(word.it), 400);
    updateWordState(word.id, 0);
    recordAnswer(false);
    const nextBtn = container.querySelector('#ex-next');
    nextBtn.style.display = 'block';
    nextBtn.addEventListener('click', () => onComplete({ result: 'wrong', word, xp: 0 }));
  });
}

/**
 * Grammatica-kaart.
 */
export function renderGrammarCard(grammarNote, container, onComplete) {
  container.innerHTML = `
    <div class="grammar-card">
      <div class="grammar-icon">📖</div>
      <div class="grammar-title">${grammarNote.title}</div>
      <div class="grammar-body">${grammarNote.body}</div>
      <button class="ex-next-btn grammar-ok-btn" id="grammar-ok">Begrepen! Verder →</button>
    </div>
  `;
  container.querySelector('#grammar-ok')
    .addEventListener('click', () => onComplete({ result: 'grammar', xp: 1 }));
}


// ═══════════════════════════════════════════════════════════════════════════════
// Vervoegen (v1.45) — vervoegingsmotor voor presente, imperfetto en futuro
// ═══════════════════════════════════════════════════════════════════════════════

const PRONOUNS   = ['io', 'tu', 'lui/lei', 'noi', 'voi', 'loro'];
const REFL_PRON  = ['mi', 'ti', 'si', 'ci', 'vi', 'si'];
const TENSE_LABELS = { presente: 'tegenwoordige tijd', passato: 'passato prossimo (voltooide tijd)', imperfetto: 'imperfetto (verleden tijd)', futuro: 'toekomende tijd' };

// ── Passato prossimo (v1.46) ─────────────────────────────────────────────────
// Voltooid deelwoord: exacte tabel → familie op achtervoegsel → regelmatig (-ato/-uto/-ito).
// Voor -ere geldt: alleen regelmatig als het werkwoord in REGULAR_ERE staat, anders geen passato.
const PARTICIPLES = { essere: 'stato', stare: 'stato', dare: 'dato', fare: 'fatto', dire: 'detto', bere: 'bevuto',
  morire: 'morto', nascere: 'nato', rinascere: 'rinato', vivere: 'vissuto', sopravvivere: 'sopravvissuto', convivere: 'convissuto',
  rimanere: 'rimasto', valere: 'valso', parere: 'parso', piacere: 'piaciuto', tacere: 'taciuto', cuocere: 'cotto',
  spegnere: 'spento', succedere: 'successo', concedere: 'concesso', rompere: 'rotto', accorgersi: 'accorto',
  chiedere: 'chiesto', rispondere: 'risposto', nascondere: 'nascosto', esprimere: 'espresso', discutere: 'discusso',
  assumere: 'assunto', riassumere: 'riassunto', dividere: 'diviso', condividere: 'condiviso', esplodere: 'esploso',
  scuotere: 'scosso', persuadere: 'persuaso', mordere: 'morso', spargere: 'sparso', friggere: 'fritto', dirigere: 'diretto',
  aprire: 'aperto', riaprire: 'riaperto', coprire: 'coperto', scoprire: 'scoperto', ricoprire: 'ricoperto', offrire: 'offerto',
  soffrire: 'sofferto', venire: 'venuto', avere: 'avuto', vedere: 'visto', prevedere: 'previsto', rivedere: 'rivisto',
  bruciare: 'bruciato', assistere: 'assistito', insistere: 'insistito', esistere: 'esistito', resistere: 'resistito',
  consistere: 'consistito', maledire: 'maledetto', benedire: 'benedetto', contraddire: 'contraddetto', soddisfare: 'soddisfatto' };
const PART_FAMILIES = [
  ['prendere', 'preso'], ['mettere', 'messo'], ['scrivere', 'scritto'], ['leggere', 'letto'], ['gliere', 'lto'],
  ['durre', 'dotto'], ['porre', 'posto'], ['trarre', 'tratto'], ['giungere', 'giunto'], ['vincere', 'vinto'],
  ['cidere', 'ciso'], ['cludere', 'cluso'], ['correre', 'corso'], ['parire', 'parso'], ['pingere', 'pinto'],
  ['tingere', 'tinto'], ['fingere', 'finto'], ['stringere', 'stretto'], ['spingere', 'spinto'], ['piangere', 'pianto'],
  ['ridere', 'riso'], ['chiudere', 'chiuso'], ['perdere', 'perso'], ['spendere', 'speso'], ['scendere', 'sceso'],
  ['pendere', 'peso'], ['fendere', 'feso'], ['tendere', 'teso'], ['rendere', 'reso'], ['volgere', 'volto'],
  ['solvere', 'solto'], ['muovere', 'mosso'], ['noscere', 'nosciuto'], ['crescere', 'cresciuto'], ['struggere', 'strutto'],
  ['teggere', 'tetto'], ['reggere', 'retto'], ['primere', 'presso'], ['fondere', 'fuso'], ['sumere', 'sunto'],
  ['orgere', 'orto'], ['mergere', 'merso'], ['cedere', 'ceduto'], ['tenere', 'tenuto'], ['venire', 'venuto'],
  ['sistere', 'sistito'], ['battere', 'battuto'], ['vedere', 'visto'], ['fare', 'fatto'], ['dire', 'detto'],
  ['chiedere', 'chiesto'], ['cendere', 'ceso'],
];
const REGULAR_ERE = new Set(['credere', 'ripetere', 'vendere', 'temere', 'ricevere', 'dovere', 'potere', 'volere', 'sapere',
  'cadere', 'godere', 'godersi', 'sedere', 'premere', 'procedere', 'gemere', 'fremere', 'dolere', 'abbattere', 'dibattere',
  'combattere', 'ricevere', 'pretendere']);
// Hulpwerkwoord essere (intransitief: beweging, verandering, toestand); wederkerend altijd essere
const ESSERE_VERBS = new Set(['andare', 'venire', 'arrivare', 'partire', 'entrare', 'uscire', 'tornare', 'ritornare',
  'rientrare', 'salire', 'scendere', 'cadere', 'nascere', 'rinascere', 'morire', 'rimanere', 'restare', 'stare', 'essere',
  'diventare', 'piacere', 'sembrare', 'apparire', 'scomparire', 'sparire', 'riuscire', 'costare', 'durare', 'mancare',
  'esistere', 'crescere', 'intervenire', 'svenire', 'convenire', 'scappare', 'fuggire', 'sopravvivere', 'guarire',
  'invecchiare', 'dimagrire', 'ingrassare', 'fiorire', 'accadere', 'emigrare', 'immigrare', 'atterrare', 'decollare',
  'avanzare', 'procedere', 'giungere', 'esplodere', 'sorgere', 'comparire', 'parere', 'avvenire', 'evadere', 'emergere',
  'scoppiare', 'impazzire', 'fallire', 'scivolare', 'affondare', 'valere', 'arrivare', 'sbocciare', 'marcire']);
// Beide hulpwerkwoorden mogelijk of onduidelijk → geen passato prossimo in de oefening
const AMBIG_AUX = new Set(['passare', 'cambiare', 'cominciare', 'iniziare', 'finire', 'terminare', 'continuare', 'correre',
  'vivere', 'volare', 'migliorare', 'peggiorare', 'aumentare', 'diminuire', 'servire', 'bruciare', 'scattare', 'suonare',
  'saltare', 'guarire', 'pesare', 'seguire', 'proseguire', 'mancare', 'bastare', 'costare', 'durare', 'esplodere']);
const AVERE_FORMS  = ['ho', 'hai', 'ha', 'abbiamo', 'avete', 'hanno'];
const ESSERE_FORMS = ['sono', 'sei', 'è', 'siamo', 'siete', 'sono'];

/** Voltooid deelwoord (mannelijk enkelvoud) of null als het niet betrouwbaar afgeleid kan worden. */
export function participle(inf) {
  const { base } = splitReflexive(inf.trim());
  if (PARTICIPLES[base]) return PARTICIPLES[base];
  for (const [suffix, part] of PART_FAMILIES) {
    if (base.endsWith(suffix)) return base.slice(0, -suffix.length) + part;
  }
  const stem = base.slice(0, -3), end = base.slice(-3);
  if (end === 'are') return stem + 'ato';
  if (end === 'ire') return stem + 'ito';
  if (end === 'ere' && REGULAR_ERE.has(base)) return stem + 'uto';
  return null;
}

function auxiliary(inf) {
  const { base, refl } = splitReflexive(inf.trim());
  if (refl) return 'essere';
  if (AMBIG_AUX.has(base)) return null;
  return ESSERE_VERBS.has(base) ? 'essere' : 'avere';
}

/** Is deze tijd betrouwbaar te vormen voor dit werkwoord? */
export function canUseTense(inf, tense) {
  if (tense !== 'passato') return isConjugatable(inf);
  return isConjugatable(inf) && participle(inf) !== null && auxiliary(inf) !== null;
}

/**
 * Passato prossimo: geaccepteerde vormen voor persoon p. De eerste is de canonieke (mannelijke) vorm;
 * bij essere volgen de vrouwelijke varianten (andata / andate).
 */
function passatoForms(inf, p) {
  const { refl } = splitReflexive(inf.trim());
  const part = participle(inf), aux = auxiliary(inf);
  if (!part || !aux) return [];
  const pre = refl ? REFL_PRON[p] + ' ' : '';
  if (aux === 'avere') return [`${pre}${AVERE_FORMS[p]} ${part}`];
  const stem = part.slice(0, -1), plural = p >= 3;
  const m = stem + (plural ? 'i' : 'o'), f = stem + (plural ? 'e' : 'a');
  return [`${pre}${ESSERE_FORMS[p]} ${m}`, `${pre}${ESSERE_FORMS[p]} ${f}`];
}

/** Alle geaccepteerde antwoorden (eerste = canoniek). */
export function conjugateAccepted(inf, p, tense = 'presente') {
  return tense === 'passato' ? passatoForms(inf, p) : [conjugate(inf, p, tense)];
}

// -ire werkwoorden met -isc- in het presente
const ISC_VERBS = new Set(['capire', 'pulire', 'guarire', 'finire', 'preferire', 'spedire', 'costruire', 'gestire',
  'garantire', 'sostituire', 'stabilire', 'suggerire', 'restituire', 'arricchire', 'diminuire', 'fallire', 'fiorire',
  'gradire', 'impedire', 'tradire', 'unire', 'riferire', 'condire', 'fornire', 'colpire', 'agire', 'chiarire',
  'definire', 'inserire', 'obbedire', 'proibire', 'reagire', 'trasferire', 'ubbidire']);

// -iare met klemtoon op de i: tu invii, noi inviamo (i blijft staan)
const STRESSED_IARE = new Set(['inviare', 'sciare', 'spiare', 'avviare']);

// Niet vervoegbaar in een oefening: onpersoonlijk, alleen 3e persoon, of geen werkwoord
const CONJ_EXCLUDE = new Set(['benessere', 'piovere', 'nevicare', 'succedere', 'accadere', 'svolgersi', 'estinguersi',
  'scomparire', 'dispiacere', 'importare', 'capitare', 'bastare', 'pregiarsi', 'occorrere', 'bisognare']);

// Volledige onregelmatige presente-vormen
const IRREG_PRES = {
  essere: ['sono', 'sei', 'è', 'siamo', 'siete', 'sono'],
  avere:  ['ho', 'hai', 'ha', 'abbiamo', 'avete', 'hanno'],
  andare: ['vado', 'vai', 'va', 'andiamo', 'andate', 'vanno'],
  fare:   ['faccio', 'fai', 'fa', 'facciamo', 'fate', 'fanno'],
  stare:  ['sto', 'stai', 'sta', 'stiamo', 'state', 'stanno'],
  dare:   ['do', 'dai', 'dà', 'diamo', 'date', 'danno'],
  dire:   ['dico', 'dici', 'dice', 'diciamo', 'dite', 'dicono'],
  bere:   ['bevo', 'bevi', 'beve', 'beviamo', 'bevete', 'bevono'],
  potere: ['posso', 'puoi', 'può', 'possiamo', 'potete', 'possono'],
  volere: ['voglio', 'vuoi', 'vuole', 'vogliamo', 'volete', 'vogliono'],
  dovere: ['devo', 'devi', 'deve', 'dobbiamo', 'dovete', 'devono'],
  sapere: ['so', 'sai', 'sa', 'sappiamo', 'sapete', 'sanno'],
  uscire: ['esco', 'esci', 'esce', 'usciamo', 'uscite', 'escono'],
  sedere: ['siedo', 'siedi', 'siede', 'sediamo', 'sedete', 'siedono'],
  morire: ['muoio', 'muori', 'muore', 'moriamo', 'morite', 'muoiono'],
  spegnere: ['spengo', 'spegni', 'spegne', 'spegniamo', 'spegnete', 'spengono'],
  cuocere:  ['cuocio', 'cuoci', 'cuoce', 'cuociamo', 'cuocete', 'cuociono'],
  riempire: ['riempio', 'riempi', 'riempie', 'riempiamo', 'riempite', 'riempiono'],
  rimanere: ['rimango', 'rimani', 'rimane', 'rimaniamo', 'rimanete', 'rimangono'],
  valere:   ['valgo', 'vali', 'vale', 'valiamo', 'valete', 'valgono'],
  salire:   ['salgo', 'sali', 'sale', 'saliamo', 'salite', 'salgono'],
  scegliere: ['scelgo', 'scegli', 'sceglie', 'scegliamo', 'scegliete', 'scelgono'],
};
// Werkwoordfamilies: achtervoegsel → vormen zonder voorvoegsel (mantenere = man + tenere)
const PRES_FAMILIES = [
  ['tenere',  ['tengo', 'tieni', 'tiene', 'teniamo', 'tenete', 'tengono']],
  ['venire',  ['vengo', 'vieni', 'viene', 'veniamo', 'venite', 'vengono']],
  ['porre',   ['pongo', 'poni', 'pone', 'poniamo', 'ponete', 'pongono']],
  ['durre',   ['duco', 'duci', 'duce', 'duciamo', 'ducete', 'ducono']],
  ['trarre',  ['traggo', 'trai', 'trae', 'traiamo', 'traete', 'traggono']],
  ['gliere',  ['lgo', 'gli', 'glie', 'gliamo', 'gliete', 'lgono']],
  ['parire',  ['paio', 'pari', 'pare', 'pariamo', 'parite', 'paiono']],
  ['piacere', ['piaccio', 'piaci', 'piace', 'piacciamo', 'piacete', 'piacciono']],
  ['uscire',  ['esco', 'esci', 'esce', 'usciamo', 'uscite', 'escono']],
];
const IRREG_IMPF_STEM = { essere: null, dire: 'dic', bere: 'bev', fare: 'fac', produrre: 'produc', tradurre: 'traduc',
  proporre: 'propon', supporre: 'suppon', attrarre: 'attra', distrarre: 'distra' };
const IRREG_FUT_STEM = { essere: 'sar', avere: 'avr', andare: 'andr', fare: 'far', stare: 'star', dare: 'dar',
  potere: 'potr', sapere: 'sapr', vedere: 'vedr', vivere: 'vivr', cadere: 'cadr', venire: 'verr', tenere: 'terr',
  mantenere: 'manterr', ottenere: 'otterr', sostenere: 'sosterr', ritenere: 'riterr', rimanere: 'rimarr', bere: 'berr',
  dire: 'dir', valere: 'varr', produrre: 'produrr', tradurre: 'tradurr', proporre: 'proporr', supporre: 'supporr',
  attrarre: 'attrarr', distrarre: 'distrarr', intervenire: 'interverr', prevenire: 'preverr', svenire: 'sverr',
  convenire: 'converr', dovere: 'dovr', volere: 'vorr' };

/** Actieve vervoegingsmotor (v1.48): Italiaans (hier) of Spaans (conjugation_es.js). */
function conjEngine() {
  return getLang().code === 'es'
    ? { pronouns: ES_PRONOUNS, labels: ES_TENSE_LABELS, is: esIsConjugatable, can: esCanUseTense,
        accepted: esConjugateAccepted, aux: () => 'haber', passatoPronoun: p => ES_PRONOUNS[p], pick: esPickTense }
    : { pronouns: PRONOUNS, labels: TENSE_LABELS, is: isConjugatable, can: canUseTense,
        accepted: conjugateAccepted, aux: auxiliary, passatoPronoun: p => (p === 2 ? 'lui' : PRONOUNS[p]), pick: null };
}

/** Is dit woord een enkelvoudige infinitief die de (Italiaanse) motor aankan? */
export function isConjugatable(it) {
  const inf = (it || '').trim();
  if (!/^[a-zàèéìòù]+(are|ere|ire|rsi|rre)$/.test(inf)) return false;
  return !CONJ_EXCLUDE.has(inf);
}

function splitReflexive(inf) {
  return inf.endsWith('rsi') ? { base: inf.slice(0, -2) + 'e', refl: true } : { base: inf, refl: false };
}

function presente(base, p) {
  if (IRREG_PRES[base]) return IRREG_PRES[base][p];
  for (const [suffix, forms] of PRES_FAMILIES) {
    if (base.endsWith(suffix) && base !== suffix) return base.slice(0, -suffix.length) + forms[p];
    if (base === suffix) return forms[p];
  }
  const stem = base.slice(0, -3), end = base.slice(-3);
  if (end === 'are') {
    const cg = /[cg]$/.test(stem), iEnd = stem.endsWith('i') && !STRESSED_IARE.has(base);
    const tu  = cg ? stem + 'hi'   : iEnd ? stem         : stem + 'i';
    const noi = cg ? stem + 'hiamo' : stem.endsWith('i') ? stem + 'amo' : stem + 'iamo';
    return [stem + 'o', tu, stem + 'a', noi, stem + 'ate', stem + 'ano'][p];
  }
  if (end === 'ere') return stem + ['o', 'i', 'e', 'iamo', 'ete', 'ono'][p];
  if (ISC_VERBS.has(base)) return stem + ['isco', 'isci', 'isce', 'iamo', 'ite', 'iscono'][p];
  return stem + ['o', 'i', 'e', 'iamo', 'ite', 'ono'][p];
}

function imperfetto(base, p) {
  if (base === 'essere') return ['ero', 'eri', 'era', 'eravamo', 'eravate', 'erano'][p];
  const irr = IRREG_IMPF_STEM[base];
  const stem = irr || base.slice(0, -3);
  const v = irr ? 'e' : base.slice(-3)[0];
  return stem + [v + 'vo', v + 'vi', v + 'va', v + 'vamo', v + 'vate', v + 'vano'][p];
}

function futuro(base, p) {
  let fstem = IRREG_FUT_STEM[base];
  if (!fstem) {
    const stem = base.slice(0, -3), end = base.slice(-3);
    if (end === 'are') {
      let s = stem;
      if (/[cg]$/.test(s)) s += 'h';
      else if (/(c|g|sc)i$/.test(s) && !STRESSED_IARE.has(base)) s = s.slice(0, -1);
      fstem = s + 'er';
    } else if (end === 'ere') fstem = stem + 'er';
    else fstem = stem + 'ir';
  }
  return fstem + ['ò', 'ai', 'à', 'emo', 'ete', 'anno'][p];
}

/** Vervoeg een infinitief (incl. wederkerend) voor persoon p (0–5) in de gegeven tijd. */
export function conjugate(inf, p, tense = 'presente') {
  if (tense === 'passato') return passatoForms(inf, p)[0] || '';
  const { base, refl } = splitReflexive(inf.trim());
  const fn = tense === 'imperfetto' ? imperfetto : tense === 'futuro' ? futuro : presente;
  const form = fn(base, p);
  return refl ? `${REFL_PRON[p]} ${form}` : form;
}

function pickTense(word) {
  const E = conjEngine();
  if (E.pick) { const t = E.pick(word); return E.can(word.it, t) ? t : 'presente'; }
  const r = Math.random();
  let tense = 'presente';
  if (word.level === 'A2') {
    // Passato prossimo vanaf les 62, futuro vanaf les 64 (volgorde van het A2-curriculum)
    if (word.lesson >= 62 && r < 0.3) tense = 'passato';
    else if (word.lesson >= 64 && r < 0.5) tense = 'futuro';
  } else if (word.level === 'B1') {
    tense = r < 0.35 ? 'presente' : r < 0.6 ? 'passato' : r < 0.8 ? 'imperfetto' : 'futuro';
  }
  return conjEngine().can(word.it, tense) ? tense : 'presente';
}

function paradigmHtml(inf, tense) {
  const E = conjEngine();
  const labels = E.pronouns.map((pr, i) => tense === 'passato' ? E.passatoPronoun(i) : pr);
  return `<div class="conj-paradigm">${labels.map((pr, i) =>
    `<span class="conj-row"><span class="conj-pron">${pr}</span><span class="conj-form">${E.accepted(inf, i, tense)[0]}</span></span>`).join('')}</div>`;
}

/**
 * Vervoegen — toon infinitief + persoon + tijd; kies (MC) of typ de juiste vorm.
 * exercise.mode: 'mc' | 'type' (anders willekeurig); exercise.person/tense optioneel.
 */
export function renderConjugation(exercise, container, onComplete) {
  const { word } = exercise;
  const E = conjEngine();
  if (!E.is(word.it)) { renderTypeExercise(exercise, container, onComplete); return; }
  const hasTTS = isTTSAvailable();
  const tense  = (exercise.tense && E.can(word.it, exercise.tense)) ? exercise.tense : pickTense(word);
  const p      = exercise.person ?? Math.floor(Math.random() * 6);
  const accepted = E.accepted(word.it, p, tense);
  const answer = accepted[0];
  const useMC  = exercise.mode ? exercise.mode === 'mc' : Math.random() < 0.5;
  const isPassato = tense === 'passato';
  const pronounLabel = isPassato ? E.passatoPronoun(p) : E.pronouns[p];
  const auxHint = isPassato ? `<div class="conj-hint">hulpwerkwoord: <strong>${E.aux(word.it)}</strong>${accepted.length > 1 ? ' · mannelijke vorm (vrouwelijk telt ook goed)' : ''}</div>` : '';

  const head = `
    <div class="ex-label">Vervoeg het werkwoord</div>
    <div class="conj-card">
      <div class="conj-inf">${word.it}</div>
      <div class="conj-nl">${word.nl}</div>
      <div class="conj-tense">${E.labels[tense]}</div>
      <div class="conj-prompt"><span class="conj-pron-big">${pronounLabel}</span> <span class="conj-blank">______</span></div>
      ${auxHint}
    </div>`;

  const finish = (result, xp) => {
    updateWordState(word.id, qualityFromResult(result === 'close' ? 'close' : result));
    recordAnswer(result === 'correct');
    const nextBtn = container.querySelector('#ex-next');
    setupNextBtn(nextBtn, () => onComplete({ result, word, xp }), result === 'correct');
  };

  if (useMC) {
    const others = [...new Set([0, 1, 2, 3, 4, 5].filter(i => i !== p).map(i => E.accepted(word.it, i, tense)[0]))]
      .filter(f => f !== answer);
    const options = shuffleEx([{ text: answer, correct: true }, ...shuffleEx(others).slice(0, 3).map(t => ({ text: t, correct: false }))]);
    container.innerHTML = head + `
      <div class="mc-options">
        ${options.map((o, i) => `<button class="mc-option" data-correct="${o.correct}"><span class="mc-letter">${['A', 'B', 'C', 'D'][i]}</span><span class="mc-text">${o.text}</span></button>`).join('')}
      </div>
      <div class="mc-feedback" id="conj-feedback"></div>
      <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>`;
    let answered = false;
    container.querySelectorAll('.mc-option').forEach(btn => btn.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const ok = btn.dataset.correct === 'true';
      container.querySelectorAll('.mc-option').forEach(b => {
        b.classList.add('disabled');
        if (b.dataset.correct === 'true') b.classList.add('correct'); else if (b === btn) b.classList.add('wrong');
      });
      const fb = container.querySelector('#conj-feedback');
      fb.className = `mc-feedback ${ok ? 'correct' : 'wrong'} show`;
      fb.innerHTML = ok ? `✓ Correct! <strong>${pronounLabel} ${answer}</strong>`
                        : `✗ Fout. Het is: <strong>${pronounLabel} ${answer}</strong>${paradigmHtml(word.it, tense)}`;
      if (hasTTS) setTimeout(() => speak(answer), 400);
      finish(ok ? 'correct' : 'wrong', ok ? 4 : 1);
    }));
    return;
  }

  container.innerHTML = head + `
    <div class="type-input-wrap">
      <input type="text" class="type-input" id="conj-input" placeholder="Typ de vervoeging..." autocomplete="off" autocorrect="off" autocapitalize="none" spellcheck="false">
      <button class="type-submit-btn" id="conj-submit">✓</button>
    </div>
    <button class="type-skip-btn" id="conj-skip">Weet ik niet →</button>
    <div class="type-feedback" id="conj-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>`;
  const input = container.querySelector('#conj-input'), submit = container.querySelector('#conj-submit');
  const fb = container.querySelector('#conj-feedback'), skip = container.querySelector('#conj-skip');
  let answered = false;
  setTimeout(() => input.focus(), 100);

  const reveal = (result, typed) => {
    answered = true;
    input.disabled = true; submit.disabled = true; skip.style.display = 'none';
    if (result === 'correct') {
      input.classList.add('input-correct');
      fb.className = 'type-feedback correct show';
      const shown = accepted.find(a => a.toLowerCase() === typed.toLowerCase().replace(/\s+/g, ' ')) || answer;
      fb.innerHTML = `✓ Perfect! <strong>${pronounLabel} ${shown}</strong>`;
    } else if (result === 'close') {
      input.classList.add('input-close');
      fb.className = 'type-feedback close show';
      fb.innerHTML = `≈ Bijna! Let op het accent: je schreef "<strong>${typed}</strong>", het is <strong>${answer}</strong>`;
    } else {
      input.classList.add('input-wrong');
      fb.className = 'type-feedback wrong show';
      fb.innerHTML = `✗ Het juiste antwoord is: <strong>${pronounLabel} ${answer}</strong>${paradigmHtml(word.it, tense)}`;
    }
    if (hasTTS) setTimeout(() => speak(answer), 400);
    finish(result, result === 'correct' ? 5 : result === 'close' ? 2 : 1);
  };
  const check = () => {
    if (answered) return;
    const typed = input.value.trim();
    if (!typed) { input.classList.add('shake'); setTimeout(() => input.classList.remove('shake'), 400); return; }
    const t = typed.toLowerCase().replace(/\s+/g, ' ');
    const exact = accepted.some(a => a.toLowerCase() === t);
    const result = exact ? 'correct' : accepted.some(a => normalize(a) === normalize(typed)) ? 'close' : 'wrong';
    reveal(result, typed);
  };
  submit.addEventListener('click', check);
  input.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
  skip.addEventListener('click', () => { if (!answered) reveal('wrong', ''); });
}


// ═══════════════════════════════════════════════════════════════════════════════
// Leestekst (v1.45) — korte tekst per blok met begripsvragen, in de toetsles
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Leestekst — toon de tekst, daarna 3 meerkeuzevragen (één tegelijk).
 * exercise.reading = { title, level, text, questions: [{ q, options: [4], answer }] }
 */
export function renderReading(exercise, container, onComplete) {
  const { reading } = exercise;
  const hasTTS = isTTSAvailable();
  const paragraphs = reading.text.split('\n').filter(Boolean);
  const wordCount = reading.text.split(/\s+/).filter(Boolean).length;

  container.innerHTML = `
    <div class="ex-label">Lees de tekst en beantwoord de vragen</div>
    <div class="reading-card">
      <div class="reading-head">
        <div class="reading-title">${reading.title}</div>
        <div class="reading-meta">${reading.level} · ${wordCount} woorden${hasTTS ? ' · <button class="reading-tts" id="reading-tts">🔊 Voorlezen</button>' : ''}</div>
      </div>
      <div class="reading-text">${paragraphs.map(pg => `<p>${pg}</p>`).join('')}</div>
    </div>
    <div class="reading-questions" id="reading-questions"></div>
    <div class="mc-feedback" id="reading-feedback"></div>
    <button class="ex-next-btn" id="ex-next" style="display:none">Volgende →</button>`;

  container.querySelector('#reading-tts')?.addEventListener('click', () => speak(reading.text.replace(/\n/g, ' ')));

  const qWrap = container.querySelector('#reading-questions');
  const fb    = container.querySelector('#reading-feedback');
  let qi = 0, score = 0;

  const showQuestion = () => {
    const q = reading.questions[qi];
    qWrap.innerHTML = `
      <div class="reading-q-num">Vraag ${qi + 1} van ${reading.questions.length}</div>
      <div class="reading-q">${q.q}</div>
      <div class="mc-options">
        ${q.options.map((o, i) => `<button class="mc-option" data-i="${i}"><span class="mc-letter">${['A', 'B', 'C', 'D'][i]}</span><span class="mc-text">${o}</span></button>`).join('')}
      </div>`;
    let answered = false;
    qWrap.querySelectorAll('.mc-option').forEach(btn => btn.addEventListener('click', () => {
      if (answered) return;
      answered = true;
      const ok = Number(btn.dataset.i) === q.answer;
      if (ok) score++;
      qWrap.querySelectorAll('.mc-option').forEach(b => {
        b.classList.add('disabled');
        if (Number(b.dataset.i) === q.answer) b.classList.add('correct'); else if (b === btn) b.classList.add('wrong');
      });
      fb.className = `mc-feedback ${ok ? 'correct' : 'wrong'} show`;
      fb.innerHTML = ok ? '✓ Goed gelezen!' : `✗ Het juiste antwoord: <strong>${q.options[q.answer]}</strong>`;
      qi++;
      if (qi < reading.questions.length) {
        setTimeout(() => { fb.className = 'mc-feedback'; showQuestion(); }, 1400);
      } else {
        const total = reading.questions.length;
        const result = score >= Math.ceil(total * 2 / 3) ? 'correct' : 'wrong';
        fb.innerHTML += `<div class="reading-score">Je had <strong>${score} van ${total}</strong> vragen goed.</div>`;
        recordAnswer(result === 'correct');
        setupNextBtn(container.querySelector('#ex-next'), () => onComplete({ result, xp: score * 3 }), false);
      }
    }));
  };
  showQuestion();
}
