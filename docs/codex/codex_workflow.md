# slicerSTRT Codex Workflow

This project uses Codex inside VS Code.

## How to start a Codex task

Open VS Code at:

`C:\stratum`

Codex should read:

`AGENTS.md`

before working.

## Good prompt pattern

Use prompts like:

"Read AGENTS.md first. Then inspect the current slicerSTRT extension. I want to..."

## Before coding

Codex must:

1. Read `AGENTS.md`
2. Read the relevant docs under `docs`
3. Inspect existing files
4. Explain the intended change
5. Make the smallest useful change

## Slicer questions

For Slicer API questions, Codex must not answer from memory.

It should inspect:

1. `C:\stratum\extensions`
2. `C:\stratum\source`
3. `C:\Users\AlejandroHerrera\.codex\skills\slicer-skill`

## Git rule

Codex must ask before:

- commit
- push
- branch
- merge
- rebase
- reset

## Preferred style

Codex should give:

1. Direct answer
2. Files inspected
3. Exact change
4. How to test it

## Sandbox workflow

For sandbox tasks, start from:

`docs/development/sandbox_roadmap.md`

Use one phase at a time.

Do not ask Codex to implement multiple phases in a single prompt.

Recommended prompt:


Read AGENTS.md and docs/development/sandbox_roadmap.md.
We are working on Phase X only.
Inspect only the files needed for this phase.
Propose the smallest safe change before editing.

## Current learning roadmap

The active learning roadmap is:

`docs/development/sandbox_roadmap.md`

Current status:

- Slicer build works.
- `slicerSTRT` module loads correctly.
- Next recommended phase: Phase 1 — Clean and understand the generated module.


