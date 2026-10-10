# Process learnings (project-local inbox)

Read only during retrospectives (`R-RETRO`) or when investigating process efficiency. Format: `- [TASK-ID / YYYY-MM-DD] observation → possible improvement`. Handling and promotion rules: `docs/agent/PROCESS_IMPROVEMENTS.md`.

## Open observations

- [KIT / first retro] Adapter structure: three adapters (Codex, Claude, Copilot) are kept so the kit works with all of them. In the first retro check whether Codex/Copilot were really used and whether the neutrality caused overhead → simplify or keep.
- [KIT / first retro] Rule loading: were rules loaded by ID as intended, or did agents read whole files? Was `scripts/run.sh` actually used, and did it hide anything needed for diagnosis → adjust the wrapper or the instructions.
- [KIT / first retro] Rule inventory: which rules in `OPERATING_MODEL.md` were never loaded? → move to `ADVANCED.md` or delete.
