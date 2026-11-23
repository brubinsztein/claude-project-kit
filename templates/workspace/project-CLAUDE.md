# {{PROJECT_NAME}}

Rules shared by every project in this workspace (communication, clarification, delegation sizing, engineering principles, git) are in the workspace `CLAUDE.md` one folder up. This file holds only what is specific to this project.

## About this project
{{PROJECT_ONE_LINER}}  Details live in the project's brief and supporting docs, not here.

## Workflow
{{WORKFLOW_STAGES}}  (for example: 1. **Product brief** → 2. **Implementation plan** → 3. **Implementation**.)
- **Current stage: {{CURRENT_STAGE}}.**
- Plan before coding: do not write implementation code until the brief and plan are approved.

## Working docs and routing
- `next-steps.md` is a short router and "where we are" entry point, never a running log.
- Default working docs: `next-steps.md`, `docs/current/todo.md`, `docs/current/decision-tracker.md`.
- Read other docs only when the task needs them: `docs/brief/`, `docs/planning/` (index in its README), `docs/reference/` (index in its README), `docs/archive/` (history; not read by default). Shared context lives in the workspace `shared/` folder.

## Keeping docs current
- While work is in progress, do not touch the docs.
- An item has landed only when its relevant tests pass and it is committed, merged or confirmed done. At that point, tick or move its line in `todo.md` in the same change.
- When a decision is made, add one line to `decision-tracker.md`.
- At a checkpoint or end of session, run the session-checkpoint skill. It reconciles the three working docs against `git log`.
- Never create dated handoff notes. Finished or superseded material goes to `docs/archive/`. `todo.md` "Recently done" holds at most 3 one-liners; older entries go to `docs/archive/done-log.md`.

## Specialists for this project
{{AGENT_TABLE}}  (one line per agent: the task type, then the agent name)

## Guardrails
{{GUARDRAILS}}
