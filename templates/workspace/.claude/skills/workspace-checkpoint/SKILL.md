---
name: workspace-checkpoint
description: Use when the owner wraps up a session that started at the workspace root and touched one or more projects. Runs the checkpoint for each project that changed: reconciles its working docs against its commits, commits, and reports what is unpushed. Does not push and does not write handoff notes.
---
# Workspace checkpoint

Each project in this workspace is its own git repository with its own `docs/current/todo.md` (which starts with a "Where we are" block) and `docs/current/decision-tracker.md`. This routine runs the normal checkpoint once for each project that changed in this session. Inside a single project, use that project's `session-checkpoint` skill instead.

## Rules
- Never create a dated handoff note. Each project's handoff is the "Where we are" block at the top of its own `docs/current/todo.md`.
- Do not run tests here. Tests run during the work; an item is ticked only after its tests pass. Report the last known test result per project, and say "tests not re-run since the last change" where code changed after the last passing run.
- Do not push. Commit, then tell the owner how many commits are unpushed in each project and ask.
- Do not commit `.claude/worktrees/`, `.claude/settings.local.json`, or temporary research folders (for example `.tmp-*`) unless asked.
- Keep the docs short. No retrospective logs.

## Steps
1. List the project folders listed in the workspace `CLAUDE.md`. For each, run `git -C <folder> status --short` and `git -C <folder> log` since its last checkpoint (the `Last checkpoint` hash in the "Where we are" block of its `docs/current/todo.md`). Skip projects with no changes and no new commits.
2. For each project that changed, in turn:
   - Reconcile its `docs/current/todo.md`: tick or move items for each commit, keep "Recently done" to at most 3 one-liners (older entries to its `docs/archive/done-log.md`), and keep "Now" and "Next steps" to live items.
   - Reconcile its `docs/current/decision-tracker.md`: record decisions made this session that are missing, and archive entries about finished one-offs.
   - Rewrite the "Where we are" block at the top of its `docs/current/todo.md` (at most 6 lines): stage, state, what to read first, and the `Last checkpoint` hash.
   - Stage only the intended files and commit with a clear message, using `git -C <folder>`.
3. If this session changed anything in `shared/`, update `shared/README.md` and commit it in whichever repository holds it (or note that it is not in a repository).
4. Report, per project: commit hash and branch, number of unpushed commits (ask whether to push), what changed in each of the two docs, last known test status, and anything intentionally left out of the commit.
