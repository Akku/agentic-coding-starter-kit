# Agentic Coding Starter Kit

**Version 0.17.0** · 🇩🇪 **Deutsche Version: [README.de.md](README.de.md)**

A minimal, growing base for agent-driven development (Claude Code, Codex, GitHub Copilot) with Git and [Backlog.md](https://github.com/MrLesk/Backlog.md) – token-efficient and traceable.

## Usage

**Standard path (no technical knowledge needed):** [download the ZIP](https://github.com/Akku/agentic-coding-starter-kit/archive/refs/heads/main.zip), unzip it, open the folder in your agent and give it the prompt from [START_HERE.md](START_HERE.md). The agent installs missing tools with you, sets up Git and Backlog.md, helps you sharpen the idea into a vertical slice, MVP and moonshot, adapts the harness to your goal, creates Backlog.md milestones and the first tasks.

**Technical users:** click **Use this template** on GitHub, or clone the repository, then use the same prompt.

At the start of each session the agent runs `scripts/session-start.sh` (short state summary).

## Staying up to date

At the start of each session the agent checks (once per day) whether a newer kit version exists and tells you. With your approval the `kit-update` skill reads the [changelog](CHANGELOG.md), picks what helps your project and merges it without overwriting your project-specific content. The `retro` skill checks the kit as well.

## Prompt to start

Give this to the agent after opening the folder:

> Set up this project: follow `SETUP.md`. Work in my language and install anything that is missing yourself (I will approve the steps). What I want to build is the following: *<your idea: what, for whom, what "done" looks like – a few sentences>*

## Contents

| File | Purpose |
| --- | --- |
| `START_HERE.md` / `STARTE_HIER.md` | Human guide (EN/DE) |
| `SETUP.md` | One-time setup procedure for the agent (deleted after setup) |
| `AGENTS.md` | Shared core rules (Codex and compatible tools) |
| `CLAUDE.md`, `.github/copilot-instructions.md` | Thin adapters pointing to `AGENTS.md` |
| `.claude/skills/` | Skills: `retro`, `design-alignment`, `handoff`, `promote-learning`, `testing-practices`, `kit-update` |
| `.claude/agents/` | Agents: `ux-designer` (for projects with a UI) |
| `scripts/githooks/pre-commit` | Guard against committing confidential source documents (activated during setup) |
| `KIT_VERSION`, `CHANGELOG.md` | Kit version this project is based on; what changed per version |
| `.claude/settings.json` | Claude Code: safe commands pre-approved, session-start hook |
| `LICENSE` | MIT (kit); `.github/kit-check.py` + workflow check the kit itself |
| `scripts/check-backlog.sh`, `scripts/retro-metrics.sh` | Backlog consistency check (also in the pre-commit hook); measured evidence for retros |
| `docs/agent/stacks/` | Stack-specific notes, loaded only when the stack applies |
| `scripts/context-report.py` | Optional retro tool (Claude Code): where the context went, longest sessions; numbers only |
| `scripts/context-check.py` | Claude Code hook: warns when the context is large and a new session is due |
| `scripts/run.sh` | Compact output for tests/CI/CLI (exit code preserved, full log outside the repo) |
| `scripts/session-start.sh` | Read-only session start (branch, changes, tasks, handoff) |
| `docs/agent/OPERATING_MODEL.md` | Rules with stable IDs (`R-*`), loaded selectively |
| `docs/agent/ADVANCED.md` | Rarely needed rules (parallelism, measurement, routing, local models) |
| `docs/agent/EXPERIMENTS.md` | Hypotheses, metrics, baselines and evidence grades for cost-carrying rules |
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
