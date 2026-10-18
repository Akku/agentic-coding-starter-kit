---
name: handoff
description: Write or refresh docs/agent/HANDOFF.md so the next session can continue without replaying history; also the end-of-session checklist. Use when ending a session, at a task or milestone boundary, after roughly 300 turns, when context is large, or before switching agents.
---

# Handoff / session end

Rules: `R-STATE`, `R-BOOTSTRAP`, `R-STATE-COHERENCE`.

1. `git status`: nothing unrelated, nothing forgotten. Commit code with its task changes, or state why not.
2. Unfinished tasks: each has a concrete continuation point in its notes (which criterion is open, next action), not "still to check".
3. Write `docs/agent/HANDOFF.md`, max ~40 lines, current state only:
   - **Active task/batch** and branch
   - **Approvals** given by the user (scope, batches, releases)
   - **Next permitted step**
   - **Evidence for current code state:** commit SHA, CI run/result, what is still missing (manual checks)
   - **Blockers / open decisions**
4. Remove finished items instead of appending. History lives in tasks and commits, durable knowledge in `docs/` or `PITFALLS.md`.
5. Notable detours/high context cost: add `Learning:` to the task (only if it happened).
