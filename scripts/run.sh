#!/usr/bin/env bash
# Compact-output wrapper: runs a command, keeps the full log outside the repo,
# prints only status, exit code, duration, a short tail and the log path.
# Usage: scripts/run.sh <label> <command> [args...]
# The wrapper exits with the ORIGINAL exit code of the command.
set -u
[ $# -ge 2 ] || { echo "usage: $0 <label> <command> [args...]" >&2; exit 2; }
label=$1; shift
logdir=${AGENT_LOG_DIR:-${TMPDIR:-/tmp}/agent-logs}
mkdir -p "$logdir"
log="$logdir/$(date +%Y%m%d-%H%M%S)-${label//[^A-Za-z0-9_-]/_}.log"
start=$(date +%s)
"$@" >"$log" 2>&1
code=$?
dur=$(( $(date +%s) - start ))
if [ "$code" -eq 0 ]; then status=PASS; else status=FAIL; fi
echo "status: $status"
echo "exit_code: $code"
echo "duration: ${dur}s"
echo "lines: $(wc -l <"$log" | tr -d ' ')"
echo "log: $log"
# Short hint for the summary line (test counts etc.); adapt per project.
grep -E -i -m3 '(passed|failed|tests?:|[0-9]+ (error|warning))' "$log" | sed 's/^/summary: /' || true
if [ "$code" -ne 0 ]; then
  echo "--- last 15 lines ---"
  tail -n 15 "$log"
fi
exit "$code"
