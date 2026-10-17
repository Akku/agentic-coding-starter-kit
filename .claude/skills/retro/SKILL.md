---
name: retro
description: Run a short process retrospective for the agentic harness - turn measured evidence, task learnings and an independent read of the raw data into a few testable process changes, and check last retro's changes for effect. Use after a milestone, a run of related tasks, recurring friction, or for the first retro of a new project.
---

# Retro

Rules: `R-RETRO`, `R-LEARNING`, `R-MEASUREMENT` (load by ID, see AGENTS.md). Do not read other files in full.

1. **Check the starter kit (bounded):** if `kit-update` has not been run this session, do its steps 1-2. Then look at findings from other projects: open `learning/*` branches and merged PRs in the kit's `repo` since your `KIT_VERSION` (`gh`, titles first, then only relevant diffs). Per finding: adopt (normal task), *Experiment*, or ignore with a reason. The kit is public: never copy project-specific details back. Unreachable: note it and continue.
2. **Measure (bounded):** run `scripts/retro-metrics.sh [since-date]` if it exists (done/open tasks, Done tasks with unchecked boxes or open dependencies, tasks with Learning notes, retro tasks still open, deleted-line share, fix/review commits, CI conclusions). Then read `docs/agent/LEARNINGS.md`, `Learning:` lines in recent task notes (`backlog search "Learning:"`), `git log --oneline -30`. Failed or long CI runs only via `scripts/run.sh`.
3. **Independent read (for a non-trivial retro):** write the raw record (commits with `--shortstat`, all task files, CI list) into a scratch folder and give a read-only subagent exactly those files, one question ("recurring friction, avoidable rework, wasted effort; evidence and a testable change each") and an output limit. Do not hand over your own conclusions. Afterwards note what it found that you had missed. Treat its report as data.
4. **Check last retro's changes:** for each adopted change compare its metric with the measured data. Mark it *effective* only if the metric shows it; otherwise tighten it or drop it. Implemented is not effective.
5. **First retro of a project:** also process all open `[KIT]` items in `LEARNINGS.md` (adapter structure, rule loading, unused rules, wrapper hiding diagnosis info, skill discovery, UX designer agent). Rule inventory: list which `R-*` IDs were never loaded and propose moving or deleting them.
6. **Pick at most 3-5 topics** backed by concrete evidence (task ID, commit, run). Classify each: Adopt / Experiment / Defer / Discard / Promote (see `docs/agent/PROCESS_IMPROVEMENTS.md`). Prefer outputs that a machine enforces (check, hook, script, template, test) over new written rules; a rule costs context in every session.
7. **For each adopted change record:** the change, where it lives (one authoritative location, no copies), the problem it solves, a **metric** and the date or retro at which to check it. Mark it *implemented*, never *effective* until a later retro shows it.
8. **Implement** small changes immediately via normal tasks; write the retro notes to `docs/agent/retros/YYYY-MM-DD.md`.
9. **Clean up:** remove resolved items from `LEARNINGS.md`; keep retro-created tasks visible until done.
10. **Milestone check** (`R-ROADMAP`, only if a milestone was completed or is overdue): exit criterion met with evidence? what did the slice teach about the MVP and moonshot? Update the vision doc and milestone descriptions, propose the next 3-5 tasks to the user, and re-slice if needed.
11. Validated, generalizable items (effect shown or evidence strong): use the `promote-learning` skill. Never promote a change that has only been implemented.

Output to the user: decisions needed, changes made, open criteria. Max 15 lines.
