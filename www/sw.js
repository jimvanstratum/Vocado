const CACHE_NAME = 'vocado-20261003-0759';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon.svg',
  './avocado.svg',
  './woordlogo.svg',
  './icon-192.png',
  './icon-512.png',
  './Vocado groot.svg',
  './js/app.js',
  './js/lang.js',
  './js/conjugation_es.js',
  './js/srs.js',
  './js/idmap.js',
  './js/progress.js',
  './js/settings.js',
  './js/audio.js',
  './js/exercises.js',
  './data/it/vocabulary.json',
  './data/it/curriculum.json',
  './data/it/readings.json',
  './data/es/vocabulary.json',
  './data/es/curriculum.json',
  './data/es/readings.json',
  './data/changelog.json'
];

self.addEventListener('install', e => {
  e.waitUntil(
    // v1.57: HTTP-cache omzeilen bij het voorcachen, anders kan een nieuwe SW vlak na een release
    // nog verouderde data (max-age van GitHub Pages) inpakken
    caches.open(CACHE_NAME).then(c => c.addAll(ASSETS.map(u => new Request(u, { cache: 'reload' }))))
  );
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  // Alleen GET-requests cachen
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(response => {
        // Sla succesvolle responses op in cache
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        }
        return response;
      }).catch(() => caches.match('./index.html'));
    })
  );
});
