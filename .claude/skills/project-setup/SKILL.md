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
- Three horizons (see `R-ROADMAP`): the **vertical slice** (thinnest end-to-end path that proves the idea), what belongs in the **MVP** (and what is explicitly out), and the **moonshot** (the dream version). If the user has no answer, propose one from the goal and ask for corrections.
- Stack/language preferences, or "decide for me".
- Which agents will be used (Claude Code / Codex / Copilot)? Keep all adapters regardless; note the answer in `docs/agent/LEARNINGS.md`.
- Confidential inputs (customer documents, scripts, exports)? Which folder holds them? Default: `inputs/`.
- Create a GitHub repository now? Default: private, none yet.

## 3. Check and install prerequisites (assume a non-technical user)
Detect the OS (`uname -s`, or `$OS`/`ver` on Windows). Check: `git --version`, `node --version`, `npm --version`, `backlog --version`; optionally `gh --version`.
**Do it yourself.** For each missing tool: say in one plain sentence what it is for, then run the install command (the tool-permission prompt is the user's approval) and verify with the version command. Give the user step-by-step instructions only if they decline the approval, the app denies the command, or a step cannot be automated (e.g. a password or admin prompt: the user types it themselves, never in chat; a GUI installer). After manual steps, re-check with the version command and continue. After an install the terminal/app may need a restart to find the tool; say so.

| Tool | macOS | Windows | Linux |
| --- | --- | --- | --- |
| Git | `xcode-select --install` (also installs Command Line Tools) or `brew install git` | `winget install --id Git.Git -e` (includes Git Bash) | `sudo apt install git` / distro equivalent |
| Node.js (LTS) | `brew install node`, or the installer from nodejs.org | `winget install --id OpenJS.NodeJS.LTS -e` | `sudo apt install nodejs npm`, or nodejs.org |
| Backlog.md | `brew install backlog-md` or `npm i -g backlog.md` | `npm i -g backlog.md` (no Windows-specific steps in its README; fallback `npx backlog.md`) | `npm i -g backlog.md` |
| GitHub CLI (optional) | `brew install gh` | `winget install --id GitHub.cli -e` | see cli.github.com |

Homebrew missing on macOS: offer the installer from brew.sh (needs the user's password, typed by the user in the terminal) or use the npm route. `winget` missing on Windows: use the installers from git-scm.com and nodejs.org.
Known pitfalls: Apple Silicon with Rosetta-installed Node/Homebrew gives "illegal hardware instruction" / "Binary package not installed" for backlog, so reinstall natively (`arch -arm64 npm i -g backlog.md`). Windows PowerShell may block npm scripts ("running scripts is disabled"); use `npm.cmd`, or after explaining it, `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` with the user's approval. Windows: the scripts in `scripts/` are bash; run them with `bash scripts/<name>.sh`.
If something cannot be installed, explain what is lost and continue where possible. Windows steps are not yet field-tested: record friction as `Learning:` in `docs/agent/LEARNINGS.md`.

## 4. Git
If this folder is not a git repository (typical for the ZIP route): `git init -b main`; set `user.name`/`user.email` only if missing (ask the user). Add a `.gitignore` for the chosen stack (include `.env*`, logs, build output). **Never commit secrets** because the repository may become public.
Always activate the pre-commit hook with `git config core.hooksPath scripts/githooks`: it blocks office/PDF/database files and rejects Done tasks with open boxes (`scripts/check-backlog.sh`). Confidential inputs: create the agreed folder and add it to `.gitignore`; stage explicit paths, not `git add -A`, while untracked inputs exist.

## 5. Initialise Backlog.md
```sh
backlog init "<project name>" --defaults --integration-mode cli --agent-instructions none
backlog config get autoCommit   # must be false: code and task changes are committed together
```
`--agent-instructions none` keeps this kit's `AGENTS.md`/`CLAUDE.md` intact. Afterwards confirm both files are unchanged. Run `backlog instructions overview` once and `backlog config --help` to see how to set a Definition of Done; add a short DoD (if code changed: verification run via `scripts/run.sh`; every acceptance criterion has evidence, or the missing evidence is recorded in the notes with a continuation point; code and task changes committed together). Done tasks with unchecked boxes are rejected by the pre-commit hook (`scripts/check-backlog.sh`); chore tasks use `--no-dod-defaults`. Design, decision and documentation tasks have no code to verify, so the first item must be conditional.

## 6. Adapt the harness to the project goal
- Fill the "Project specifics" block in `AGENTS.md` (goal, stack, verification commands). Keep it under ~15 lines.
- Make sure there is one obvious final verification command and fast targeted ones; document them in `AGENTS.md`. Always via `scripts/run.sh <label> <command>`.
- Claude Code: add the project's verification commands to `permissions.allow` in `.claude/settings.json` as narrow patterns (e.g. `Bash(scripts/run.sh test npm test)`); never a wildcard on `scripts/run.sh` (it runs arbitrary commands).
- Adapt the summary `grep` in `scripts/run.sh` to the test runner's output format, if needed.
- Create `docs/agent/HANDOFF.md` (max ~40 lines: current task, approvals, next step, blockers). `scripts/session-start.sh` prints it.
- Add stack-specific pitfalls to `docs/agent/PITFALLS.md` only if already known.
- Do not add further agents, skills, hooks or telemetry now (`R-DECISION`). If the project has a user interface, keep `.claude/agents/ux-designer.md`; otherwise delete it.

## 7. First backlog
If the direction is unclear or the project has a user interface, follow `R-CONCEPT` first (concept phase); the `ux-designer` agent prepares the mockup rounds. Also check whether existing skill collections offer skills that fit the stack.
Follow `R-ROADMAP`: write the vision (audience, core value, non-goals, moonshot ideas) as a Backlog.md doc (`backlog doc create "Vision"`, check `--help`), then create the milestones `backlog milestone add "M1 Vertical slice" -d "<goal + exit criterion>"`, `M2 MVP`, and `M3 Moonshot` (description only).
Create 3–7 tasks for M1 with `backlog task create ... -m <milestone>` (check `--help`): small, each with checkable acceptance criteria. The first task is a walking skeleton that already runs the verification command end to end. Tasks for M2 are created later (`R-ROADMAP`).

## 8. Project README, commit and report
Replace the kit's `README.md`/`README.de.md` with a short project README (goal, how to run, verification command); keep `START_HERE.md`/`STARTE_HIER.md`/`KIT_VERSION`/`CHANGELOG.md` unless the user wants them removed.
Remove kit-maintenance files that do not belong in a project: `.github/workflows/kit-check.yml`, `.github/kit-check.py`, `.github/bump-version.sh`. Replace the kit's `LICENSE` (MIT, the kit's license) with the project's own choice: ask the user; if unsure, delete it and say that no license means all rights reserved.


Check `git status`, commit "Set up agentic harness", optionally push if the user agreed to a remote. Then set `Setup status:` in `AGENTS.md` to `DONE` and tell the user in ≤10 lines: what exists, the milestones, which commands to use, which task comes first.

## Later
- First retro: run `R-RETRO` and process the open `[KIT]` observations in `docs/agent/LEARNINGS.md`.
- Valuable, validated learnings can go back into the kit repository via pull request (`docs/agent/PROCESS_IMPROVEMENTS.md`, "Cross-project promotion").
