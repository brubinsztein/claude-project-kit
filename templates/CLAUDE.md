# {{PROJECT_NAME}}

## About me
- {{ABOUT_ME}}  (for example: "I'm a Product Manager. I'm not a technical person.")
- Project: {{PROJECT_NAME}}. Details live in the active brief and supporting docs, not here.

## Workflow
1. **Product brief** → 2. **Implementation plan** → 3. **Implementation**. Stay in each stage until I approve moving on.
- Plan before coding: do not write implementation code until the brief and plan are approved by me.
- Brief stage: ask clarifying questions one at a time, write the answers into `docs/brief/product-brief.md`, and keep it updated as decisions land.
- Plan stage: draft a step-by-step plan in `docs/planning/implementation-plan.md` with task order, dependencies and what can run in parallel, at a middle level of detail. Put deeper technical detail in focused docs under `docs/planning/`.
- Implementation stage: build against the approved brief and plan, and do not reopen settled scope by default.
- Ask before big decisions (architecture, new dependencies or tools, scope changes, anything hard to reverse). Within a stage, proceed without asking about small things.
- **Current stage: {{CURRENT_STAGE}}.**

### Sizing the work: when to write a brief and a plan
Work comes in three sizes. Match the paperwork to the size.
- **Small change** (a fix, a wording change, a tweak inside something that exists): no brief or plan. Add a line to `docs/current/todo.md`, add a line to `docs/current/decision-tracker.md` if a decision was made, then do it.
- **New feature** (a self-contained capability): a midweight brief and plan. First go through clarification and refinement with me using AskUserQuestion, one question at a time, until you are highly confident you understand what I want. Then write one short document in `docs/brief/features/<feature-name>.md` covering what it is, why, what success looks like, what is in and out of scope, the steps in order, and open questions. Add one line to the `docs/brief/` index. Wait for my approval before writing code. When the feature is live, archive the document with `git mv`.
- **Set of features** (for example an MVP build, or a major new area): a full brief in `docs/brief/` and a full plan in `docs/planning/implementation-plan.md`, with task order, dependencies and what can run in parallel. Go through the same clarification and refinement with AskUserQuestion first, and go deeper than for a single feature. Wait for my approval of the brief and the plan before writing code.

Before starting any request, tell me which size you are treating it as and what that means in practice, then ask me to confirm using AskUserQuestion. For example: "I'm treating this as a new feature. That means I'll ask you clarifying questions, write a short feature brief in `docs/brief/features/`, and wait for your approval before writing code. Confirm?" Offer the other sizes as alternatives. Do not start the work until I confirm. If a request changes who the product is for or its overall scope, say so, and update the main brief only after I confirm.

## Communication
- Be concise and direct. Lead with the conclusion; give a recommendation rather than a survey of options.
- Explain technical decisions in plain language: what it is, why it matters, and the trade-off. Define jargon the first time.
- For any human-facing writing (reports, one-pagers, summaries), follow `docs/reference/writing-style-rules.md` if it exists.

## Working docs and routing
- Default working docs: `docs/current/todo.md` (starts with a short "Where we are" block) and `docs/current/decision-tracker.md`.
- Read other docs only when the task needs them: `docs/brief/`, `docs/planning/` (index in its README), `docs/reference/` (index in its README), `docs/archive/` (history; not read by default).

## Keeping docs current
- While work is in progress, do not touch the docs.
- An item has landed only when its relevant tests pass and it is committed, merged or confirmed done. At that point, tick or move its line in `todo.md` in the same change.
- When a decision is made, add one line to `decision-tracker.md`.
- At a checkpoint or end of session, run the session-checkpoint skill. It reconciles the two working docs against `git log`.
- Never create dated handoff notes. Finished or superseded material goes to `docs/archive/`. `todo.md` "Recently done" holds at most 3 one-liners; older entries go to `docs/archive/done-log.md`.

## Clarification and assumptions
- Lean toward asking, not assuming. Use the AskUserQuestion tool for clarifying questions: short multiple-choice questions, one small group at a time, with your recommended option first and a line on each choice. Keep asking until you are highly confident you understand the request.
- If you must make an assumption, state it and get my approval before relying on it.
- Flag uncertainty and anything unverified rather than guessing silently.

## Delegation
The main chat plans, decides with me, briefs helpers and checks their results. Helpers do the heavy reading and editing in their own space and return a short summary, which keeps the main conversation small. Delegate large, research-heavy, file-heavy or parallel work to a specialist; do single-file or few-line edits directly in the main chat. Use general-purpose only when no specialist fits.
{{AGENT_TABLE}}  (one line per agent: the task type, then the agent name)
Brief narrowly: goal, files in scope, a stop condition and a return format of at most 15 lines. Name any skill the agent must run, and check the report shows it ran. A "probe" is not an integration. Agents do not merge, push or sync deployments.

## Engineering principles
- Keep it simple. No over-engineering, speculative abstractions or unrequested features.
- Only do what was asked; mention nice-to-haves instead of building them.
- No automated tests for one-off experiments or offline analysis code until I decide to ship them. Tests are required for anything that touches live code; add them when an experiment is approved to ship.

## Git
- Commit at important milestones with clear messages. Push only when I ask, and tell me about unpushed commits at the end of a session.
- Keep this folder (the main working folder) on `{{MAIN_BRANCH}}` at all times. Do branch work in a separate worktree, and after merging bring this folder up to date. I own this housekeeping; the owner should not have to manage git.
- Never put tokens or passwords in files or chat.
