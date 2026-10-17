#!/usr/bin/env bash
# Read-only session bootstrap: compact current-state summary. Changes nothing.
set -u
echo "## git"
if git rev-parse --git-dir >/dev/null 2>&1; then
  echo "branch: $(git branch --show-current)"
  [ "$(git config core.hooksPath)" = "scripts/githooks" ] || echo "WARNING: pre-commit guard inactive -> git config core.hooksPath scripts/githooks"
  echo "changes: $(git status --porcelain | wc -l | tr -d ' ') file(s)"
  git status --porcelain | head -10
  echo "recent commits:"; git log --oneline -5
else
  echo "no git repository"
fi
echo; echo "## kit"
if [ -f KIT_VERSION ]; then
  lv=$(sed -n 's/^version: *//p' KIT_VERSION | head -1); repo=$(sed -n 's/^repo: *//p' KIT_VERSION | head -1)
  echo "kit version: ${lv:-unknown}"
  cache="${TMPDIR:-/tmp}/agent-logs/kit-check-$(printf %s "$PWD" | cksum | cut -d' ' -f1)"; mkdir -p "$(dirname "$cache")"
  if [ -n "$repo" ] && command -v curl >/dev/null 2>&1 && { [ ! -f "$cache" ] || [ -n "$(find "$cache" -mtime +0 2>/dev/null)" ]; }; then
    raw="${repo/github.com/raw.githubusercontent.com}/main/KIT_VERSION"
    rv=$(curl -fsS --max-time 3 "$raw" 2>/dev/null | sed -n 's/^version: *//p' | head -1)
    [ -n "$rv" ] && printf '%s\n' "$rv" >"$cache"
  fi
  rv=$(cat "$cache" 2>/dev/null)
  if [ -n "$rv" ] && [ -n "$lv" ] && [ "$rv" != "$lv" ] && [ "$(printf '%s\n%s\n' "$lv" "$rv" | sort -V | tail -1)" = "$rv" ]; then
    echo "KIT UPDATE AVAILABLE: $lv -> $rv (offer the kit-update skill; do not update unasked)"
  fi
else
  echo "no KIT_VERSION file"
fi
echo; echo "## backlog"
if command -v backlog >/dev/null 2>&1 && { [ -d backlog ] || [ -d .backlog ]; }; then
  echo "milestones:"; backlog milestone list --plain 2>/dev/null | sed -n '/^Active/,/^Completed/p' | grep -v '^Completed' | head -8
  echo "in progress:"; backlog task list -s "In Progress" --plain 2>/dev/null | head -15
  echo "ready (unblocked, to do):"; backlog task list -s "To Do" --ready --plain 2>/dev/null | head -10
else
  echo "backlog not initialised (run the project-setup skill)"
fi
echo; echo "## handoff"
if [ -f docs/agent/HANDOFF.md ]; then sed -n '1,40p' docs/agent/HANDOFF.md; else echo "no HANDOFF.md"; fi
echo; echo "Rules: see AGENTS.md; further rules by ID via docs/agent/OPERATING_MODEL.md"
