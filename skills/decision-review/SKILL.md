---
name: decision-review
description: "WHEN about to commit to a direction and want a sharp adversarial pass. Triggers: 'should we do X?', 'is this worth it?', 'pressure-test this plan/principle/vision', 'pick between A and B', 're-check the call we made two weeks ago', 'play devil's advocate'. Direct, not balanced. OUTPUT: verdict (do/delay/narrow/compare/kill), strongest case for and against, cheapest test. PAIR BEFORE: ticket-scoping (file the chosen path). Use post-hoc mode for older calls."
---

# decision-review

Adversarial review of a single direction or choice between a few. This culls existing options; it does not generate new ones.

## Workflow

1. Restate the decision in one sentence.
2. Identify the actual constraint: time, money, trust, focus, technical risk, market risk, or reversibility.
3. Make the strongest case for the direction.
4. Make the strongest case against it.
5. List hidden assumptions.
6. Identify the cheapest test.
7. Recommend: do, delay, narrow, compare, or kill.

## Post-hoc Mode

When the user asks whether a past call still holds (e.g. "we decided X two weeks ago - is that still right?"):

1. Recover the original decision and its assumptions from memory / repo / docs.
2. List which assumptions are now confirmed, broken, or unknown.
3. Re-run steps 3-7 with current facts.
4. Recommend: keep, revise, or reverse - and the smallest action to lock it in.

## Output Shape

- Decision
- Verdict
- Strongest case for
- Strongest case against
- Hidden assumptions
- Cheap test
- What would change the verdict

## Rules

- Be direct. Do not balance weak arguments for politeness.
- If the real issue is positioning, say so.
- If the real issue is execution capacity, say so.
- Distinguish reversible choices from one-way doors.
- Recommend the smallest action that creates evidence.

