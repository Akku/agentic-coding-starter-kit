#!/usr/bin/env bash
# Read-only session bootstrap: compact current-state summary. Changes nothing.
set -u
echo "## git"
if git rev-parse --git-dir >/dev/null 2>&1; then
  echo "branch: $(git branch --show-current)"
  echo "changes: $(git status --porcelain | wc -l | tr -d ' ') file(s)"
  git status --porcelain | head -10
  echo "recent commits:"; git log --oneline -5
else
  echo "no git repository"
fi
echo; echo "## backlog"
if command -v backlog >/dev/null 2>&1 && { [ -d backlog ] || [ -d .backlog ]; }; then
  echo "in progress:"; backlog task list -s "In Progress" --plain 2>/dev/null | head -15
  echo "ready (unblocked, to do):"; backlog task list -s "To Do" --ready --plain 2>/dev/null | head -10
else
  echo "backlog not initialised (run the project-setup skill)"
fi
echo; echo "## handoff"
if [ -f docs/agent/HANDOFF.md ]; then sed -n '1,40p' docs/agent/HANDOFF.md; else echo "no HANDOFF.md"; fi
echo; echo "Rules: see AGENTS.md; further rules by ID via docs/agent/OPERATING_MODEL.md"
