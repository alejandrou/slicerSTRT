---
id: BSSL-004
title: Automate slicerSTRT test execution
status: active
branch:
priority: high
depends_on:
required_skills: [slicer]
optional_tools: []
related_adrs: []
---

# BSSL-004 - Automate slicerSTRT test execution

## Goal

Make the existing slicerSTRT tests repeatable from PowerShell and expose them through the supported Slicer testing mechanism.

## Context

`slicerSTRTTest` currently covers environment reporting and scalar-volume metadata with synthetic MRML data. The module has Slicer generic testing enabled, while its additional Python CMake test registration is currently only a placeholder. Repeatable execution is needed before stateful and workflow changes are added.

## Requirements

- Assess and preserve the current `slicerSTRTTest` coverage.
- Define a PowerShell entry point for Slicer command-line test execution with clear process exit codes.
- Register the test with CMake/CTest when appropriate for the local Slicer build and extension structure.
- Handle missing `config/local.json` and missing or unusable Slicer executables clearly.
- Preserve Reload and Reload and Test behavior.
- Keep Ruff and Pyright checks separate from Slicer test execution.

## Out of scope

- New production behavior or algorithm providers.
- Finalizing unsupported Slicer command syntax or CMake registration details before local Slicer-source and skill verification.
- Replacing manual Reload and Reload and Test verification.

## Files allowed

Likely areas include test CMake files, a PowerShell test helper, module tests, and narrowly scoped documentation. The exact allowlist requires inspection and approval during specification.

## Relevant skills and references

- Slicer skill for supported test invocation and CMake/CTest integration.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`
- `extensions/slicerSTRT/slicerSTRT/Testing/`
- `.ai/workflows/manual-verification-workflow.md`

## Implementation plan

To be defined during specification after local Slicer executable, source, and build conventions are verified.

## Acceptance criteria

- Existing coverage remains represented and repeatable through the approved Slicer test path.
- PowerShell and any CTest registration report reliable success and failure exit codes.
- Missing configuration or executable conditions are actionable.
- Reload, Reload and Test, Ruff, and Pyright responsibilities remain distinct.

## Test plan

To be defined during specification; it must include available, missing-configuration, missing-executable, and failing-test paths.

## Manual verification

Run the module in Slicer, use Reload and Reload and Test, and verify the approved automated command against synthetic data. Record the local Slicer version and executable-selection result.

## Risks

Slicer test command and CMake registration details vary by local Slicer version and build. Incorrect assumptions could produce a command that appears configured but does not run the intended test.

## Documentation impact

Document only the approved developer invocation and prerequisites after specification. Do not duplicate the general task or manual-verification workflow.

## Completion evidence

Reserved for implementation, automated-test, manual-verification, review, and approval evidence.

## Review findings

Reserved for later independent review.

## Human approval

Human approval received before activation and implementation.

## Implementation evidence

Status: Active implementation completed; CTest validation passed; manual Slicer verification remains pending.

Files inspected:

- AGENTS.md
- .ai/workflows/task-lifecycle.md
- .ai/policies/code-quality.md
- .ai/policies/git-workflow.md
- extensions/slicerSTRT/slicerSTRT/CMakeLists.txt
- extensions/slicerSTRT/slicerSTRT/Testing/CMakeLists.txt
- extensions/slicerSTRT/slicerSTRT/Testing/Python/CMakeLists.txt
- extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py
- docs/development/testing_strategy.md
- config/local.example.json
- config/local.json (read-only; values not recorded)
- Slicer source SlicerMacroPythonTesting.cmake and slicer/testing.py

Files created:

- extensions/slicerSTRT/slicerSTRT/Testing/Python/slicerSTRTModuleTest.py
- scripts/development/run-slicer-tests.ps1

Files modified:

- extensions/slicerSTRT/slicerSTRT/Testing/Python/CMakeLists.txt
- docs/development/testing_strategy.md
- This task card

Validation performed:

- PowerShell parser: passed.
- Adapter Python syntax compilation: passed.
- CMake registration statically verified; the expected generated name is py_slicerSTRTModuleTest.
- PowerShell runner from the repository root: passed; all three existing tests ran and returned exit code 0.
- PowerShell runner from %TEMP%: passed; all three existing tests ran and returned exit code 0; caller location preserved.
- Slicer executable resolved from config/local.json; local configuration was not modified.
- CTest listing: standalone extension build C:\stratum\build\slicerSTRT returned both registered tests:
  - py_nomainwindow_qSlicerslicerSTRTModuleGenericTest
  - py_slicerSTRTModuleTest
- Focused CTest execution:
  - Command: ctest --test-dir "C:\stratum\build\slicerSTRT" -C Release -R "^py_slicerSTRTModuleTest$" --output-on-failure
  - Result: 1/1 passed; 100% tests passed out of 1.
  - Exit code: 0.
  - Execution time: 3.93 seconds reported by CTest; 3.959 seconds measured by the invoking PowerShell command.
- The upstream Slicer SuperBuild directory is not the CTest project used for this extension validation.
- Separate Ruff/Pyright command: correctly reported both tools unavailable and returned exit code 1 without installing or modifying dependencies.

Slicer output included the existing three tests:

- test_environmentCheckReport
- test_inspectVolumeMetadata_withScalarVolume
- test_inspectVolumeMetadata_withoutSelection

Manual verification remains required: start Slicer, use Reload and Reload and Test, verify the module behavior, then run the PowerShell and focused CTest commands after extension reconfiguration. Only synthetic MRML data was used by the automated test.
