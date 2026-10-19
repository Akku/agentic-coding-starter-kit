#!/usr/bin/env python3
"""Kit self-check (kit maintenance only; removed from projects by SETUP.md).
Checks rule markers, rule index, script syntax, skill frontmatter, JSON and version consistency."""
import json, re, subprocess, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
errors = []
def err(m): errors.append(m)

# rules: markers balanced, index covers rules
for f in ("docs/agent/OPERATING_MODEL.md", "docs/agent/ADVANCED.md"):
    t = (root / f).read_text()
    starts = re.findall(r"<!-- RULE:(R-[A-Z-]+):START -->", t)
    ends = re.findall(r"<!-- RULE:(R-[A-Z-]+):END -->", t)
    if starts != ends: err(f"{f}: START/END markers differ")
    if len(set(starts)) != len(starts): err(f"{f}: duplicate rule IDs")
    idx = re.search(r"<!-- RULE:R-INDEX:START -->(.*?)<!-- RULE:R-INDEX:END -->", t, re.S)
    table = idx.group(1) if idx else re.search(r"\| Rule ID.*?\n\n", t, re.S).group(0)
    indexed = set(re.findall(r"\| `(R-[A-Z-]+)` \|", table))
    rules = set(starts) - {"R-INDEX"}
    if indexed != rules: err(f"{f}: index mismatch: {sorted(indexed ^ rules)}")

# shell scripts parse
for s in list((root / "scripts").glob("*.sh")) + [root / "scripts/githooks/pre-commit", root / ".github/bump-version.sh"]:
    if subprocess.run(["bash", "-n", str(s)]).returncode: err(f"{s.name}: bash syntax error")

for s in (root / "scripts").glob("*.py"):
    if subprocess.run([sys.executable, "-m", "py_compile", str(s)]).returncode: err(f"{s.name}: python syntax error")

# JSON
for j in (root / ".claude/settings.json",):
    try: json.loads(j.read_text())
    except Exception as e: err(f"{j.name}: {e}")

# skills/agents frontmatter
for d in (root / ".claude/skills").iterdir():
    m = re.match(r"---\nname: (.+)\ndescription: .+\n---", (d / "SKILL.md").read_text())
    if not m or m.group(1) != d.name: err(f"skill {d.name}: bad frontmatter/name")
for a in (root / ".claude/agents").glob("*.md"):
    if not re.match(r"---\n(?:.*\n)*?name: " + a.stem, a.read_text()): err(f"agent {a.name}: bad frontmatter/name")

# version consistency
v = re.search(r"^version: (\S+)", (root / "KIT_VERSION").read_text(), re.M).group(1)
for f in ("README.md", "README.de.md", "START_HERE.md", "STARTE_HIER.md"):
    if f"**Version {v}**" not in (root / f).read_text(): err(f"{f}: version != {v}")
if not re.search(r"^## " + re.escape(v) + r"$", (root / "CHANGELOG.md").read_text(), re.M): err(f"CHANGELOG.md: no entry for {v}")

# SETUP.md exists and the hidden paths it checks are really in the kit
if not (root / "SETUP.md").exists(): err("SETUP.md missing")
for pth in (".claude/skills", ".claude/settings.json", ".github", ".gitignore", "scripts/githooks/pre-commit"):
    if not (root / pth).exists(): err(f"{pth} missing (SETUP.md step 0 expects it)")

# AGENTS.md is loaded in every session: keep it within budget; settings deny secrets
if len((root / "AGENTS.md").read_bytes()) > 6144: err("AGENTS.md exceeds the 6 KB budget (move rules to OPERATING_MODEL.md)")
st = json.loads((root / ".claude/settings.json").read_text())
if "Read(./.env)" not in st.get("permissions", {}).get("deny", []): err("settings.json: deny rule for .env missing")

# skills listed in AGENTS.md exist
agents = (root / "AGENTS.md").read_text()
for d in (root / ".claude/skills").iterdir():
    if f"`{d.name}`" not in agents: err(f"AGENTS.md does not mention skill {d.name}")

print("\n".join(errors) if errors else f"kit-check OK (version {v})")
sys.exit(1 if errors else 0)
