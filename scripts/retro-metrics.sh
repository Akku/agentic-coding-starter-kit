#!/usr/bin/env bash
# Measured evidence for a retro (R-RETRO): cheap, repeatable numbers. Usage: scripts/retro-metrics.sh [since-date]  (default: 14 days)
set -u
cd "$(dirname "$0")/.."
# --snapshot: also store the output as a dated baseline (docs/agent/baselines/) before changing a cost-carrying rule.
if [ "${1:-}" = "--snapshot" ]; then
  shift; mkdir -p docs/agent/baselines; out="docs/agent/baselines/$(date +%F).txt"
  n=2; while [ -e "$out" ]; do out="docs/agent/baselines/$(date +%F)-$n.txt"; n=$((n+1)); done  # never overwrite an earlier baseline
  "$0" "$@" | tee "$out"; echo "baseline saved: $out"; exit 0
fi
# --repo PATH (repeatable): also count commits of another repository (e.g. the product repo of a STEM project).
repos=()
while [ "${1:-}" = "--repo" ]; do repos+=("$2"); shift 2; done
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
# Handoff overhead and untracked work: handoff commits and commits without a task ID (TASK-n / task n), per repository.
commit_stats() {  # $1 = repo path, $2 = label
  local all hand notask
  all=$(git -C "$1" log --since="$since 00:00" --format=%s | wc -l | tr -d ' ')
  hand=$(git -C "$1" log --since="$since 00:00" --format=%s | grep -ciE '^handoff|handoff update|; handoff' || true)
  notask=$(git -C "$1" log --since="$since 00:00" --format=%s | grep -vciE 'task[- ]?[0-9]' || true)
  echo "$2: $all commits, $hand handoff, $notask without task ID ($([ "$all" -gt 0 ] && echo $((100*notask/all)) || echo 0) %), fix/review $(git -C "$1" log --since="$since 00:00" --format=%s | grep -ciE 'fix|review' || true)"
}
commit_stats . "this repo"
for r in "${repos[@]+"${repos[@]}"}"; do commit_stats "$r" "repo $r"; done
if command -v gh >/dev/null 2>&1; then
  echo "CI runs since $since (conclusions):"; gh run list --limit 100 --json conclusion,createdAt --jq "[.[]|select(.createdAt>=\"$since\")]|group_by(.conclusion)|map({(.[0].conclusion):length})|add" 2>/dev/null | sed 's/^/  /'
fi
# Normalise by accepted work (Done tasks updated since the start date); absolute sums mislead when the amount of work differs.
done_p=0
for f in "${files[@]}"; do
  [ -f "$f" ] || continue
  grep -q '^status: Done' "$f" || continue
  u=$(awk -F"'" '/^updated_date:/{print substr($2,1,10); exit}' "$f")
  [ -n "$u" ] && [ "$u" \> "$since" -o "$u" = "$since" ] && done_p=$((done_p+1))
done
echo "accepted tasks in period (Done, updated since $since): $done_p"
py=""; for c in python3 python "py -3"; do $c -c "import sys; sys.exit(sys.version_info[0] < 3)" 2>/dev/null && { py=$c; break; }; done   # Windows: python3 is often a Store stub
if [ -f scripts/context-report.py ] && [ -n "$py" ]; then
  b=$($py scripts/context-report.py --since "$since" --brief 2>/dev/null | head -1)
  case "$b" in sessions=*)
    echo "usage: $b"
    t=$(echo "$b" | sed -n 's/.* turns=\([0-9]*\).*/\1/p'); c=$(echo "$b" | sed -n 's/.*cache_read=\([0-9]*\).*/\1/p')
    if [ "$done_p" -gt 0 ]; then echo "per accepted task: turns $((t/done_p)), cache_read $((c/done_p/1000))k tokens (small numbers of tasks: an indication, not proof)"; fi ;;
  *) echo "usage: not evaluable" ;;
  esac
fi
