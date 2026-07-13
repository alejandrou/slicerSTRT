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

Read-only Git inspection is allowed. Git mutations require an explicit user request.

`.ai/policies/git-workflow.md` is the authoritative owner of Git restrictions and local-change handling.

## MCP Restrictions

MCP is disabled by default.

`.ai/policies/mcp-policy.md` is the authoritative owner of MCP permissions, limits, and evidence requirements.

## Medical Data Restrictions

Private or sensitive medical data and unvalidated clinical use are prohibited.

`.ai/policies/medical-data-policy.md` is the authoritative owner of allowed and prohibited medical data. `.ai/policies/algorithm-boundary-policy.md` is the authoritative owner of algorithm-result validation boundaries.

## Expected Completion Report

For implementation tasks, report:

1. Files inspected.
2. Files created.
3. Files modified.
4. Validation performed and results.
5. How to test manually, including Slicer Reload / Reload and Test when production module code changes.
6. Risks, ambiguities, or follow-up tasks.
