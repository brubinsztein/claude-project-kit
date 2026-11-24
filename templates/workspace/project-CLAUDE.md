# {{PROJECT_NAME}}

Rules shared by every project in this workspace (communication, clarification, delegation sizing, engineering principles, git) are in the workspace `CLAUDE.md` one folder up. This file holds only what is specific to this project.

## About this project
{{PROJECT_ONE_LINER}}  Details live in the project's brief and supporting docs, not here.

## Workflow
Plan before coding: do not write implementation code until the brief and plan for that work are approved by me. How much paperwork a request needs depends on its size (below).
- Every feature has its own status: **brief, plan, build, live**. `docs/current/todo.md` lists each feature in flight with its status, so there is no project-wide stage. Once a feature is live, small tweaks to it need no new brief (see the small-change tests).
- Ask before big decisions (architecture, new dependencies or tools, scope changes, anything hard to reverse). Technical choices such as language, database or hosting are made with me through questions, each with your recommendation and the trade-off, and recorded in the plan's "Technical approach" section. Within a piece of work, proceed without asking about small things.

### Sizing the work: when to write a brief and a plan
Work comes in three sizes. Match the paperwork to the size.
- **Small change:** a fix, a wording change or a tweak inside something that already exists. It must meet ALL of these: no new user-visible capability, no new data source, database change, dependency or scheduled job, easy to undo, and doable in one short sitting. No brief or plan. Add a line to `docs/current/todo.md` when you start, tick it when it lands, and add a line to `docs/current/decision-tracker.md` if a decision was made.
- **New feature:** a self-contained capability. Its brief, then its plan, live together in `docs/brief/features/<feature-name>.md`, started from the template `docs/brief/product-brief.md`. Add one line to the `docs/brief/` index. When the feature is live, archive the document with `git mv`.
- **Set of features** (for example an MVP build, or a major new area): the same steps with a full brief in `docs/brief/product-brief.md` and a full plan in `docs/planning/implementation-plan.md` (task order, dependencies, what can run in parallel). Go deeper in the questions than for a single feature.

Never treat something as a small change if it fails any of the tests above. If you are unsure between two sizes, treat it as the larger one and say why.

Before starting any request, tell me which size you are treating it as, a one-line complexity read (small, medium or sprawling: how many parts of the project it touches; no time estimates), and what the process means in practice. Then ask me to confirm using AskUserQuestion. For a new feature or a set of features, always ask and do not start until I confirm. For a change that clearly meets every small-change test, state in one line that you are treating it as small and what you will do, then carry on unless I object. If a request changes who the product is for or its overall scope, say so, and update the main brief only after I confirm.

### How a brief or plan gets agreed
1. **Scoping questions.** Ask with AskUserQuestion only what you need to be confident enough to write a first draft.
2. **Draft and hand over.** Write the draft, then send a short review message and stop: a clickable link to the file (the interface may not open it for me), what to look at, and the open questions. Do not ask the refinement questions yet, because the draft often holds context I need to read first. End by asking me to say when I am ready for them.
3. **Refinement.** When I say so, ask the remaining questions with AskUserQuestion, each with its own context (the relevant point, the options, the trade-off, your recommendation first), so I can answer without re-reading. Put the answers into the document and ask for approval.
4. Brief approved, then repeat steps 2 and 3 for the plan. Build only once the plan is approved.
- **UI or UX work:** offer me a visual-only mock-up first (fake data, minimal effort, such as a clickable page or the existing screen with the change faked). I review it and commit to the design before any real data or backend work. It sits between the approved brief and the approved plan, lives with the feature's brief, and is archived with it. It is an offer, not a rule.
- **Before a feature is ticked done:** report against the brief's "what success looks like", and say plainly if anything visual was not viewed. When it ships, update `docs/reference/what-exists-today.md`.
- **Change of direction or a dropped feature:** archive its brief and plan with `git mv`, add a decision line, and go back to the main brief if the product changes. Feedback from other people becomes to-do or Parked lines, or a small change.

## Working docs and routing
- Default working docs: `docs/current/todo.md` (starts with a short "Where we are" block) and `docs/current/decision-tracker.md`.
- Read other docs only when the task needs them: `docs/brief/` (index in its README), `docs/planning/` (index in its README), `docs/reference/` (index in its README, including `what-exists-today.md`), `docs/archive/` (history; not read by default). Shared context lives in the workspace `shared/` folder.

## Keeping docs current
- No running commentary in the docs while you work. Add the to-do line when work starts and tick it when it lands.
- An item has landed only when its relevant tests pass and it is committed, merged or confirmed done. At that point, tick or move its line in `todo.md` in the same change, and update the feature's status.
- When a decision is made, add one line to `decision-tracker.md`.
- At a checkpoint or end of session, run the session-checkpoint skill. It reconciles the two working docs against `git log`.
- Never create dated handoff notes. Finished or superseded material goes to `docs/archive/`. `todo.md` "Recently done" holds at most 3 one-liners; older entries go to `docs/archive/done-log.md`.

## Specialists for this project
{{AGENT_TABLE}}  (one line per agent: the task type, then the agent name)

## Guardrails
{{GUARDRAILS}}

<!-- Kit version: 2.0. See "Keeping the kit current" in the kit README. -->
