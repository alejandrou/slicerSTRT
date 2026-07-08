# Codex Context Management

## Goal

Use AI heavily, but avoid wasting context.

## Rules

1. Do not load the whole project by default.
2. Start with `AGENTS.md`.
3. Load only the documentation file relevant to the task.
4. Load only the source file that needs to be changed.
5. Search Slicer source only when Slicer API details are needed.
6. Search `slicer-skill` only for Slicer-specific patterns or examples.
7. Start a new chat when changing task.
8. Save reusable conclusions into `docs`.
9. Use cheaper/faster models for documentation and simple edits.
10. Use stronger models for architecture, debugging, C++, MRML, VTK, ITK, CMake, and medical-image logic.

## Prompt pattern

For small tasks:

Read `AGENTS.md` and only the file I mention.
Do not inspect the full repository.

For Slicer API tasks:

Read `AGENTS.md`.
Inspect the local slicerSTRT module.
Then search only the relevant Slicer source folders.
Do not guess APIs.

For architecture tasks:

Read `AGENTS.md`, `project_structure.md`, `coding_standards.md`, and the current module.
Propose a plan before editing.
