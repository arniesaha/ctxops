---
name: recall-prior-work
description: "WHEN the user references past sessions, prior decisions, or work outside current context: search persistent memory FIRST before answering. Triggers: 'did we already X?', 'how did we solve Y last time?', 'what was decided about Z?', 'last time we tried this…'. Requires a persistent-memory tool (e.g. claude-mem); degrades to git history + docs without one. OUTPUT: found / decided / tried-but-unresolved / stale-risk, with dates. PAIR: feed results into ctx-pack or status-update. NOT FOR: current-session recall (it's in context), repo-state questions (read the repo)."
---

# recall-prior-work

Memory-only lookup, distinct from `ctx-pack` (which also pulls memory but blends it with files/diffs) and `project-briefing` (which reads the live repo).

## Workflow

Three layers, always in order. Never fetch full details before filtering. Tool names below are claude-mem's; map them to whatever memory tool is installed. If none is, say so and fall back to git history, status docs, and ADRs. Do not fabricate continuity.

1. **Search** - memory `search` with a focused query, project filter, and a date window if known. Read titles only.
2. **Timeline** - if a single hit looks load-bearing, pull `timeline` around it for surrounding context.
3. **Fetch** - `get_observations` on the small set of IDs that actually matter. Batch the call.

Then:
- Distinguish what was *decided* from what was *tried*. Decisions stick; experiments may not.
- Note the date of each fact. Memory is a snapshot, not ground truth.
- Verify load-bearing claims (file paths, flag names, ticket IDs) against the current repo before recommending action.

## Output Shape

- **Found** - 1-line per relevant memory with date and ID.
- **Decided** - what was settled, and when.
- **Tried but unresolved** - so we do not re-litigate or re-attempt blindly.
- **Stale risk** - facts whose freshness matters; what to re-verify.
- **Next step** - either an answer or the verification command.

## Rules

- Filter before fetching. Titles first, full text only for finalists.
- If memory and current repo disagree, trust the repo and update memory.
- Do not paste long memory excerpts into the response; cite IDs and summarize.
- If no relevant memory exists, say so explicitly. Do not fabricate continuity.
- Respect project scope: pass the `project` filter so memory from unrelated repos does not leak in.
