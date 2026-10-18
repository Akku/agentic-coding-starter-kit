# Agent instructions (shared core)

Applies to Codex, Claude Code (via `CLAUDE.md`), Copilot (via `.github/copilot-instructions.md`) and any AGENTS-compatible tool.

**Setup status:** TODO  <!-- SETUP.md sets this to DONE and deletes itself -->
If TODO: follow `SETUP.md` first (when the user asks to set up; otherwise ask once).

**Language:** talk to the user in the user's language; keep instruction files and task/rule text in English.

**Communication:** guided  <!-- guided until the first retro; the retro asks whether to switch to `concise`. The user's own instructions override this. -->
- `guided`: briefly say what you do and why; explain a new term (backlog, task, milestone, retro) in one sentence at first use; after each phase (setup step, finished task, session end) give 3-5 lines: what happened, what the user can do now, what comes next; ask questions with options and a recommendation. No narration of every tool call; at most ~12 lines per message.
- `concise`: results, decisions needed and problems only; status messages one sentence.
- This governs messages to the user only. Context discipline (compact tool output, rules by ID) stays the same in both modes.

**Skills** (`.claude/skills/<name>/SKILL.md`; agents without skill support read the file when needed): `retro`, `handoff`, `promote-learning`, `testing-practices`, `kit-update`.
**Agents** (`.claude/agents/<name>.md`; other tools read the file as instructions for a subagent): `ux-designer` for projects with a user interface (concept phase, mockups, UX reviews of new screens; see `R-DELEGATION` for the brief).

## Session start
In Claude Code a `SessionStart` hook (`.claude/settings.json`) injects `scripts/session-start.sh` output; if you do not see its output (other tools, hook disabled), run the script once per session (read-only state summary). Do not replay history. If it reports a newer kit version, tell the user once and offer the `kit-update` skill (`R-KIT-UPDATE`); never update unasked.

## Core rules (full text by ID: `docs/agent/OPERATING_MODEL.md`)
1. **Task first** (`R-LIFECYCLE`): every change is a Backlog.md task: task → plan → implement → verify → evidence → done. Use the `backlog` CLI only; run `backlog instructions overview` once per session and `backlog <cmd> --help` for unknown commands.
1b. **Follow-ups** (`R-LIFECYCLE` 1.7): when finishing a task, propose useful out-of-scope follow-up tasks (max. 3, with reason and rough size) to the user; create them only after agreement. Do not silently expand the current task.
1c. **Roadmap** (`R-ROADMAP`): work belongs to a milestone; when a milestone runs out of ready tasks, propose the next 3-5 (user agrees before creation).
2. **Compact output** (`R-CONTEXT-OUTPUT`): run tests, builds, CI and other verbose commands via `scripts/run.sh <label> <command>`. Read the log only on failure, and only the relevant part. Never re-read output that was already summarized.
3. **One source per rule** (`R-INSTRUCTIONS`): never copy rules into other files; reference the rule ID.
4. **Evidence has limits** (`R-VERIFY`): green CI is not proof of required manual checks. Keep missing evidence open with a concrete continuation point.
5. **Git state** (`R-STATE-COHERENCE`): check `git status` before committing and before ending a session. Commit code together with its task changes; never include unrelated changes.
6. **Bounded delegation** (`R-DELEGATION`): subagents get exact files/diff, one question and an output format. Skip delegation for small mechanical changes.
7. **Stop conditions** (`R-AUTONOMY`): stop and ask on repeated failure, missing product decision or ambiguous destructive action. `BLOCKED` is a valid outcome.
8. **Learnings** (`R-LEARNING`): for notable detours, aborts or high context cost, add `Learning: <observation> → <improvement>` to the task notes. Otherwise add nothing.

Load other rules only when their trigger applies (index below), never the whole file:

```sh
sed -n '/<!-- RULE:R-INDEX:START -->/,/<!-- RULE:R-INDEX:END -->/p' docs/agent/OPERATING_MODEL.md
ID=R-REVIEW; sed -n "/<!-- RULE:${ID}:START -->/,/<!-- RULE:${ID}:END -->/p" docs/agent/OPERATING_MODEL.md
```

## Project specifics
<!-- Filled in during setup (SETUP.md): project goal, stack, verification commands. -->
- Goal: _(set during setup)_
- Verify: _(command, always via `scripts/run.sh`)_
