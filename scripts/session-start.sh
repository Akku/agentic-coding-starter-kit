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
    rv=$(curl -fsSL --max-time 3 "$raw" 2>/dev/null | sed -n 's/^version: *//p' | head -1)
    [ -n "$rv" ] && printf '%s\n' "$rv" >"$cache"
  fi
  rv=$(cat "$cache" 2>/dev/null)
  if [ -n "$rv" ] && [ -n "$lv" ] && [ "$rv" != "$lv" ] && [ "$(printf '%s\n%s\n' "$lv" "$rv" | sort -V | tail -1)" = "$rv" ]; then
    echo "KIT UPDATE AVAILABLE: $lv -> $rv (offer the kit-update skill; do not update unasked)"
  fi
else
  echo "no KIT_VERSION file"
fi
if [ -f .github/kit-check.py ] && command -v gh >/dev/null 2>&1; then
  # kit maintainer only (this file is removed from projects): incoming learnings
  prs=$(gh pr list --state open --limit 5 --json number,title,headRefName -q '.[]|"#\(.number) \(.headRefName): \(.title)"' 2>/dev/null)
  [ -n "$prs" ] && { echo "KIT MAINTAINER: open pull requests (review, merge or close):"; echo "$prs"; }
  lb=$(git ls-remote --heads origin 'learning/*' 2>/dev/null | sed 's#.*refs/heads/##' | head -5)
  [ -n "$lb" ] && { echo "learning branches on origin:"; echo "$lb"; }
fi
echo; echo "## backlog"
if command -v backlog >/dev/null 2>&1 && { [ -d backlog ] || [ -d .backlog ]; }; then
  echo "milestones:"; backlog milestone list --plain 2>/dev/null | sed -n '/^Active/,/^Completed/p' | grep -v '^Completed' | head -8
  echo "in progress:"; backlog task list -s "In Progress" --plain 2>/dev/null | head -15
  echo "ready (unblocked, to do):"; backlog task list -s "To Do" --ready --plain 2>/dev/null | head -10
else
  echo "backlog not initialised (follow SETUP.md)"
fi
echo; echo "## backlog check"; scripts/check-backlog.sh 2>/dev/null | head -10; [ "${PIPESTATUS[0]:-0}" -eq 0 ] && echo "ok"
echo; echo "## handoff"
if [ -f docs/agent/HANDOFF.md ]; then
  sed -n '1,40p' docs/agent/HANDOFF.md
  [ "$(wc -c < docs/agent/HANDOFF.md)" -gt 2048 ] && echo "WARNING: HANDOFF.md is over 2 KB: rewrite it from scratch (handoff skill); it is loaded every session"
else echo "no HANDOFF.md"; fi
echo; echo "Rules: see AGENTS.md; further rules by ID via docs/agent/OPERATING_MODEL.md"
