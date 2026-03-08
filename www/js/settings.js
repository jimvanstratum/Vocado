/**
 * Settings — gebruikersinstellingen opslaan en ophalen.
 * Sprint 10: thema (auto/licht/donker), dagdoel in minuten.
 */

const SETTINGS_KEY = 'italiano_settings_v1';

const SETTINGS_DEFAULTS = {
  dagdoel:        100,   // XP dagdoel per dag (50/100/150/200 = ~5/10/15/20 min)
  ttsRate:        1.0,   // TTS spreeksnelheid (0.7 = langzaam, 1.0 = normaal, 1.3 = snel)
  placementDone:  false, // plaatsingstoets al afgerond?
  theme:          'auto' // 'auto' | 'light' | 'dark'
};

export function getSettings() {
  try {
    const raw = localStorage.getItem(SETTINGS_KEY);
    return raw ? { ...SETTINGS_DEFAULTS, ...JSON.parse(raw) } : { ...SETTINGS_DEFAULTS };
  } catch { return { ...SETTINGS_DEFAULTS }; }
}

export function saveSettings(partial) {
  const updated = { ...getSettings(), ...partial };
  try { localStorage.setItem(SETTINGS_KEY, JSON.stringify(updated)); } catch {}
  return updated;
}

/** Sprint 10: migreer oude dagdoel-waarden (10/20/30/50) naar nieuwe XP-waarden. */
export function migrateSettingsV10() {
  const s = getSettings();
  if (s.settingsMigratedV10) return;
  const oldToNew = { 10: 50, 20: 100, 30: 150, 50: 200 };
  const newDagdoel = oldToNew[s.dagdoel] || s.dagdoel;
  saveSettings({ dagdoel: newDagdoel, settingsMigratedV10: true });
}

export function isPlacementDone()  { return getSettings().placementDone; }
export function markPlacementDone(){ saveSettings({ placementDone: true }); }
