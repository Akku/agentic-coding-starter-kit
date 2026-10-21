#!/usr/bin/env python3
"""Context watchdog for Claude Code (UserPromptSubmit hook). Prints a short notice into the agent's context when the
current context exceeds a threshold, then again every +30k. Threshold = smallest of: first-turn context of the session + 40k (the
fixed floor of system prompt, tools and instructions is not session growth), a cap of 100k (env CONTEXT_WARN_TOKENS) and half the model's
window (model read from the transcript; unknown model -> no window term, so the cap of 100k applies).
Reads the hook JSON from stdin (transcript_path, session_id); manual use: scripts/context-check.py --transcript FILE.
Silent and exit 0 on any problem or below the threshold. Numbers only, no transcript content is printed."""
import json, os, sys

CAP = int(os.environ.get("CONTEXT_WARN_TOKENS", "100000"))
GROWTH = 40000
STEP = 30000
WINDOW = 200000  # any claude-* model without a "[1m]" marker; other models: unknown

def usage_of(r):
    u = (r.get("message") or {}).get("usage") if r.get("type") == "assistant" and not r.get("isSidechain") else None
    return u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0) if u else None

def read_lines(path, tail):
    with open(path, "rb") as f:
        if tail: f.seek(0, 2); size = f.tell(); f.seek(max(0, size - 400000))
        else: return f.read(400000).decode("utf-8", "replace").splitlines()
        return f.read().decode("utf-8", "replace").splitlines()

def scan(path):
    """(current context = last assistant message, first-turn context = first assistant message, model of the last one)."""
    last, model = None, ""
    for line in reversed(read_lines(path, True)):
        try: r = json.loads(line)
        except ValueError: continue
        n = usage_of(r)
        if n is not None: last, model = n, str((r.get("message") or {}).get("model", "")); break
    first = None
    for line in read_lines(path, False):
        try: r = json.loads(line)
        except ValueError: continue
        first = usage_of(r)
        if first is not None: break
    return last or 0, first, model

def threshold(first, model):
    if "[1m]" in model: window = 1000000
    elif model.startswith("claude-"): window = WINDOW
    else: return CAP  # unknown model: window unknown, fixed cap
    return min([CAP, window // 2] + ([first + GROWTH] if first else []))

def main():
    args = sys.argv[1:]
    try:
        if "--transcript" in args:
            path, sid = args[args.index("--transcript") + 1], "manual"
        else:
            data = json.load(sys.stdin); path, sid = data.get("transcript_path", ""), str(data.get("session_id", "x"))
        tokens, first, model = scan(path)
        THRESHOLD = threshold(first, model)
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
    print("CONTEXT NOTICE (hook): the context holds about %dk tokens (threshold %dk, session started at %dk). %s" % (tokens // 1000, THRESHOLD // 1000, (first or 0) // 1000,
          "Recommend the switch to a new session now: write docs/agent/HANDOFF.md (handoff skill) and tell the user." if urgent else
          "Do not interrupt the current task. When it is finished, check: hand off only if at least ~5 turns of unrelated work are ahead; continue in this session if the rest is short, closely related (batch) or needs hard-won context. If handing off, as the last paragraph tell the user (in their language): the context is large, you wrote docs/agent/HANDOFF.md (handoff skill), and give a ready sentence to continue in a new session."))
    return 0

if __name__ == "__main__":
    sys.exit(main())
