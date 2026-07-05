---
name: project-briefing
description: "WHEN resuming a repo after time away, onboarding another agent, preparing a handoff, or checking what needs attention. Produces a one-page operational brief for a whole project. Triggers: 'where am I on this', 'brief me on repo X', 'pick up where we left off', 'what does the next agent need'. OUTPUT: one-page brief (status, how to run/verify, risks, next action). NOT FOR: a single decision/task (use ctx-pack), prior-session lookup (use recall-prior-work)."
---

# project-briefing

Use for whole-project resume/handoff. Different from `ctx-pack` (task-specific) and `recall-prior-work` (memory-only).

## Workflow

1. Read existing status docs first: `README`, `STATUS`, `AGENTS`, runbooks, deployment notes.
2. Check recent changes: git status, recent commits, open TODOs.
3. If the working tree is clean or the repo has been idle, pull a persistent-memory timeline for the project (e.g. claude-mem), if available, to recover what was last in flight.
4. Identify runtime surfaces: local URLs, deployed URLs, commands, tests, dashboards.
5. Summarize operationally.

## Output Shape

- What this project is
- Current status
- Recent changes
- How to run or verify
- Known risks
- Open threads
- Suggested next action

## Rules

- Do not rewrite the project docs unless asked.
- Do not include every file. Include the files that affect action.
- If the deployment path is known, include the exact verification path.
- If status is uncertain, say what command or page would verify it.

