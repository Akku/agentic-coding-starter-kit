---
name: retro
description: Run a short process retrospective for the agentic harness - turn evidence (task learnings, commits, CI, usage) into a few testable process changes. Use after a milestone, a run of related tasks, recurring friction, or for the first retro of a new project.
---

# Retro

Rules: `R-RETRO`, `R-LEARNING`, `R-MEASUREMENT` (load by ID, see AGENTS.md). Do not read other files in full.

1. **Check the starter kit first (bounded):** use the `kit-update` skill's steps 1-2 (changelog since your `KIT_VERSION`). Then, for findings from other projects: read `repo` and `version` in `KIT_VERSION`; with `gh` (or a shallow clone in a temp folder outside the project) look at what the kit gained since that version: releases, merged PRs and open `learning/*` branches from other projects (titles first, then only the relevant diffs). Per finding decide: adopt here (as a normal task), note as *Experiment* for the retro list, or ignore with a reason. The kit is public: never copy project-specific details back. If the kit is unreachable, say so in the retro notes and continue.
2. **Collect evidence (bounded):** `docs/agent/LEARNINGS.md`; `Learning:` lines in recent task notes (`backlog search "Learning:"`); `git log --oneline -30`; failed/long CI runs via `scripts/run.sh`; usage data only if already available.
3. **First retro of a project:** also process all open `[KIT]` items in `LEARNINGS.md` (adapter structure, rule loading, unused rules, wrapper hiding diagnosis info).
4. **Pick at most 3-5 topics** backed by concrete evidence (task ID, commit, run). Classify each: Adopt / Experiment / Defer / Discard / Promote (see `docs/agent/PROCESS_IMPROVEMENTS.md`).
5. **For each adopted change record:** the change, where it lives (one authoritative location, no copies), the problem it solves, an observable success criterion for the next retro. Mark it *implemented*, never *effective* until the next retro shows it.
6. **Implement** small changes immediately via normal tasks; update the retro notes (a short doc under `backlog/docs` or `docs/agent/retros/YYYY-MM-DD.md`).
7. **Clean up:** remove resolved items from `LEARNINGS.md`; check last retro's success criteria.
8. **Milestone check** (`R-ROADMAP`, only if a milestone was completed or is overdue): exit criterion met with evidence? what did the slice teach about the MVP and moonshot? Update the vision doc and milestone descriptions, propose the next 3-5 tasks to the user, and re-slice if needed.
9. Validated, generalizable items: use the `promote-learning` skill.

Output to the user: decisions needed, changes made, open criteria. Max 15 lines.
