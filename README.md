# Claude project kit

A ready-made way of working with Claude Code, Anthropic's AI assistant that reads and edits files in your project folder. The kit gives Claude a short rulebook, a small set of project notes that stay up to date, specialist helpers for recurring jobs, and safe permission settings.

Hand it to anyone starting a project, or to an AI agent, and say "set this project up". No coding knowledge is needed. It assumes Claude Code is installed. If your project is not yet in a git repository (git keeps the history of your files), or you are starting from nothing, setup creates one for you. Terms you may not know are explained in `WHY.md`.

## What you get

- Claude reads two short files at the start of each session and knows where the project stands, what is next, and what has been decided, so you never re-explain.
- The to-do list, the decisions and the "where we are" summary are updated as part of the work, at set moments, so you do not maintain them.
- Every docs folder has a short index of what is current, and finished material moves to an archive that searches skip, so Claude reads the right file instead of wading through old ones.
- Recurring jobs go to specialist agents that Claude picks from a short table, and Claude does small edits itself.
- Harmless commands run without asking, anything that pushes code or deletes things asks first, and destructive commands are blocked.
- Less to read at the start means lower cost and a clearer head for the real work.

## The core principles

Everything in the kit follows from seven ideas. Each comes with the reason, so you can judge it and change it.

1. Plan before building. Claude works from what it is told, and a vague start produces work that has to be redone. So Claude drafts a brief and a plan with you first, lets you read them before it asks its detailed questions, and builds only once you approve them.
2. Claude asks instead of assuming. When something is unclear, Claude stops and asks using Claude Code's built-in question tool: short multiple-choice questions that you answer with a click, with its recommended option first and a free-text "Other" always available. A wrong guess costs far more than a ten-second question, and your answers become decisions Claude writes down.
3. Claude writes the notes, at set moments. Claude forgets everything between sessions, so written notes are the project's only memory. Claude writes them from your conversation, and updates them at a few fixed moments so they stay current without constant upkeep.
4. Delegate the heavy work to specialist helpers. Claude's main conversation is its working memory, and it has a size limit. Big jobs, such as reading dozens of files, trying options or running tests, would fill it quickly and make Claude slower, costlier and less sharp. So Claude hands those jobs to a helper that works in its own separate space and reports back a short summary. The main conversation stays small and focused, long sessions stay sharp, and helpers can work side by side.
5. Keep what Claude reads at the start small, and index the rest. Whatever Claude loads at the start of a session costs time and money every time. The kit keeps that load short, and gives each docs folder a short index so Claude opens only the file a task needs.
6. Safe by default. Harmless commands run without asking. Pushing code and deleting things ask first, and destructive commands are blocked, so Claude can move quickly without risking your work.
7. Claude looks after git, and your main folder stays current. You should not have to manage version control. Claude keeps your main folder on the project's main branch, does branch work in separate copies, and tells you what has not been pushed.

## How the setup works

Claude forgets everything between sessions. Whatever is not written in a file is gone, and whatever Claude must read at the start of a session costs time and money. Left alone, projects drift into out-of-date notes and a heavy startup load. The kit sets up a few parts that work together to avoid both.

| Part | Role |
|---|---|
| A short rulebook (`CLAUDE.md`) | The standing rules Claude reads at the start of every session: how to talk to you, when to ask, when to update notes, how to handle git. Short, because it is read every time. |
| Two working notes (a to-do list that starts with a "where we are" summary, and a decision tracker) | The project's memory between sessions. One says where things stand and what is next, the other records decisions and the reason for each. |
| A wrap-up routine (the session-checkpoint skill) | At the end of a session it compares what was saved with what the notes say, fixes the gaps, and refreshes the "where we are" block. |
| Specialist helpers (agents) | Small definitions for recurring jobs, such as changing code or rewriting documents. Each says when to use it, so Claude picks correctly. |
| Safe permissions (`settings.json`) | Which commands run freely, which ask first, and which are blocked. |
| Indexes and an archive | A short index in each docs folder lists what is current. Finished material moves to `docs/archive/`, which searches skip by default. |

```
Start of session:   Claude reads CLAUDE.md (rules) and the top of todo.md (where we are)
During work:        notes are left alone; helpers take big jobs, Claude does small edits
Work finishes:      one line ticked in the to-do list; one line added if a decision was made
End of session:     the wrap-up routine fixes any gaps and refreshes the "where we are" block
```

## Brief, plan, then build

By default Claude does not start building straight away. How much planning a request gets depends on its size, and Claude tells you which size it is treating the request as, with a one-line read of how complex it is, and asks you to confirm.

| Size | What it is | What Claude does |
|---|---|---|
| Small change | A fix or tweak inside something that exists. No new capability, data source, database change, dependency or scheduled job; easy to undo; one short sitting. | Adds a line to the to-do list, does it, ticks it. No brief or plan. |
| New feature | A self-contained capability. | A short brief, then a plan, each approved by you, kept in one file in `docs/brief/features/`. Then builds. |
| Set of features | For example an MVP build or a major new area. | The same two approvals with a full product brief and a full implementation plan. Deeper questions. |

If it is unclear which size applies, Claude treats the request as the larger one and says why. There is no project-wide stage. Each feature has its own status: brief, plan, build, live. The to-do list shows each feature in flight with its status. A live feature can still get small tweaks without a new brief.

For every brief and plan, Claude follows the same four steps:
1. Scoping questions. Claude asks only what it needs to be confident enough to write a first draft.
2. Draft and review. Claude writes the draft and sends you a short message with a link to open it, what to look at and the open questions. Then it stops. You read the draft, which often answers questions you would otherwise have to guess, and say when you are ready.
3. Refinement. Claude asks the remaining questions, each with its own context and a recommended option, and writes your answers into the document. You approve it.
4. The brief is approved first, then the plan goes through steps 2 and 3. Claude builds only after the plan is approved.

For work that changes what people see, Claude offers a visual-only mock-up first, with fake data and minimal effort. You review it and commit to the design before any real data or backend work, which avoids rework. You can decline the offer.

Big decisions, such as architecture, tools, language, database, hosting or anything hard to undo, always come to you first, each with Claude's recommendation and the trade-off in plain words. Before Claude calls a feature done, it reports against the brief's success criteria and says plainly if something visual was not viewed. If you change direction or drop a feature, Claude archives its brief and plan and records the decision. Feedback from other people becomes to-do or Parked lines. You can change any of this in the Workflow section of `CLAUDE.md`.

## How Claude asks you questions

Claude Code has a built-in question tool, and the kit tells Claude to use it whenever it is not highly confident it understands a request. Instead of guessing, or burying questions in a long message, Claude shows a short multiple-choice question in the interface. You pick an option with a click, or type your own answer in the "Other" box. Claude puts the option it recommends first and explains each choice in a line, so you can decide quickly without needing the technical background.

Claude asks a few related questions at a time, and a question can be about anything from the wording of the brief to how far a change should go. If Claude has to make an assumption anyway, it says so and asks for your approval first. Your answers feed straight into the notes: an answer that is a decision becomes a line in the decision tracker, and answers while a brief or plan is being written go into that document. Claude asks the up-front scoping questions straight away, but holds the finer refinement questions until you have read the draft and said you are ready. If you would like fewer questions on a small project, relax the "Clarification and assumptions" section of `CLAUDE.md`.

## Where the notes come from

Claude writes the notes from your conversation. You make the decisions and approve; you rarely type a note yourself. You can also say "write that down" at any moment.

| Note | Created when | Written by |
|---|---|---|
| Product brief (`docs/brief/`) | At the start of a set of features such as an MVP, from Claude's questions and your answers. Also the template for feature briefs. Updated when the shape of the product changes. | Claude drafts, you approve |
| Feature brief (`docs/brief/features/`) | When a new feature is asked for. Claude asks scoping questions, writes a short brief, hands it over for you to read, asks the refinement questions when you are ready, and gets your approval. It then adds a plan to the same document and repeats. An index line is added, and it is archived when the feature is live. | Claude drafts, you approve |
| Implementation plan (`docs/planning/`) | After the product brief is approved. Includes a "Technical approach" section for choices such as language, database and hosting, made with you through questions. | Claude drafts, you approve |
| To-do list (`docs/current/todo.md`) | Built from the plan. New ideas are added as next steps or parked as you raise them. Ticked when work lands. | Claude |
| Decision tracker (`docs/current/decision-tracker.md`) | One line each time you decide something, with the reason. | Claude |
| Focused design notes (`docs/planning/`) | When a feature needs thinking through. An index line is added, and the note is archived when the work is finished. | Claude |
| Reference docs (`docs/reference/`) | When something stable needs writing down, such as how to run the project or a map of the code. An index line is added. `what-exists-today.md` is updated each time a feature goes live, so there is always a plain record of what the product does now. | Claude |
| "Where we are" (top of `docs/current/todo.md`) | Rewritten by the wrap-up routine at the end of each session. | Claude |
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

1. Start a session. Open Claude Code in the project folder and start talking. Claude reads its rulebook and the top of the to-do list on its own. If you want a summary, ask "where are we?".
2. Ask for work. Describe what you want. Claude says which size it is treating the work as and asks you to confirm. Then answer its questions as they come up (see "How Claude asks you questions"). For anything beyond a small change, Claude takes you through a brief and a plan before it builds (see "Brief, plan, then build"), and waits for you to read each draft. Later it asks questions if anything is unclear, hands large jobs to a specialist helper and reads only the short report it sends back (see "How helpers work"), and does small edits itself. Anything big or hard to undo comes to you for a decision first.
3. While something is in progress, Claude adds no running commentary to the notes, which keeps them free of clutter. The to-do line goes in when work starts.
4. When a piece of work is done, Claude ticks its line in the to-do list and updates the feature's status. "Done" means the tests pass and the work is saved, and for a feature, that Claude has reported against its success criteria.
5. When you decide something ("let's go with option B"), Claude adds one line to the decision tracker with the reason.
6. At the end of a session, say "run the checkpoint" (or "wrap up"). Claude compares what was saved with what the notes say, fixes anything missed, rewrites the short "where we are" block, saves everything, and tells you what has not been pushed to the shared copy. It asks before pushing.
7. Next session, a fresh Claude picks up from the to-do list.

| You | Claude |
|---|---|
| Say what you want and make the decisions | Asks questions, does or delegates the work, runs the tests |
| Say "run the checkpoint" when you stop | Updates the to-do list (including "where we are") and the decision tracker, then saves |
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
   - Whether the project is new (it starts with a product brief) or already under way, and if so which features exist and what status each has (brief, plan, build or live), and which notes already exist.
   - Whether a git repository exists. If not, run `git init` after asking, and use the main branch name the owner chooses (suggest `main`). Also whether a remote repository exists.
   - The command that runs the tests, and where the tests and main code live. If there are no tests yet, say so: leave the test-command permission line out of `.claude/settings.json` and add "set up tests" as an early step in the plan.
   - The project's guardrails (things agents must never do), if any.
   - Which kinds of work come up often (for example writing code, writing reports, researching), so you know which agents to keep and which new ones to add.
2. Copy the templates from `templates/` into the project root, keeping the folder layout. Replace every `{{PLACEHOLDER}}` using the answers (table below). If an answer is unknown, ask rather than guess.
3. Agents: keep only the agents the project needs. Rewrite each description to name the project's real files and keywords ("Use proactively when..."), and fill the agent table in `CLAUDE.md` (five lines or fewer). Remove any agent file you do not use.
4. Permissions: set the test command prefix in `.claude/settings.json`. Leave project-specific one-off permissions out; they build up in `.claude/settings.local.json`, which stays out of git.
5. Git: make sure `.claude/.gitignore` is in place, create `docs/archive/` (the template `done-log.md` is already there) and `docs/brief/features/`, and make sure the main working folder is on the main branch. Make one initial commit of the setup. Do not push unless asked.
5a. Automatic checks: switch on the hooks in `.githooks/` (see its README): run `git config core.hooksPath .githooks` and `chmod +x .githooks/pre-commit .githooks/pre-push .githooks/claude-edit-hook.sh`. If the main branch is not called `main`, or ruff is not on the path, copy `.githooks/config.sh.example` to `.githooks/config.sh` and edit it. If the project is Python, ask the owner whether to use ruff (a new dev tool, so it needs their approval) and, if yes, copy `templates/python/ruff.toml` to the project root and install ruff. If something runs from a separate copy of the code, copy `.githooks/pre-push-reminder.example.txt` to `.githooks/pre-push-reminder.txt` and edit it. Project-specific checks, such as "a schema change needs a changelog line", go in `.githooks/project-checks.sh` (start from the `.example`). Leave out the files that do not apply. Tell the owner that hooks are per clone, so a fresh clone needs the `git config` line again.
6. Start the notes. Treat a new project as a set of features and follow "How a brief or plan gets agreed" in `CLAUDE.md`: scoping questions with AskUserQuestion, then draft `docs/brief/product-brief.md` from the template, hand it over for review with a link, and stop. When the owner says they are ready, ask the refinement questions and get approval. Then do the same for `docs/planning/implementation-plan.md`, including its "Technical approach" section (language, database, hosting and so on, each asked with a recommendation, and if the owner is not technical, explain the trade-off in plain words). Then build the first "Next steps" in `docs/current/todo.md` from the plan, and fill in the "Where we are" block at the top of that file, listing features in flight with their status. For a project already under way, ask where its existing notes are, summarise them into the two working notes, and record each feature's status.
7. Baseline: run `/context` in a fresh session and note the starting size in `docs/current/decision-tracker.md`, so later changes can be measured.
8. Report to the owner in plain language: what was created, what to review, and the routine in "Day to day" above.

| Placeholder | Filled from |
|---|---|
| `{{PROJECT_NAME}}`, `{{DATE}}` | Project name; today's date |
| `{{ABOUT_ME}}` | The owner's role and how technical they are |
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
    docs/current/todo.md, decision-tracker.md    this project's notes
    .claude/         this project's permissions, helpers and checkpoint skill
  project-b/
```

What goes where:
- The workspace `CLAUDE.md` holds the rules that stay the same across projects: how to communicate, when to ask, how big a job must be before it goes to a helper, and how to handle git. It also lists the projects, one line each. Every session loads it, so keep it short.
- Each project's own `CLAUDE.md` holds only its workflow and sizing rules, its guardrails, its helpers and where its notes are. Use `templates/workspace/project-CLAUDE.md`.
- Each project keeps its own working notes (the to-do list with its "where we are" block, and the decision tracker). Leave project status out of the workspace files; they only point to each project.
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

For a general assistant workspace, keep the rulebook, the two working notes, the wrap-up routine and `shared/` (put your preferences, recurring contacts and context there). Drop the coder helper, the test command and the git rules if there is no repository. Add helpers for the jobs you repeat, such as drafting, research or meeting notes.

## What is inside

| File | What it is |
|---|---|
| `templates/CLAUDE.md` | The rulebook. |
| `templates/docs/current/todo.md`, `templates/docs/current/decision-tracker.md` | The two working notes. |
| `templates/docs/brief/product-brief.md`, `templates/docs/brief/features/`, `templates/docs/planning/implementation-plan.md` | Starting points for the brief (also the template for feature briefs) and the plan that Claude drafts with you. |
| `templates/docs/reference/what-exists-today.md`, `templates/docs/archive/done-log.md` | A short record of what is live, and the log that older "Recently done" lines move to. |
| `templates/.claude/skills/session-checkpoint/` | The wrap-up routine. |
| `templates/.claude/agents/` | Two starter helpers: an implementation coder and a docs maintainer. |
| `templates/.claude/settings.json`, `templates/.claude/.gitignore` | Permissions, the edit-time check hook, and git ignore rules that keep personal settings out of the repository. |
| `templates/.githooks/`, `templates/python/ruff.toml` | The automatic checks: git hooks (main folder stays on the main branch, silencing comments need a reason, no workaround excuses in comments, ruff on new lines) and a starter ruff config for Python projects. Its README explains each check. |
| `templates/docs/brief/README.md`, `templates/docs/planning/README.md`, `templates/docs/reference/README.md`, `templates/.rgignore` | Folder indexes, and the search ignore that skips the archive. |
| `templates/workspace/` | For a workspace that holds several projects: the workspace rulebook, a lean per-project rulebook, the shared-context index, and a checkpoint skill that covers every project. |
| `WHY.md` | How each part works and what it gives you. Start here to understand or change the setup. |

## Things you can change

None of this is fixed. Change what suits your project, and read the matching section of `WHY.md` first so you know what it was doing.

- Workflow and tone: the sizing rules, the review flow and the "Communication" rules in `CLAUDE.md`. If you would rather not plan first on a small project, relax the "plan before coding" rule there.
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

## When the product gets bigger: keep a feature map

This is guidance for a real product with real users, not for a prototype or an MVP. Do not build it earlier.

A feature map is a short list of every screen and control in the product, named from the user's side, for example "the filter bar on the Dashboard" or "the Topic detail page". Keep it in `docs/reference/` and link it from the project's `CLAUDE.md`.

Why it helps: when you say "the thingy in the left sidebar", Claude has to guess which one you mean. With a feature map you and Claude use the same names, and checks that drive the product (a browser test, a screenshot review) can say exactly which part they looked at. Add an entry whenever a feature ships, and remove it when the feature is retired. Source: Lauren Tan's talk "All Code Is Slop (Except Mine)" (AI Engineer CODE 2026), where the team keeps one for their app.

## Keeping the kit current

When your setup improves, change the kit in the same sitting: update the template, then add a line below.

- 23 Nov 2026: first version.
- 23 Nov 2026: added guidance and templates for a workspace that holds several projects; removed MEASURING.md.
- 23 Nov 2026: merged `next-steps.md` into the top of the to-do list, so there are two working notes instead of three.
- 24 Nov 2026 (version 2.0): gap review. Removed the project-wide "Current stage" and added a status per feature (brief, plan, build, live). Added the work-sizing rule (small change, new feature, set of features) with a complexity read and a confirmation step. Added the review hand-over flow (scoping questions, draft with a link, refinement questions when the owner is ready), the visual mock-up option for UI work, a success check before a feature is ticked done, and short procedures for a change of direction and for feedback. Briefs and plans now live per feature in `docs/brief/features/`, using `product-brief.md` as the template. Added a "Technical approach" section to the plan template, `what-exists-today.md`, `docs/archive/done-log.md`, brief reconciliation in both checkpoint skills, and corrected the docs-maintainer's folders. Setup now covers no repository and no tests. Added `git worktree add` and `git merge` to the allowed commands (not yet tested).
- 25 Nov 2026 (version 2.1): automatic checks. Added `templates/.githooks/` (git hooks and an edit-time Claude Code hook: the main folder stays on the main branch, warning-silencing comments need a reason, no workaround excuses in comments, ruff on added lines only, a push reminder, an optional project-specific check) and `templates/python/ruff.toml`. Added the "a correction becomes a check", "automatic checks" and "comments" rules to `templates/CLAUDE.md`, setup step 5a, and the feature-map guidance for bigger products. Source: Lauren Tan's talk "All Code Is Slop (Except Mine)".

## Bringing an existing project up to date

Each project's `CLAUDE.md` ends with a line `Kit version: X`. A project with no such line was set up from version 1.x. To update it:

1. Open Claude Code in the project and say: "Read `<path to this kit>/README.md`. Bring this project up to date with the kit, from the version it was set up with, using 'Bringing an existing project up to date'. Show me each change before you make it."
2. Claude reads the lines above in "Keeping the kit current" that are newer than the project's version, and compares the project's `CLAUDE.md`, working notes, skills and agents with the matching files in `templates/`.
3. For each difference, Claude explains it in plain words and asks whether to apply it. It never overwrites a file without showing the change first, and it keeps anything the project has customised (agents, guardrails, the agent table, project-specific rules).
4. Claude updates the `Kit version` line, runs the checkpoint skill, and commits. It does not push.

For version 2.0, the main changes to carry over are: replace the Workflow section of `CLAUDE.md`; remove the stage line from the "Where we are" block and list features in flight instead; add `docs/brief/features/`, `docs/reference/what-exists-today.md` and `docs/archive/done-log.md`; add the "Technical approach" section to the plan; and update both checkpoint skills and the docs-maintainer agent.
For version 2.1, the main changes to carry over are: copy `.githooks/` and (for Python) `ruff.toml` into the project and follow setup step 5a; add the `hooks` block from `templates/.claude/settings.json` to the project's `.claude/settings.json` without disturbing its permissions; and add the three new bullets ("A correction becomes a check", "Automatic checks", "Comments") to "Engineering principles" in `CLAUDE.md`. Convert the project's own enforceable rules into checks, one at a time, only with the owner's approval. Existing code is not cleaned up: the checks look only at added lines.
