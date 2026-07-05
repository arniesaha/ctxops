# Skill-on vs. skill-off A/B results, July 2026

Each eval prompt in `ctxops-evals.json` was run twice by independent agents against this repo: one agent instructed to follow the skill's `SKILL.md`, one given only the task. A separate judge scored both outputs blind (labeled A/B, assignment alternated per eval to cancel position bias) against the eval's rubric, 0 to 2 per rubric item plus an overall item, max 8.

| Eval | Skill-on | Skill-off | Winner | Deciding factor (judge's note, condensed) |
| --- | --- | --- | --- | --- |
| ctx-pack | 8 | 6 | **skill-on** | Skill-off asserted a false load-bearing fact (repo already public: it is private, judge verified); skill-on flagged it as the open blocker. |
| project-briefing | 8 | 7 | **skill-on** | Skill-off wrongly claimed the latest commit was unpushed; skill-on's claims verified true. |
| recall-prior-work | 8 | 7 | **skill-on** | Skill-on re-verified memory claims against the current repo with dated citations; skill-off presented stale details in present tense. |
| ticket-scoping | 8 | 7 | **skill-on** | Skill-on tied each size to its driving assumption and each AC to a verification artifact. |
| decision-review | 8 | 8 | tie | Both named the real constraint and landed an actionable verdict. |
| artifact-packager | 8 | 8 | tie | Equivalent evidence extraction, privacy flagging, and checklists. |
| status-update | 8 | 8 | tie | Both outcome-grouped with identifiers and a dated checkpoint. |

**Totals: 4 skill-on wins, 3 ties, 0 skill-off wins (56/56 vs. 51/56 rubric points).**

The pattern in every decided eval: the skill-off arm lost on an **unverified or stale load-bearing claim**, which is precisely the failure mode the skills' Rules sections target ("date load-bearing facts", "verify against the current repo before recommending", "state the assumption that drives the size"). The ties landed on tasks where a capable model's default behavior already matches the rubric.

## Caveats

- n=1 run per eval per arm; single blind judge per eval (two judges independently verified factual claims against the live repo/GitHub before scoring).
- Both arms used the same capable model; ties are expected where the task is well-specified.
- Evals ran against this repo; other codebases may shift results.

## Retrospective value audit (real usage)

Separately, the post-invocation window of every auditable real invocation from 26 days of instrumented use (9 of 10; one transcript no longer on disk) was classified from session transcripts:

**8 adopted** (output posted to a tracker/wiki, written to a deliverable file, or acted on directly) · **1 adapted** (used after meaningful edits) · **0 abandoned**.

The one adapted case (status-update) failed on voice/altitude (too ticket-number-heavy for its leadership audience), not structure, which is a concrete lead for improving that skill's audience-calibration rules.
