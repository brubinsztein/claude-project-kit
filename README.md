# Claude project kit

A ready-made way of working with Claude Code, Anthropic's AI assistant that reads and edits files in your project folder. The kit gives Claude a short rulebook, a small set of project notes that stay up to date, specialist helpers for recurring jobs, and safe permission settings.

Hand it to anyone starting a project, or to an AI agent, and say "set this project up". No coding knowledge is needed. It assumes Claude Code is installed and your project is in a git repository (git keeps the history of your files). Terms you may not know are explained in `WHY.md`.

## What you get

- Claude reads two short files at the start of each session and knows where the project stands, what is next, and what has been decided, so you never re-explain.
- The to-do list, the decisions and the "where we are" summary are updated as part of the work, at set moments, so you do not maintain them.
- Every docs folder has a short index of what is current, and finished material moves to an archive that searches skip, so Claude reads the right file instead of wading through old ones.
- Recurring jobs go to specialist agents that Claude picks from a short table, and Claude does small edits itself.
- Harmless commands run without asking, anything that pushes code or deletes things asks first, and destructive commands are blocked.
- Less to read at the start means lower cost and a clearer head for the real work.

## The core principles

Everything in the kit follows from six ideas. Each comes with the reason, so you can judge it and change it.

1. Plan before building. Claude works from what it is told, and a vague start produces work that has to be redone. So Claude drafts a brief and a plan with you first, and builds only once you approve them.
2. Claude writes the notes, at set moments. Claude forgets everything between sessions, so written notes are the project's only memory. Claude writes them from your conversation, and updates them at a few fixed moments so they stay current without constant upkeep.
3. Delegate the heavy work to specialist helpers. Claude's main conversation is its working memory, and it has a size limit. Big jobs, such as reading dozens of files, trying options or running tests, would fill it quickly and make Claude slower, costlier and less sharp. So Claude hands those jobs to a helper that works in its own separate space and reports back a short summary. The main conversation stays small and focused, long sessions stay sharp, and helpers can work side by side.
4. Keep what Claude reads at the start small, and index the rest. Whatever Claude loads at the start of a session costs time and money every time. The kit keeps that load short, and gives each docs folder a short index so Claude opens only the file a task needs.
5. Safe by default. Harmless commands run without asking. Pushing code and deleting things ask first, and destructive commands are blocked, so Claude can move quickly without risking your work.
6. Claude looks after git, and your main folder stays current. You should not have to manage version control. Claude keeps your main folder on the project's main branch, does branch work in separate copies, and tells you what has not been pushed.

## How the setup works

Claude forgets everything between sessions. Whatever is not written in a file is gone, and whatever Claude must read at the start of a session costs time and money. Left alone, projects drift into out-of-date notes and a heavy startup load. The kit sets up a few parts that work together to avoid both.

| Part | Role |
|---|---|
| A short rulebook (`CLAUDE.md`) | The standing rules Claude reads at the start of every session: how to talk to you, when to ask, when to update notes, how to handle git. Short, because it is read every time. |
| Three working notes (`next-steps.md`, a to-do list, a decision tracker) | The project's memory between sessions. One says where things stand, one lists what is next, one records decisions and the reason for each. |
| A wrap-up routine (the session-checkpoint skill) | At the end of a session it compares what was saved with what the notes say, fixes the gaps, and refreshes the "where we are" block. |
| Specialist helpers (agents) | Small definitions for recurring jobs, such as changing code or rewriting documents. Each says when to use it, so Claude picks correctly. |
| Safe permissions (`settings.json`) | Which commands run freely, which ask first, and which are blocked. |
| Indexes and an archive | A short index in each docs folder lists what is current. Finished material moves to `docs/archive/`, which searches skip by default. |

```
Start of session:   Claude reads CLAUDE.md (rules) and next-steps.md (where we are)
During work:        notes are left alone; helpers take big jobs, Claude does small edits
Work finishes:      one line ticked in the to-do list; one line added if a decision was made
End of session:     the wrap-up routine fixes any gaps and refreshes next-steps.md
```

## Brief, plan, then build

By default Claude does not start building straight away. A project moves through three stages, and Claude stays in each one until you approve moving on.

1. Brief. Claude asks you clarifying questions, one at a time, and writes the answers into a short product brief: what you are making, who it is for, and what success looks like.
2. Plan. Once you approve the brief, Claude drafts a step-by-step implementation plan: the tasks in order, what depends on what, and what can run in parallel. The plan stays at a middle level of detail, and deeper technical detail goes in separate focused documents that the plan links to.
3. Build. Once you approve the plan, Claude builds against it and does not reopen settled decisions unless you ask.

Big decisions, such as architecture, new tools or anything hard to undo, always come to you first, whatever the stage. Mistakes are cheapest to fix while they are still words on a page, and an approved brief and plan give every later session, and every helper agent, the same picture of what is being built. If a project is already under way, tell Claude which stage it is at and it starts there. You can rename the stages or change the rule in the Workflow section of `CLAUDE.md`.

## Where the notes come from

Claude writes the notes from your conversation. You make the decisions and approve; you rarely type a note yourself. You can also say "write that down" at any moment.

| Note | Created when | Written by |
|---|---|---|
| Product brief (`docs/brief/`) | At the start, from Claude's questions and your answers. Updated when the shape of the product changes. | Claude drafts, you approve |
| Implementation plan (`docs/planning/`) | After the brief is approved. | Claude drafts, you approve |
| To-do list (`docs/current/todo.md`) | Built from the plan. New ideas are added as next steps or parked as you raise them. Ticked when work lands. | Claude |
| Decision tracker (`docs/current/decision-tracker.md`) | One line each time you decide something, with the reason. | Claude |
| Focused design notes (`docs/planning/`) | When a feature needs thinking through. An index line is added, and the note is archived when the work is finished. | Claude |
| Reference docs (`docs/reference/`) | When something stable needs writing down, such as how to run the project or a map of the code. An index line is added. | Claude |
| "Where we are" (`next-steps.md`) | Rewritten by the wrap-up routine at the end of each session. | Claude |
| Memory (kept outside the project) | When you correct Claude or state a preference. | Claude |

## How helpers work

Think of the main conversation as a project manager and the helpers as specialists. The main conversation talks with you, makes the plan, writes the brief for each job, and checks the result. A helper takes one job, reads what it needs, makes the changes, runs the tests, and reports back in at most 15 lines. You see a short report in place of the hundreds of lines of work behind it.

A few rules keep this working well:
- Each helper has a one-line description saying when to use it, and `CLAUDE.md` holds a table of five lines or fewer that matches task types to helpers. Claude uses the table to pick.
- Large, research-heavy, file-heavy or parallel work goes to a helper. Claude does small edits itself, because starting a helper has its own cost and a helper cannot ask you a question halfway through.
- Every brief gives the goal, the files in scope, where to stop, and the report format. A narrow brief stops a helper from wandering into extra work. A request to look at something is not a request to build it.
- If you name a particular tool or skill, the brief repeats it, and Claude checks the report shows it was used.
- Helpers do not merge, push or deploy. They hand that back, so you stay in control of what leaves your machine.
- Helpers on separate jobs can run at the same time, each in its own working copy, so they do not overwrite each other's files.

You can ask "which helper would you use for this?" at any time. To add a helper for a job your project repeats, see "Things you can change".

## Day to day: how you use it

This is the whole routine once the project is set up.

1. Start a session. Open Claude Code in the project folder and start talking. Claude reads its rulebook and `next-steps.md` on its own. If you want a summary, ask "where are we?".
2. Ask for work. Describe what you want. Early in a project Claude takes you through the brief and the plan before it builds anything (see "Brief, plan, then build"). Later it asks questions if anything is unclear, hands large jobs to a specialist helper and reads only the short report it sends back (see "How helpers work"), and does small edits itself. Anything big or hard to undo comes to you for a decision first.
3. While something is in progress, Claude leaves the notes alone, which keeps them free of clutter.
4. When a piece of work is done, Claude ticks its line in the to-do list. "Done" means the tests pass and the work is saved.
5. When you decide something ("let's go with option B"), Claude adds one line to the decision tracker with the reason.
6. At the end of a session, say "run the checkpoint" (or "wrap up"). Claude compares what was saved with what the notes say, fixes anything missed, rewrites the short "where we are" block, saves everything, and tells you what has not been pushed to the shared copy. It asks before pushing.
7. Next session, a fresh Claude picks up from `next-steps.md`.

| You | Claude |
|---|---|
| Say what you want and make the decisions | Asks questions, does or delegates the work, runs the tests |
| Say "run the checkpoint" when you stop | Updates the to-do list, decision tracker and `next-steps.md`, then saves |
| Approve pushes and deletes when asked | Keeps the project folder tidy and on the main branch |

Useful things to say:
- "Where are we?" when you return after a break.
- "Update the notes from the commits" if you suspect they have drifted.
- "Which helper would you use for this?" if you are unsure how work will be handled.
- "That is a decision: ..." so it gets recorded with its reason.

## Setting it up on a new project

Open Claude Code in the new project folder and say:

> Read `<path to this kit>/README.md` and set this project up using the "Setup procedure". Ask me the questions first.

To share the kit, send a colleague the whole folder (or a zip of it) and the same sentence.

### Setup procedure (for Claude)

Follow these steps in order. Never overwrite a file that already exists: if one does, show the owner the difference and ask.

1. Ask the owner these questions with AskUserQuestion, one short group at a time, and wait for answers:
   - Whether this is a single project or a shared workspace that holds several projects. If it is a shared workspace, follow "Setting up a shared workspace" below as well.
   - Project name and a one-line description.
   - The owner's role and how technical they are (this fills "About me" and sets how much you explain).
   - Whether the project is new (it starts at the brief) or already under way, and if so which stage it is at and which notes already exist.
   - The main branch name, and whether a remote repository exists.
   - The command that runs the tests, and where the tests and main code live.
   - The project's guardrails (things agents must never do), if any.
   - Which kinds of work come up often (for example writing code, writing reports, researching), so you know which agents to keep and which new ones to add.
2. Copy the templates from `templates/` into the project root, keeping the folder layout. Replace every `{{PLACEHOLDER}}` using the answers (table below). If an answer is unknown, ask rather than guess.
3. Agents: keep only the agents the project needs. Rewrite each description to name the project's real files and keywords ("Use proactively when..."), and fill the agent table in `CLAUDE.md` (five lines or fewer). Remove any agent file you do not use.
4. Permissions: set the test command prefix in `.claude/settings.json`. Leave project-specific one-off permissions out; they build up in `.claude/settings.local.json`, which stays out of git.
5. Git: make sure `.claude/.gitignore` is in place and the main working folder is on the main branch. Make one initial commit of the setup. Do not push unless asked.
6. Start the notes. For a new project, interview the owner one question at a time (AskUserQuestion) to draft `docs/brief/product-brief.md` from the template, and stop for approval. Once the brief is approved, draft `docs/planning/implementation-plan.md` from its template and stop for approval again. Then build the first "Next steps" in `docs/current/todo.md` from the plan and fill in the "Where we are" block in `next-steps.md`. For a project already under way, ask where its existing notes are, summarise them into the three working notes, and record which stage it is at.
7. Baseline: run `/context` in a fresh session and note the starting size in `docs/current/decision-tracker.md`, so later changes can be measured.
8. Report to the owner in plain language: what was created, what to review, and the routine in "Day to day" above.

| Placeholder | Filled from |
|---|---|
| `{{PROJECT_NAME}}`, `{{DATE}}` | Project name; today's date |
| `{{ABOUT_ME}}` | The owner's role and how technical they are |
| `{{CURRENT_STAGE}}` | The stage the project is at (brief, plan or implementation) |
| `{{MAIN_BRANCH}}` | The main branch name |
| `{{TEST_COMMAND_PREFIX}}` | The command that runs tests (for example `python -m pytest`) |
| `{{AGENT_TABLE}}` | One line per kept agent: task type, then agent name |
| `{{GUARDRAILS}}` | Things agents must never do |
| `{{CODE_AREAS}}`, `{{REPO_SUMMARY}}` | The code areas the coder owns; three or four lines on layout, tests and what to update with a schema change |
| `{{WORKSPACE_NAME}}` | The name of the shared workspace folder |
| `{{PROJECT_1}}`, `{{PROJECT_1_FOLDER}}`, `{{PROJECT_1_ONE_LINER}}` | A project in the workspace: its name, its folder, and one line on what it is |

## Several projects in one workspace

Many people keep their projects in one workspace folder because the projects share context. One workspace might hold every internal tool you build, and another might be a general work assistant. The kit supports this with a few changes.

```
workspace/
  CLAUDE.md          rules for every project, plus a one-line list of the projects
  .claude/           workspace-level permissions and the workspace-checkpoint skill
  shared/            context used by more than one project, with an index (README.md)
  project-a/         its own git repository
    CLAUDE.md        only what is specific to this project
    next-steps.md, docs/current/...    this project's notes
    .claude/         this project's permissions, helpers and checkpoint skill
  project-b/
```

What goes where:
- The workspace `CLAUDE.md` holds the rules that stay the same across projects: how to communicate, when to ask, how big a job must be before it goes to a helper, and how to handle git. It also lists the projects, one line each. Every session loads it, so keep it short.
- Each project's own `CLAUDE.md` holds only its stage, its guardrails, its helpers and where its notes are. Use `templates/workspace/project-CLAUDE.md`.
- Each project keeps its own working notes (`next-steps.md`, to-do list, decision tracker). Leave project status out of the workspace files; they only point to each project.
- `shared/` holds background more than one project needs, such as who your audiences are or your writing rules. Add one line to its index for each file. If only one project needs something, keep it in that project.

How day to day changes:
- Start Claude at the workspace root when the work spans projects or needs shared context. Start inside a project folder for focused work. The workspace rules still apply either way, because Claude loads the `CLAUDE.md` files in the folders above the one it started in.
- At the end of a session, run the project's checkpoint skill when you worked inside one project. When you started at the root, use `workspace-checkpoint`, which runs the checkpoint for each project that changed and commits in each repository separately.
- Always name the project when you hand work to a helper or ask for a change, so the work lands in the right repository.
- Claude's memory is kept separately for each project. A preference that applies everywhere ("keep answers short", "always use the skill I name") belongs in the workspace `CLAUDE.md`, not in memory.
- Permissions come from the folder you start in. The workspace root and each project each need their own `.claude/settings.json`; copy the template into each.
- Claude looks for helpers and skills only as far up as the repository root. When you start inside a project, helpers and skills defined at the workspace root are not available there, so put the helpers a project needs in that project (or in your personal `~/.claude` folder if every project should have them). Give each helper a description that names its project, so work goes to the right one.

To check what Claude loaded in a session, type `/status` and look at the setting sources.

### Setting up a shared workspace

1. Copy `templates/workspace/CLAUDE.md` to the workspace root and fill it in, then copy `templates/workspace/shared/` and `templates/workspace/.claude/` to the root. Copy `templates/.claude/settings.json` into the root `.claude/` as well and trim the test command line, which belongs to individual projects.
2. For each project, create its folder, run `git init` (or use the existing repository), then copy the normal project templates into it. Use `templates/workspace/project-CLAUDE.md` as the project's `CLAUDE.md`, and leave out the project-level rules the workspace file already covers.
3. Add each project to the table in the workspace `CLAUDE.md`.

### Adding a project later, or moving an existing one in

- New project: repeat step 2 above and add its row to the workspace table.
- Existing project: move its folder inside the workspace, replace its `CLAUDE.md` rules that the workspace file now covers (communication, clarification, delegation sizing, engineering principles, git) with a pointer, and add its row to the table. Its notes, history and permissions travel with the repository. Claude's saved memory does not travel, because memory is kept per project location, so copy anything worth keeping into the project's `CLAUDE.md` or `shared/`.

### A workspace that is not about code

For a general assistant workspace, keep the rulebook, the three working notes, the wrap-up routine and `shared/` (put your preferences, recurring contacts and context there). Drop the coder helper, the test command and the git rules if there is no repository. Add helpers for the jobs you repeat, such as drafting, research or meeting notes.

## What is inside

| File | What it is |
|---|---|
| `templates/CLAUDE.md` | The rulebook. |
| `templates/next-steps.md`, `templates/docs/current/todo.md`, `templates/docs/current/decision-tracker.md` | The three working notes. |
| `templates/docs/brief/product-brief.md`, `templates/docs/planning/implementation-plan.md` | Starting points for the brief and the plan that Claude drafts with you. |
| `templates/.claude/skills/session-checkpoint/` | The wrap-up routine. |
| `templates/.claude/agents/` | Two starter helpers: an implementation coder and a docs maintainer. |
| `templates/.claude/settings.json`, `templates/.claude/.gitignore` | Permissions, and git ignore rules that keep personal settings out of the repository. |
| `templates/docs/planning/README.md`, `templates/docs/reference/README.md`, `templates/.rgignore` | Folder indexes, and the search ignore that skips the archive. |
| `templates/workspace/` | For a workspace that holds several projects: the workspace rulebook, a lean per-project rulebook, the shared-context index, and a checkpoint skill that covers every project. |
| `WHY.md` | How each part works and what it gives you. Start here to understand or change the setup. |

## Things you can change

None of this is fixed. Change what suits your project, and read the matching section of `WHY.md` first so you know what it was doing.

- Stages and tone: the workflow stages and the "Communication" rules in `CLAUDE.md`. If you would rather not plan first on a small project, relax the "plan before coding" rule there.
- Helpers: add, remove or rename agents. To add one for a job your project repeats, copy `templates/.claude/agents/implementation-coder.md`, change its name and description (say when to use it and name the real files), and add a line to the agent table in `CLAUDE.md`. Keep the table to five lines or fewer.
- Permissions: add generic rules for commands you use often. Never put a password or key in a rule.
- The wrap-up routine: its steps are in `templates/.claude/skills/session-checkpoint/SKILL.md`. Add a step if your project needs one.
- How big a job must be before it goes to a helper: the "Delegation" section of `CLAUDE.md`.
- When notes are updated: the "Keeping docs current" section of `CLAUDE.md`.
- Optional tools: see below.

## Optional tools

These are personal choices and sit outside the kit. The numbers come from one project, so check your own: `rtk gain`, `ctx_stats` and `/context` show what they save.

- rtk shortens command output before it reaches Claude. 336 commands saved about 35% of tokens, almost all from search results.
- context-mode keeps very large outputs out of the conversation and adds session search. It kept about 91% of large-output bytes out of the chat over a week.
- caveman makes replies terse. Its fixed cost was about 2.6k tokens per session plus about 1.2k per helper. Its own report could not confirm a saving, so test it before keeping it.

## Keeping the kit current

When your setup improves, change the kit in the same sitting: update the template, then add a line below.

- 23 Nov 2026: first version.
- 23 Nov 2026: added guidance and templates for a workspace that holds several projects; removed MEASURING.md.
