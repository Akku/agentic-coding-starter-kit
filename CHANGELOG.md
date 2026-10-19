# Changelog

Newest first. Projects read the entries newer than their `KIT_VERSION` (see `kit-update` skill). Each entry: what changed and who benefits.

## 0.13.0
- **One communication standard instead of guided/concise:** always explain what happens and why, summarize phases, define new terms at first use; the setup question about the mode is gone and the retro asks whether the amount of explanation was right. (Feedback from a second project: the concise mode left the user without a good explanation.)
- **Links:** whenever the user should test, review or decide something, the message contains the direct way (URL with port/route, clickable path, PR/CI URL or exact command), what to check and which answer is needed.
- **Proactive batches:** the agent offers batches of related ready tasks itself (`AGENTS.md` rule 1c, `R-BATCHING`). Benefits: all projects.

## 0.12.0
- **Model recommendation:** `SETUP.md` asks which model/effort the user uses (after the agents question) and ends with a short recommendation (mid-tier model at medium effort by default, escalate for concrete reasons) to avoid unnecessary cost; the default is written to the `Model:` line in `AGENTS.md`; `R-ROUTING` carries the guidance; first retro checks it. Based on the maintainer's experience (anecdotal). Benefits: new users.

## 0.11.0
- **Context measurement:** optional `scripts/context-report.py` (Claude Code transcripts, numbers only) used by the retro. First sample: session length dominated cache-read tokens (3 of 36 sessions ~80 %), tool results at most ~25 %. Observed in one project, estimates rough.
- **Rules:** `R-CONTEXT-OUTPUT` (load only the needed part of stored output and source files) and `R-BATCHING` session-length hypothesis (hand off at task/milestone boundary or ~300 turns; to be verified in the first retro); `handoff` triggers adjusted. Benefits: all projects.

## 0.10.0
- **Retro asks for input:** started without instructions, the `retro` skill first asks the user once whether they want to contribute problems, ideas or goals. Benefits: all projects.
- **Incoming learnings (kit maintainer):** a GitHub Action opens a pull request automatically when a `learning/**` branch is pushed (GitHub then notifies the maintainer); the kit self-check also runs on such branches; `session-start.sh` lists open PRs and learning branches when run inside the kit repo. Setup removes these maintenance files from projects.

## 0.9.0
- **Guided communication until the first retro:** `Communication: guided|concise` in `AGENTS.md`. Guided mode explains steps and terms and summarizes each phase; context discipline is unchanged. Setup asks for the preference; the first retro asks whether to switch to `concise` and checks the context cost. Benefits: new users.

## 0.8.0
- **`SETUP.md` replaces the `project-setup` skill:** a visible root file, so the setup still works when the ZIP route lost hidden folders. Step 0 checks that hidden files arrived and restores missing ones from the kit ZIP. Setup deletes `SETUP.md` at the end, so its description no longer costs context in every session. Human guides warn about hidden files. Benefits: all new projects.

## 0.7.0
- **Backlog check:** `scripts/check-backlog.sh` + pre-commit hook reject Done tasks with unchecked boxes or unfinished dependencies; session start reports problems. Setup always activates the hook. Source: one project (observed once). Benefits: all projects.
- **Retro:** `scripts/retro-metrics.sh` (measured evidence), independent subagent read, effect check of last retro's changes; promote only changes with shown effect. Source: one project, effect not yet measured.
- **Knowledge moved:** web/PWA notes in `docs/agent/stacks/web-pwa.md`, Playwright and contrast checks in `testing-practices`. Benefits: web projects.

## 0.6.0
- **License:** MIT. Projects choose their own (setup asks).
- **Claude Code settings:** safe commands pre-approved (`backlog`, read-only `git`, session start); `SessionStart` hook injects the state summary automatically. Verification commands are added narrowly by setup. Benefits: all Claude Code projects, fewer approval prompts.
- **Kit self-check:** `.github/kit-check.py` + GitHub Action (rule markers and index, scripts, frontmatter, version consistency). Setup removes these maintenance files from projects.

## 0.5.1
- `project-setup` installs missing tools itself (the permission prompt is the approval) and gives manual instructions only if the user declines or a step cannot be automated. Prompt texts adjusted. Benefits: new projects.

## 0.5.0
- **Update check:** `scripts/session-start.sh` reports a newer kit version once per day; new `kit-update` skill and rule `R-KIT-UPDATE`. Benefits: all projects.
- **Milestones:** `project-setup` sharpens the idea into vertical slice, MVP and moonshot, creates Backlog.md milestones and a vision doc; rule `R-ROADMAP` lets the agent propose next tasks; `retro` reviews milestones. Benefits: all projects.
- **Setup per OS:** concrete install steps for macOS, Windows and Linux in `project-setup`. Benefits: new projects.

## 0.4.0
- `retro` starts by checking the kit for findings from other projects.

## 0.3.0
- Rule `R-LIFECYCLE` 1.7: propose follow-up tasks instead of hiding or silently creating them.

## 0.2.0
- `ux-designer` agent, concept phase (`R-CONCEPT`), confidential-input folder with pre-commit guard, skill discovery and UX checks in retro. Benefits: projects with a UI.

## 0.1.0
- Initial kit: rules by ID, `run.sh`, `session-start.sh`, skills `project-setup`, `retro`, `handoff`, `promote-learning`, `testing-practices`, bilingual guides.
