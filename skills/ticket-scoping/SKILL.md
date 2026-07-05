---
name: ticket-scoping
description: "WHEN turning a finding, RCA, PR comment, or rough idea into trackable work. Triggers: 'file an issue', 'break this epic down', 'scope this work', 'sharpen this ticket', 'turn this finding into a ticket', 'what should the AC be?'. OUTPUT: paste-ready issue(s) for Linear/Jira/GitHub (title, problem, approach, AC checklist, size). PAIR AFTER: decision-review (file the chosen path). NOT FOR: writing an update on existing tickets (use status-update)."
---

# ticket-scoping

Use when turning intent into trackable work artifacts. Different from `status-update` (reports on existing work).

## Workflow

1. Restate the outcome in one sentence. If the user gave a solution, recover the problem behind it.
2. Decide the shape:
   - single issue
   - epic + 2-5 children
   - spike (time-boxed investigation) before any of the above
3. For each issue, draft:
   - title (verb-led, concrete)
   - problem and observed evidence (link to memory / logs / dashboards)
   - proposed approach (one paragraph, not a design doc)
   - acceptance criteria (testable, not aspirational)
   - out of scope
   - dependencies / blockers
   - rough size: XS / S / M / L (L means break it up)
4. If filing into an existing project, look up the parent epic, label conventions, and any related issues before writing.
5. End with a one-line summary the user can paste into a tracker.

## Output Shape

Per issue:
- Title
- Problem
- Approach
- Acceptance criteria (checklist)
- Out of scope
- Dependencies
- Size
- Suggested parent / labels

For epics, add: child list with order and which can run in parallel.

## Rules

- Acceptance criteria must be checkable from artifact, log, or dashboard. No "improved UX" without a measurable signal.
- A child issue that has no AC is a spike. Mark it that way.
- Do not invent issue keys or PR numbers. If a parent epic is unknown, leave a placeholder.
- Sizing is a call, not a vote. State the assumption that drives the size.
- If the work is reversible and small, prefer one issue. Do not over-decompose.
- Flag anything that needs cross-team buy-in before it can start.
