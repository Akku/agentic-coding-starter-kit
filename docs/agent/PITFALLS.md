# Recurring technical pitfalls (project-local)

Durable, project-specific pitfalls found during work. Keep entries short: symptom → cause → what to do. Starter hints from the kit (verify whether they apply to your stack):

- Verification has a proof boundary: DOM/unit tests ≠ real browser ≠ assistive technology ≠ real database. State which level was tested (`R-VERIFY`).
- Fixtures must mirror real load order and lifecycle, otherwise they can hide bugs.
- Fake servers/mocks drift from the real API contract; maintain them with it.
- Performance measurements are invalid while other checks run in parallel.
- Give tests isolation and mandatory cleanup (timers, listeners, shared state).

<!-- Project entries: -->
