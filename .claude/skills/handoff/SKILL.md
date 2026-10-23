---
name: handoff
description: Rewrite docs/agent/HANDOFF.md from scratch so the next session can continue without replaying history, then run the end-of-session checklist. Use when ending a session, at a task or milestone boundary, when a context notice reports a large context (threshold in `R-BATCHING`), or before switching agents.
---

# Handoff / session end

Rules: `R-STATE`, `R-BOOTSTRAP`, `R-STATE-COHERENCE`. The handoff holds only what git and the backlog cannot tell the next session; the session-start script already prints branch, commits, active and ready tasks.

## 1. Write `docs/agent/HANDOFF.md`
Always rewrite the whole file, never append or "refresh" (`Earlier:` sections are how it bloats). Max 2 KB / 40 lines; the session-start script warns above that. Use these headings, drop empty ones:

```
# Handoff
**State:** <date>, stem <version from STEM_VERSION>, <branch> @ <commit SHA>; <what is true in one or two sentences>
**Approvals:** <what the user allowed, date>; <scope, batch, release>
**Next step:** <one concrete action, with the file/command to start>
**Evidence open:** <what was verified at which SHA; what is still missing, e.g. manual check>
**Blockers / decisions:** <what waits for the user>
**Notes:** <max 3 lines: facts the next run needs that are written nowhere else; re-justify each one at every rewrite, else drop>
```

Per line test: does git or the backlog already show it (finished tasks, active task, commit messages)? Then delete it. Durable knowledge goes to `docs/` or `PITFALLS.md`, not into Notes, history stays in tasks and commits.

## 2. Check before saving
Sections agree with each other, approvals are still valid, evidence names the SHA it verified (`R-STATE-COHERENCE`).

## 3. Session-end checklist
1. `git status`: nothing unrelated, nothing forgotten. Commit code together with its task changes and the handoff, or state why not.
2. Unfinished tasks: each has a concrete continuation point in its notes (open criterion, next action), not "still to check".
3. Notable detours or high context cost: add `Learning:` to the task (only if it happened).

If a step did not fit or you deviated from it: `Learning: skill handoff: <what> -> <change>` in the task notes (`R-LEARNING`).
