# AGENTS.md - ctxops

This repo packages reusable agent skills for context assembly, fast ideation, and decision quality.

## Working Rules

- Keep skills compact. Put only trigger-critical behavior in `SKILL.md`.
- Move long examples and comparative notes into `references/`.
- Prefer deterministic scripts for validation and packaging.
- Validate frontmatter after editing skills.
- Avoid maintainer-specific private paths, names, and ticket prefixes anywhere in the repo. Use generic examples and placeholders instead.

## Publishing Intent

This repo should stay publishable. Private local knowledge can live in separate notes outside this repo or in ignored files.

## Validation

Run:

```bash
python3 scripts/validate.py
```

