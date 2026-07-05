#!/usr/bin/env python3
"""PostToolUse hook: log every Skill tool invocation to a local JSONL file.

Wire it in your Claude Code settings (e.g. ~/.claude/settings.json):

    {
      "hooks": {
        "PostToolUse": [
          {
            "matcher": "Skill",
            "hooks": [
              {
                "type": "command",
                "command": "python3 /path/to/ctxops/scripts/log_skill_invocation.py"
              }
            ]
          }
        ]
      }
    }

Logs ALL skill invocations (not just this plugin's) so usage share can be
computed. The log lives outside any repo so it never leaks into commits.
Always exits 0: a metrics hook must never break a session.
"""
import json
import os
import sys
import time

LOG_DIR = os.path.expanduser(os.environ.get("SKILL_METRICS_DIR", "~/.claude/skill-metrics"))
LOG_FILE = os.path.join(LOG_DIR, "invocations.jsonl")


def main() -> None:
    payload = json.load(sys.stdin)
    if payload.get("tool_name") != "Skill":
        return
    tool_input = payload.get("tool_input") or {}
    record = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "skill": tool_input.get("skill"),
        "cwd": payload.get("cwd"),
        "session_id": payload.get("session_id"),
    }
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(LOG_FILE, "a") as fh:
        fh.write(json.dumps(record) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
