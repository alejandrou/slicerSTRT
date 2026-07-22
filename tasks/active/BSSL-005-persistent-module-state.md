---
id: BSSL-005
title: Introduce persistent module state
status: active
branch: feature/BSSL-005-persistent-module-state
priority: high
depends_on: BSSL-004
required_skills: [slicer]
optional_tools: []
related_adrs: []
---

# BSSL-005 - Introduce persistent module state

## Goal

Persist the selected input-volume reference in MRML using Slicer's supported typed parameter-node wrapper so the selection survives scene save/load and remains synchronized with the module UI.

## Context

The current `slicerSTRTWidget` reads `inputVolumeNodeComboBox` directly when inspection is requested. `slicerSTRTLogic.getParameterNode()` provides the supported singleton scripted-module node, and the current Slicer source demonstrates typed `parameterNodeWrapper` state plus scene-close observers. BSSL-004 supplies the repeatable Slicer test runner required to validate this behavior.

## Requirements

- Add a typed `slicerSTRTParameterNode` wrapper with one optional `inputVolumeNode` MRML reference.
- Store and retrieve that reference through the singleton parameter node returned by `slicerSTRTLogic.getParameterNode()`.
- Synchronize the combo box to MRML on every user selection change and synchronize MRML to the combo box whenever the parameter node changes.
- Initialize the wrapper when the module is set up or entered; release the wrapper before scene close and recreate it after close only when the module is entered.
- Keep the default state empty. Do not automatically select a scene volume.
- Preserve the existing inspection behavior, but make it read the persistent `inputVolumeNode` state.
- Add focused synthetic-MRML tests for default state, setting/clearing the reference, and scene save/load persistence.

## Out of scope

- Algorithm providers, processing behavior, or result generation.
- Clinical data or clinical claims.
- Unrelated UI redesign or persistence of transient presentation details.
- Persisting environment reports, inspection reports, status labels, button state, or collapsible-panel presentation state.
- New dependencies, CMake test registration changes, or changes outside the `slicerSTRT` extension and this task card.

## Files allowed

Implementation files approved for this task:

- `extensions/slicerSTRT/slicerSTRT/CMakeLists.txt`
- `extensions/slicerSTRT/slicerSTRT/Testing/Python/slicerSTRTModuleTest.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTParameterNode.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`
- `tasks/active/BSSL-005-persistent-module-state.md`

## Relevant skills and references

- Slicer skill for MRML scene and parameter-node patterns.
- Dependency: BSSL-004.
- Current Slicer source: `Base/Python/slicer/parameterNodeWrapper/` and `Modules/Scripted/VectorToScalarVolume/VectorToScalarVolume.py`.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTLogic.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`

## Implementation plan

1. Define the typed wrapper in a dedicated state-support file and package it as a module Python script.
2. Add widget ownership, observer lifecycle, and guarded two-way synchronization around the existing volume selector.
3. Route inspection through the persisted reference without persisting transient report UI.
4. Add synthetic-MRML tests for empty, set/clear, and saved/reloaded state.
5. Keep the existing thin unittest discovery adapter Ruff-compliant while running the Slicer test runner and Python quality checks; record results below.

## Acceptance criteria

- The selected input volume is represented by the singleton `slicerSTRT` scripted-module parameter node and is restored after a saved scene is loaded.
- Changing the selector updates the parameter-node reference; changing the parameter-node reference updates the selector without recursion.
- The default and cleared states are `None`, and closing a scene does not leave the widget holding a stale parameter node.
- Environment and inspection output remain transient and existing inspection results remain correct.
- Automated tests cover empty/default, setting, clearing, and save/load persistence with synthetic MRML data.

## Test plan

Run `scripts/development/run-slicer-tests.ps1` from the repository root. The existing module test suite must pass, including new synthetic-MRML state tests for default, set, clear, and save/load behavior. Run `scripts/development/run-python-quality.ps1` with the ignored root `.venv` activated. No private or sensitive medical data may be used.

## Manual verification

In Slicer, open `slicerSTRT`, select and clear a synthetic or public sample volume, save and reopen the scene to confirm the selection returns, then close/open a scene to confirm the empty default and no stale UI. Use Reload and Reload and Test; record the owner-provided results later. Manual verification is not complete in this task activation.

## Risks

Incorrect observer cleanup could retain a cleared parameter node or duplicate callbacks after Reload. Persisting report UI would create misleading stale output, so only the input reference is in scope. Save/load behavior depends on normal Slicer scene persistence and still requires owner manual verification.

## Documentation impact

No separate developer-document update is needed: the task card documents the module-specific state contract, and no reusable repository convention is introduced.

## Completion evidence

Status: Active. Implementation and fast automated tests are complete; manual verification, review, human approval, and completion remain pending.

Implementation summary:

- Added `slicerSTRTParameterNode`, a supported typed `parameterNodeWrapper` around the singleton `slicerSTRT` scripted-module node. Its only persisted field is the optional `inputVolumeNode` reference.
- Updated the widget to initialize, observe, and release/recreate the wrapper across module entry and MRML scene-close events. Combo-box changes update MRML, and parameter-node modifications update the combo box with a recursion guard.
- Preserved transient environment and volume-metadata reports. Inspection now reads the persisted input reference.
- Added synthetic-MRML coverage for the empty default, selecting a volume, clearing it, and saving/reloading the selected reference. The discovery adapter had one redundant blank line removed to keep the already-used test path Ruff-compliant.

Files created:

- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTParameterNode.py`

Files modified:

- `extensions/slicerSTRT/slicerSTRT/CMakeLists.txt`
- `extensions/slicerSTRT/slicerSTRT/Testing/Python/slicerSTRTModuleTest.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`
- `tasks/active/BSSL-005-persistent-module-state.md`

Automated validation on 2026-07-16:

- `git diff --check`: passed (exit code 0). Git emitted only existing Windows line-ending conversion notices.
- `./.venv/Scripts/Activate.ps1; ./scripts/development/run-python-quality.ps1`: passed (exit code 0). Ruff reported `All checks passed!`; Pyright reported 0 errors and 15 expected warnings for Slicer/VTK runtime imports unavailable to ordinary system Python.
- `./scripts/development/run-slicer-tests.ps1`: passed (exit code 0). The configured Slicer executable ran all five tests: environment report, volume inspection with and without selection, parameter-node default/set/clear state, and parameter-node scene save/load persistence.
- The test output included an unrelated pre-existing CropVolume dependency-load warning while the isolated project test suite still completed successfully.

No MCP, private medical data, dependencies, CMake test-registration changes, commits, pushes, pull requests, review transitions, or completion transitions were performed.

## Review findings

Reserved for later independent review.

## Human approval

The project owner's `Start the next task` instruction on 2026-07-16 approved this proportional specification and activation under `.ai/workflows/begin-task.md`. It does not authorize manual-verification completion, review, completion, commit, push, or pull-request actions.
