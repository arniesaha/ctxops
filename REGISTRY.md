# ctxops Registry

This is the working inventory for dogfooding. It is not a public taxonomy yet.

## Status Labels

- `dogfood`: use on real tasks and capture feedback.
- `candidate-public`: likely safe to publish after examples are sanitized.
- `private-adapter`: useful locally, but should not ship with maintainer-specific paths, tools, or memory assumptions.
- `needs-eval`: behavior is plausible but not proven enough.
- `incubating`: lives in `incubating/`, dogfooded via symlink only; excluded from the published plugin until measured usage supports promotion into `skills/`.

## Skills

| Skill | Use | Status | Privacy | Notes |
| --- | --- | --- | --- | --- |
| `ctx-pack` | Assemble compact context before planning or execution. | dogfood | candidate-public | Highest leverage. Needs examples from multiple project types. |
| `project-briefing` | One-page operational brief for a repo/project. | dogfood | candidate-public | Good for onboarding work projects and agents. |
| `decision-review` | Stress-test a plan before committing. | dogfood | candidate-public | Needs calibration so it is sharp without becoming performative. |
| `artifact-packager` | Turn private work into publishable artifacts. | needs-eval | candidate-public | Genericized; keep personal publishing preferences in private notes, not the skill body. |
| `status-update` | Compose tracker / Slack / weekly status updates from git + memory + open threads. | dogfood | candidate-public | Watch: adopted in June, zero invocations in the July window. If the next window stays dry, revisit triggers. |
| `ticket-scoping` | Turn a finding or proposal into well-formed ticket(s) with AC, deps, sizing. | dogfood | candidate-public | Pairs with `decision-review` for filing follow-ups. |
| `recall-prior-work` | Search persistent memory before answering "did we already do X?". | dogfood | candidate-public | Watch: near-zero measured usage; overlaps ctx-pack's memory pull and memory tools' own search skills. Cut-or-reposition candidate if the next window stays dry. |
| `blindspot-pass` | Surface unknowns in a plan/spec before implementation: interview + ambiguity/assumption scan. | dogfood | candidate-public | Graduated July 2026: real usage narrowed a live architecture decision; A/B gate tie 8-8. |
| `ctx-ignore` | Scan a repo and generate agent ignore files (.contextignore plus tool-specific variants). | dogfood | candidate-public | Graduated July 2026: pattern tables ported from the archived Go CLI; A/B gate win 8-7. |

## Current Dogfood Targets

Dogfood each skill across at least three different project types before promotion:

- An active work project with a tracker and stakeholders (status-update, ticket-scoping, recall-prior-work).
- A personal or side project where ground truth is easy to verify (project-briefing, ctx-pack).
- A multi-agent or cross-machine handoff (project-briefing, ctx-pack).

Measure invocations with `scripts/log_skill_invocation.py` + `scripts/report_skill_usage.py` rather than relying on recall.

## Review Questions

- Did the skill cause the agent to load less but better context?
- Did it change the next action, or only make the answer look organized?
- Did it reduce repeated explanations across sessions?
- Did it preserve privacy boundaries without requiring reminders?
- Did it produce an artifact worth keeping?
- Could a public user run this without maintainer-specific assumptions?
