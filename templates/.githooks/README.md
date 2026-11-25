# .githooks: automatic checks

These checks run whether or not Claude remembers the rule. A failed check stops the action and says what to do instead.

**Switch them on (once per clone):** `git config core.hooksPath .githooks`. Then make the scripts executable: `chmod +x .githooks/pre-commit .githooks/pre-push .githooks/claude-edit-hook.sh`.

| Check | Where it runs | What it stops |
|---|---|---|
| A | pre-commit | A commit in the main working folder while it is on a branch other than the main branch. Worktrees are exempt. |
| B | pre-commit | Whatever `project-checks.sh` says. Optional, per project (see `project-checks.example.sh`). |
| C | pre-commit and Claude edit hook | A comment that silences a warning (noqa, type: ignore, eslint-disable and similar) without a reason. Write `-- <why>` after it. |
| D | pre-commit and Claude edit hook | A comment that says workaround, hack, quick fix, temporary fix, band-aid or kludge. |
| R | pre-commit and Claude edit hook | ruff findings, only when the project has a `ruff.toml`. |
| Reminder | pre-push | Nothing. Prints `pre-push-reminder.txt` when code is pushed to the main branch. |

- C, D and R look only at lines added by the change, so old code never blocks.
- Override: `git commit --no-verify`. Claude may use it only when the owner says so in that turn.
- The Claude edit hook is wired up in `.claude/settings.json`. It runs the same checks right after Claude edits a file, so the problem is fixed during the edit and not at commit time.
- Optional files, each with an `.example`: `config.sh` (main branch name, ruff location), `project-checks.sh`, `pre-push-reminder.txt`.
