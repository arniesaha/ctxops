# Dogfood Guide

Use ctxops on real project work before polishing it for public release.

## How To Use It

1. Pick a live task, not a toy prompt.
2. Choose the smallest useful skill chain.
3. Save private outputs in `local/` so they stay out of git.
4. After the task, write a short note with:
   - project
   - task
   - skills used
   - what improved
   - what was noisy
   - what should change

## Suggested Chains

### Resume a Project

Use `project-briefing`.

Good for: opening a repo after time away, onboarding an agent, preparing a handoff.

Expected output: current status, risks, verification commands, and next action.

### Make a Direction Call

Use `ctx-pack` -> `decision-review`.

Good for: architecture choice, project direction, whether to build a feature, whether to publish an artifact.

Expected output: a clear recommendation and the cheapest evidence-producing test.

### Prepare Something Public

Use `ctx-pack` -> `artifact-packager`.

Good for: README, case study, blog draft, launch page, demo script.

Expected output: useful artifact plus privacy checklist.

## Measuring Adoption

Skill descriptions only matter if they change invocation behavior. Measure, don't recall:

1. Wire the logging hook into your Claude Code settings (user-level `settings.json`):

```json
"hooks": {
  "PostToolUse": [
    {
      "matcher": "Skill",
      "hooks": [
        { "type": "command", "command": "python3 /path/to/ctxops/scripts/log_skill_invocation.py" }
      ]
    }
  ]
}
```

2. Work normally for a week or two.
3. Run `python3 scripts/report_skill_usage.py --days 14` to see per-skill counts, session and project spread, and ctxops' share of all skill invocations.

A skill with zero invocations across two weeks of fitting work has a description problem, an overlap problem, or no reason to exist. Fix or cut.

## Feedback Loop

The improvement cycle, end to end. All measurement is local; sharing is opt-in and aggregate-only.

1. **Measure**: the hook logs invocations; `scripts/report_skill_usage.py` shows adoption and share.
2. **Audit value**: `scripts/skill_retro.py` classifies each invocation as adopted, adapted, or unclear from your local transcripts. Use `--windows-dir` to dump digests your agent can classify for a sharper pass.
3. **Feed back**: open a "Skill misfire" or "Skill output needed rework" issue (templates enforce the same vocabulary), or paste aggregate report output into GitHub Discussions. Nothing sensitive leaves your machine.
4. **Change**: fixes land as skill edits; new ideas land in `incubating/` and only promote on measured usage.
5. **Gate**: `scripts/ab_eval.py` re-runs the blind skill-on/skill-off eval against the rubrics before a release, so edits that regress a skill get caught.
6. **Ship**: a semver bump in the manifests releases the change through the plugin marketplace.

## What To Watch

- Over-structured output that looks useful but does not change action.
- Skills that ask for context already available in files.
- Public/private leakage through examples, paths, names, company details, or credentials.
- Chains that should be recipes because they recur often.
- Skills that need scripts instead of prose.

## Promotion Criteria

A skill can move toward public release when:

- It has at least three successful real uses across different project types.
- It has starter eval prompts.
- Its examples are sanitized.
- It does not depend on maintainer-specific memory, private paths, credentials, or services.
- Its `SKILL.md` stays compact and trigger-focused.
