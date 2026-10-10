# Agentic Coding Starter Kit

*Deutsch: [README.de.md](README.de.md)*

A minimal, growing base for agent-driven development (Claude Code, Codex, GitHub Copilot) with Git and [Backlog.md](https://github.com/MrLesk/Backlog.md) – token-efficient and traceable.

## Usage

1. Choose **Use this template** on GitHub (or copy the folder) and open the new project locally.
2. Give the agent the folder and the prompt from [START_HERE.md](START_HERE.md) (`project-setup` skill + your project goal).
3. The agent checks prerequisites, sets up Git and Backlog.md, adapts the harness to your goal and creates the first tasks. Development then starts.

At the start of each session the agent runs `scripts/session-start.sh` (short state summary).

## Contents

| File | Purpose |
| --- | --- |
| `START_HERE.md` / `STARTE_HIER.md` | Human guide (EN/DE) |
| `AGENTS.md` | Shared core rules (Codex and compatible tools) |
| `CLAUDE.md`, `.github/copilot-instructions.md` | Thin adapters pointing to `AGENTS.md` |
| `.claude/skills/` | Skills: `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices` |
| `scripts/run.sh` | Compact output for tests/CI/CLI (exit code preserved, full log outside the repo) |
| `scripts/session-start.sh` | Read-only session start (branch, changes, tasks, handoff) |
| `docs/agent/OPERATING_MODEL.md` | Rules with stable IDs (`R-*`), loaded selectively |
| `docs/agent/ADVANCED.md` | Rarely needed rules (parallelism, measurement, routing, local models) |
| `docs/agent/LEARNINGS.md` | Observations for retros (includes starting points for the first retro) |
| `docs/agent/PITFALLS.md` | Growing list of technical pitfalls |
| `docs/agent/PROCESS_IMPROVEMENTS.md` | Retro handling and feeding learnings back into the kit |

## Principles

- Information architecture over "answer shorter": short entry points, deeper detail on demand, full logs outside the context.
- One authoritative source per rule; adapters only point to it.
- The harness grows through retros, not by stockpiling (`R-DECISION`).
- Humans read English/German docs; agent instructions are English; agents talk to users in the user's language.

## Contributing

Please contribute proven learnings via pull request (pattern: problem, pattern, applicability, evidence – see `docs/agent/PROCESS_IMPROVEMENTS.md` or the `promote-learning` skill). No project or company internals, no credentials – this repository is public.
