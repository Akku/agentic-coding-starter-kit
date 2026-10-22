#!/usr/bin/env bash
# Lists learnings worth promoting to STEM: rows of docs/agent/EXPERIMENTS.md and lines of docs/agent/NEXT_RETRO.md
# with grade G2 or higher, an "effective" result and no "promoted" mark. Prints nothing when there are none.
# Usage: scripts/promote-check.sh   (run at retro end, retro skill; mark promoted items with "promoted <PR link>")
set -u
exp=docs/agent/EXPERIMENTS.md; lrn=docs/agent/NEXT_RETRO.md
effective='(^|[^a-z])effective' ; not_effective='(not|in)[ -]?effective'
if [ -f "$exp" ]; then
  # table columns: | rule | hypothesis | metric | baseline | check by | confounders | result | grade |
  awk -F'|' -v ok="$effective" -v no="$not_effective" '
    /^\| / && $2 !~ /Rule \/ change|^ *-+ *$/ && NF >= 10 {
      res = tolower($8); gr = $9
      if (gr ~ /G[2-9]/ && res ~ ok && res !~ no && tolower($0) !~ /promoted/) { r = $2; gsub(/^ +| +$/, "", r); print "promote candidate: EXPERIMENTS.md: " substr(r, 1, 100) }
    }' "$exp"
fi
if [ -f "$lrn" ]; then
  grep -E '^- ' "$lrn" | grep -E '(^|[^A-Za-z0-9])G[2-9]([^0-9]|$)' | grep -i -E "$effective" | grep -v -i -E "$not_effective|promoted" \
    | cut -c1-100 | sed 's/^/promote candidate: NEXT_RETRO.md: /'
fi
exit 0
