---
name: git-control
description: "Inspect, organize, and prepare Git changes for review in Slicer-related projects. Use when reviewing the working tree, grouping commits, choosing Slicer-style commit messages, or preparing a change for review."
---

# Git Control Skill

Use this skill whenever you need to inspect, organize, commit, or prepare changes for review in a Slicer-related project.

The goal is to keep Git history readable, reviewable, and aligned with Slicer commit message rules.

## Core behavior

Before suggesting or creating any commit, always inspect the current Git state.

Run:

```bash
git status --short
git diff --stat
git diff
```

If there are staged changes, also inspect:

```bash
git diff --cached --stat
git diff --cached
```

Never assume that all changed files belong in the same commit.

Group changes by purpose:

- bug fix
- new feature
- documentation
- refactor or style-only change
- test update
- build/compiler fix
- work in progress

If unrelated changes are mixed together, recommend separate commits.

Do not commit generated files, temporary files, caches, local IDE files, build outputs, logs, or experimental artifacts unless the user explicitly says they should be versioned.

## Safety rules

Do not run `git commit`, `git push`, `git reset --hard`, `git clean`, `git rebase`, or destructive Git commands unless the user explicitly approves.

It is safe to suggest commands.

It is safe to stage specific files only if the user has asked you to prepare a commit.

Prefer explicit staging:

```bash
git add path/to/file.py path/to/file.md
```

Avoid broad staging unless the change set has already been reviewed:

```bash
git add .
git add -A
```

## Commit message format

Use the standard Slicer commit prefixes:

- `BUG:` Fix for runtime crash or incorrect result
- `COMP:` Compiler error or warning fix
- `DOC:` Documentation change
- `ENH:` New functionality
- `PERF:` Performance improvement
- `STYLE:` No logic impact, such as indentation or comments
- `WIP:` Work in progress not ready for merge

The subject line must:

- start with one of the allowed prefixes
- be capitalized after the prefix
- use imperative mood
- not end with a period
- stay below 72 characters, ideally around 50
- describe user-visible intent, not just implementation detail

Good examples:

```text
BUG: Fix crash when applying Stratum analysis
ENH: Add scripted module structure notes
DOC: Document Slicer reload workflow
COMP: Fix Visual Studio build warning in module setup
STYLE: Normalize imports in Stratum widget
WIP: Add initial density map prototype
```

Bad examples:

```text
BUG: Check pointer validity before dereferencing
ENH: More work in widget
COMP: Typo in CMake variable
STYLE: Small changes
DOC: Update docs.
```

## Commit body rules

Add a blank line between the subject and the body.

The body should explain:

- what changed
- why it changed
- how the solution works at a useful level
- any alternatives considered, if relevant
- any known limitations

Wrap the body at approximately 80 characters.

Use semantic line feeds: one idea per line or small paragraph.

If relevant, include:

- Slicer forum links
- GitHub issue closing keywords
- minimal compiler error messages
- regression test references
- commands used to validate the change

Example:

```text
BUG: Fix crash when applying Stratum analysis

The Apply button could run while the selected markups node contained no
control points.

This caused the scripted module logic to access missing point data and fail
during interactive use.

The widget now validates the selected input before enabling Apply.
The logic also keeps a defensive check so the module fails safely if called
from the Python console.

Fixes #123.
```

## Prefix selection guide

Use `BUG:` when the change fixes incorrect behavior, a crash, broken UI flow,
wrong results, or a regression.

Use `ENH:` when the change adds new behavior, a new workflow, a new module
capability, or a user-visible improvement.

Use `DOC:` when only documentation, markdown, comments intended as docs,
README files, or usage instructions change.

Use `COMP:` when the change fixes compiler errors, build failures, dependency
compatibility issues, CMake errors, or warnings.

Use `PERF:` when the main reason for the change is speed, memory usage, loading
time, or computational efficiency.

Use `STYLE:` when there is no logic impact. This includes formatting, import
ordering, indentation, naming cleanup, or comment cleanup.

Use `WIP:` only for temporary commits that are not ready for review or merge.

## Review workflow

When asked to prepare a commit, follow this process:

1. Inspect the working tree.
2. Summarize the changed files.
3. Identify whether changes should be split into multiple commits.
4. Suggest the commit grouping.
5. Suggest one Slicer-style commit message per group.
6. Ask for approval before running commit commands.

When the user wants a commit message only, return only the recommended message.

When the user wants a Git review, include:

- files changed
- likely commit prefix
- whether the commit is clean or should be split
- proposed subject line
- proposed body
- validation commands to run before committing

## Validation before commit

Prefer running relevant checks before committing.

For Python projects, consider:

```bash
python -m pytest
python -m compileall .
```

For Slicer scripted modules, consider:

```bash
python -m compileall path/to/module
```

If tests are not available, say so clearly and suggest the smallest useful
manual validation.

For Slicer modules, useful manual validation may include:

- start Slicer
- load the extension/module path
- use Reload and Test
- open the module UI
- check that widgets enable and disable correctly
- run the main workflow with valid input
- run the workflow with missing or invalid input
- confirm that no Python errors appear in the Slicer console

## Output templates

### Commit review template

```text
Changed files:
- path/to/file.py
- path/to/file.md

Recommended split:
1. DOC: Documentation-only changes
2. ENH: Module behavior changes

Suggested commit message:

ENH: Add Stratum scripted module validation

The module now validates the selected input before running the main logic.

This prevents invalid UI states from reaching the processing layer and makes
the scripted module safer to reload and test during development.
```

### Commit command template

```bash
git add path/to/file.py path/to/file.md

git commit -m "ENH: Add Stratum scripted module validation" -m "The module now validates the selected input before running the main logic.

This prevents invalid UI states from reaching the processing layer and makes
the scripted module safer to reload and test during development."
```

## Final rule

A good commit message should explain the reason for the change better than the
"diff itself can.

Do not describe only the implementation detail.

Describe the meaningful change from the perspective of the project reviewer.
