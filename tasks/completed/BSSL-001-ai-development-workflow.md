---
id: BSSL-001
title: Establish the AI development workflow foundation
status: completed
branch: feature/BSSL-001-ai-development-workflow
required_skills: []
optional_tools: []
related_adrs: []
---

# BSSL-001 - Establish the AI development workflow foundation

## Goal

Establish a minimal, reliable, and traceable Codex development workflow for this Windows 11 and 3D Slicer repository.

## Context

This repository is the active SLIAFlow-related 3D Slicer learning sandbox. The workflow must describe how this repository is developed now, not how a future repository might be onboarded or migrated.

## Requirements

- Refactor root `AGENTS.md` into a short router.
- Establish `.ai/policies/`, `.ai/workflows/`, and `.ai/templates/`.
- Establish `tasks/backlog/`, `tasks/active/`, `tasks/review/`, and `tasks/completed/`.
- Establish `docs/architecture/decisions/`.
- Create `config/local.example.json`.
- Ignore `config/local.json`.
- Support specification-driven development with one active task at a time.
- Require human approval before implementation and before completion.
- Separate planning, implementation, review, and manual verification procedures.
- Preserve traceability between task cards, ADRs, code, tests, manual verification, review findings, and completion evidence.
- Keep MCP disabled by default.
- Keep Git actions disabled unless explicitly requested.
- Use only synthetic, anonymized, mock, public sample, or explicitly approved public medical data.

## Out of scope

- Modifying production code under `extensions/`.
- Modifying `source/`, `apps/`, or `knowledge/`.
- Adding dependencies.
- Configuring Ruff or Pyright.
- Creating PowerShell test scripts.
- Implementing Slicer features, algorithm providers, prototype functionality, or `parameterNodeWrapper`.
- Using MCP.
- Creating a Git branch.
- Committing, pushing, merging, rebasing, resetting, or deleting tracked files.
- Deleting or rewriting existing tracked documentation.

## Files allowed

- `AGENTS.md`
- `.gitignore`
- `.ai/**`
- `tasks/**`
- `docs/architecture/decisions/**`
- `config/local.example.json`

## Relevant skills and references

No external skill is required for this Markdown and repository-workflow task.

The Slicer skill is intentionally not loaded because this task does not ask for Slicer APIs, MRML, Qt, VTK, ITK, CMake, extension packaging, or Slicer testing details.

References inspected:

- `AGENTS.md`
- `.agents/task_protocol.md`
- `.agents/slicer_workflow.md`
- `.agents/code_style.md`
- `.agents/review_checklist.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/development/sandbox_roadmap.md`
- `docs/codex/codex_workflow.md`
- `docs/codex/context_management.md`
- `docs/codex/context_handoff.md`
- `docs/codex/instructions.md`
- `tasks/phase_2a_check_environment.md`
- `tasks/phase_2b_volume_metadata.md`
- `tasks/phase_2c_template_cleanup.md`

## Implementation plan

1. Create the required `.ai/`, `tasks/`, `docs/architecture/decisions/`, and `config/` structure.
2. Add focused policy, workflow, and template files without duplicating the same rule everywhere.
3. Refactor root `AGENTS.md` into a short router.
4. Add `config/local.example.json` and ignore `config/local.json`.
5. Record existing documentation consolidation candidates for BSSL-002.
6. Run validation checks that do not require Slicer, MCP, Git commands, or new dependencies.

## Acceptance criteria

- Root `AGENTS.md` defines repository identity, editable/protected directories, source-of-truth hierarchy, one-active-task rule, lifecycle, skill routing, Git restrictions, MCP restrictions, medical-data restrictions, and expected completion report.
- All required `.ai/` policy, workflow, and template files exist.
- Required task directories exist.
- `tasks/active/BSSL-001-ai-development-workflow.md` exists and uses the task template.
- `docs/architecture/decisions/` exists.
- `config/local.example.json` exists with portable placeholder paths.
- `config/local.json` is ignored by `.gitignore`.
- Exactly one task exists across `tasks/active/` and `tasks/review/`.
- No production module files are modified.

## Test plan

- Confirm required workflow files exist.
- Confirm exactly one task exists in `tasks/active/` and `tasks/review/` combined.
- Confirm `.gitignore` contains `config/local.json`.
- Confirm `AGENTS.md` references existing files.
- Search new files for obvious duplicated workflow rules.
- Confirm no files under `extensions/`, `source/`, or `apps/` were intentionally modified.

## Manual verification

The user should manually review:

- `AGENTS.md`
- `.ai/policies/*.md`
- `.ai/workflows/*.md`
- `.ai/templates/*.md`
- `tasks/active/BSSL-001-ai-development-workflow.md`
- `config/local.example.json`

No Slicer manual verification is required because this task does not modify production module code.

## Risks

- Existing docs still contain overlapping legacy workflow guidance until BSSL-002 consolidates them.
- The active BSSL-001 task remains in `tasks/active/` until the user approves moving it through review and completion.
- Without Git commands, validation relies on file inspection and intended edit scope rather than repository status output.

## Documentation impact

The new source of truth for AI workflow is:

1. `AGENTS.md`
2. `.ai/policies/`
3. `.ai/workflows/`
4. `.ai/templates/`
5. `tasks/`
6. `docs/architecture/decisions/`

Existing docs should be consolidated in BSSL-002 rather than deleted or rewritten in this task.

## Completion evidence

Created workflow foundation files and validated the BSSL-001 acceptance criteria on 2026-07-12.

Validation performed and results:

- Required files and directories exist: `AGENTS.md`, `.gitignore`, `.ai/policies/*.md`, `.ai/workflows/*.md`, `.ai/templates/*.md`, `tasks/backlog/`, `tasks/active/`, `tasks/review/`, `tasks/completed/`, `docs/architecture/decisions/`, and `config/local.example.json`.
- Exactly one task card exists across `tasks/active/` and `tasks/review/`: `tasks/active/BSSL-001-ai-development-workflow.md`. `tasks/review/.gitkeep` is present but is not a task card.
- `config/local.json` is ignored by Git through `.gitignore` entry `/config/local.json`, confirmed with `git check-ignore -v config/local.json`.
- Paths referenced by `AGENTS.md` exist, except `config/local.json`, which is intentionally private, ignored by Git, and not created by this task.
- Read-only Git inspection commands were used during validation, including `git status`, `git diff`, and `git check-ignore`.
- No Git-visible modifications or untracked files were found under `extensions/`, `source/`, or `apps/`.
- Reviewed the new `.ai/` policy, workflow, and template files for obvious rule duplication. The remaining repeated guidance is intentional routing overlap: root `AGENTS.md` names the repository-level rule, and the focused policy/workflow file gives the procedure or limits.
- No state-changing Git operation was performed. No commit, push, pull, branch creation or switch, merge, rebase, reset, staging, tracked-file deletion, Slicer, MCP, dependency, or production-code action was performed.

Manual verification recorded from the user:

- `AGENTS.md` is a short repository router.
- `.ai/policies/` contains mandatory rules.
- `.ai/workflows/` contains procedures.
- `.ai/templates/` contains reusable structures.
- `.ai/project-context/` does not exist.
- Exactly one task exists across `tasks/active/` and `tasks/review/`.
- `config/local.example.json` uses portable placeholder paths.
- `config/local.json` is ignored by Git.
- No production code under `extensions/` was modified.
- No files under `source/` or `apps/` were modified.

Independent review and closeout evidence:

- Independent AI review result: `APPROVE WITH MINOR CHANGES`.
- No `BLOCKING` findings were reported.
- No `IMPORTANT` findings were reported.
- All approved minor findings were resolved.
- Human approval for completion was granted on 2026-07-12.
- Legacy-document consolidation was explicitly deferred to `BSSL-002 - Consolidate and de-duplicate repository documentation`.

Deferred work for `BSSL-002 - Consolidate and de-duplicate repository documentation`:

The independent review found legacy documentation duplication in the existing `.agents/`, `docs/codex/`, development, Slicer, task, and README documentation. This is deferred to BSSL-002. No legacy documentation was consolidated or modified in BSSL-001.

BSSL-002 should assess these existing documentation files for consolidation or retirement:

- `.agents/task_protocol.md`
- `.agents/slicer_workflow.md`
- `.agents/code_style.md`
- `.agents/review_checklist.md`
- `docs/codex/codex_workflow.md`
- `docs/codex/context_management.md`
- `docs/codex/context_handoff.md`
- `docs/codex/instructions.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/development/sandbox_roadmap.md`
- `tasks/phase_2a_check_environment.md`
- `tasks/phase_2b_volume_metadata.md`
- `tasks/phase_2c_template_cleanup.md`
- `README.md`
- `README_SLIAFlow_Build.md`

## Review findings

Independent AI review completed with result: `APPROVE WITH MINOR CHANGES`.

No `BLOCKING` or `IMPORTANT` findings were reported.

Approved minor findings resolved in BSSL-001:

- Corrected Git validation evidence to state that read-only Git inspection commands were used.
- Recorded manual verification evidence from the user.

Deferred follow-up:

- Legacy documentation duplication is deferred to `BSSL-002 - Consolidate and de-duplicate repository documentation`.

## Human approval

Human approval to complete BSSL-001 was granted by the user on 2026-07-12 after:

- implementation was completed;
- structural validation passed;
- manual verification was completed by the user;
- independent review returned `APPROVE WITH MINOR CHANGES`;
- all approved minor findings were resolved;
- legacy-document consolidation was deferred to BSSL-002.
