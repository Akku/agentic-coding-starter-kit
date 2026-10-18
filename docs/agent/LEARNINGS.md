# Process learnings (project-local inbox)

Read only during retrospectives (`R-RETRO`) or when investigating process efficiency. Format: `- [TASK-ID / YYYY-MM-DD] observation → possible improvement`. Handling and promotion rules: `docs/agent/PROCESS_IMPROVEMENTS.md`.

## Open observations

- [KIT / first retro] Adapter structure: three adapters (Codex, Claude, Copilot) are kept so the kit works with all of them. In the first retro check whether Codex/Copilot were really used and whether the neutrality caused overhead → simplify or keep.
- [KIT / first retro] Rule loading: were rules loaded by ID as intended, or did agents read whole files? Was `scripts/run.sh` actually used, and did it hide anything needed for diagnosis → adjust the wrapper or the instructions.
- [KIT / every retro] Skill discovery: check whether official or well-known skill collections and plugin marketplaces (e.g. the Anthropic skills repository, vendor plugin catalogs) now offer skills that fit this project (stack, testing, accessibility, design, release). Adopt only what has a concrete use; note source, license and version in the task or a notices file (`R-DECISION`).
- [KIT / first retro] UX designer agent: the kit now ships `.claude/agents/ux-designer.md` for projects with a UI. Was it used? Check especially the concept phase at the start (mockups and UX review before the first UI tasks) and later reviews of new screens → keep, adapt, or remove if it was never used.
- [KIT / first retro] Rule inventory: which rules in `OPERATING_MODEL.md` were never loaded? → move to `ADVANCED.md` or delete.
- [KIT / first retro] Session length: in one sample project (36 transcripts, ~6800 turns) three sessions of 1000-2000 turns caused ~80 % of cache-read tokens (avg ~360k carried tokens/turn); tool results were at most ~25 % (85 % of that Bash). Run `scripts/context-report.py`: do your sessions look similar? Did a fresh session at task/milestone boundaries (or ~300 turns) reduce cache-read per accepted task without hurting quality? → keep, tune or drop the threshold in `R-BATCHING`.
