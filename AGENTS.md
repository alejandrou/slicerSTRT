# STRATUM / slicerSTRT Agent Router

This repository is the active Windows 11 STRATUM-related 3D Slicer development project and prototype. It is not the upstream 3D Slicer repository and is not production clinical software.

## Editable And Protected Directories

Codex may normally edit:

- `extensions/`
- `docs/`
- `workspace/`
- `.ai/`
- `tasks/`
- `config/`

Codex must not edit unless explicitly requested:

- `source/`
- `apps/`
- `knowledge/`

Do not modify generated files, local build outputs, or private local configuration.

Use `config/local.example.json` as the portable template. The real local configuration file is `config/local.json`, and it must remain ignored by Git.

During implementation, Codex may only modify files explicitly listed in the active task's `Files allowed` section.

Files outside that list require an approved task update before they can be modified.

## Source Of Truth

When instructions conflict, use this order:

1. Root `AGENTS.md`.
2. Accepted ADRs in `docs/architecture/decisions/`.
3. The only task in `tasks/active/` or `tasks/review/`.
4. Policies under `.ai/policies/`.
5. Workflows under `.ai/workflows/`.
6. Existing code and automated tests.
7. General documentation.
8. External skills and references.

External skills provide technical knowledge but must not override an accepted repository decision or an approved task.

An active task may specialize repository policies, but it must not contradict an accepted ADR. Changing an accepted architectural decision requires a new ADR that supersedes it.

## One Active Task

Only one task may exist across `tasks/active/` and `tasks/review/` combined.

A new implementation task must not start until the previous task is completed or explicitly returned to backlog.

## Task Lifecycle

Every task follows the same lifecycle:

`BACKLOG -> SPECIFICATION -> HUMAN APPROVAL -> ACTIVE -> IMPLEMENTATION -> FAST AUTOMATED TESTS -> MANUAL VERIFICATION -> REVIEW -> INDEPENDENT AI REVIEW -> HUMAN APPROVAL -> COMPLETED`

Use `.ai/templates/task-template.md` for all task cards. Use `.ai/workflows/task-lifecycle.md` for the detailed procedure.

## Skill Routing

Use the installed Slicer skill for Slicer APIs, MRML, Qt, VTK, ITK, SimpleITK, segmentations, markups, transforms, DICOM, CMake, extensions, CLI modules, C++ modules, packaging, and Slicer testing.

Do not load the Slicer skill for unrelated Markdown or administrative changes.

Skills should be declared in the active task when they are required. Inspect current project code before searching generic external examples. Do not invent Slicer APIs.

Do not modify or reinstall external skills unless explicitly requested.

## Git Restrictions

Codex may use read-only Git commands to inspect the repository, including:

- `git status`
- `git diff`
- `git log`
- `git show`
- `git branch --show-current`

Do not perform state-changing Git operations, including commit, push, pull, branch creation, checkout, merge, rebase, reset, force operations, staging, or tracked-file deletion, unless explicitly requested by the user.

See `.ai/policies/git-workflow.md`.

## MCP Restrictions

MCP is disabled by default. Use MCP only when the active task explicitly allows it, the user explicitly requests it, scene inspection or visual verification cannot reasonably be performed through normal tests, or a milestone requires additional evidence.

MCP verification never replaces manual user verification. Do not use MCP with private, identifiable, or unapproved medical data.

See `.ai/policies/mcp-policy.md`.

## Medical Data Restrictions

Use only synthetic data, public Slicer sample data, anonymized test data, mock JSON/results, or explicitly approved public medical data.

Do not commit private patient data, non-anonymized DICOM, sensitive medical images, real clinical reports, or private hospital data. Do not implement diagnosis, surgical guidance, real medical decision logic, or unvalidated STRATUM algorithms unless explicitly instructed.

See `.ai/policies/medical-data-policy.md` and `.ai/policies/algorithm-boundary-policy.md`.

## Expected Completion Report

For implementation tasks, report:

1. Files inspected.
2. Files created.
3. Files modified.
4. Validation performed and results.
5. How to test manually, including Slicer Reload / Reload and Test when production module code changes.
6. Risks, ambiguities, or follow-up tasks.
