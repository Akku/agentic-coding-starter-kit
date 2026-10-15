# Start here

**Version 0.2.0** · 🇩🇪 **Deutsche Version: [STARTE_HIER.md](STARTE_HIER.md)**

This kit is a starting point for agent-driven development with Git and Backlog.md. You give the agent your project goal; it installs what is missing, sets up the tooling, adapts the rules to your goal and then works task by task. No technical knowledge is required for the standard path.

## Standard path: download the ZIP

1. **Download** the kit: [agentic-coding-starter-kit.zip](https://github.com/Akku/agentic-coding-starter-kit/archive/refs/heads/main.zip) (also: green **Code** button → **Download ZIP** on the GitHub page).
2. **Unzip** it (macOS: double-click; Windows: right-click → *Extract All*). Rename the folder to your project name and put it where you keep your projects.
3. **Open your agent** (e.g. the Claude desktop app, Code tab) and choose that folder as the working folder.
4. **Give the agent this prompt**, with your goal filled in:

   > Set up this project with the `project-setup` skill (`.claude/skills/project-setup/SKILL.md`). Work in my language and guide me step by step through installing anything that is missing. What I want to build is the following: *<your idea: what, for whom, what "done" looks like – a few sentences>*

5. **Answer the questions** (technology, which agents you use, GitHub yes/no). The agent checks which tools are missing (Git, Node.js, Backlog.md) and guides you through installing them step by step. You approve every install. If an installer asks for your computer password, type it yourself, never into the chat. On Windows the helper scripts need Git for Windows (includes *Git Bash*); the agent will guide you.
6. **At the end** the agent summarizes what exists and which task comes first. Tell it to start.

## For technical users: via GitHub

- Click **Use this template** on the GitHub page (creates your own repository), clone it, open it in your agent, then give the prompt from step 4. Or: `git clone` this repository and remove the `.git` folder to start with a fresh history.
- Already have `git`, `node` and `backlog` installed? The agent will detect that and skip the installation steps.
- Improvements and validated learnings are welcome as pull requests (see `promote-learning` skill).

## What you get

- Git, Backlog.md and the first 3–7 tasks derived from your goal.
- Short agent rules (`AGENTS.md`) that load further rules only when needed – saves tokens.
- `scripts/run.sh` keeps long test/CI output out of the context; `scripts/session-start.sh` gives a compact status at session start.
- Skills for recurring work: `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices`.

## Working day to day

- Work is backlog-driven: every change is a task with acceptance criteria. View it with `backlog board` or `backlog browser`.
- End a session with the `handoff` skill; the next session starts from `docs/agent/HANDOFF.md`.
- After the first milestone, run a retro (`retro` skill). It also reviews the harness itself, including the open questions in `docs/agent/LEARNINGS.md`.
- Never put secrets into the repository.

## Trying the kit on a real project: what to watch

- Did the agent read only `AGENTS.md` at the start instead of everything?
- Are `backlog/` and the first tasks there, and is `AGENTS.md` still intact?
- Does verification run through `scripts/run.sh`?
- Is `Setup status: DONE` set in `AGENTS.md` and everything committed?
- Does a second session continue via `scripts/session-start.sh` without re-asking?
- Note stumbling blocks or unclear points (or let the agent record them as `Learning:`). They are the input for the first retro.

## Language

These files are for humans (English and German). Instructions for agents are in English, but agents talk to you in your language.
