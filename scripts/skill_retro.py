#!/usr/bin/env python3
"""Local value audit: was each skill invocation's output actually used?

Reads the invocation log written by log_skill_invocation.py, finds each
session transcript under ~/.claude/projects/, and inspects the window of
events after every matching skill invocation. Classifies each invocation:

  adopted    output visibly used downstream (posted, saved, committed)
  adapted    used, but the user first asked for meaningful changes
  unclear    heuristics found no signal; review the window yourself

Heuristics are conservative and everything stays on this machine. For a
sharper pass, run with --windows-dir and have your agent read the digests
and classify them (that is exactly how the maintainer audit was done).

Usage:
    python3 scripts/skill_retro.py [--days 30] [--prefix ctxops]
                                   [--windows-dir DIR] [--window 300]
"""
import argparse
import glob
import json
import os
import time

LOG_FILE = os.path.expanduser(
    os.path.join(os.environ.get("SKILL_METRICS_DIR", "~/.claude/skill-metrics"), "invocations.jsonl")
)

ADOPTION_TOOLS = (
    "slack_send", "save_issue", "save_comment", "save_document", "save_project",
    "save_status_update", "save_milestone", "createJira", "editJira",
    "addComment", "createConfluence", "Write", "Edit",
)
REWORK_MARKERS = (
    "rewrite", "redo", "instead", "don't include", "do not include", "too technical",
    "not what i", "that's wrong", "change this", "keep it non-technical", "tighter",
)


def load_invocations(days: int, prefixes: tuple) -> list:
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
            skill = row.get("skill") or ""
            if not skill.startswith(prefixes):
                continue
            try:
                ts = time.mktime(time.strptime(row.get("ts", "")[:19], "%Y-%m-%dT%H:%M:%S"))
            except ValueError:
                continue
            if ts >= cutoff:
                rows.append(row)
    return rows


def find_transcript(row: dict):
    proj = (row.get("cwd") or "").replace("/", "-")
    matches = glob.glob(os.path.expanduser(f"~/.claude/projects/{proj}/{row['session_id']}*.jsonl"))
    return matches[0] if matches else None


def event_blocks(event: dict):
    msg = event.get("message") or {}
    content = msg.get("content")
    if isinstance(content, str):
        content = [{"type": "text", "text": content}]
    for block in content or []:
        if isinstance(block, dict):
            yield msg.get("role") or event.get("type"), block


def classify(events: list, skill: str, window: int):
    start = None
    for i, ev in enumerate(events):
        for _, block in event_blocks(ev):
            if block.get("type") == "tool_use" and block.get("name") == "Skill" \
                    and (block.get("input") or {}).get("skill") == skill:
                start = i
        if start is not None:
            break
    if start is None:
        return "unclear", "skill invocation not found in transcript"

    adopted_evidence = None
    rework_evidence = None
    for ev in events[start: start + window]:
        for role, block in event_blocks(ev):
            if block.get("type") == "tool_use" and any(k in (block.get("name") or "") for k in ADOPTION_TOOLS):
                adopted_evidence = adopted_evidence or block.get("name")
            if role == "user" and block.get("type") == "text":
                text = (block.get("text") or "").lower()
                # skill-launch injection carries SKILL.md content as a user
                # message; it is not user feedback
                if "base directory for this skill" in text:
                    continue
                for m in REWORK_MARKERS:
                    idx = text.find(m)
                    if idx >= 0:
                        rework_evidence = rework_evidence or text[max(0, idx - 30): idx + 50]
                        break
    if adopted_evidence and rework_evidence:
        return "adapted", f"rework requested ('{rework_evidence}') then used via {adopted_evidence}"
    if adopted_evidence:
        return "adopted", f"downstream use via {adopted_evidence}"
    if rework_evidence:
        return "adapted", f"rework requested: '{rework_evidence}'"
    return "unclear", "no adoption or rework signal in window"


def dump_window(events, skill, window, path):
    start = 0
    for i, ev in enumerate(events):
        for _, block in event_blocks(ev):
            if block.get("type") == "tool_use" and block.get("name") == "Skill" \
                    and (block.get("input") or {}).get("skill") == skill:
                start = i
    with open(path, "w") as out:
        for ev in events[start: start + window]:
            for role, block in event_blocks(ev):
                if block.get("type") == "text" and (block.get("text") or "").strip():
                    out.write(f"[{role} text] {block['text'][:900]}\n")
                elif block.get("type") == "tool_use":
                    out.write(f"[tool_use {block.get('name')}] {json.dumps(block.get('input', {}))[:300]}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--prefix", default="ctxops",
                        help="comma-separated skill-name prefixes to audit")
    parser.add_argument("--window", type=int, default=300, help="events to inspect after each invocation")
    parser.add_argument("--windows-dir", help="also dump a readable digest per invocation for agent/human review")
    args = parser.parse_args()

    prefixes = tuple(p.strip() for p in args.prefix.split(","))
    rows = load_invocations(args.days, prefixes)
    if not rows:
        print(f"no matching invocations in the last {args.days} days ({LOG_FILE})")
        return
    if args.windows_dir:
        os.makedirs(args.windows_dir, exist_ok=True)

    totals = {"adopted": 0, "adapted": 0, "unclear": 0, "missing": 0}
    print(f"{'date':<12} {'skill':<28} {'verdict':<9} evidence")
    for n, row in enumerate(rows, 1):
        transcript = find_transcript(row)
        label = row["skill"]
        if not transcript:
            totals["missing"] += 1
            print(f"{row['ts'][:10]:<12} {label:<28} {'missing':<9} transcript not on disk")
            continue
        events = []
        with open(transcript) as fh:
            for line in fh:
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        verdict, evidence = classify(events, row["skill"], args.window)
        totals[verdict] += 1
        print(f"{row['ts'][:10]:<12} {label:<28} {verdict:<9} {evidence}")
        if args.windows_dir:
            dump_window(events, row["skill"], args.window,
                        os.path.join(args.windows_dir, f"{n:02d}_{row['ts'][:10]}_{label}.txt"))

    audited = sum(v for k, v in totals.items() if k != "missing")
    print(f"\n{audited} audited: {totals['adopted']} adopted, {totals['adapted']} adapted, "
          f"{totals['unclear']} unclear ({totals['missing']} missing transcripts)")
    print("aggregates above are safe to share; transcripts and windows never leave this machine")


if __name__ == "__main__":
    main()
