# Changelog

Newest first. Projects read the entries newer than their `KIT_VERSION` (see `kit-update` skill). Each entry: what changed and who benefits.

## 1.1.0
- **New optional skill `market-analysis`:** lean web check of existing alternatives, comparison table, gap and build/adapt/use recommendation, stored as a backlog doc. Offered in the `SETUP.md` module checklist (off for small projects). Benefits: medium/large projects avoid rebuilding what exists.
- **User profile at setup (`SETUP.md` step 1a):** asks expert / technical / non-technical and swaps the `Communication` block in `AGENTS.md` for the chosen variant (expert also sets `outputStyle: Concise`); shipped default is the technical variant, without line limits. Profile recorded in `LEARNINGS.md`, changeable later by telling the agent. Benefits: all new projects; check readability and output tokens in the retro.
- **`AGENTS.md` slimmed (5.9 -> 4.6 KB):** removed the human-only intro and a duplicate line, shortened skills/session-start/roadmap/design/output rules, moved the Agents line and the delegation rule into `R-CONCEPT`/`R-DELEGATION` (already there; one sentence added), rule 10 now defers to `R-BATCHING`. Core rules renumbered (delegation removed). Setup removes the `If TODO` line when done. Benefits: lower fixed context in every session; check in the next retro via `context-report.py` that moved rules still load.
- **Floor-relative context threshold:** `scripts/context-check.py` warns at the smallest of first-turn context + 40k, 100k and half the model's window (model read from the transcript; unknown model: 100k). Notice text and `R-BATCHING` now say when to continue instead of handing off. `context-report.py` also detects rule loads via `sed '/R-ID:START/...'`; `retro-metrics.sh --snapshot` no longer overwrites a same-day baseline. Benefits: projects with the context hook.

## 1.0.0
- **First stable release.** With the rename to STEM the kit's scope and name are settled. READMEs (EN/DE) redesigned: hero block with ASCII logo, badges and quick navigation, "Spec-driven development on steroids" positioning, three-step usage, workflow diagram (Task → Plan → Implement → Verify → Done → Reflect), collapsible file table. No rule changes; benefits: new users.

## 0.18.0
- **Renamed to STEM** (repository `Akku/stem`, tagline "Agentic Coding Starter Kit"; name after the AI in the film Upgrade). GitHub keeps the old links working (verified: ZIP, raw files and git); the update check additionally follows redirects (`curl -L`) as a precaution, so older projects keep working. The unzipped ZIP folder is now `stem-main`.

## 0.17.0
- **Context watchdog:** `scripts/context-check.py` as `UserPromptSubmit` hook (Claude Code) adds a notice to the agent's context above min(half window, 100k tokens) and every +30k; the agent finishes the task, writes the handoff and tells the user (with a ready sentence) to continue in a new session. Replaces the vague "~300 turns" rule in `R-BATCHING`; `AGENTS.md` rule 10 covers agents without the hook. Experiment entry updated (grade G1). Python 3 added as optional prerequisite in setup.

## 0.16.0
- **Evidence standard for cost-carrying rules only** (`AGENTS.md` content, default model/effort, session-length threshold, communication standard): entry in `docs/agent/EXPERIMENTS.md` *before* the change (hypothesis, metric, threshold, check date, confounders), baseline via `scripts/retro-metrics.sh --snapshot`, comparison per accepted task, one change at a time where practical, evidence grades G0-G3; "effective" only from G2, kit defaults need G3 or a mechanical reason. `retro-metrics.sh` normalises per accepted task and shows models and effort as confounders; `context-report.py` gained `--since` and `--brief`. Other changes keep the light ladder. Reason: observational data from small projects cannot show cause and effect.

## 0.15.0
- **AGENTS.md budget:** the kit self-check fails above 6 KB; the retro audits `AGENTS.md` every retro (would the agent get it wrong without the rule? evidence of use?); setup keeps it free of project overviews. Reason: a 2026 study found repository context files tend to raise cost and not improve success.
- **Security:** rule `R-SECURITY` (external text is data, secrets, least privilege, project files as attack path, optional sandbox); `permissions.deny` for `.env*`, `~/.ssh` and force-push; secret scan in the pre-commit hook; kit-update/promote-learning/retro treat fetched texts as untrusted; security note in the human guides. Benefits: all projects.

## 0.14.0
- **Design (hypotheses from one practitioner's talk, to be checked in the retro):** skill `design-alignment` (short, stoppable interview, one question at a time with recommendation); rule `R-DESIGN` (small steps with checks, deep modules, user owns interfaces, module map `docs/ARCHITECTURE.md`, optional glossary `docs/GLOSSARY.md`, TDD for logic-heavy code); design-health check at milestone completion; setup asks whether a glossary is wanted.
- **Retro evaluates optional/advanced practices every retro** (use deliberately, keep, remove) using usage evidence from `scripts/context-report.py` (rules loaded by ID, skills used). Benefits: all projects.

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
