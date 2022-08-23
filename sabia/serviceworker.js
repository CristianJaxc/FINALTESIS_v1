// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py
const CACHE_NAME = 'offline';
const OFFLINE_URL = 'offline.html';


var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/django-pwa-app.css',
    // '/static/images/icons/icon-72x72.png',
    // '/static/images/icons/icon-96x96.png',
    // '/static/images/icons/icon-128x128.png',
    // '/static/images/icons/icon-144x144.png',
    // '/static/images/icons/icon-152x152.png',
    // '/static/images/icons/icon-192x192.png',
    // '/static/images/icons/icon-384x384.png',
    // '/static/images/icons/icon-512x512.png',
    // '/static/images/icons/splash-640x1136.png',
    // '/static/images/icons/splash-750x1334.png',
    // '/static/images/icons/splash-1242x2208.png',
    // '/static/images/icons/splash-1125x2436.png',
    // '/static/images/icons/splash-828x1792.png',
    // '/static/images/icons/splash-1242x2688.png',
    // '/static/images/icons/splash-1536x2048.png',
    // '/static/images/icons/splash-1668x2224.png',
    // '/static/images/icons/splash-1668x2388.png',
    // '/static/images/icons/splash-2048x2732.png'
];

// Cache on install

self.addEventListener('instalar', (evento) => {
 console.log('instalar', evento); self.skipWaiting(); });

self.addEventListener('activar', (evento) => {
 console.log('activar', evento); return self.clients.claim(); });

/*
self.addEventListener('fetch', function(evento) {
  event.respondWith(fetch(event.request));
  event.respondWith( caches.match( event.request).then(function(response) { return response || fetch(event. request); }) );
   });
*/

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