/**
 * Spaanse vervoegingsmotor (v1.48) — presente, pretérito perfecto, pretérito imperfecto, futuro.
 * Zelfde tijd-sleutels als de Italiaanse motor: 'presente' | 'passato' | 'imperfetto' | 'futuro'.
 */

export const ES_PRONOUNS = ['yo', 'tú', 'él/ella', 'nosotros', 'vosotros', 'ellos/ellas'];
const REFL = ['me', 'te', 'se', 'nos', 'os', 'se'];
export const ES_TENSE_LABELS = {
  presente: 'tegenwoordige tijd', passato: 'pretérito perfecto (voltooide tijd)',
  imperfetto: 'pretérito imperfecto (verleden tijd)', futuro: 'toekomende tijd',
  indefinido: 'pretérito indefinido (verleden tijd)', condicional: 'condicional (zou-vorm)',
  subjuntivo: 'subjuntivo presente',
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
// ── v1.58: pretérito indefinido, condicional, subjuntivo presente ────────────
// Sterke preterita: stam + -e, -iste, -o, -imos, -isteis, -ieron (na j: -eron)
const STRONG_PRET = { tener: 'tuv', estar: 'estuv', andar: 'anduv', poder: 'pud', poner: 'pus', saber: 'sup', hacer: 'hic',
  querer: 'quis', venir: 'vin', decir: 'dij', traer: 'traj', haber: 'hub', caber: 'cup', conducir: 'conduj',
  traducir: 'traduj', producir: 'produj', mantener: 'mantuv', obtener: 'obtuv', contener: 'contuv', detener: 'detuv',
  suponer: 'supus', componer: 'compus', proponer: 'propus', deshacer: 'deshic', satisfacer: 'satisfic', convenir: 'convin',
  distraer: 'distraj', atraer: 'atraj' };
const IRREG_PRET = { ser: ['fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron'], ir: ['fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron'],
  dar: ['di', 'diste', 'dio', 'dimos', 'disteis', 'dieron'], ver: ['vi', 'viste', 'vio', 'vimos', 'visteis', 'vieron'] };
// -ir werkwoorden met klinkerwisseling in 3e persoon indefinido (e→i, o→u) en in nosotros/vosotros subjuntivo
const IR_STEM_PRET = { pedir: ['e', 'i'], servir: ['e', 'i'], repetir: ['e', 'i'], seguir: ['e', 'i'], vestir: ['e', 'i'],
  conseguir: ['e', 'i'], elegir: ['e', 'i'], reír: ['e', 'i'], sonreír: ['e', 'i'], corregir: ['e', 'i'], despedir: ['e', 'i'],
  medir: ['e', 'i'], freír: ['e', 'i'], impedir: ['e', 'i'], competir: ['e', 'i'], perseguir: ['e', 'i'], sentir: ['e', 'i'],
  preferir: ['e', 'i'], divertir: ['e', 'i'], mentir: ['e', 'i'], convertir: ['e', 'i'], hervir: ['e', 'i'], sugerir: ['e', 'i'],
  advertir: ['e', 'i'], referir: ['e', 'i'], dormir: ['o', 'u'], morir: ['o', 'u'] };
const IRREG_SUBJ = { ser: ['sea', 'seas', 'sea', 'seamos', 'seáis', 'sean'], estar: ['esté', 'estés', 'esté', 'estemos', 'estéis', 'estén'],
  ir: ['vaya', 'vayas', 'vaya', 'vayamos', 'vayáis', 'vayan'], haber: ['haya', 'hayas', 'haya', 'hayamos', 'hayáis', 'hayan'],
  saber: ['sepa', 'sepas', 'sepa', 'sepamos', 'sepáis', 'sepan'], dar: ['dé', 'des', 'dé', 'demos', 'deis', 'den'] };

function swapStem(stem, from, to) {
  const i = stem.lastIndexOf(from);
  return i < 0 ? stem : stem.slice(0, i) + to + stem.slice(i + from.length);
}
function indefinido(base, p) {
  if (IRREG_PRET[base]) return IRREG_PRET[base][p];
  const strong = STRONG_PRET[base];
  if (strong) {
    const E = ['e', 'iste', 'o', 'imos', 'isteis', strong.endsWith('j') ? 'eron' : 'ieron'];
    if (base === 'hacer' && p === 2) return 'hizo';
    return strong + E[p];
  }
  const end = endingOf(base);
  let stem = stemOf(base);
  if (end === 'ar') {
    if (p === 0) {
      if (stem.endsWith('c')) return stem.slice(0, -1) + 'qué';
      if (stem.endsWith('g')) return stem + 'ué';
      if (stem.endsWith('z')) return stem.slice(0, -1) + 'cé';
    }
    return stem + ['é', 'aste', 'ó', 'amos', 'asteis', 'aron'][p];
  }
  const sc = IR_STEM_PRET[base];
  if (sc && (p === 2 || p === 5)) stem = swapStem(stem, sc[0], sc[1]);
  // klinker + -ió/-ieron → -yó/-yeron (leyó, oyó, cayó, construyó); reír: rio/rieron
  if ((p === 2 || p === 5) && /[aeiou]$/.test(stem) && !base.endsWith('guir')) {
    if (base.endsWith('eír')) return stem.slice(0, -1) + (p === 2 ? 'io' : 'ieron');   // rio, rieron
    return stem + (p === 2 ? 'yó' : 'yeron');
  }
  // stam op a/e/o: accent op de i (leíste, oíste, caímos)
  const acc = /[aeo]$/.test(stem);
  return stem + ['í', acc ? 'íste' : 'iste', 'ió', acc ? 'ímos' : 'imos', acc ? 'ísteis' : 'isteis', 'ieron'][p];
}
function condicional(base, p) {
  let stem = IRREG_FUT_STEM[base];
  if (!stem) for (const k of Object.keys(IRREG_FUT_STEM)) if (base.endsWith(k) && base !== k) { stem = base.slice(0, -k.length) + IRREG_FUT_STEM[k]; break; }
  if (!stem) stem = base.replace(/ír$/, 'ir');
  return stem + ['ía', 'ías', 'ía', 'íamos', 'íais', 'ían'][p];
}
function subjuntivo(base, p) {
  if (IRREG_SUBJ[base]) return IRREG_SUBJ[base][p];
  const end = endingOf(base);
  // stam uit de yo-vorm (tengo → teng-, conozco → conozc-, construyo → construy-)
  const yo = presente(base, 0);
  const yoStem = yo.endsWith('oy') ? yo.slice(0, -2) : yo.slice(0, -1);
  const irregularYo = !!(IRREG_YO[base] || IRREG_PRES[base]);
  let stem = yoStem;
  if (p === 3 || p === 4) {
    if (irregularYo) {
      stem = yoStem;                     // tengamos, hagamos, digamos, veamos, oigamos, elijamos, sigamos
    } else {
      // klinkerwisseling ie/ue verdwijnt in nosotros/vosotros, behalve -ir (e→i, o→u)
      stem = stemOf(base);
      const sc = IR_STEM_PRET[base];
      if (sc) stem = swapStem(stem, sc[0], sc[1]);                                  // durmamos, pidamos, sintamos
      if (/[aeiou]c[ei]r$/.test(base)) stem = stemOf(base).slice(0, -1) + 'zc';      // conozcamos
      if (base.endsWith('uir') && !base.endsWith('guir')) stem = stemOf(base) + 'y'; // construyamos
    }
  }
  if (end === 'ar') {
    if (stem.endsWith('c')) stem = stem.slice(0, -1) + 'qu';
    else if (stem.endsWith('g')) stem += 'u';
    else if (stem.endsWith('z')) stem = stem.slice(0, -1) + 'c';
    return stem + ['e', 'es', 'e', 'emos', 'éis', 'en'][p];
  }
  return stem + ['a', 'as', 'a', 'amos', 'áis', 'an'][p];
}

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

export function esCanUseTense(inf, tense) { return esIsConjugatable(inf) && (tense in ES_TENSE_LABELS); }

/** Tijdkeuze per niveau (volgorde van het Spaanse curriculum). */
export function esPickTense(word) {
  const r = Math.random(), L = word.level, n = word.lesson;
  const pick = (opts) => { let acc = 0; for (const [t, w] of opts) { acc += w; if (r < acc) return t; } return 'presente'; };
  if (L === 'A1') return 'presente';
  if (L === 'A2') return pick([['presente', 0.4], ['passato', n >= 62 ? 0.2 : 0], ['imperfetto', n >= 63 ? 0.15 : 0],
                               ['futuro', n >= 64 ? 0.15 : 0], ['indefinido', n >= 91 ? 0.1 : 0]]);
  return pick([['presente', 0.2], ['passato', 0.15], ['imperfetto', 0.15], ['indefinido', 0.15], ['futuro', 0.1],
               ['condicional', n >= 131 ? 0.1 : 0], ['subjuntivo', n >= 141 ? 0.15 : 0]]);
}

/** Geaccepteerde antwoorden voor persoon p (eerste = canoniek). */
export function esConjugateAccepted(inf, p, tense = 'presente') {
  const { base, refl } = split(inf);
  const pre = refl ? REFL[p] + ' ' : '';
  if (tense === 'passato') return [pre + perfecto(base, p)];
  const fn = { imperfetto: imperfecto, futuro, indefinido, condicional, subjuntivo }[tense] || presente;
  return [pre + fn(base, p)];
}
export function esConjugate(inf, p, tense = 'presente') { return esConjugateAccepted(inf, p, tense)[0]; }
