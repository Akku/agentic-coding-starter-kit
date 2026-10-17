# Stack notes: web app / PWA

Load when the project is a browser app, PWA or uses service workers. Source: one project, observed once.

- **iOS PWA storage:** the installed app has its own storage and the Cache API behaves differently from Chromium (a service-worker data cache that passed the Chromium offline test failed on an iPhone). Keep an app-level fallback (the page stores what it last loaded) and give PWA/offline/camera tasks a real-device check by the user.
- **Service worker:** call `response.clone()` before returning the response to the page; cloning inside the asynchronous cache callback fails silently and the offline start never works.
