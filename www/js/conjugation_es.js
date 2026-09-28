/**
 * Spaanse vervoegingsmotor (v1.48) — presente, pretérito perfecto, pretérito imperfecto, futuro.
 * Zelfde tijd-sleutels als de Italiaanse motor: 'presente' | 'passato' | 'imperfetto' | 'futuro'.
 */

export const ES_PRONOUNS = ['yo', 'tú', 'él/ella', 'nosotros', 'vosotros', 'ellos/ellas'];
const REFL = ['me', 'te', 'se', 'nos', 'os', 'se'];
export const ES_TENSE_LABELS = {
  presente: 'tegenwoordige tijd', passato: 'pretérito perfecto (voltooide tijd)',
  imperfetto: 'pretérito imperfecto (verleden tijd)', futuro: 'toekomende tijd',
};

// Onpersoonlijke of 3e-persoonsconstructies: niet als oefening
const EXCLUDE = new Set(['llover', 'nevar', 'haber', 'gustar', 'encantar', 'doler', 'importar', 'faltar', 'quedar',
  'parecer', 'ocurrir', 'suceder', 'pasar', 'amanecer', 'anochecer', 'bastar', 'apetecer', 'interesar', 'molestar']);

// Klinkerwisseling in het presente (niet bij nosotros/vosotros): [van, naar]
const STEM_CHANGE = {
  querer: ['e', 'ie'], pensar: ['e', 'ie'], empezar: ['e', 'ie'], comenzar: ['e', 'ie'], entender: ['e', 'ie'],
  preferir: ['e', 'ie'], cerrar: ['e', 'ie'], despertar: ['e', 'ie'], sentir: ['e', 'ie'], sentar: ['e', 'ie'],
  perder: ['e', 'ie'], recomendar: ['e', 'ie'], divertir: ['e', 'ie'], mentir: ['e', 'ie'], encender: ['e', 'ie'],
  tener: ['e', 'ie'], venir: ['e', 'ie'], mantener: ['e', 'ie'], obtener: ['e', 'ie'], contener: ['e', 'ie'],
  detener: ['e', 'ie'], convenir: ['e', 'ie'], defender: ['e', 'ie'], descender: ['e', 'ie'], calentar: ['e', 'ie'],
  merendar: ['e', 'ie'], nevar: ['e', 'ie'], confesar: ['e', 'ie'], atender: ['e', 'ie'], convertir: ['e', 'ie'],
  hervir: ['e', 'ie'], sugerir: ['e', 'ie'], advertir: ['e', 'ie'], referir: ['e', 'ie'], fregar: ['e', 'ie'],
  poder: ['o', 'ue'], dormir: ['o', 'ue'], volver: ['o', 'ue'], encontrar: ['o', 'ue'], recordar: ['o', 'ue'],
  contar: ['o', 'ue'], costar: ['o', 'ue'], almorzar: ['o', 'ue'], morir: ['o', 'ue'], mostrar: ['o', 'ue'],
  acostar: ['o', 'ue'], llover: ['o', 'ue'], sonar: ['o', 'ue'], soñar: ['o', 'ue'], devolver: ['o', 'ue'],
  mover: ['o', 'ue'], probar: ['o', 'ue'], volar: ['o', 'ue'], doler: ['o', 'ue'], acordar: ['o', 'ue'],
  resolver: ['o', 'ue'], aprobar: ['o', 'ue'], colgar: ['o', 'ue'], rogar: ['o', 'ue'], oler: ['o', 'hue'],
  envolver: ['o', 'ue'], morder: ['o', 'ue'], torcer: ['o', 'ue'], jugar: ['u', 'ue'],
  pedir: ['e', 'i'], servir: ['e', 'i'], repetir: ['e', 'i'], seguir: ['e', 'i'], vestir: ['e', 'i'],
  conseguir: ['e', 'i'], decir: ['e', 'i'], elegir: ['e', 'i'], reír: ['e', 'i'], sonreír: ['e', 'i'],
  corregir: ['e', 'i'], despedir: ['e', 'i'], medir: ['e', 'i'], freír: ['e', 'i'], impedir: ['e', 'i'],
  competir: ['e', 'i'], perseguir: ['e', 'i'],
};
// Onregelmatige yo-vorm (rest regelmatig, evt. met klinkerwisseling)
const IRREG_YO = { tener: 'tengo', venir: 'vengo', hacer: 'hago', poner: 'pongo', salir: 'salgo', decir: 'digo',
  traer: 'traigo', caer: 'caigo', saber: 'sé', dar: 'doy', valer: 'valgo', caber: 'quepo', seguir: 'sigo',
  conseguir: 'consigo', perseguir: 'persigo', elegir: 'elijo', corregir: 'corrijo', coger: 'cojo', escoger: 'escojo',
  recoger: 'recojo', proteger: 'protejo', dirigir: 'dirijo', exigir: 'exijo', vencer: 'venzo', convencer: 'convenzo',
  ejercer: 'ejerzo', torcer: 'tuerzo', mantener: 'mantengo', obtener: 'obtengo', contener: 'contengo', detener: 'detengo',
  convenir: 'convengo', suponer: 'supongo', componer: 'compongo', proponer: 'propongo', deshacer: 'deshago',
  rehacer: 'rehago', satisfacer: 'satisfago', distraer: 'distraigo', atraer: 'atraigo', contraer: 'contraigo' };
// Volledig onregelmatig presente
const IRREG_PRES = {
  ser: ['soy', 'eres', 'es', 'somos', 'sois', 'son'], estar: ['estoy', 'estás', 'está', 'estamos', 'estáis', 'están'],
  ir: ['voy', 'vas', 'va', 'vamos', 'vais', 'van'], haber: ['he', 'has', 'ha', 'hemos', 'habéis', 'han'],
  ver: ['veo', 'ves', 've', 'vemos', 'veis', 'ven'], dar: ['doy', 'das', 'da', 'damos', 'dais', 'dan'], oír: ['oigo', 'oyes', 'oye', 'oímos', 'oís', 'oyen'],
  reír: ['río', 'ríes', 'ríe', 'reímos', 'reís', 'ríen'], sonreír: ['sonrío', 'sonríes', 'sonríe', 'sonreímos', 'sonreís', 'sonríen'],
  freír: ['frío', 'fríes', 'fríe', 'freímos', 'freís', 'fríen'], oler: ['huelo', 'hueles', 'huele', 'olemos', 'oléis', 'huelen'],
};
const IRREG_IMPF = { ser: ['era', 'eras', 'era', 'éramos', 'erais', 'eran'], ir: ['iba', 'ibas', 'iba', 'íbamos', 'ibais', 'iban'],
  ver: ['veía', 'veías', 'veía', 'veíamos', 'veíais', 'veían'] };
const IRREG_FUT_STEM = { tener: 'tendr', poner: 'pondr', salir: 'saldr', venir: 'vendr', valer: 'valdr', poder: 'podr',
  saber: 'sabr', haber: 'habr', querer: 'querr', hacer: 'har', decir: 'dir', caber: 'cabr', mantener: 'mantendr',
  obtener: 'obtendr', contener: 'contendr', detener: 'detendr', suponer: 'supondr', componer: 'compondr',
  proponer: 'propondr', deshacer: 'deshar', rehacer: 'rehar', satisfacer: 'satisfar', convenir: 'convendr' };
const PARTICIPLES = { hacer: 'hecho', decir: 'dicho', ver: 'visto', poner: 'puesto', escribir: 'escrito', abrir: 'abierto',
  volver: 'vuelto', morir: 'muerto', romper: 'roto', cubrir: 'cubierto', resolver: 'resuelto', descubrir: 'descubierto',
  devolver: 'devuelto', freír: 'frito', imprimir: 'impreso', satisfacer: 'satisfecho', describir: 'descrito',
  componer: 'compuesto', deshacer: 'deshecho', envolver: 'envuelto', absolver: 'absuelto', suponer: 'supuesto',
  proponer: 'propuesto', rehacer: 'rehecho', prever: 'previsto', inscribir: 'inscrito', suscribir: 'suscrito' };
const PART_FAMILIES = [['poner', 'puesto'], ['hacer', 'hecho'], ['decir', 'dicho'], ['scribir', 'scrito'], ['volver', 'vuelto'],
  ['cubrir', 'cubierto'], ['solver', 'suelto'], ['abrir', 'abierto']];
const HABER = ['he', 'has', 'ha', 'hemos', 'habéis', 'han'];

function split(inf) {
  const s = inf.trim();
  return s.endsWith('se') ? { base: s.slice(0, -2), refl: true } : { base: s, refl: false };
}
export function esIsConjugatable(it) {
  const inf = (it || '').trim();
  if (!/^[a-záéíóúñü]+(ar|er|ir|ír)(se)?$/.test(inf)) return false;
  return !EXCLUDE.has(split(inf).base);
}
function endingOf(base) { const e = base.slice(-2); return e === 'ír' ? 'ir' : e; }
function stemOf(base) { return base.slice(0, -2); }

function presente(base, p) {
  if (IRREG_PRES[base]) return IRREG_PRES[base][p];
  const end = endingOf(base);
  let stem = stemOf(base);
  if (p === 0 && IRREG_YO[base]) return IRREG_YO[base];
  // -uir: y-invoeging (construyo) behalve nosotros/vosotros
  if (base.endsWith('uir') && !base.endsWith('guir') && p !== 3 && p !== 4) stem += 'y';
  // -cer/-cir na klinker: yo -zco (conozco)
  if (p === 0 && /[aeiou]c[ei]r$/.test(base) && !IRREG_YO[base]) return stem.slice(0, -1) + 'zco';
  const sc = STEM_CHANGE[base];
  if (sc && p !== 3 && p !== 4) {
    const i = stem.lastIndexOf(sc[0]);
    if (i >= 0) stem = stem.slice(0, i) + sc[1] + stem.slice(i + sc[0].length);
  }
  const E = end === 'ar' ? ['o', 'as', 'a', 'amos', 'áis', 'an']
          : end === 'er' ? ['o', 'es', 'e', 'emos', 'éis', 'en']
          :                ['o', 'es', 'e', 'imos', 'ís', 'en'];
  if (base.endsWith('uir') && !base.endsWith('guir') && p === 4) return stemOf(base) + 'ís';
  return stem + E[p];
}
function imperfecto(base, p) {
  if (IRREG_IMPF[base]) return IRREG_IMPF[base][p];
  const stem = stemOf(base);
  return endingOf(base) === 'ar' ? stem + ['aba', 'abas', 'aba', 'ábamos', 'abais', 'aban'][p]
                                 : stem + ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían'][p];
}
function futuro(base, p) {
  let stem = IRREG_FUT_STEM[base];
  if (!stem) {
    for (const k of Object.keys(IRREG_FUT_STEM)) if (base.endsWith(k) && base !== k) { stem = base.slice(0, -k.length) + IRREG_FUT_STEM[k]; break; }
  }
  if (!stem) stem = base.replace(/ír$/, 'ir');
  return stem + ['é', 'ás', 'á', 'emos', 'éis', 'án'][p];
}
export function esParticiple(inf) {
  const { base } = split(inf);
  if (PARTICIPLES[base]) return PARTICIPLES[base];
  for (const [suf, part] of PART_FAMILIES) if (base.endsWith(suf) && base !== suf) return base.slice(0, -suf.length) + part;
  const stem = stemOf(base), end = endingOf(base);
  if (end === 'ar') return stem + 'ado';
  if (/[aeo]$/.test(stem)) return stem + 'ído';   // leído, creído, caído, oído, traído
  return stem + 'ido';
}
function perfecto(inf, p) {
  return `${HABER[p]} ${esParticiple(inf)}`;
}

export function esCanUseTense(inf, tense) { return esIsConjugatable(inf); }

/** Geaccepteerde antwoorden voor persoon p (eerste = canoniek). */
export function esConjugateAccepted(inf, p, tense = 'presente') {
  const { base, refl } = split(inf);
  const pre = refl ? REFL[p] + ' ' : '';
  if (tense === 'passato') return [pre + perfecto(base, p)];
  const fn = tense === 'imperfetto' ? imperfecto : tense === 'futuro' ? futuro : presente;
  return [pre + fn(base, p)];
}
export function esConjugate(inf, p, tense = 'presente') { return esConjugateAccepted(inf, p, tense)[0]; }
