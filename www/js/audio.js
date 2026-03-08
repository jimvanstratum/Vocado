/**
 * Audio — Text-to-Speech wrapper voor iOS/Safari.
 * Werkt met de ingebouwde Web Speech API.
 */

let ttsReady = false;
let itVoice = null;
let _globalRate = 0.85; // instelbare snelheid via settings

/** Initialiseer TTS en zoek de beste Italiaanse stem. */
export function initAudio() {
  if (!('speechSynthesis' in window)) return;

  const tryFindVoice = () => {
    const voices = window.speechSynthesis.getVoices();
    // Zoek Italiaanse stem, bij voorkeur een native (niet 'compact') stem
    itVoice = voices.find(v => v.lang === 'it-IT' && !v.name.includes('compact'))
           || voices.find(v => v.lang === 'it-IT')
           || voices.find(v => v.lang.startsWith('it'))
           || null;
    ttsReady = true;
  };

  // iOS laadt stemmen asynchroon
  if (window.speechSynthesis.getVoices().length > 0) {
    tryFindVoice();
  } else {
    window.speechSynthesis.onvoiceschanged = tryFindVoice;
    // Fallback timeout
    setTimeout(tryFindVoice, 500);
  }
}

/** Stel de globale TTS-snelheid in vanuit instellingen. */
export function setTTSRate(rate) {
  _globalRate = rate;
}

/** Geeft de huidige globale TTS-snelheid terug. */
export function getTTSRate() { return _globalRate; }

/**
 * Spreek een Italiaanse tekst uit.
 * @param {string} text        - Te spreken tekst
 * @param {number} [overrideRate] - Overschrijft globale snelheid indien opgegeven
 */
export function speak(text, overrideRate) {
  const rate = overrideRate ?? _globalRate;
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();

  const utter = new SpeechSynthesisUtterance(text);
  utter.lang  = 'it-IT';
  utter.rate  = rate;
  utter.pitch = 1;
  utter.volume = 1;

  if (itVoice) utter.voice = itVoice;

  // iOS Safari fix: soms crasht TTS, dan opnieuw proberen
  utter.onerror = () => {
    setTimeout(() => window.speechSynthesis.speak(utter), 100);
  };

  window.speechSynthesis.speak(utter);
}

/** Spreek langzaam uit (voor luisteroefeningen). */
export function speakSlow(text) {
  speak(text, 0.6);
}

/** Geeft true als TTS beschikbaar is. */
export function isTTSAvailable() {
  return 'speechSynthesis' in window;
}

/** Stop alle spraak. */
export function stopSpeech() {
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
}

/**
 * Speelt een kort, subtiel correct-geluid (880→1174 Hz sine-toon).
 * Laag volume (0.10) zodat het TTS niet overstemt.
 */
export function playCorrectSound() {
  try {
    const ctx  = new (window.AudioContext || window.webkitAudioContext)();
    const osc  = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.type = 'sine';
    osc.frequency.setValueAtTime(880, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1174, ctx.currentTime + 0.10);
    gain.gain.setValueAtTime(0.10, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
    osc.start(ctx.currentTime);
    osc.stop(ctx.currentTime + 0.35);
    setTimeout(() => ctx.close(), 600);
  } catch (e) { /* Geen Web Audio beschikbaar — stille fallback */ }
}
