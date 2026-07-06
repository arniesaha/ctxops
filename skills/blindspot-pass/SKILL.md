---
name: blindspot-pass
description: "WHEN a plan, spec, or big prompt is about to drive real work and the unknowns haven't been surfaced. Run it before implementation starts. Triggers: 'what am I missing?', 'poke holes in this plan', 'what would you ask me?', 'sanity-check this spec', 'interview me about X', before a handoff prompt. OUTPUT: prioritized questions that would reshape the approach, plus flagged ambiguities, weak assumptions, and undefined behavior. PAIR AFTER: ctx-pack (ground first). PAIR BEFORE: decision-review (pressure-test the reshaped plan). NOT FOR: choosing between options (use decision-review), gathering context (use ctx-pack)."
---

# blindspot-pass

Surfaces the map/territory gap before work starts: what the plan assumes, what it leaves undefined, and what the user knows but never wrote down. An agent acts on the map it is handed, not the territory of the real project. This pass shrinks the difference.

## Workflow

1. Read the plan/spec/prompt and the relevant territory: the files it touches, the docs it cites.
2. Interview: ask up to 5 prioritized questions, highest-leverage first: questions whose answers would change the architecture, scope, or success criteria. One round; do not interrogate. Use the harness's structured question tool (for example AskUserQuestion) when available; otherwise plain text.
   - Target unknown-knowns: things the user would recognize instantly but never thought to state (conventions, constraints, taste, prior failed attempts).
3. Scan for unknown-unknowns in four buckets:
   - Ambiguity: terms or requirements with two plausible readings.
   - Missing context: territory the plan never looked at.
   - Weak assumptions: load-bearing claims nobody verified.
   - Undefined behavior: edge cases, failure paths, and "what happens when X" the plan is silent on.
4. For each finding, state why it matters and the cheapest resolution: a question, a file to read, or a command to run.
5. End with the riskiest remaining unknown, the one to resolve before any code.

## Output Shape

- Questions for you (prioritized, max 5)
- Ambiguities
- Weak assumptions
- Undefined behavior
- Missing context
- Riskiest unknown + cheapest resolution

## Rules

- Questions must need the user's head to answer. If a file read or command would answer it, do that instead of asking.
- No generic checklist items. Every finding cites the specific plan line, file, or gap that triggered it.
- Prefer 3 sharp findings over 10 padded ones.
- If the plan is genuinely tight, say so and stop. Do not invent blindspots.
- Write the answers back into the plan or a notes file so the next agent inherits them.
- If an answer changes a premise of an already-made decision, re-run `decision-review` on that decision with the revised constraints instead of silently keeping the old verdict.
