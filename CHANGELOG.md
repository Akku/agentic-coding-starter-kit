# Changelog

Newest first. Projects read the entries newer than their `KIT_VERSION` (see `kit-update` skill). Each entry: what changed and who benefits.

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
