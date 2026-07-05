# Competitive Review

## Superpowers

Repository: https://github.com/obra/superpowers

What is strong:

- Clear methodology bundle, not just prompt snippets.
- Skills map to phases: brainstorming, planning, TDD, subagent execution, review, branch finish.
- Enforces workflow checkpoints.
- Good multi-runtime packaging and tests.

What ctxops should borrow:

- Phase-specific skills.
- Lean `SKILL.md` files with references loaded on demand.
- Explicit trigger behavior.
- Validation and cross-runtime install story.

Where ctxops should differ:

- Focus on context assembly and ideation before execution.
- Cover non-code workflows: product strategy, writing, career, research, launch, infra operations.
- Treat stale assumptions and context exclusion as first-class.

## gstack

Repository: https://github.com/garrytan/gstack

What is strong:

- Broad AI engineering workflow with specialist roles: CEO reviewer, engineering reviewer, designer, QA, release, security, and more.
- Strong review gauntlet pattern: one command can run multiple lenses over a plan.
- Includes browser/QA loops, deployment verification, context save/restore, retros, benchmarking, and safety/scoping skills.
- Treats agent workflow as an operating environment, not just a prompt library.

What ctxops should borrow:

- Multi-lens reviews for important decisions.
- Context save/restore as an explicit skill surface.
- QA and verification as part of the workflow, not afterthoughts.
- Skill docs that encode real operational behavior.

Where ctxops should differ:

- Stay narrower and more portable.
- Avoid becoming a whole developer environment.
- Focus on context utilization, ideation, decision quality, and artifact packaging.
- Add commands only after skills prove repeated invocation value.

## Matt Pocock Skills

Repository: https://github.com/mattpocock/skills

What is strong:

- Small, composable skills for real engineering work.
- Grill-me pattern for resolving ambiguity before execution.
- `grill-with-docs` turns discussion into shared project language and ADRs.
- Strong emphasis on fundamentals: TDD, diagnosis, issue slicing, architecture, and codebase design.
- Explicitly avoids letting large process frameworks remove user control.

What ctxops should borrow:

- Shared language as a way to reduce verbosity and improve agent navigation.
- One-question-at-a-time grilling when user judgement is actually needed.
- Documentation capture during decision-making, not after.
- Small skills that can be adapted instead of a rigid master process.

Where ctxops should differ:

- Extend beyond software engineering into product strategy, writing, launch work, research, and personal operating context.
- Be autonomous first: inspect docs/files/memory before interviewing the user.
- Package context packs and artifacts, not only PRDs/issues/ADRs.

## Grill Me

Representative implementation: https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md

What is strong:

- Very clear use case: interview the user until ambiguity is resolved.
- Narrow trigger.
- Conversational but forceful.

What ctxops should borrow:

- Relentless ambiguity reduction.
- One-question-at-a-time mode for decisions that are genuinely blocked by user preference.

Where ctxops should differ:

- Be more autonomous by default. Search files, status docs, memory, and repos before asking.
- Use adversarial review without requiring a full interview every time.

## Claude-Mem-style Tools

Representative docs: https://docs.claude-mem.ai/

What is strong:

- Persistent memory outside the active context window.
- Retrieval instead of repeated full context loading.
- Session continuity across restarts.

What ctxops should borrow:

- Search-first memory access.
- Summarized episodes over raw logs.
- Context packs that can be reused by other agents.

Where ctxops should differ:

- Stay storage-agnostic in v0.1.
- Work with files, MCP tools, Recall, local memory, or future vector stores.
- Emphasize judgement about what to include, not only retrieval.
