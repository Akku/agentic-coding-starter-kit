---
name: project-setup
description: One-time setup of a new project from the Agentic Coding Starter Kit - asks for the project goal, checks/installs prerequisites, sets up Git and Backlog.md, adapts the harness, creates the first tasks. Use when AGENTS.md says "Setup status: TODO" or the user asks to set up the project.
---

# Project setup (one-time)

Talk to the user in their language. Keep status messages to one sentence. Ask before anything with side effects outside this folder (global installs, creating remote repositories, pushing).

## 1. Understand the kit (≈2 min, do not read everything)
Read only `AGENTS.md`. Other files are loaded on demand by rule ID. Skills live in `.claude/skills/*/SKILL.md`; other agents read the file directly.

## 2. Ask the user (one message, all questions together)
- Project goal in 3–5 sentences (what, for whom, what "done" looks like).
- Stack/language preferences, or "decide for me".
- Which agents will be used (Claude Code / Codex / Copilot)? Keep all adapters regardless; note the answer in `docs/agent/LEARNINGS.md`.
- Confidential inputs (customer documents, scripts, exports)? Which folder holds them? Default: `inputs/`.
- Create a GitHub repository now? Default: private, none yet.

## 3. Check and install prerequisites (assume a non-technical user)
Check: `git --version`, `node --version`, `npm --version`, `backlog --version`, optionally `gh --version`. Detect the OS first.
For each missing tool: say in one plain sentence what it is for, propose the install command for the user's OS (macOS: Homebrew if present; Windows: `winget`; otherwise the official installer), wait for approval, run it, verify with the version command. If an installer needs a password or admin approval, tell the user to enter it themselves, never in chat. Backlog.md: see its README for the current install command; verify with `backlog --version`.
Windows: the scripts in `scripts/` are bash. Install Git for Windows (includes Git Bash) and run them with `bash scripts/<name>.sh`. If something cannot be installed, explain what is lost and continue where possible.
If a tool is installed but not found, the terminal may need a restart; say so.

## 4. Git
If this folder is not a git repository (typical for the ZIP route): `git init -b main`; set `user.name`/`user.email` only if missing (ask the user). Add a `.gitignore` for the chosen stack (include `.env*`, logs, build output). **Never commit secrets** because the repository may become public.
Confidential inputs: create the agreed folder, add it to `.gitignore`, and activate the pre-commit guard with `git config core.hooksPath scripts/githooks` (it blocks office/PDF/database files). Stage explicit paths, not `git add -A`, while untracked inputs exist.

## 5. Initialise Backlog.md
```sh
backlog init "<project name>" --defaults --integration-mode cli --agent-instructions none
backlog config get autoCommit   # must be false: code and task changes are committed together
```
`--agent-instructions none` keeps this kit's `AGENTS.md`/`CLAUDE.md` intact. Afterwards confirm both files are unchanged. Run `backlog instructions overview` once and `backlog config --help` to see how to set a Definition of Done; add a short DoD (if code changed: verification run via `scripts/run.sh`; missing manual evidence stays open; working tree checked). Design, decision and documentation tasks have no code to verify, so the first item must be conditional.

## 6. Adapt the harness to the project goal
- Fill the "Project specifics" block in `AGENTS.md` (goal, stack, verification commands). Keep it under ~15 lines.
- Make sure there is one obvious final verification command and fast targeted ones; document them in `AGENTS.md`. Always via `scripts/run.sh <label> <command>`.
- Adapt the summary `grep` in `scripts/run.sh` to the test runner's output format, if needed.
- Create `docs/agent/HANDOFF.md` (max ~40 lines: current task, approvals, next step, blockers). `scripts/session-start.sh` prints it.
- Add stack-specific pitfalls to `docs/agent/PITFALLS.md` only if already known.
- Do not add agents, skills, hooks or telemetry now (`R-DECISION`).

## 7. First backlog
Create 3–7 tasks from the goal with `backlog task create` (check `--help`): small, each with checkable acceptance criteria. The first task should be a walking skeleton that already runs the verification command end to end.

## 8. Project README, commit and report
Replace the kit's `README.md`/`README.de.md` with a short project README (goal, how to run, verification command); keep `START_HERE.md`/`STARTE_HIER.md`/`KIT_VERSION` unless the user wants them removed.


Check `git status`, commit "Set up agentic harness", optionally push if the user agreed to a remote. Then set `Setup status:` in `AGENTS.md` to `DONE` and tell the user in ≤10 lines: what exists, which commands to use, which task comes first.

## Later
- First retro: run `R-RETRO` and process the open `[KIT]` observations in `docs/agent/LEARNINGS.md`.
- Valuable, validated learnings can go back into the kit repository via pull request (`docs/agent/PROCESS_IMPROVEMENTS.md`, "Cross-project promotion").
