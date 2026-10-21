#!/usr/bin/env python3
"""Context watchdog for Claude Code (UserPromptSubmit hook). Prints a short notice into the agent's context when the
current context exceeds a threshold (default 100k tokens, env CONTEXT_WARN_TOKENS), then again every +30k.
Reads the hook JSON from stdin (transcript_path, session_id); manual use: scripts/context-check.py --transcript FILE.
Silent and exit 0 on any problem or below the threshold. Numbers only, no transcript content is printed."""
import json, os, sys

THRESHOLD = int(os.environ.get("CONTEXT_WARN_TOKENS", "100000"))
STEP = 30000

def current_context(path):
    """Context size of the last assistant message: fresh input + cache read + cache write tokens."""
    with open(path, "rb") as f:
        f.seek(0, 2); size = f.tell(); f.seek(max(0, size - 400000))
        lines = f.read().decode("utf-8", "replace").splitlines()
    for line in reversed(lines):
        try: r = json.loads(line)
        except ValueError: continue
        u = (r.get("message") or {}).get("usage") if r.get("type") == "assistant" and not r.get("isSidechain") else None
        if u: return u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
    return 0

def main():
    args = sys.argv[1:]
    try:
        if "--transcript" in args:
            path, sid = args[args.index("--transcript") + 1], "manual"
        else:
            data = json.load(sys.stdin); path, sid = data.get("transcript_path", ""), str(data.get("session_id", "x"))
        tokens = current_context(path)
    except Exception:
        return 0
    if tokens < THRESHOLD: return 0
    state = os.path.join(os.environ.get("TMPDIR", "/tmp"), "agent-logs", "ctx-" + "".join(c for c in sid if c.isalnum())[:40])
    last = 0
    try: last = int(open(state).read().strip() or 0)
    except Exception: pass
    if "--transcript" not in args and last and tokens < last + STEP: return 0
    try:
        os.makedirs(os.path.dirname(state), exist_ok=True); open(state, "w").write(str(tokens))
    except Exception: pass
    urgent = tokens >= THRESHOLD * 1.5
    print("CONTEXT NOTICE (hook): the context holds about %dk tokens (threshold %dk). %s" % (tokens // 1000, THRESHOLD // 1000,
          "Recommend the switch to a new session now: write docs/agent/HANDOFF.md (handoff skill) and tell the user." if urgent else
          "Do not interrupt the current task. When it is finished, as the last paragraph tell the user (in their language): the context is large, you wrote docs/agent/HANDOFF.md (handoff skill), and give a ready sentence to continue in a new session."))
    return 0

if __name__ == "__main__":
    sys.exit(main())
