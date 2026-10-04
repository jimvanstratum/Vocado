/**
 * Audio — Text-to-Speech wrapper (Web Speech API) voor iOS, Android en desktop.
 *
 * v1.62: robuust gemaakt voor Android (Chrome/Samsung Internet):
 *  - stem wordt lazy gezocht (stemmen laden asynchroon; 'es_ES' met underscore wordt ook herkend)
 *  - cancel() direct gevolgd door speak() laat Android de nieuwe zin soms vallen → korte pauze ertussen
 *  - 'interrupted'/'canceled' (door onze eigen cancel) wordt niet meer als fout herhaald; voorheen
 *    werd een afgebroken zin eindeloos opnieuw ingepland
 *  - onbekende taal op het toestel → eenmalige melding via het event 'vocado-tts-unavailable'
 *  - referentie naar de utterance vasthouden (Chrome ruimt hem anders soms op vóór het afspelen)
 */

import { getLang } from './lang.js?v=2';

let voice = null;         // stem van de actieve taal (null = laat het toestel kiezen op utter.lang)
let voiceLang = null;     // taalcode waarvoor `voice` is gezocht
let _globalRate = 0.85;   // instelbare snelheid via instellingen
let _lastUtter = null;    // GC-bescherming
let _warnedLang = null;   // taal waarvoor al een 'geen stem'-melding is gegeven
let _speakTimer = null;

const norm = l => (l || '').replace('_', '-').toLowerCase();

/** Zoek de beste stem voor de actieve taal. Geeft true als er een stem gevonden is. */
function findVoice() {
  if (!('speechSynthesis' in window)) return false;
  const code = getLang().tts, short = code.split('-')[0].toLowerCase();
  const voices = window.speechSynthesis.getVoices() || [];
  const exact = voices.filter(v => norm(v.lang) === code.toLowerCase());
  const same  = voices.filter(v => norm(v.lang).startsWith(short));
  voice = exact.find(v => !/compact/i.test(v.name)) || exact[0] || same.find(v => v.localService) || same[0] || null;
  voiceLang = code;
  return !!voice;
}

/** Initialiseer TTS en zoek de stem van de actieve taal (ook na taalwissel aanroepen). */
export function initAudio() {
  if (!('speechSynthesis' in window)) return;
  voice = null; voiceLang = null;
  findVoice();
  // Stemmen laden asynchroon (iOS, Android): opnieuw zoeken zodra ze binnenkomen
  window.speechSynthesis.onvoiceschanged = () => findVoice();
  setTimeout(findVoice, 500);
  setTimeout(findVoice, 2000);
}

/** Stel de globale TTS-snelheid in vanuit instellingen. */
export function setTTSRate(rate) { _globalRate = rate; }

/** Geeft de huidige globale TTS-snelheid terug. */
export function getTTSRate() { return _globalRate; }

/**
 * Spreek een tekst uit in de actieve taal.
 * @param {string} text        - Te spreken tekst
 * @param {number} [overrideRate] - Overschrijft globale snelheid indien opgegeven
 */
export function speak(text, overrideRate) {
  if (!('speechSynthesis' in window) || !text) return;
  const synth = window.speechSynthesis;
  const rate = overrideRate ?? _globalRate;
  const code = getLang().tts;
  if (voiceLang !== code || (!voice && synth.getVoices().length)) findVoice();

  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = code;
  utter.rate = rate;
  utter.pitch = 1;
  utter.volume = 1;
  if (voice) utter.voice = voice;
  _lastUtter = utter;

  let retried = false;
  utter.onerror = (ev) => {
    const err = ev && ev.error;
    // Door onszelf afgebroken (nieuwe kaart) of geblokkeerd: niets doen
    if (err === 'interrupted' || err === 'canceled' || err === 'not-allowed') return;
    if (err === 'language-unavailable' || err === 'language-not-supported' || err === 'voice-unavailable') {
      if (_warnedLang !== code) {
        _warnedLang = code;
        window.dispatchEvent(new CustomEvent('vocado-tts-unavailable', { detail: { lang: code, name: getLang().name } }));
      }
      // Probeer één keer zonder expliciete stem (toestel kiest zelf)
      if (!retried && utter.voice) { retried = true; utter.voice = null; setTimeout(() => synth.speak(utter), 150); }
      return;
    }
    // Overige fouten (synthesis-failed, audio-busy, network): één keer opnieuw
    if (!retried) { retried = true; setTimeout(() => synth.speak(utter), 150); }
  };

  clearTimeout(_speakTimer);
  const go = () => { if (synth.paused) { try { synth.resume(); } catch (e) {} } synth.speak(utter); };
  if (synth.speaking || synth.pending) {
    // Android laat een speak() direct na cancel() soms vallen: korte pauze
    synth.cancel();
    _speakTimer = setTimeout(go, 80);
  } else {
    go();
  }
}

/** Spreek langzaam uit (voor luisteroefeningen). */
export function speakSlow(text) { speak(text, 0.6); }

/** Geeft true als TTS beschikbaar is. */
export function isTTSAvailable() { return 'speechSynthesis' in window; }

/** Stop alle spraak. */
export function stopSpeech() {
  clearTimeout(_speakTimer);
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
