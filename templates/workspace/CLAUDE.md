# {{WORKSPACE_NAME}}

This workspace holds several projects. Rules here apply to all of them. Each project has its own `CLAUDE.md` with only what is specific to it.

## About me
- {{ABOUT_ME}}  (for example: "I'm a Product Manager. I'm not a technical person.")

## Projects
One line each. State lives in each project's own `docs/current/todo.md`, never here.

| Project | Folder | What it is |
|---|---|---|
| {{PROJECT_1}} | `{{PROJECT_1_FOLDER}}/` | {{PROJECT_1_ONE_LINER}} |

Shared context used by more than one project: `shared/README.md` (index). Read only what the task needs.

## Communication
- Be concise and direct. Lead with the conclusion; give a recommendation rather than a survey of options.
- Explain technical decisions in plain language: what it is, why it matters, and the trade-off. Define jargon the first time.
- For any human-facing writing (reports, one-pagers, summaries), follow `shared/writing-style-rules.md` if it exists.

## Clarification and assumptions
- Lean toward asking, not assuming. Use the AskUserQuestion tool for clarifying questions: short multiple-choice questions, one small group at a time, with your recommended option first and a line on each choice. Keep asking until you are highly confident you understand the request.
- If you must make an assumption, state it and get my approval before relying on it.
- Flag uncertainty and anything unverified rather than guessing silently.
- If I name a specific tool or skill, use exactly that, and say plainly if it was not used.

## Delegation
The main chat plans, decides with me, briefs helpers and checks their results. Helpers do the heavy reading and editing in their own space and return a short summary, which keeps the main conversation small. Delegate large, research-heavy, file-heavy or parallel work to a specialist; do single-file or few-line edits directly in the main chat. Use general-purpose only when no specialist fits. Each project's `CLAUDE.md` lists its own specialists.
Brief narrowly: goal, files in scope, a stop condition and a return format of at most 15 lines. Always say which project the work is in. Name any skill the agent must run, and check the report shows it ran. Agents do not merge, push or sync deployments.

## Engineering principles
- Keep it simple. No over-engineering, speculative abstractions or unrequested features.
- Only do what was asked; mention nice-to-haves instead of building them.
- No automated tests for one-off experiments or offline analysis code until I decide to ship them. Tests are required for anything that touches live code.
- **A correction becomes a check.** When I correct you for the same thing a second time, do not just add a line to a rulebook. Propose an automatic check (a lint rule, a test or a hook in the project's `.githooks/`) that fails when the rule is broken, with an error message that says what to do instead, and ask me before adding it.
- **Automatic checks.** Where a project has `.githooks/`, its checks run on every commit and after each file edit. When one blocks, fix the cause. Use `git commit --no-verify` only when I say so in that turn.
- **Comments.** Do not write comments that justify a workaround; fix the root cause. A comment that silences a warning (`noqa`, `type: ignore`, `eslint-disable`) must give a reason after ` -- `, and only after fixing the code is not possible.

## Git
- Commit at important milestones with clear messages. Push only when I ask, and tell me about unpushed commits at the end of a session.
- Each project is its own git repository. Keep each project's main folder on its main branch. Do branch work in a separate worktree, and after merging bring the main folder up to date. I own this housekeeping; the owner should not have to manage git.
- Never put tokens or passwords in files or chat.

## Working across projects
- When a task touches more than one project, say which project each change belongs to, and commit in each repository separately.
- Keep project notes in the project they describe. Put something in `shared/` only when more than one project needs it.
