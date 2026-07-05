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

1. Identify the audience and the artifact type.
2. Extract source material from real work, not generic claims.
3. Choose the thesis or narrative spine.
4. Draft the artifact in the target format.
5. Remove private details, sensitive paths, credentials, names, and unnecessary brand references.
6. Add a short publish checklist.

## Rules

- Preserve concrete technical detail where it proves the point.
- Remove chatty session residue.
- Do not invent proof.
- Mark placeholders clearly.
- Ask before publishing externally.

