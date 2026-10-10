# Process Improvement Inbox

Purpose: keep a small **project-local** set of observations that may justify a future change to this project's agentic-development process.

This file is NOT part of normal task context. Read it during retrospectives or when explicitly investigating process efficiency. It is not itself a cross-project knowledge base.

## Capture rule

Prefer recording an observation first where its evidence naturally lives, for example in the current Backlog.md task's Implementation Notes:

```text
Learning: <observation> → <possible improvement or question>
```

Do not require a learning note after every task.

Promote an observation into this inbox only when it appears reusable across tasks, repeated, unusually costly, or surprisingly effective. Do not duplicate every task-local learning here.

Typical candidates:

- repeated manual work;
- repeated review findings;
- context that is hard to discover;
- missing/flaky verification;
- excessive or repeated command output entering model context;
- duplicated or drifting rules;
- a batching decision that worked especially well or badly;
- a candidate automation;
- an agent/tool whose overhead appears disproportionate;
- a test/evaluation whose proof boundary was misunderstood.

## Open observations

<!-- Minimal format:
- [TASK-123 / BATCH-X / YYYY-MM-DD] Observation → possible improvement or question
-->

## Retro handling

During a retrospective, classify useful observations as:

- **Adopt** — implement the improvement or create the appropriate Backlog.md task.
- **Experiment** — gather narrowly scoped evidence before deciding.
- **Defer** — keep only while the question remains relevant.
- **Discard** — remove; it did not generalize or is no longer useful.
- **Promote** — copy the generalized pattern, with evidence and applicability limits, into the shared cross-project pattern library.

For adopted measures, keep implementation and demonstrated effectiveness separate. Define an observable success criterion for a future retro.

Resolved observations should be removed or archived so this inbox stays small.

## Cross-project promotion

Learnings intended for other projects go into the kit repository (this template) via pull request, e.g. into `docs/agent/PITFALLS.md` or `OPERATING_MODEL.md`. Do not export raw observations automatically. A promoted pattern should state:

- generalized problem;
- recommended pattern;
- when it applies;
- when it does not apply;
- evidence/source projects;
- confidence or validation status.
