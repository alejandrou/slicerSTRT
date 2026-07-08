# STRATUM Slicer Codex Instructions

This is a Windows 11 3D Slicer development workspace for STRATUM.

Codex must use this file as the entry point, then read the linked documentation files depending on the task.

## Main paths

- Slicer source root: `C:\stratum\source`
- Slicer build root: `C:\stratum\apps\SR`
- Built Slicer executable: `C:\stratum\apps\SR\Slicer-build\Slicer.exe`
- STRATUM extensions: `C:\stratum\extensions`
- Project documentation: `C:\stratum\docs`
- User Slicer skill: `C:\Users\AlejandroHerrera\.codex\skills\slicer-skill`

## Project documentation to read

Before changing or explaining project structure, read:

- `docs/development/project_structure.md`

Before writing or modifying code, read:

- `docs/development/coding_standards.md`

Before adding or changing tests, read:

- `docs/development/testing_strategy.md`

Before answering Slicer API/module questions, read:

- `docs/slicer/slicer_knowledge_index.md`

Before deciding how to use Codex in this project, read:

- `docs/codex/codex_workflow.md`

## Search order before answering Slicer questions

1. Inspect local STRATUM files first.
2. Then inspect `C:\slicerSTRT\source`.
3. Then inspect `C:\Users\AlejandroHerrera\.codex\skills\slicer-skill`.
4. Do not invent Slicer APIs.
5. Mention exact local paths used as evidence.

## Hard rules

- Do not edit `C:\slicerSTRT\apps\SR` unless explicitly asked.
- Do not edit `C:\slicerSTRT\source` unless explicitly asked.
- Normal project code goes under `C:\slicerSTRT\extensions`.
- Start with Python scripted modules unless C++ or CLI is clearly required.
- Ask before Git operations.
- Prefer small, readable, testable changes.
- The sandbox is for learning only. Do not implement clinical diagnosis, surgical guidance, or real STRATUM algorithms unless explicitly instructed.

Before large AI-assisted tasks, read:

- `docs/codex/context_management.md`

For the human developer workflow, refer to:

- `docs/codex/instructions.md`

Before planning or implementing the STRATUM sandbox roadmap, read:

- `docs/development/sandbox_roadmap.md`
