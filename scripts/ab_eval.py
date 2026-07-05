#!/usr/bin/env python3
"""Skill-on vs. skill-off A/B eval with a blind judge.

For each eval in evals/ctxops-evals.json, runs the prompt twice through
`claude -p` (one arm follows the SKILL.md, one gets only the task), then a
judge scores both blind against the eval's expected rubric. Arm-to-label
assignment alternates per eval to cancel position bias.

Requires the `claude` CLI on PATH. Each eval costs three model calls, so a
full run over 7 evals is 21 calls; use --skill to run a subset. Results are
written to evals/ab-results-<date>.json and printed as a table.

Usage:
    python3 scripts/ab_eval.py [--skill NAME ...] [--model MODEL] [--dry-run]
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GEN_LIMIT = "Keep the deliverable under 600 words. Reply with only the deliverable."


def run_claude(prompt: str, model: str | None, dry: bool) -> str:
    cmd = ["claude", "-p", prompt, "--output-format", "text"]
    if model:
        cmd += ["--model", model]
    if dry:
        print(f"  would run: claude -p <{len(prompt)} chars>")
        return ""
    out = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, timeout=600)
    if out.returncode != 0:
        sys.exit(f"claude -p failed: {out.stderr[:500]}")
    return out.stdout.strip()


def judge_prompt(task: str, rubric: list, a: str, b: str) -> str:
    items = "\n".join(f"{i+1}. {r}" for i, r in enumerate(rubric))
    return (
        "You are a blind grader. Two anonymous responses answer this task:\n"
        f'"{task}"\n\nRubric (score each item 0 to 2 per response, plus one overall '
        "0 to 2 item: could the reader act on this directly?):\n"
        f"{items}\n\nResponse A:\n<<<\n{a}\n>>>\n\nResponse B:\n<<<\n{b}\n>>>\n\n"
        "Do not speculate about how either response was produced. Return ONLY JSON: "
        '{"a_score": <int>, "b_score": <int>, "winner": "A"|"B"|"tie", "note": "<one sentence>"}'
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", action="append", help="limit to these skill names (repeatable)")
    parser.add_argument("--model", help="model override passed to claude -p")
    parser.add_argument("--dry-run", action="store_true", help="print planned calls without running them")
    args = parser.parse_args()

    evals = json.loads((ROOT / "evals/ctxops-evals.json").read_text())["evals"]
    if args.skill:
        evals = [e for e in evals if e["skill"] in set(args.skill)]
    if not evals:
        sys.exit("no matching evals")

    results = []
    for i, ev in enumerate(evals):
        name, task, rubric = ev["skill"], ev["prompt"], ev["expected"]
        skill_dir = next((d for d in ("skills", "incubating") if (ROOT / d / name / "SKILL.md").exists()), None)
        if skill_dir is None:
            print(f"skip {name}: no SKILL.md found")
            continue
        skill_md = (ROOT / skill_dir / name / "SKILL.md").read_text()
        print(f"[{i+1}/{len(evals)}] {name}")

        on = run_claude(
            f"You are working in this repo. Follow this skill exactly:\n\n{skill_md}\n\nTask: {task}\n{GEN_LIMIT}",
            args.model, args.dry_run)
        off = run_claude(
            f"You are working in this repo. Task: {task}\nApproach it however you see fit. {GEN_LIMIT}",
            args.model, args.dry_run)
        if args.dry_run:
            print("  would run: judge")
            continue

        # alternate which arm is labeled A to cancel position bias
        a, b = (on, off) if i % 2 == 0 else (off, on)
        raw = run_claude(judge_prompt(task, rubric, a, b), args.model, False)
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if not match:
            print(f"  judge returned no JSON, skipping: {raw[:200]}")
            continue
        verdict = json.loads(match.group())
        on_label = "A" if i % 2 == 0 else "B"
        winner = verdict["winner"]
        outcome = "tie" if winner == "tie" else ("skill-on" if winner == on_label else "skill-off")
        on_score = verdict["a_score"] if on_label == "A" else verdict["b_score"]
        off_score = verdict["b_score"] if on_label == "A" else verdict["a_score"]
        results.append({"skill": name, "on": on_score, "off": off_score,
                        "outcome": outcome, "note": verdict.get("note", "")})
        print(f"  on={on_score} off={off_score} -> {outcome}")

    if args.dry_run or not results:
        return
    out_path = ROOT / f"evals/ab-results-{date.today().isoformat()}.json"
    out_path.write_text(json.dumps(results, indent=2) + "\n")
    wins = sum(r["outcome"] == "skill-on" for r in results)
    ties = sum(r["outcome"] == "tie" for r in results)
    losses = sum(r["outcome"] == "skill-off" for r in results)
    print(f"\nskill-on: {wins} wins, {ties} ties, {losses} losses  -> {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
