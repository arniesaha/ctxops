#!/usr/bin/env python3
"""Summarize skill invocations logged by log_skill_invocation.py.

Usage:
    python3 scripts/report_skill_usage.py [--days N] [--prefix ctxops]

Shows per-skill counts, share of total skill invocations, distinct
sessions and projects, split for the given prefix vs everything else.
"""
import argparse
import json
import os
import time
from collections import Counter, defaultdict

LOG_FILE = os.path.expanduser(
    os.path.join(os.environ.get("SKILL_METRICS_DIR", "~/.claude/skill-metrics"), "invocations.jsonl")
)


def load(days: int) -> list[dict]:
    if not os.path.exists(LOG_FILE):
        return []
    cutoff = time.time() - days * 86400
    rows = []
    with open(LOG_FILE) as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            try:
                ts = time.mktime(time.strptime(row.get("ts", "")[:19], "%Y-%m-%dT%H:%M:%S"))
            except ValueError:
                continue
            if ts >= cutoff:
                rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--prefix", default="ctxops",
                        help="comma-separated prefixes counted as this plugin's skills")
    args = parser.parse_args()

    rows = load(args.days)
    if not rows:
        print(f"no invocations logged in the last {args.days} days ({LOG_FILE})")
        return

    counts = Counter(r["skill"] for r in rows if r.get("skill"))
    sessions = defaultdict(set)
    projects = defaultdict(set)
    for r in rows:
        skill = r.get("skill")
        if not skill:
            continue
        if r.get("session_id"):
            sessions[skill].add(r["session_id"])
        if r.get("cwd"):
            projects[skill].add(r["cwd"])

    total = sum(counts.values())
    prefixes = tuple(p.strip() for p in args.prefix.split(","))
    matched = sum(n for s, n in counts.items() if s.startswith(prefixes))
    print(f"last {args.days} days: {total} skill invocations, "
          f"{matched} ({matched * 100 // max(total, 1)}%) match prefix(es) '{args.prefix}'\n")
    print(f"{'skill':<42} {'count':>5} {'sessions':>8} {'projects':>8}")
    for skill, n in counts.most_common():
        marker = "*" if skill.startswith(prefixes) else " "
        print(f"{marker} {skill:<40} {n:>5} {len(sessions[skill]):>8} {len(projects[skill]):>8}")
    print("\n* = matches prefix")


if __name__ == "__main__":
    main()
