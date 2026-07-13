---
id: BSSL-002
title: Consolidate and de-duplicate repository documentation
status: review
branch: feature/BSSL-002-documentation-audit
required_skills: []
optional_tools: []
related_adrs: []
---

# BSSL-002 - Consolidate and de-duplicate repository documentation

## Goal

Consolidate legacy repository documentation so every documentation responsibility has one authoritative owner, while preserving useful technical 3D Slicer, scripted-module, MRML, testing, module-architecture, and local-build knowledge.

## Context

BSSL-001 established the repository workflow foundation in root `AGENTS.md`, `.ai/policies/`, `.ai/workflows/`, `.ai/templates/`, and `tasks/`. BSSL-001 is completed and merged into `main`.

Legacy documentation still contains overlapping workflow rules, old `.agents/` references, phase-based roadmap material, and historical project status. Some of that content is obsolete or duplicated by the new `.ai/` source-of-truth structure, but some remains technically valuable and should be preserved, merged, or pointed to from the correct owner instead of deleted casually.

This task is staged. The initial inventory and migration matrix were completed first. The user approved the migration matrix on 2026-07-13 and authorized the consolidation phase described in `Files allowed`.

## Requirements

- Inventory the existing Markdown documentation before consolidation work begins.
- Create a documentation migration matrix before any existing tracked document is deleted, merged, substantially rewritten, or replaced with a pointer.
- Classify every inventoried document as exactly one of:
  - `keep`
  - `keep with minor updates`
  - `merge`
  - `rewrite`
  - `replace with a short pointer`
  - `delete after approval`
- For each document, identify relevant issues, including:
  - duplicated rules;
  - contradictions;
  - obsolete information;
  - outdated project status;
  - old `.agents/` workflow references;
  - phase-based roadmap references;
  - personal absolute paths;
  - broken or outdated internal links.
- Preserve useful technical documentation about:
  - Slicer development;
  - scripted modules;
  - MRML;
  - testing;
  - module architecture;
  - the local build workflow.
- Remove complete policy copies now owned by `.ai/policies/`.
- Remove complete workflow copies now owned by `.ai/workflows/`.
- Replace duplicated rules with short references to the authoritative owner instead of maintaining parallel copies.
- Record the proposed authoritative owner for each migrated responsibility.
- Record explicit user approval of the migration matrix before deleting tracked files.
- Apply only the approved consolidation changes listed in `Files allowed`.
- Confirm that no production code is modified.

## Out of scope

- Production code.
- Slicer module functionality.
- Ruff.
- Pyright.
- PowerShell test automation.
- Slicer test automation.
- Algorithm providers.
- Parameter nodes.
- Datasets.
- MCP.
- Extension restructuring.
- Repository renaming.
- Creating or switching Git branches.
- Committing, pushing, pulling, merging, rebasing, resetting, staging, or deleting tracked files without explicit user request.
- Changing accepted ADRs without a superseding ADR.

## Files allowed

Approved consolidation phase, authorized by the user on 2026-07-13 after review of `docs/planning/BSSL-002-documentation-migration-matrix.md`.

Workflow and legacy documentation authorized for deletion:

- `.agents/**`
- `docs/codex/**`
- `docs/development/sandbox_roadmap.md`
- `tasks/phase_2a_check_environment.md`
- `tasks/phase_2b_volume_metadata.md`
- `tasks/phase_2c_template_cleanup.md`

Current documentation authorized for modification:

- `AGENTS.md`, only when links or references require correction
- `.ai/policies/medical-data-policy.md`
- `.ai/workflows/manual-verification-workflow.md`
- `README.md`
- `README_Stratum_Slicer_Build.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/slicer/slicer_knowledge_index.md`
- `docs/slicer/slicer_module_architecture.md`
- `docs/slicer/scripted_module_structure.md`
- `docs/knowledge/README.md`
- `docs/planning/BSSL-002-documentation-migration-matrix.md`
- `tasks/active/BSSL-002-consolidate-repository-documentation.md`

No other file is authorized for modification or deletion.

Do not modify:

- `extensions/**`
- `source/**`
- `apps/**`
- `knowledge/**`
- production Python
- production CMake
- UI files
- tests
- generated files
- dependencies

## Relevant skills and references

No external skill is required for the initial documentation inventory and migration matrix.

The Slicer skill should be used only if a later approved consolidation phase needs to validate Slicer-specific API, MRML, Qt, VTK, ITK, CMake, extension packaging, or Slicer testing guidance. External skills must not override root `AGENTS.md`, accepted ADRs, `.ai/policies/`, `.ai/workflows/`, or the approved task card.

References for planning and ownership:

- `AGENTS.md`
- `.ai/workflows/task-lifecycle.md`
- `.ai/workflows/planning-workflow.md`
- `.ai/policies/*.md`
- `.ai/templates/task-template.md`
- `tasks/completed/BSSL-001-ai-development-workflow.md`

Known documentation candidates from BSSL-001 completion evidence and current Markdown layout include:

- `README.md`
- `README_Stratum_Slicer_Build.md`
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
- `docs/slicer/slicer_knowledge_index.md`
- `docs/slicer/slicer_module_architecture.md`
- `docs/slicer/scripted_module_structure.md`
- `docs/knowledge/README.md`
- `tasks/phase_2a_check_environment.md`
- `tasks/phase_2b_volume_metadata.md`
- `tasks/phase_2c_template_cleanup.md`

## Implementation plan

1. Inventory existing Markdown documentation and `.agents/` documentation candidates without changing them.
2. Create `docs/planning/BSSL-002-documentation-migration-matrix.md` with one row per inventoried document.
3. In the matrix, classify each document, identify duplicated or obsolete content, record useful technical content to preserve, and name the authoritative owner or proposed destination.
4. Stop and request user review and explicit approval of the migration matrix before deleting, merging, substantially rewriting, or replacing any tracked documentation.
5. After approval, update this task card with the exact files allowed for the approved consolidation phase.
6. Apply only the approved consolidation changes.
7. Validate remaining documentation links and ownership references.
8. Copy a concise migration summary into this task card.
9. Delete `docs/planning/BSSL-002-documentation-migration-matrix.md` after its summary is recorded here.
10. Record completion evidence, manual verification needs, and any deferred follow-up tasks.

## Acceptance criteria

- The initial implementation produces only a Markdown documentation inventory and migration matrix.
- The migration matrix covers every existing Markdown documentation file and `.agents/` documentation file considered by the task.
- Every inventoried document is classified as `keep`, `keep with minor updates`, `merge`, `rewrite`, `replace with a short pointer`, or `delete after approval`.
- The matrix identifies duplicated rules, contradictions, obsolete information, outdated project status, old `.agents/` workflow references, phase-based roadmap references, personal absolute paths, and broken or outdated internal links where present.
- The matrix identifies useful Slicer development, scripted-module, MRML, testing, module-architecture, and local-build content that must be preserved.
- No tracked file is deleted before explicit user approval of the migration matrix.
- No existing tracked documentation is merged or substantially rewritten before explicit user approval of the migration matrix.
- Complete policy copies are removed or replaced only after confirming the authoritative owner under `.ai/policies/`.
- Complete workflow copies are removed or replaced only after confirming the authoritative owner under `.ai/workflows/`.
- Duplicated rules that remain outside their authoritative owner are reduced to short references.
- The final documentation set has one authoritative owner for each documentation responsibility touched by this task.
- No files under `extensions/`, `source/`, `apps/`, or `knowledge/` are modified.
- No production CMake or Python files are modified.

## Test plan

- Use filename-level Markdown discovery to confirm the inventory is complete.
- Review the migration matrix against `.ai/policies/`, `.ai/workflows/`, root `AGENTS.md`, accepted ADRs, and the relevant legacy documents.
- Search remaining documentation for old `.agents/` workflow references, phase-based roadmap references, personal absolute paths, stale project-status claims, and duplicated policy or workflow copies.
- Check internal Markdown links in touched documentation.
- Confirm any deleted, merged, substantially rewritten, or pointer-replaced tracked document appears in the approved migration matrix.
- Confirm no files under `extensions/`, `source/`, `apps/`, or `knowledge/` were modified.
- Confirm no production CMake or Python files were modified.

## Manual verification

Before consolidation changes, the user must review and explicitly approve:

- `docs/planning/BSSL-002-documentation-migration-matrix.md`;
- the classification for each document;
- proposed authoritative owners;
- proposed deletions;
- proposed merges, rewrites, and pointer replacements.

After consolidation changes, the user should manually review:

- every deleted, merged, substantially rewritten, or pointer-replaced document;
- preserved Slicer and build documentation;
- remaining references to `.ai/policies/`, `.ai/workflows/`, and `AGENTS.md`;
- the final deferred-follow-up list.

No Slicer Reload or Reload and Test verification is required because this task must not modify production Slicer module code.

## Risks

- The task may be too broad if it attempts to inventory, approve, consolidate, and verify all documentation in one pass.
- Useful technical Slicer or build guidance could be lost if legacy documents are reduced to pointers too aggressively.
- Some old phase-based documents may be better marked archival than deleted.
- Link checking may expose unrelated documentation cleanup that should be deferred.
- The approved consolidation phase may require splitting into smaller follow-up tasks if the migration matrix identifies many substantial rewrites.

## Documentation impact

This task is documentation-only. It should clarify authoritative ownership, reduce duplicated rules, and preserve useful technical knowledge in the correct place.

The expected new planning artifact is:

- `docs/planning/BSSL-002-documentation-migration-matrix.md`

## Completion evidence

Initial inventory phase completed on 2026-07-13.

The user reviewed and approved `docs/planning/BSSL-002-documentation-migration-matrix.md` on 2026-07-13 and authorized the consolidation phase. The task card was updated with exact allowed modifications and deletions before legacy documentation was changed.

Approved BSSL-002 correction pass applied on 2026-07-13:

- Corrected `docs/slicer/scripted_module_structure.md` after read-only inspection of `extensions/slicerSTRT/slicerSTRT/`.
- Restored concise local build helper script commands for clean build, incremental build, and optional launch in `README_Stratum_Slicer_Build.md`.
- Added explicit executable result checks for `apps/SR/Slicer-build/Slicer.exe` and `apps/SR/Slicer-build/bin/Release/SlicerApp-real.exe`.
- Clarified that exact Qt and CMake paths belong in local build scripts or local environment variables, not unsupported `config/local.json` fields.
- Clarified ownership of root `knowledge/` versus `docs/knowledge/` in the README, project structure guide, and knowledge README.
- Confirmed no production module parameter-node wrapper or sample-data registration function is documented as implemented.

Files modified by this correction pass:

- `README.md`
- `README_Stratum_Slicer_Build.md`
- `docs/development/project_structure.md`
- `docs/knowledge/README.md`
- `docs/slicer/scripted_module_structure.md`
- `tasks/active/BSSL-002-consolidate-repository-documentation.md`

Files inspected:

- `AGENTS.md`
- `README.md`
- `README_Stratum_Slicer_Build.md`
- `config/local.example.json`
- `.ai/policies/algorithm-boundary-policy.md`
- `.ai/policies/code-quality.md`
- `.ai/policies/dependency-policy.md`
- `.ai/policies/git-workflow.md`
- `.ai/policies/mcp-policy.md`
- `.ai/policies/medical-data-policy.md`
- `.ai/workflows/implementation-workflow.md`
- `.ai/workflows/manual-verification-workflow.md`
- `.ai/workflows/planning-workflow.md`
- `.ai/workflows/review-workflow.md`
- `.ai/workflows/task-lifecycle.md`
- `.ai/templates/adr-template.md`
- `.ai/templates/review-template.md`
- `.ai/templates/task-template.md`
- `.agents/task_protocol.md`
- `.agents/slicer_workflow.md`
- `.agents/code_style.md`
- `.agents/review_checklist.md`
- `.agents/skills/git-control/SKILL.md`
- `docs/codex/codex_workflow.md`
- `docs/codex/context_management.md`
- `docs/codex/context_handoff.md`
- `docs/codex/instructions.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/development/sandbox_roadmap.md`
- `docs/knowledge/README.md`
- `docs/slicer/slicer_knowledge_index.md`
- `docs/slicer/slicer_module_architecture.md`
- `docs/slicer/scripted_module_structure.md`
- `tasks/phase_2a_check_environment.md`
- `tasks/phase_2b_volume_metadata.md`
- `tasks/phase_2c_template_cleanup.md`
- `tasks/completed/BSSL-001-ai-development-workflow.md`
- `tasks/active/BSSL-002-consolidate-repository-documentation.md`
- `docs/planning/BSSL-002-documentation-migration-matrix.md`
- `extensions/slicerSTRT/**` read-only, only to confirm the documented scripted-module structure
- `extensions/slicerSTRT/slicerSTRT/slicerSTRT.py` read-only, to confirm entry-point responsibilities
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/__init__.py` read-only, to confirm exported helper classes
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTLogic.py` read-only, to confirm current logic class and methods
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py` read-only, to confirm widget responsibilities
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py` read-only, to confirm test coverage focus

Files created:

- `docs/planning/BSSL-002-documentation-migration-matrix.md`

Files deleted:

- `.agents/code_style.md`
- `.agents/review_checklist.md`
- `.agents/skills/git-control/SKILL.md`
- `.agents/slicer_workflow.md`
- `.agents/task_protocol.md`
- `docs/codex/codex_workflow.md`
- `docs/codex/context_handoff.md`
- `docs/codex/context_management.md`
- `docs/codex/instructions.md`
- `docs/development/sandbox_roadmap.md`
- `tasks/phase_2a_check_environment.md`
- `tasks/phase_2b_volume_metadata.md`
- `tasks/phase_2c_template_cleanup.md`

Directories deleted:

- `.agents/`
- `docs/codex/`

Files rewritten:

- `README.md`
- `README_Stratum_Slicer_Build.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/slicer/slicer_knowledge_index.md`
- `docs/slicer/slicer_module_architecture.md`
- `docs/slicer/scripted_module_structure.md`
- `docs/knowledge/README.md`
- `.ai/policies/medical-data-policy.md`
- `.ai/workflows/manual-verification-workflow.md`

Files updated:

- `README.md`
- `README_Stratum_Slicer_Build.md`
- `docs/development/project_structure.md`
- `docs/knowledge/README.md`
- `docs/slicer/scripted_module_structure.md`
- `tasks/active/BSSL-002-consolidate-repository-documentation.md`

Files intentionally retained:

- `AGENTS.md`: no links to deleted files required correction.
- `.ai/policies/*.md`: authoritative repository policies.
- `.ai/workflows/*.md`: authoritative repository workflows.
- `.ai/templates/*.md`: authoritative task, ADR, and review templates.
- `tasks/completed/BSSL-001-ai-development-workflow.md`: historical completion evidence, not active guidance.
- `docs/architecture/decisions/.gitkeep`: preserves the ADR directory.
- `docs/knowledge/.gitkeep`: preserves the knowledge directory.

Unique technical information preserved:

- Local Slicer build prerequisites, configuration, clean/incremental build helper commands, optional launcher command, executable result checks, Reload versus rebuild guidance, and troubleshooting were preserved in `README_Stratum_Slicer_Build.md`.
- Repository folder responsibilities and extension development locations were preserved in `docs/development/project_structure.md`.
- UI, logic, test, naming-with-units, coordinate-system naming, cohesion, and comment guidance were preserved in `docs/development/coding_standards.md`.
- Logic-first tests, Slicer Reload/Reload and Test, synthetic/public/anonymized/mock data, and manual verification references were preserved in `docs/development/testing_strategy.md`.
- Slicer search order and local verification expectations were preserved in `docs/slicer/slicer_knowledge_index.md`.
- MRML, module entry point, widget, logic, tests, parameter nodes, Qt `.ui` files, and architectural mistakes were preserved in `docs/slicer/slicer_module_architecture.md`.
- Current scripted-module layout and Reload guidance were preserved in `docs/slicer/scripted_module_structure.md`. The logic documentation now reflects the current `slicerSTRTLogic` implementation: environment reporting, import/package checks, selected-volume metadata inspection, and report formatting. It does not claim that a production parameter-node wrapper or sample-data registration function exists.
- `knowledge/` is documented as ignored local reference material, downloaded files, and private working notes. `docs/knowledge/` is documented as curated, non-sensitive, version-controlled reference notes useful to the project.

Final documentation tree after deleting the temporary matrix:

```text
AGENTS.md
README.md
README_Stratum_Slicer_Build.md
.ai/
  policies/
  templates/
  workflows/
docs/
  architecture/decisions/
  development/
  knowledge/
  slicer/
tasks/
  active/
  backlog/
  completed/
  review/
config/
```

Migration matrix lifecycle:

- The migration matrix was used to guide consolidation.
- Its final summary was copied into this task card.
- `docs/planning/BSSL-002-documentation-migration-matrix.md` was deleted after this evidence was recorded.
- `docs/planning/` was removed because it became empty and had no continuing responsibility.

Validation performed and results:

- `rg --files -g "*.md"` was used to inventory Markdown files.
- `Get-ChildItem -LiteralPath .agents -Recurse -File` was used to inventory legacy `.agents/` files.
- `Get-ChildItem -LiteralPath tasks\active -File` and `Get-ChildItem -LiteralPath tasks\review -File` confirmed one task card across active/review: `tasks/active/BSSL-002-consolidate-repository-documentation.md`; `.gitkeep` files are not task cards.
- `rg --files extensions/slicerSTRT/slicerSTRT` listed the current scripted-module files without modifying them.
- `rg -n "^(class|def)\s+|registerSampleData|parameterNode|ParameterNode|slicerSTRT" extensions/slicerSTRT/slicerSTRT/...` confirmed `slicerSTRTLogic.py` currently defines `slicerSTRTLogic` and not `registerSampleData()` or `slicerSTRTParameterNode`.
- Read-only inspection of `slicerSTRTLogic.py` confirmed current responsibilities: `collectEnvironmentReport`, `formatEnvironmentReport`, `inspectVolumeMetadata`, and `formatVolumeMetadataReport`.
- Targeted search confirmed the build guide includes clean build, incremental build, optional launcher, x64 Native Tools Command Prompt guidance, and executable checks for `apps/SR/Slicer-build/Slicer.exe` and `apps/SR/Slicer-build/bin/Release/SlicerApp-real.exe`.
- Targeted search found no unsupported Qt or CMake path fields in `README_Stratum_Slicer_Build.md` or `config/local.example.json`; exact Qt and CMake paths are directed to local build scripts or local environment variables.
- Targeted search confirmed distinct documented responsibilities for root `knowledge/` and `docs/knowledge/`.
- Scoped Markdown link check across retained repository documentation found no broken relative Markdown links after the correction pass.
- Targeted retained-doc search across `README.md`, `README_Stratum_Slicer_Build.md`, `AGENTS.md`, `docs/`, and `.ai/` found no obsolete `.agents`, `docs/codex`, phase-roadmap, context-handoff, or personal absolute-path references.
- Full repository Markdown search still finds legacy path names only in historical/completion task-card evidence and this active task card's approved scope/evidence, not in active guidance documentation.
- `git diff --name-only -- '*.py' '*.cmake' 'CMakeLists.txt' '*.ui' 'extensions/**' 'source/**' 'apps/**' 'knowledge/**'` reported no production code, production CMake, UI, generated output, protected-directory, or dependency changes.
- `Get-ChildItem -LiteralPath tasks\active,tasks\review -File | Where-Object { $_.Name -ne '.gitkeep' }` confirmed `tasks/active/BSSL-002-consolidate-repository-documentation.md` remains the only active or review task card.
- Read-only Git inspection was used: `git branch --show-current` reported `feature/BSSL-002-documentation-audit`.
- Read-only Git inspection was used: `git status --short` reported `?? tasks/active/BSSL-002-consolidate-repository-documentation.md` before matrix creation. This pre-existing untracked task-card state was not reverted.
- After matrix creation, `git status --short` reported only untracked `docs/planning/` and `tasks/active/BSSL-002-consolidate-repository-documentation.md`.
- `git diff --name-only` reported no tracked-file diff because the changed task card and new matrix are currently untracked.
- `git ls-files --others --exclude-standard` reported `docs/planning/BSSL-002-documentation-migration-matrix.md` and `tasks/active/BSSL-002-consolidate-repository-documentation.md`.
- `config/local.example.json` exists and contains placeholder paths, not personal local paths.
- Deleted-path existence checks confirmed `.agents/`, `docs/codex/`, `docs/development/sandbox_roadmap.md`, and old phase task files no longer exist.
- Deleted-path existence checks confirmed `docs/planning/` and `docs/planning/BSSL-002-documentation-migration-matrix.md` no longer exist.
- Scoped Markdown link check across retained repository documentation found no broken relative Markdown links.
- Targeted retained-doc search found no references to `.agents`, `docs/codex`, `sandbox_roadmap`, old phase task files, stale context-handoff/current-state instructions, `C:\stratum`, or `C:\Users`.
- Redundancy search found complete policy and workflow owner text only in the authoritative `.ai/policies/` and `.ai/workflows/` files.
- Exactly one task card exists across `tasks/active/` and `tasks/review/`: this BSSL-002 task card.
- No files under `extensions/`, `source/`, `apps/`, or `knowledge/` were modified.
- No production Python, CMake, UI, image, generated file, dependency file, Slicer source, or Slicer build output was modified.

Read-only Git validation:

- `git status --short` was used to inspect the final working tree.
- Final `git status --short` showed only approved documentation modifications.
- No commit, push, pull, branch creation, checkout, merge, rebase, reset, staging, or Git deletion command was run.

Authoritative policy and workflow owners:

- Editable/protected paths and source-of-truth routing: `AGENTS.md`.
- Git restrictions: `.ai/policies/git-workflow.md`.
- MCP restrictions: `.ai/policies/mcp-policy.md`.
- Medical-data restrictions: `.ai/policies/medical-data-policy.md`.
- Algorithm-boundary validation: `.ai/policies/algorithm-boundary-policy.md`.
- Dependency policy: `.ai/policies/dependency-policy.md`.
- Code-quality policy: `.ai/policies/code-quality.md`.
- Task lifecycle: `.ai/workflows/task-lifecycle.md`.
- Planning workflow: `.ai/workflows/planning-workflow.md`.
- Implementation workflow: `.ai/workflows/implementation-workflow.md`.
- Review workflow: `.ai/workflows/review-workflow.md`.
- Manual verification workflow: `.ai/workflows/manual-verification-workflow.md`.
- Task template: `.ai/templates/task-template.md`.
- ADR template: `.ai/templates/adr-template.md`.
- Review template: `.ai/templates/review-template.md`.
- Current task scope: this task card.

Remaining risks and ambiguities:

- `tasks/completed/BSSL-001-ai-development-workflow.md` still contains historical references to legacy files as completion evidence. It is intentionally retained and was not authorized for modification in this consolidation phase.
- The documentation points to `config/local.json` for supported local Slicer path fields, while exact Qt and CMake paths depend on the user's private local build scripts or environment variables.
- No Slicer runtime verification was performed because this task is documentation-only and did not modify production module code.

Manual verification required before independent review:

- Review `README.md` and `README_Stratum_Slicer_Build.md` for clarity and current local build accuracy.
- Review `docs/development/` and `docs/slicer/` to confirm useful technical knowledge was preserved without obsolete workflow content.
- Confirm `.agents/`, `docs/codex/`, `docs/development/sandbox_roadmap.md`, and old phase task files are gone.
- Confirm `config/local.example.json` remains portable and `config/local.json` remains private.
- Confirm no Slicer Reload or Reload and Test is needed because production module code was not modified.

## Review findings

Pending.

## Human approval

Pending.
