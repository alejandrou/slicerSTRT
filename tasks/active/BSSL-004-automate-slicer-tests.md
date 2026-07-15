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

Before BSSL-004, generic Slicer tests were enabled and the project-specific Python CMake registration was a placeholder. `slicerSTRTTest` remains the source of truth for the existing environment-reporting and scalar-volume metadata coverage with synthetic MRML data. The `slicerSTRTModuleTest.py` file is now the thin unittest discovery adapter, and `slicer_add_python_unittest` now registers `py_slicerSTRTModuleTest`; the existing generic test remains registered separately. BSSL-005 depends on this completed testing foundation.

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

Implementation files approved for this task:

- `extensions/slicerSTRT/slicerSTRT/Testing/Python/CMakeLists.txt`
- `extensions/slicerSTRT/slicerSTRT/Testing/Python/slicerSTRTModuleTest.py`
- `scripts/development/run-slicer-tests.ps1`
- `docs/development/testing_strategy.md`
- `.gitignore`
- `tasks/{backlog,active,review,completed}/BSSL-004-automate-slicer-tests.md`

`.gitignore` was changed only to add `/build/`, preventing generated standalone extension CMake/CTest files from appearing as source changes.

## Relevant skills and references

- Slicer skill for supported test invocation and CMake/CTest integration.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`
- `extensions/slicerSTRT/slicerSTRT/Testing/`
- `.ai/workflows/manual-verification-workflow.md`

## Implementation plan

1. Verify the local Slicer executable, extension build directory, and supported Slicer
   test conventions without changing local configuration.
2. Preserve the existing `slicerSTRTTest` coverage and expose it through the
   PowerShell runner and CTest registration.
3. Validate success, failure, missing-configuration, and missing-executable paths;
   keep Ruff/Pyright separate from Slicer test execution.
4. Document the approved commands, explicitly distinguishing the upstream Slicer
   SuperBuild from the standalone slicerSTRT extension build.

## Acceptance criteria

- Existing coverage remains represented and repeatable through the approved Slicer test path.
- PowerShell and any CTest registration report reliable success and failure exit codes.
- Missing configuration or executable conditions are actionable.
- Reload, Reload and Test, Ruff, and Pyright responsibilities remain distinct.

## Test plan

- Available path: run the PowerShell runner from the repository root and from `%TEMP%`;
  confirm all three existing tests pass, exit code `0`, and caller location is preserved.
- CTest path: list tests and run `py_slicerSTRTModuleTest` with `--test-dir`
  pointing to the standalone extension build; confirm `1/1` passes and exit code `0`.
- Missing-configuration path: verify the runner reports missing `config/local.json`
  or its required `slicerExecutable` value and returns nonzero without modifying config.
- Missing-executable path: verify an absent or unusable configured executable is
  reported clearly and returns nonzero.
- Failing-test path: verify a Slicer test failure propagates a nonzero process exit code.
- Quality path: run Ruff and Pyright separately; their availability/results do not
  change Slicer test execution.

## Manual verification

Manual verification performed and confirmed by the project owner.

- Slicer started successfully.
- The `slicerSTRT` module loaded correctly.
- Reload passed.
- Reload and Test passed.
- The project-specific tests passed.
- The module remained usable after testing.
- Check Environment worked.
- Inspect Volume worked with synthetic data.
- No private patient or medical data was used.

No Slicer version, timestamp, screenshot, executable path, or other unrecorded
environment detail is asserted here.

## Risks

Slicer test command and CMake registration details vary by local Slicer version and build. Incorrect assumptions could produce a command that appears configured but does not run the intended test.

## Documentation impact

`docs/development/testing_strategy.md` documents the PowerShell prerequisites and
CTest invocation. The CTest command explicitly targets the standalone
slicerSTRT extension build with `--test-dir`; the upstream Slicer SuperBuild is
identified separately and is not presented as the extension CTest project.

## Completion evidence

Implementation and automated-test evidence is recorded below. Documentation
verification for this pass: the CTest command includes `--test-dir`, uses a
portable `<slicerSTRT-extension-build-directory>` placeholder, and distinguishes
the upstream Slicer SuperBuild (`slicerBuildDirectory`) from the standalone
extension build (`C:\stratum\build\slicerSTRT`). The discovery listing is documented
with both expected registered test names.

Lifecycle status: implementation, fast automated tests, and manual Slicer
verification are complete. The task remains active and is ready for independent
review; it has not been moved to `tasks/review/`.

## Review findings

Reserved for later independent review.

## Human approval

Human approval received before activation and implementation.

## Implementation evidence

Status: Active implementation completed; automated validation passed; project-owner manual Slicer verification completed.

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
- .gitignore
- tasks/active/BSSL-004-automate-slicer-tests.md

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

Failure-path validation was performed in a temporary sandbox under `$env:TEMP`
using copies of the runner and test module; the repository files and
`config/local.json` were not modified, and the sandbox was removed afterward.

- Missing `config/local.json`: reported the missing configuration and returned exit code 1.
- Malformed `config/local.json`: reported malformed JSON and returned exit code 1.
- Missing or empty `slicerExecutable`: reported the absent or empty field and returned exit code 1.
- Nonexistent executable path: reported that the configured executable does not exist and returned exit code 1.
- Existing but unusable executable: reported that Slicer could not be started and returned exit code 1.
- Deliberately failing discovered Slicer test: a temporary assertion in `test_environmentCheckReport` caused the Slicer process and runner to return exit code 1; the runner reported the failed test exit code.

Slicer output included the existing three tests:

- test_environmentCheckReport
- test_inspectVolumeMetadata_withScalarVolume
- test_inspectVolumeMetadata_withoutSelection

Manual verification was performed and confirmed by the project owner: Slicer
started, the module loaded, Reload and Reload and Test passed, the project-specific
tests passed, the module remained usable, Check Environment worked, and Inspect
Volume worked with synthetic data. No private patient or medical data was used.
