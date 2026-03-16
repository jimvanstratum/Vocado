/**
 * Exercises — Sprint 10
 * Types: flashcard, multiple-choice, listen-choose, listen-type, type, word-order, grammar, intro
 */

import { speak, isTTSAvailable, getTTSRate } from './audio.js?v=10';
import { updateWordState, qualityFromResult } from './srs.js?v=10';
import { recordAnswer } from './progress.js?v=10';

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
  const pool = allWords.filter(w => w.id !== word.id && w.it !== word.it);
  return [...pool].sort(() => Math.random() - 0.5).slice(0, count);
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

  // Review: random type, inclusief word-order, listen-type en sentence-choice als beschikbaar
  reviewWords.forEach(word => {
    const types = ['multiple-choice', 'type'];
    if (ttsOk) {
      types.push('listen-choose');
      types.push('listen-type');   // dictee als extra review-type
    }
    if (sentenceToTokens(word.ex).length >= 3) types.push('word-order');
    if (word.ex && word.exNl) types.push('sentence-choice');
    const type = types[Math.floor(Math.random() * types.length)];
    queue.push({ type, word, isNew: false });
  });

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
    <div class="ex-label">Vertaal naar Italiaans</div>
    <div class="flashcard-ex" id="fc-scene">
      <div class="fc-card" id="fc-card">
        <div class="fc-front">
          <div class="fc-lang">Nederlands</div>
          <div class="fc-word">${word.nl}</div>
          <div class="fc-tap-hint">Tik om te onthullen</div>
        </div>
        <div class="fc-back">
          <div class="fc-lang">Italiaans</div>
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
    <div class="ex-label">Wat is de Italiaanse vertaling?</div>
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
    <div class="ex-label">Typ het Italiaanse woord</div>
    <div class="type-question">
      <div class="type-nl">${word.nl}</div>
      ${word.exNl ? `<div class="type-context">"${word.exNl}"</div>` : ''}
    </div>
    <div class="type-input-wrap">
      <input
        type="text"
        class="type-input"
        id="type-input"
        placeholder="Typ hier in het Italiaans..."
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
    <div class="ex-label">Wat hoor je? Typ het Italiaanse woord</div>

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
