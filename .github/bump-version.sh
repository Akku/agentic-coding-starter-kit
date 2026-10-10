#!/usr/bin/env bash
# Maintainer helper: set the kit version everywhere. Usage: .github/bump-version.sh 0.2.0
# Then: git commit, git tag v<version>, git push --follow-tags
set -eu
v=${1:?usage: $0 X.Y.Z}
sed -i.bak -E "s/^version: .*/version: $v/" KIT_VERSION
for f in README.md README.de.md START_HERE.md STARTE_HIER.md; do
  sed -i.bak -E "s/\*\*Version [0-9]+\.[0-9]+\.[0-9]+\*\*/**Version $v**/" "$f"
done
rm -f ./*.bak
grep -n "Version\|^version" KIT_VERSION README.md README.de.md START_HERE.md STARTE_HIER.md | head
