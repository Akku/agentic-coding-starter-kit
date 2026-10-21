# Experiments on cost-carrying rules

Read in retros only. Standard and evidence grades: `R-MEASUREMENT` ("Standard for cost-carrying rules", `docs/agent/ADVANCED.md`). One row per rule change that affects every session; fill it **before** the change, then update at the check date. Baselines: `scripts/retro-metrics.sh --snapshot` (stored in `docs/agent/baselines/`).

| Rule / change | Hypothesis | Metric (per accepted task) and threshold | Baseline | Check by | Confounders to note | Result | Grade |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Session length: hand off at task/milestone boundary or ~300 turns (`R-BATCHING`) | Fresh sessions lower cache-read per accepted task without more rework | cache_read per task down >= 25 %; fix/review commits not up | take at first retro | second retro | model, effort, task size, batching | open | G1 (one project, observational) |
| Default model: mid-tier at medium effort (`R-ROUTING`) | Enough for routine work, cheaper than the largest model | no rise in fix/review commits or user-reported rework; cost per task lower | take at first retro | second retro | task difficulty, escalations | open | G0 (maintainer experience) |
| `AGENTS.md` budget 6 KB and per-rule audit (retro step) | A smaller `AGENTS.md` does not lower quality and lowers cost per task | turns and cache_read per task not up; rule violations not up | take before first pruning | after pruning | task mix, other rule changes | open | G0 (external study: tendency) |
| Communication standard (explanations, summaries, links) | Costs little context; improves user's understanding | cache_read per task change < 5 %; user rating in retro | take at first retro | first retro | verbosity creep | open | G0 |

<!-- New entries above this line. -->
