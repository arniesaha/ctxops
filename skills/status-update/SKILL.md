---
name: status-update
description: "WHEN composing any short stakeholder progress message. Triggers: ticket comment, Slack post, weekly note, pre-read, manager DM, founder ping, EOD, demo recap, leadership update, 'where are we on X', 'send my manager a note', 'draft a quick update'. Pulls from git + memory + open threads. OUTPUT: headline, shipped / in-flight / blocked, next checkpoint, asks. PAIR BEFORE: ctx-pack if context is thin. NOT FOR: one-off durable artifacts like blog posts or design docs (use artifact-packager)."
---

# status-update

Use for recurring, audience-facing progress messages. Different from `artifact-packager` (one-off durable artifacts). If you'd send it again next week with new content, use this skill.

## Workflow

1. Ask only what is missing: target surface (tracker / Slack / doc), audience, time window.
2. Gather, in this order:
   - `git log` for the relevant range and `git status` for in-flight work
   - persistent memory (e.g. claude-mem `search` + `timeline`) for the project over the window, if available
   - Open tracker issues / PRs cited in the window (Linear, Jira, GitHub)
   - Implementation notes / deviation logs from the window (e.g. `implementation-notes.md`), if present
   - Any status doc already in the repo
3. Group changes by outcome, not by commit. Drop intermediate churn.
4. Lead with what changed for the reader, not what you did.
5. Include the next concrete checkpoint or ask.

## Output Shape

- **Headline** - one line a busy reader can act on.
- **Shipped / merged** - outcome-level bullets with links (PR, Linear, commit).
- **In flight** - what is open, with the next step and owner.
- **Blocked / risks** - what could move the date, with the smallest unblocker.
- **Next checkpoint** - date + what will be demonstrable then.
- **Asks** - explicit decisions or reviews needed.

## Rules

- Match altitude to the audience: leadership gets outcomes, dates, and risks in plain language (no ticket numbers or internals); peers get identifiers and detail. When unsure, ask which.
- Be specific about identifiers (issue keys, PR numbers, ticket IDs) at peer altitude.
- Cut anything the reader already knows. No "as discussed earlier."
- No celebratory adjectives. Outcomes over effort.
- If a claim cannot be verified from git / tracker / memory, mark it as `unconfirmed:` and ask.
- For Slack: lead with the headline, attach detail below. For a tracker comment: lead with status delta since the last update.
- Never paste raw logs or full session transcripts.
