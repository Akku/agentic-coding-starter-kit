#!/usr/bin/env python3
"""Fixture tests for the kit scripts (kit maintenance only; run by kit-check.py or directly: python3 .github/tests/test_scripts.py).
Each test builds its own sandbox repository or transcript folder in a temp dir, so nothing depends on the real project."""
import json, os, pathlib, shutil, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SCRIPTS = ROOT / "scripts"
GIT_ENV = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}


def run(cmd, cwd, env=None, stdin=None):
    e = dict(os.environ, **GIT_ENV, **(env or {}))
    return subprocess.run(cmd, cwd=cwd, env=e, input=stdin, capture_output=True, text=True)


def assistant(model, tokens, sidechain=False, content=None, ts="2026-10-20T10:00:00Z"):
    return {"type": "assistant", "timestamp": ts, "isSidechain": sidechain,
            "message": {"model": model, "content": content or [], "usage": {"input_tokens": tokens, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0, "output_tokens": 10}}}


def write_jsonl(path, records):
    path.write_text("\n".join(json.dumps(r) for r in records) + "\n")


class Sandbox(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)


class ContextCheck(Sandbox):
    def check(self, records, env=None):
        t = self.tmp / "t.jsonl"; write_jsonl(t, records)
        return run([sys.executable, str(SCRIPTS / "context-check.py"), "--transcript", str(t)], self.tmp, {"TMPDIR": str(self.tmp), **(env or {})})

    def test_silent_below_threshold(self):
        r = self.check([assistant("claude-sonnet-5-5", 10000), assistant("claude-sonnet-5-5", 30000)])
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_notice_above_floor_relative_threshold(self):
        # first turn 10k -> threshold 50k; current 60k
        r = self.check([assistant("claude-sonnet-5-5", 10000), assistant("claude-sonnet-5-5", 60000)])
        self.assertIn("CONTEXT NOTICE", r.stdout)
        self.assertIn("threshold 50k", r.stdout)

    def test_subagent_records_are_ignored(self):
        r = self.check([assistant("claude-sonnet-5-5", 10000), assistant("claude-sonnet-5-5", 190000, sidechain=True)])
        self.assertEqual(r.stdout, "")

    def test_unknown_model_uses_cap(self):
        low = self.check([assistant("other-model", 80000), assistant("other-model", 90000)])
        high = self.check([assistant("other-model", 80000), assistant("other-model", 110000)], env={"CONTEXT_WARN_TOKENS": "100000"})
        self.assertEqual(low.stdout, "")
        self.assertIn("threshold 100k", high.stdout)

    def test_bad_input_is_silent(self):
        r = run([sys.executable, str(SCRIPTS / "context-check.py"), "--transcript", str(self.tmp / "missing.jsonl")], self.tmp, {"TMPDIR": str(self.tmp)})
        self.assertEqual((r.returncode, r.stdout), (0, ""))
        r = run([sys.executable, str(SCRIPTS / "context-check.py")], self.tmp, {"TMPDIR": str(self.tmp)}, stdin="not json")
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_hook_mode_repeats_only_after_step(self):
        t = self.tmp / "t.jsonl"; write_jsonl(t, [assistant("claude-sonnet-5-5", 10000), assistant("claude-sonnet-5-5", 60000)])
        hook = lambda: run([sys.executable, str(SCRIPTS / "context-check.py")], self.tmp, {"TMPDIR": str(self.tmp)}, stdin=json.dumps({"transcript_path": str(t), "session_id": "s1"})).stdout
        self.assertIn("CONTEXT NOTICE", hook())
        self.assertEqual(hook(), "")  # same size: no second notice


class ContextReport(Sandbox):
    def report(self, records, *args, cwd=None):
        d = self.tmp / "transcripts"; d.mkdir(exist_ok=True)
        write_jsonl(d / "abcdef12-session.jsonl", records)
        return run([sys.executable, str(SCRIPTS / "context-report.py"), *args, str(d)], cwd or self.tmp)

    def test_empty_folder_not_evaluable(self):
        d = self.tmp / "none"; d.mkdir()
        self.assertIn("not evaluable", run([sys.executable, str(SCRIPTS / "context-report.py"), str(d)], self.tmp).stdout)

    def test_brief_counts_turns_and_models(self):
        r = self.report([assistant("claude-sonnet-5-5", 1000), assistant("claude-sonnet-5-5", 2000)], "--brief")
        self.assertIn("sessions=1 turns=2", r.stdout)
        self.assertIn("models=claude-sonnet-5-5", r.stdout)

    def test_since_filters_old_records(self):
        r = self.report([assistant("claude-sonnet-5-5", 1000, ts="2026-01-01T00:00:00Z")], "--brief", "--since", "2026-06-01")
        self.assertIn("not evaluable", r.stdout)

    def test_rule_load_via_sed_and_skill_read_are_detected(self):
        cmd = "ID=R-VERIFY; sed -n \"/<!-- RULE:${ID}:START -->/,/<!-- RULE:${ID}:END -->/p\" docs/agent/OPERATING_MODEL.md"
        sed_only = "sed -n '/<!-- RULE:R-REVIEW:START -->/,/<!-- RULE:R-REVIEW:END -->/p' docs/agent/OPERATING_MODEL.md"
        recs = [assistant("claude-sonnet-5-5", 1000, content=[
            {"type": "tool_use", "id": "1", "name": "Bash", "input": {"command": cmd}},
            {"type": "tool_use", "id": "2", "name": "Bash", "input": {"command": sed_only}},
            {"type": "tool_use", "id": "3", "name": "Read", "input": {"file_path": "/p/.claude/skills/retro/SKILL.md"}}])]
        r = self.report(recs)
        self.assertIn("'R-VERIFY': 1", r.stdout)
        self.assertIn("'R-REVIEW': 1", r.stdout)
        self.assertIn("'retro': 1", r.stdout)


class SandboxRepo(Sandbox):
    """A project folder with the kit scripts, a git repository and a few backlog tasks."""
    def setUp(self):
        super().setUp()
        self.repo = self.tmp / "proj"
        shutil.copytree(SCRIPTS, self.repo / "scripts", ignore=shutil.ignore_patterns("__pycache__", "local"))
        (self.repo / "backlog/tasks").mkdir(parents=True)
        run(["git", "init", "-q", "-b", "main"], self.repo)
        self.nogh = self.tmp / "bin"; self.nogh.mkdir()  # stub: no network calls from tests
        (self.nogh / "gh").write_text("#!/bin/sh\nexit 1\n"); (self.nogh / "gh").chmod(0o755)
        self.env = {"PATH": f"{self.nogh}{os.pathsep}{os.environ['PATH']}", "TMPDIR": str(self.tmp)}

    def task(self, n, status="Done", updated="2026-10-20 10:00", extra=""):
        (self.repo / f"backlog/tasks/task-{n} - T{n}.md").write_text(
            f"---\nid: TASK-{n}\ntitle: T{n}\nstatus: {status}\ncreated_date: '2026-10-01 10:00'\nupdated_date: '{updated}'\nlabels: []\n---\n\n{extra}\n")

    def commit(self, msg):
        run(["git", "add", "-A"], self.repo); return run(["git", "commit", "-qm", msg], self.repo)


class RetroMetrics(SandboxRepo):
    def test_snapshot_never_overwrites_same_day_baseline(self):
        self.task(1); self.commit("TASK-1 done")
        for _ in range(2): run(["bash", "scripts/retro-metrics.sh", "--snapshot", "2000-01-01"], self.repo, self.env)
        self.assertEqual(len(list((self.repo / "docs/agent/baselines").glob("*.txt"))), 2)

    def test_counts_tasks_and_untracked_commits(self):
        self.task(1); self.task(2, status="To Do"); self.commit("TASK-1 done")
        (self.repo / "x.txt").write_text("x"); self.commit("quick fix without id")
        out = run(["bash", "scripts/retro-metrics.sh", "2000-01-01"], self.repo, self.env).stdout
        self.assertIn("tasks: 1 done, 1 open", out)
        self.assertRegex(out, r"this repo: 2 commits, 0 handoff, 1 without task ID \(50 %\)")

    def test_repo_option_adds_second_repository(self):
        self.task(1); self.commit("TASK-1 done")
        other = self.tmp / "product"; other.mkdir(); run(["git", "init", "-q", "-b", "main"], other)
        (other / "a").write_text("a"); run(["git", "add", "-A"], other); run(["git", "commit", "-qm", "Handoff update"], other)
        out = run(["bash", "scripts/retro-metrics.sh", "--repo", str(other), "2000-01-01"], self.repo, self.env).stdout
        self.assertRegex(out, r"repo .*product: 1 commits, 1 handoff, 1 without task ID")

    def test_duplicate_ids_reported_by_backlog_check(self):
        self.task(1); (self.repo / "backlog/tasks/task-1 - copy.md").write_text((self.repo / "backlog/tasks/task-1 - T1.md").read_text())
        r = run(["bash", "scripts/check-backlog.sh"], self.repo, self.env)
        self.assertEqual(r.returncode, 1)
        self.assertIn("duplicate task id: task-1", r.stdout)


class SessionStart(SandboxRepo):
    def start(self, extra_env=None):
        return run(["bash", "scripts/session-start.sh"], self.repo, {**self.env, **(extra_env or {})}).stdout

    def test_summary_sections_without_backlog_cli_state(self):
        (self.repo / "KIT_VERSION").write_text("version: 1.0.0\n"); self.commit("init")
        out = self.start()
        for s in ("## git", "branch: main", "kit version: 1.0.0", "WARNING: pre-commit guard inactive", "## handoff", "no HANDOFF.md"):
            self.assertIn(s, out)

    def test_oversized_handoff_warns(self):
        (self.repo / "docs/agent").mkdir(parents=True); (self.repo / "docs/agent/HANDOFF.md").write_text("x" * 3000)
        self.assertIn("HANDOFF.md is over 2 KB", self.start())

    def test_retro_due_after_threshold_and_cleared_by_retro_notes(self):
        for n in (1, 2, 3): self.task(n)
        self.assertIn("RETRO DUE: 3 tasks done", self.start({"RETRO_DUE_AFTER": "3"}))
        self.assertNotIn("RETRO DUE", self.start({"RETRO_DUE_AFTER": "4"}))
        (self.repo / "docs/agent/retros").mkdir(parents=True); (self.repo / "docs/agent/retros/2026-10-25.md").write_text("retro\n")
        self.assertNotIn("RETRO DUE", self.start({"RETRO_DUE_AFTER": "3"}))  # all tasks older than the retro

    def test_check_backlog_problem_is_shown(self):
        self.task(1, extra="- [ ] #1 open box")
        self.assertIn("TASK-1: Done with 1 unchecked box", self.start())


if __name__ == "__main__":
    unittest.main(verbosity=1)
