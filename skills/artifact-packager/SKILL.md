---
name: artifact-packager
description: "WHEN shaping a one-off durable shareable artifact. Triggers: blog post, README, case study, teardown, vision doc, design doc summary, launch page, demo script, internal whitepaper, 'write the v1 of X', 'turn this thread into a doc'. OUTPUT: draft artifact in target format plus a publish checklist. PAIR BEFORE: ctx-pack (ground the artifact in real work). NOT FOR: recurring progress messages (use status-update). If you'd send a fresh version next week, that's status-update territory."
---

# artifact-packager

One-off durable artifacts. Different from `status-update` (recurring progress). The heuristic is recurrence: would you send another version with new content next week? If yes, use `status-update`.

## Artifact Types

- Blog post
- LinkedIn post
- GitHub README
- Product landing copy
- Teardown page
- Case study
- Demo script
- Launch checklist
- Change explainer + comprehension quiz (post-implementation: what changed and why, bundled with spec and implementation notes, ending with a short quiz that checks the reader actually absorbed it)
- Internal-facing: Linear update, Slack announcement, weekly note, design doc summary

For internal artifacts, use `status-update` instead when the goal is recurring progress reporting. Use this skill when shaping a one-off durable artifact.

## Workflow

1. Identify the audience, the artifact type, and the delivery format (one-pager driven in a meeting versus long-form read; when unsure, ask).
2. Extract source material from real work, not generic claims.
3. Choose the thesis or narrative spine.
4. Draft the artifact in the target format, for what this reader should see, not everything you know.
5. Scrub pass over the draft: internal identifiers (ticket keys, internal URLs), named individuals, private paths, credentials, brand references, and any punctuation or phrasing the user has banned (for example em dashes). Search the text; do not rely on having been careful.
6. Add a short publish checklist.
7. If publishing to an external surface, also save a local canonical copy the next session can read.

## Rules

- Evidence is the artifact's spine and outranks everything else when space is tight: every claim carries its concrete figure, date, or outcome, pulled exactly from the source material. Do not round, summarize away, or placeholder a number that exists in the sources.
- Scrub identifiers and people, never evidence: the scrub targets ticket keys, internal URLs, named individuals, and banned phrasing, not the numbers that prove the point.
- Write for the reader, not the process: no analysis narrative, review history, or method commentary in stakeholder-facing artifacts. No named individuals or owner assignments unless asked; if the artifact will be shared with someone, never reference that person inside it.
- Do not invent proof. Keep the publish checklist to five lines or fewer.
- Ask before publishing externally.

