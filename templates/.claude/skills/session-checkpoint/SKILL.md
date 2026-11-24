---
name: session-checkpoint
description: Use this whenever the owner wants to wrap up a work session or the context is running low. Reconciles the working docs (todo with its "Where we are" block, and the decision tracker) against the commits made, commits the intended changes, and reports what is unpushed. Does not push and does not write handoff notes.
---
# Session checkpoint

End a working session cleanly: make the two working docs match reality, commit, and report. The aim is that the next session starts from `docs/current/todo.md` and `docs/current/decision-tracker.md` alone.

## Rules
- Never create a dated handoff note. The handoff is the "Where we are" block at the top of `docs/current/todo.md`.
- Do not run tests here. Tests run during the work; an item is ticked only after its tests pass. Report the last known test result, and if code changed after the last passing run, say "tests not re-run since the last change".
- Do not push. Commit, then tell the owner how many commits are unpushed and ask.
- Do not commit `.claude/worktrees/`, `.claude/settings.local.json`, or temporary research folders (for example `.tmp-*`) unless asked. Repo-local agents in `.claude/agents/` and skills in `.claude/skills/` are fine to commit.
- Keep the docs short. No retrospective logs.

## Steps
1. Run `git status --short`, note the branch, and list the commits since the last checkpoint (the `Last checkpoint` hash in the "Where we are" block of `docs/current/todo.md`).
2. Reconcile `docs/current/todo.md`:
   - For each commit, check the matching item is ticked or moved. Fix any that are not.
   - Keep "Recently done" to at most 3 one-liners; move older entries to `docs/archive/done-log.md`.
   - "Now" and "Next steps" hold only live items, in order.
3. Reconcile `docs/brief/`: each feature document's status (brief, plan, build, live) matches the work, each has a line in the `docs/brief/README.md` index, and a live feature's document is archived with `git mv` and its line removed. Check `docs/reference/what-exists-today.md` was updated for anything that went live.
4. Reconcile `docs/current/decision-tracker.md`: record any decision made this session that is missing; archive entries about finished one-offs or older than about 7 days unless they still describe live behaviour.
5. Rewrite the "Where we are" block at the top of `docs/current/todo.md` (at most 6 lines): features in flight with their status, state in one or two sentences, what to read first, and the `Last checkpoint` hash (the current HEAD before you commit).
6. Stage only the intended files and commit with a clear message.
7. Report:
   - commit hash and branch
   - number of unpushed commits (ask whether to push)
   - what changed in each of the two docs, and any feature whose status changed
   - last known test status
   - anything intentionally left out of the commit
