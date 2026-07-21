// Service worker for offline caching of the interactive resume.
const CACHE = 'sb-resume-v2';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './favicon.ico',
  './assets/images/Sudhanshu.jpeg',
  './assets/files/Sudhanshu-Bhatnagar.pdf',
  'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap',
];

self.addEventListener('install', (e) => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS.filter(u => !u.startsWith('https://')))));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  // Network-first for HTML so updates are picked up quickly; cache-first for static assets.
  if (e.request.mode === 'navigate' || (url.pathname.endsWith('.html'))) {
    e.respondWith(
      fetch(e.request).then((resp) => {
        const copy = resp.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy));
        return resp;
      }).catch(() => caches.match(e.request).then((r) => r || caches.match('./index.html')))
    );
    return;
  }
  e.respondWith(
    caches.match(e.request).then((c) => c || fetch(e.request).then((resp) => {
      if (resp.ok && (url.origin === location.origin || url.hostname === 'fonts.gstatic.com')) {
        const copy = resp.clone();
        caches.open(CACHE).then((c) => c.put(e.request, copy));
      }
      return resp;
    }).catch(() => new Response('offline', { status: 503 })))
  );
});
