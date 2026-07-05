---
name: ctx-pack
description: "WHEN you need task-specific grounding before writing, deciding, or building. Pulls files, memory, diffs, and open threads into one pack. Triggers: 'ground in what exists', 'before I draft this', 'gather context for X', 'set up before brainstorm/decision', any moment you're tempted to dispatch parallel grounding agents. OUTPUT: a compact pack (goal, current state, decisions made, open threads, risks, next actions). PAIR BEFORE: artifact-packager, status-update, decision-review. NOT FOR: repo resume/handoff (use project-briefing), 'did we already do X' (use recall-prior-work)."
---

# ctx-pack

Use when grounding a specific task: drafting a doc, making a decision, planning a change. Different from `project-briefing` (whole-repo resume) and `recall-prior-work` (memory-only lookup).

## Workflow

1. Identify the target: project, decision, artifact, person, or workflow.
2. Load the smallest useful set of sources:
   - current status docs
   - persistent memory for the project, if a memory tool is available (e.g. claude-mem `search`/`timeline`; use `recall-prior-work` if the answer depends on prior sessions)
   - relevant repo files
   - recent commits or diffs
   - implementation notes or deviation logs from prior runs (e.g. `implementation-notes.md`), if present
   - open tracker issues / PRs cited by the work
   - deployment or runbook notes
3. Separate current facts from stale assumptions.
4. Produce a context pack, not a transcript dump.

## Output Shape

- Goal: what this context is for.
- Current state: what is true now, with dates when useful.
- Decisions already made: avoid re-litigating them.
- Useful source files: paths or links.
- Open threads: unresolved work.
- Risks and stale assumptions: what needs verification.
- Next likely actions: 3-5 concrete options.

## Rules

- Prefer status docs and curated memory over raw logs.
- Do not load private long-term memory in shared or public contexts.
- If source material conflicts, state the conflict instead of blending it.
- Date load-bearing facts. Memory is a snapshot; the repo is ground truth.
- Keep the pack brief enough to paste into another agent.

