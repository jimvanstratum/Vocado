/**
 * Lang — taalconfiguratie (v1.48). Eén actieve taal per keer; voortgang en SRS zijn per taal opgeslagen.
 * Italiaans behoudt zijn oorspronkelijke opslagsleutels, zodat bestaande gebruikers niets merken.
 */

export const LANGS = {
  it: {
    code: 'it', name: 'Italiaans', adj: 'Italiaanse', flag: '🇮🇹', tts: 'it-IT', levels: 'A1 · A2 · B1',
    articleRe: /^(il |la |lo |l'|i |le |gli |un |una |uno |un')/i,
    articleHint: "Lidwoorden: il, la, l', lo",
    keys: { progress: 'italiano_progress_v2', srs: 'italiano_srs_v2', placement: 'placementDone' },
  },
  es: {
    code: 'es', name: 'Spaans', adj: 'Spaanse', flag: '🇪🇸', tts: 'es-ES', levels: 'A1 · A2 · B1',
    articleRe: /^(el |la |los |las |un |una |unos |unas )/i,
    articleHint: 'Lidwoorden: el, la, los, las',
    keys: { progress: 'vocado_es_progress_v1', srs: 'vocado_es_srs_v1', placement: 'placementDone_es' },
  },
};

const ACTIVE_KEY = 'vocado_active_lang';

/** Code van de actieve taal ('it' als er nog niets gekozen is). */
export function getActiveLangCode() {
  try { const c = localStorage.getItem(ACTIVE_KEY); return LANGS[c] ? c : 'it'; } catch { return 'it'; }
}

/** Is er ooit expliciet een taal gekozen? (false → taalkeuzescherm tonen) */
export function hasChosenLang() {
  try { return !!LANGS[localStorage.getItem(ACTIVE_KEY)]; } catch { return false; }
}

export function getLang() { return LANGS[getActiveLangCode()]; }

export function setActiveLangCode(code) {
  if (!LANGS[code]) return;
  try { localStorage.setItem(ACTIVE_KEY, code); } catch {}
}
