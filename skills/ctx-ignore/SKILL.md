---
name: ctx-ignore
description: "WHEN an agent keeps reading noise (node_modules, lockfiles, build output, generated code, fixtures) or a repo needs ignore files for AI tools. Triggers: 'generate a claudeignore', 'keep the agent out of X', 'my agent wastes context on generated files', 'set up ignore files', new repo onboarding. OUTPUT: a ranked noise report, an annotated .contextignore as source of truth, and tool-specific ignore files (.claudeignore, .cursorignore, .copilotignore, .windsurfignore). PAIR BEFORE: ctx-pack (exclude noise before assembling context). NOT FOR: choosing what to load for one task (use ctx-pack), .gitignore hygiene alone."
---

# ctx-ignore

Decide what an agent should never read, once, instead of paying for the noise on every request. The other half of context assembly is context exclusion.

## Workflow

1. Walk the repo tree, respecting `.gitignore`. Note file sizes.
2. Categorize noise candidates against `patterns.md` in this skill's directory (dependencies, lockfiles, build output, generated code, binaries, test artifacts, IDE/OS noise). Red entries always exclude; yellow entries (test files, migrations) need user confirmation.
3. Score each remaining candidate by context cost versus usefulness: large and mechanically produced ranks highest.
4. Show a ranked report with a one-line reason per entry. Get confirmation before writing anything.
5. Write `.contextignore` as the annotated source of truth (grouped, commented, dated header), then derive the tool-specific files the user wants: `.claudeignore`, `.cursorignore`, `.copilotignore`, `.windsurfignore`.
6. If existing ignore files are present, merge additions under a marked section. Never clobber hand-written entries.

## Output Shape

- Ranked noise report: path, size, category, one-line reason
- `.contextignore` (source of truth)
- Tool-specific ignore files derived from it
- Skipped-on-purpose list: things that looked like noise but stay readable, with reasons

## Rules

- Never exclude source, docs, or config that shapes runtime behavior, even when large.
- Lockfiles are noise for reading but load-bearing for reproducibility: exclude from agent context, never delete.
- When unsure whether a directory is generated, check for a generator config or header comment before excluding it.
- Report first, write second. No silent writes.
- Keep entries as directory or glob patterns, not hundreds of individual files.
