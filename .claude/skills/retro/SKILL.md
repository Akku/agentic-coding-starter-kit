---
name: retro
description: Run a short process retrospective for the agentic harness - turn evidence (task learnings, commits, CI, usage) into a few testable process changes. Use after a milestone, a run of related tasks, recurring friction, or for the first retro of a new project.
---

# Retro

Rules: `R-RETRO`, `R-LEARNING`, `R-MEASUREMENT` (load by ID, see AGENTS.md). Do not read other files in full.

1. **Collect evidence (bounded):** `docs/agent/LEARNINGS.md`; `Learning:` lines in recent task notes (`backlog search "Learning:"`); `git log --oneline -30`; failed/long CI runs via `scripts/run.sh`; usage data only if already available.
2. **First retro of a project:** also process all open `[KIT]` items in `LEARNINGS.md` (adapter structure, rule loading, unused rules, wrapper hiding diagnosis info).
3. **Pick at most 3-5 topics** backed by concrete evidence (task ID, commit, run). Classify each: Adopt / Experiment / Defer / Discard / Promote (see `docs/agent/PROCESS_IMPROVEMENTS.md`).
4. **For each adopted change record:** the change, where it lives (one authoritative location, no copies), the problem it solves, an observable success criterion for the next retro. Mark it *implemented*, never *effective* until the next retro shows it.
5. **Implement** small changes immediately via normal tasks; update the retro notes (a short doc under `backlog/docs` or `docs/agent/retros/YYYY-MM-DD.md`).
6. **Clean up:** remove resolved items from `LEARNINGS.md`; check last retro's success criteria.
7. Validated, generalizable items: use the `promote-learning` skill.

Output to the user: decisions needed, changes made, open criteria. Max 15 lines.
