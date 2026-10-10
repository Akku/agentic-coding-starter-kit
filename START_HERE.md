# Start here

*Deutsch: [STARTE_HIER.md](STARTE_HIER.md)*

This kit is a starting point for agent-driven development with Git and Backlog.md. You give the agent your project goal; it sets up the tooling, adapts the rules to your goal and begins working task by task.

## How to start

1. Create your project from this template (GitHub: **Use this template**) or copy this folder to where the project should live. Open it in your agent (Claude Code, Codex, Copilot).
2. Give the agent this prompt, with your goal filled in:

   > Set up this project using the `project-setup` skill (`.claude/skills/project-setup/SKILL.md`). Project goal: *<what, for whom, what "done" looks like – 3–5 sentences>*. Work in my language.

3. Answer the agent's questions (stack, which agents you use, GitHub repository yes/no) and approve installs it proposes. Check what it wants to install before approving.
4. At the end the agent summarizes what exists and which task comes first. Tell it to start.

## What you get

- Git, Backlog.md and the first 3–7 tasks derived from your goal.
- Short agent rules (`AGENTS.md`) that load further rules only when needed, which saves tokens.
- `scripts/run.sh` keeps long test/CI output out of the context; `scripts/session-start.sh` gives a compact status at session start.
- Skills for recurring work: `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices`.

## Working day to day

- Work is backlog-driven: every change is a task with acceptance criteria. Look at it with `backlog board` or `backlog browser`.
- End a session with the `handoff` skill; the next session starts from `docs/agent/HANDOFF.md`.
- After the first milestone, run a retro (`retro` skill). It reviews the harness itself, including the open questions in `docs/agent/LEARNINGS.md`.
- Never put secrets into the repository.

## Language

These files are for humans (English and German). Instructions for agents are in English, but agents talk to you in your language.
