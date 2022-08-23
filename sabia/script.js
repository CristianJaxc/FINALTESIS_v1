const divInstall = document.getElementById('installContainer');
const butInstall = document.getElementById('butInstall');

/* Put code here */



/* Only register a service worker if it's supported */
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js');
}

/**
 * Warn the page must be served over HTTPS
 * The `beforeinstallprompt` event won't fire if the page is served over HTTP.
 * Installability requires a service worker with a fetch event handler, and
 * if the page isn't served over HTTPS, the service worker won't load.
 */
if (window.location.protocol === 'http:') {
  const requireHTTPS = document.getElementById('requireHTTPS');
  const link = requireHTTPS.querySelector('a');
  link.href = window.location.href.replace('http://', 'https://');
  requireHTTPS.classList.remove('hidden');
}
/*
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});*/
// Clear cache on activate
/*self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});*/

// Serve from Cache
/*self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});*/
/*

self.addEventListener("fetch", event => {
    event.respondWith(
        fetch(event.request)
        .then(function(result){
        return caches.open(staticCacheName)
        .then(function(c){
        c.put(event.request.url, result.clone())
        return result;
        })
        })
        .catch(function(e){
        return caches.match(event.request);

        })


    )
});
*/
/*
{ "name": "Geekflare", "short_name": "Geekflare", "description": "Geekflare produce artículos de tecnología y finanzas de alta calidad, crea herramientas y API para ayudar a las empresas y a las personas a crecer", "start_url": "/", "iconos": [{ "origen": "activos/icono/icono-128x128.png", "tamaños": "128x128", "tipo": "imagen/png" }, { "origen": "activos/icono/icono-152x152.png", "tamaños": "152x152", "tipo": "imagen/png" }, { "src": "activos/icono/icono-192x192.png", "tamaños ": "192x192", "tipo": "imagen/png" }, { "origen": "activos/icono/icono-384x384.png", "tamaños": "384x384", "tipo": "imagen/png " }, { "src": "assets/icon/icon-512x512.png", "sizes": "512x512", "type": "image/png" }], "background_color": "#EDF2F4", " display": "independiente", "theme_color": "#B20422", "scope": "/",
"shortcuts": [{ "name": "Artículos", "short_name": "Artículos", "descripción": "1595 artículos sobre seguridad, administrador de sistemas, marketing digital, computación en la nube, desarrollo y muchos otros temas"., "url": "/articles", "icons": [{ "src": "/assets/icon/icon- 152x152.png", "tamaño s": "152x152" }] },
{ "name": "Autores", "short_name": "Autores", "descripción": "Geekflare - Autores", "url": "/autores", "iconos": [{ "src": "/assets/icon/icon-152x152.png", "sizes": "152x152" }] },
{ "name": "Tools", "short_name": "Tools", "description" : "Geekflare - Herramientas", "url": "/herramientas", "iconos": [{ "src": "/assets/icon/icon-152x152.png", "tamaños": "152x152" }] },
{ "name": "Ofertas", "short_name": "Ofertas", "descripción": "Geekflare - Ofertas", "url": "/ofertas", "iconos": [{ "src": "/activos/ icono/icono-152x152.png", "tamaños": "152x152" }] } ] }*/
