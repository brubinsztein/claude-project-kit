# How the setup works, and what each part gives you

This page explains each part of the kit and what you can change. You do not need any background in Claude Code. If you only want to set up a project, `README.md` is enough. Come here to understand the setup, or before you change a template.

## Words used on this page

- **Claude Code:** the version of Claude that works inside your project folder, reads and edits files, and runs commands.
- **Session:** one working conversation with Claude. When it ends, Claude forgets everything that was not written down in a file.
- **Context:** everything Claude holds in mind during a session: your messages, the files it has read, and the standing instructions it loads at the start. It has a size limit, and a bigger context costs more and can make Claude less sharp.
- **Token:** the unit Claude counts text in. Roughly four characters, so about three-quarters of a word. Cost and context size are both measured in tokens.
- **CLAUDE.md:** a file at the top of your project that Claude reads at the start of every session. It holds the standing rules for how to work with you.
- **Agent (or subagent):** a helper that Claude starts for one job, such as "fix this bug". It works on its own, then reports back a summary. Specialist agents are defined in small files under `.claude/agents/`.
- **Skill:** a saved procedure, such as "wrap up a session". Only its one-line description is loaded each session; the full steps load when it is used.
- **Hook and plugin:** a plugin is an add-on package. A hook is a small script an add-on runs automatically, for example before each command or at the start of each session.
- **Git, commit, push, branch:** git keeps the history of your project's files. A commit saves a snapshot. A push uploads commits to a shared copy, for example on GitHub. A branch is a separate line of work.
- **Workspace:** a folder that holds one or several projects and is what you open Claude Code in. A project is often a git repository of its own.
- **Worktree:** an extra working copy of the same project, used so an agent can change files without disturbing your main folder.

## The idea behind all of it

Claude has no memory between sessions, and it reads whatever is in front of it. Two things decide how well a project goes: what is written down for the next session, and how much Claude has to read before it can start. The kit keeps the written-down part short and current, and keeps the read-at-start part small.

## 1. Notes that stay current

Three small files act as the project's memory. `next-steps.md` says where things stand and what to read first. `docs/current/todo.md` lists what is next. `docs/current/decision-tracker.md` records decisions and the reason for each.

Updates happen at set moments:
- While work is in progress, nothing is updated.
- When a piece of work is finished (its tests pass and it is saved), one line in the to-do list is ticked.
- When you make a decision, one line goes in the decision tracker.
- At the end of a session, the wrap-up routine compares what was saved with what the to-do list says, fixes any gaps, and rewrites a short "where we are" block in `next-steps.md`.

There is one handoff, in `next-steps.md`, and no pile of dated notes. A new session can start from these three short files and know the state of the project. The notes need no constant upkeep, and half-finished work does not clutter them.

The moments for updating notes are written in the "Keeping docs current" section of `CLAUDE.md`, and the wrap-up steps are in `templates/.claude/skills/session-checkpoint/SKILL.md`. Change them there.

## 2. Folders Claude can navigate

Each docs folder (`docs/planning/`, `docs/reference/`) has a short `README.md` that lists only what is current. Finished or superseded material lives in `docs/archive/`, and a `.rgignore` file tells Claude's search to skip the archive by default.

Claude reads the index, then opens only the file the task needs. When a document is finished and nothing live points at it, move it to the archive with `git mv` and remove its line from the index. Long lists that only grow, such as a change log, live in their own file next to the main reference doc, so the main doc stays short. Claude reads only the part of a reference doc it is changing, and adds one line to the change log.

This helps Claude find the right document quickly and keeps outdated material from being treated as current. Reading less on each task also lowers cost.

You can change the folder names and decide what counts as finished. If a script or test reads a file, leave the file in place, or update the script when you move it.

## 3. Specialist helpers

Each recurring kind of job can have a helper, defined in a small file under `.claude/agents/`. The starter kit has an implementation coder and a docs maintainer. Add more for jobs your project repeats.

Claude chooses a helper mainly from its one-line description. So each description says when to use the helper, names the project's real files and keywords, and starts with "Use proactively when...". `CLAUDE.md` holds a table of five lines or fewer that matches task types to helpers. Each helper has its tools and model set explicitly. Each brief gives the goal, the files in scope, where to stop, and a report limit of 15 lines.

Large, research-heavy or parallel work goes to a helper. Claude does small edits itself, because starting a helper has its own cost and a helper cannot ask you a question halfway through. If you name a particular tool or skill, the brief repeats it and Claude checks that the report shows it was used.

Work lands with the helper that knows the area, reports come back short, and Claude's main conversation stays uncluttered.

You can add, remove or rename helpers, and adjust how big a job must be before it is handed over (the "Delegation" section of `CLAUDE.md`). Add a helper only when work keeps going to the wrong place, because every helper's description is loaded into every session.

## 4. Permissions

The settings file `.claude/settings.json` says which commands Claude may run freely, which must ask first, and which are blocked:
- Allowed without asking: read-only commands (looking at history, listing files, searching), saving work, and running your tests.
- Ask first: anything that pushes code to a shared copy or deletes things.
- Blocked: force-pushing and hard resets, which can destroy work.

Personal, machine-specific rules go in `.claude/settings.local.json`. That file stays out of git, because it can contain commands with sensitive details. If you use a tool that rewrites commands, such as `rtk`, a push can appear as `rtk git push`, so write the rule for both forms.

You get few interruptions for safe actions and a pause before anything risky. You can add generic rules for commands you use often. Never put a password or key in a rule.

## 5. The main folder stays on the main branch

`CLAUDE.md` says the folder you work in always stays on the project's main branch. Branch work happens in a separate working copy (a worktree), and after a merge Claude brings your folder up to date.

New sessions therefore always start from the current rules and notes, and you never have to manage git yourself. The branch name is set during setup.

## 6. Where each kind of rule lives

- **CLAUDE.md:** rules every helper needs. Keep it short, because it is loaded every session and costs tokens every time.
- **Memory:** things Claude has learned about you and your corrections. Only the main conversation sees memory, not helpers. Review it now and then against `CLAUDE.md` and your docs, and delete duplicates and out-of-date entries.
- **Project docs:** facts about the project. Put a rule next to the file it governs, for example the to-do list's structure in the to-do file's own header.
- **Skills:** procedures you use sometimes. Only their one-line description loads each session.

## 7. Keeping the startup load light

Everything Claude loads at the start of a session is paid for on every session: the rulebook, the memory index, and the one-line description of every skill, agent and add-on. The kit keeps these short and moves detail into places Claude reads only when needed, such as indexes, skills and reference docs.

Before you add or remove an add-on, measure what it costs. Estimates can be well off, and removing something for a small gain wastes effort. Open a fresh session and run `/context` to see the starting size and what makes it up. Run `claude plugin details <name>` to see what one add-on costs every session. After a change, check again in a fresh session.

## 8. Several projects in one workspace

If your projects share a lot of context, keeping them in one workspace folder works well. How Claude loads things explains how the kit is arranged for it:
- Claude loads the `CLAUDE.md` in the folder it starts in and in every folder above it. It loads a `CLAUDE.md` in a subfolder only when it reads or edits a file there.
- Claude's memory is kept separately for each git repository. A workspace folder that is not a repository gets memory of its own.
- Permission settings come from the folder you start in.
- Claude looks for helpers and skills from the folder you start in up to the repository root, and loads skills in subfolders when it first touches a file there.

The workspace `CLAUDE.md` is always loaded, so it carries only the rules that are the same everywhere and lists projects in one line each. Each project's own `CLAUDE.md` loads when you work in that project, so projects do not load each other's details. Shared background lives in `shared/` behind an index, and Claude reads a file from it only when the task needs it. Memory belongs to each project, so preferences that apply to every project go in the workspace `CLAUDE.md`.

Two points are worth checking on your machine. Parent-folder settings may not be merged into a session that starts inside a project, so each project carries its own `.claude/settings.json`. And it is not confirmed that helpers defined inside a nested project load when you start at the workspace root, so define helpers you need everywhere at the root, and start inside a project for deep work on it. Type `/status` in a session to see which settings files were loaded.

The README section "Several projects in one workspace" has the layout and the steps for adding or moving a project.

## How much to trust these choices

The firm points come from Claude Code's official documentation: the descriptions of add-ons and skills load every session, agents are chosen by their description, deny rules are checked before allow rules, and detail should load only when needed. Other choices, such as how short a rulebook should be and when to hand work to a helper, come from experience and community advice. Treat them as sensible starting points. Keep the ones that measurably help your project and drop the ones that do not.
