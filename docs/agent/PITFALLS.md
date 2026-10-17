# Recurring technical pitfalls (project-local)

Durable, project-specific pitfalls found during work. Keep entries short: symptom → cause → what to do. Starter hints from the kit (verify whether they apply to your stack):

- Verification has a proof boundary: DOM/unit tests ≠ real browser ≠ assistive technology ≠ real database. State which level was tested (`R-VERIFY`).
- Fixtures must mirror real load order and lifecycle, otherwise they can hide bugs.
- Fake servers/mocks drift from the real API contract; maintain them with it.
- Performance measurements are invalid while other checks run in parallel.
- Give tests isolation and mandatory cleanup (timers, listeners, shared state).

<!-- Project entries: -->
- PWA on iOS: the installed app has its own storage and the Cache API behaves differently from Chromium (a service-worker data cache that passed the Chromium offline test failed on an iPhone). Keep an app-level fallback (the page stores what it last loaded) and give PWA/offline/camera tasks a real-device check by the user.
- Service worker: call `response.clone()` before returning the response to the page; cloning inside the asynchronous cache callback fails silently and the offline start never works.
- Git hooks and Backlog.md: task file names contain spaces, so pass paths NUL-separated and test the hook with the real file names.
- Playwright: the default desktop viewport may open a two-pane layout; run the main flows in a phone viewport. `getByText` matches substrings case-insensitively; give indicators their own element or use `exact`. A shared e2e database makes names collide: use unique ones per test.
- Contrast checks: a design token the browser serializes as `#fff` parses as NaN in a 6-digit parser, and a NaN ratio never fails. Assert every token is a valid colour.
