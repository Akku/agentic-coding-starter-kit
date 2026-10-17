#!/usr/bin/env bash
# Measured evidence for a retro (R-RETRO): cheap, repeatable numbers. Usage: scripts/retro-metrics.sh [since-date]  (default: 14 days)
set -u
cd "$(dirname "$0")/.."
since=${1:-$(date -v-14d +%Y-%m-%d 2>/dev/null || date -d '14 days ago' +%Y-%m-%d)}
echo "== retro metrics since $since =="
files=(backlog/tasks/*.md)
done_n=$(grep -l '^status: Done' "${files[@]}" | wc -l | tr -d ' ')
open_n=$(grep -L '^status: Done' "${files[@]}" | wc -l | tr -d ' ')
echo "tasks: $done_n done, $open_n open"
echo "backlog check (Done with unchecked boxes or open dependencies):"; scripts/check-backlog.sh | sed 's/^/  /'; [ "${PIPESTATUS[0]}" -eq 0 ] && echo "  none"
learn=$(grep -l 'Learning' "${files[@]}" | wc -l | tr -d ' ')
echo "tasks with a Learning note: $learn"
echo "retro-created tasks still open:"
for f in "${files[@]}"; do
  grep -q '^status: Done' "$f" && continue
  grep -qi 'retro' "$f" && echo "  $(awk -F': ' '/^id:/{print $2; exit}' "$f") $(awk '/^title:/{ if ($0 ~ />-$/) {getline; sub(/^ +/, ""); print; exit} sub(/^title: /, ""); print; exit}' "$f")"
done
commits=$(git log --since="$since 00:00" --oneline | wc -l | tr -d ' ')
echo "commits: $commits"
read -r add del < <(git log --since="$since 00:00" --numstat --format= | awk '{a+=$1; d+=$2} END{print a+0, d+0}')
share=0; [ "${add:-0}" -gt 0 ] && share=$(( 100*del/add ))
echo "lines added/deleted: ${add:-0} / ${del:-0} (deleted share $share %; high values right after features point to rework)"
echo "review/fix commits (message contains fix or review): $(git log --since="$since 00:00" --oneline | grep -ciE 'fix|review')"
if command -v gh >/dev/null 2>&1; then
  echo "CI runs since $since (conclusions):"; gh run list --limit 100 --json conclusion,createdAt --jq "[.[]|select(.createdAt>=\"$since\")]|group_by(.conclusion)|map({(.[0].conclusion):length})|add" 2>/dev/null | sed 's/^/  /'
fi
