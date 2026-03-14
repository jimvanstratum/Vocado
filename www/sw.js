const CACHE_NAME = 'vocado-20260314-2133';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon.svg',
  './avocado.svg',
  './woordlogo.svg',
  './icon-192.png',
  './icon-512.png',
  './js/app.js',
  './js/srs.js',
  './js/progress.js',
  './js/settings.js',
  './js/audio.js',
  './js/exercises.js',
  './data/vocabulary.json',
  './data/curriculum.json'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(c => c.addAll(ASSETS))
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
