# ctxops

Agent skills for the work that happens around the implementation loop: assembling the right context, pressure-testing directions, and shaping the output into updates, tickets, and durable artifacts.

ctxops follows the [Agent Skills](https://agentskills.io) open standard. Every skill is a plain `SKILL.md` file, so the set works in Claude Code, Codex, Gemini CLI, OpenCode, and any other harness that reads Agent Skills. Claude Code users get a one-command plugin install; other harnesses point at the `skills/` directory.

## Why

Most skill bundles optimize how an agent writes code. ctxops optimizes the steps before and after.

The premise: an agent acts on the map you hand it (prompt, skills, context), not the territory of the real project. Where the map is silent, wrong, or stale is where agents fail, confidently. ctxops shrinks that gap at the bookends of the loop:

- Before: pull the territory into the map (`ctx-pack`, `project-briefing`, `recall-prior-work`), keep noise off it (`ctx-ignore`), and surface unknowns and hidden assumptions before committing (`blindspot-pass`, `decision-review`).
- After: shape the output for its audience without losing the load-bearing facts (`status-update`, `ticket-scoping`, `artifact-packager`).

This is not just framing. In blind skill-on/skill-off evals, every decided comparison turned on exactly this: the skill arm verified load-bearing facts that the freeform arm stated wrongly or stale (`evals/ab-results-2026-07.md`).

ctxops treats context as an operating surface, not a pile of files.

## Skills

| Skill | One-liner |
| --- | --- |
| `ctx-pack` | Assemble a tight working context pack for a task or decision. |
| `project-briefing` | One-page operational brief to resume or hand off a whole project. |
| `recall-prior-work` | Search persistent memory before answering "did we already do X?". |
| `ctx-ignore` | Scan a repo and generate agent ignore files; exclusion is half of assembly. |
| `blindspot-pass` | Interview + scan to surface a plan's unknowns before implementation. |
| `decision-review` | Adversarial pass on a direction before committing; post-hoc mode for old calls. |
| `status-update` | Stakeholder progress messages from git, memory, and open threads. |
| `ticket-scoping` | Turn a finding or idea into paste-ready issues with checkable AC. |
| `artifact-packager` | Turn real work into a durable shareable artifact with a publish checklist. |

The set is deliberately bookends-only: input-shaping and output-shaping skills, no middle "reasoning" layer. Reasoning is the model's job.

The skills are tool-agnostic. Trackers (Linear, Jira, GitHub), chat surfaces, and persistent-memory tools (for example [claude-mem](https://docs.claude-mem.ai/)) appear only as examples; every skill degrades to git history and status docs when a tool is absent.

## Install

Claude Code, as a plugin:

```
/plugin marketplace add arniesaha/ctxops
/plugin install ctxops@ctxops
```

Any harness that reads Agent Skills: copy or symlink the skill directories into your harness's skill path, for example:

```bash
CTXOPS_ROOT="$(pwd)"
for d in "$CTXOPS_ROOT"/skills/*; do
  ln -s "$d" "$HOME/.claude/skills/ctxops-$(basename "$d")"
done
```

A Codex-style manifest is included at `.codex-plugin/plugin.json`.

Use one install method per harness, or skills will load twice.

## Measuring Whether It Works

A skill bundle is only useful if the skills actually get invoked and their output actually gets used. ctxops ships its own instrumentation:

- `scripts/log_skill_invocation.py`: a hook that logs every skill invocation to `~/.claude/skill-metrics/invocations.jsonl` (all skills, so share can be computed; never inside a repo).
- `scripts/report_skill_usage.py`: per-skill counts, session and project spread, and ctxops' share of total invocations.
- `scripts/skill_retro.py`: classifies each invocation as adopted, adapted, or unclear from your local session transcripts.
- `scripts/ab_eval.py`: blind skill-on/skill-off eval against the rubrics, used as a regression gate before releases.

Everything runs locally. If you want to help tune the skills, paste aggregate report output into [Discussions](https://github.com/arniesaha/ctxops/discussions) or use the structured issue templates; see the Feedback Loop section of `DOGFOOD.md`.

### Results so far (maintainer dogfood, July 2026)

- **Adoption:** in the first 26 days of instrumented use, all 7 skills were invoked, across 7 different projects. Baseline before the trigger-focused description rework: one invocation, ever.
- **Value audit:** every auditable real invocation (9) was classified from its session transcript: **8 adopted** downstream (posted, committed, or acted on directly), **1 adapted** after edits, **0 abandoned**.
- **Skill-on vs. skill-off:** each eval prompt run with and without the skill, blind-judged against its rubric: **4 wins for skill-on, 3 ties, 0 losses**. Every decided eval turned on the skill preventing an unverified or stale load-bearing claim. Method, table, and caveats: `evals/ab-results-2026-07.md`.

## Useful Chains

- `ctx-pack` then `blindspot-pass` then `decision-review`: ground, surface unknowns, decide.
- `ctx-pack` then `decision-review` then `ticket-scoping`: ground, decide, file.
- `recall-prior-work` then `status-update`: recover the week, report it.
- `ctx-pack` then `artifact-packager`: ground a public artifact in real work.

## Repo Files

- `REGISTRY.md`: skill inventory, status, and privacy classification.
- `DOGFOOD.md`: how to test these skills on real work and measure adoption.
- `evals/ctxops-evals.json`: starter prompts for skill behavior checks.
- `scripts/validate.py`: frontmatter, manifest, registry, and eval sanity checks.

## Validation

```bash
python3 scripts/validate.py
```

## License

MIT. See `LICENSE`.
