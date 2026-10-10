---
name: testing-practices
description: Practical test-quality lessons (isolation, realistic fixtures, deterministic time, real integrations, proof boundaries). Use when designing a test strategy, adding test infrastructure, or interpreting what a green result proves.
---

# Testing practices

Rule: `R-VERIFY`. Every check has a proof boundary; keep it visible in the task evidence.

- **Isolation:** each test gets its own instance (DOM/app/DB) and mandatory cleanup of timers, listeners, shared state; otherwise later tests are influenced.
- **Fixtures mirror reality:** include real load order and lifecycle (e.g. a harness providing a component earlier than the server does can hide bugs).
- **Determinism:** fake time and deliberately held-back responses make double clicks, races and stale polling reproducible.
- **Fakes drift:** a fake server needs maintenance together with the real API contract (shared schema/contract test).
- **Real integrations where behavior matters:** SQL and framework behavior with a real database; mocks mostly confirm expected calls.
- **Characterization + mutation:** characterization tests pin existing behavior before refactoring; targeted mutations show that tests detect relevant faults.
- **Layers complement each other:** unit/DOM, integration, browser, manual. A11y tools and green CI do not prove real screen reader announcements; if required, keep a manual check open.
- **Performance:** measure only under exclusive conditions (no parallel checks).
- Run suites via `scripts/run.sh`; load only failing sections of a log.
