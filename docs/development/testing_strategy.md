# Testing Strategy

This document describes how STRATUM Slicer code should be tested. Manual verification procedure details live in `.ai/workflows/manual-verification-workflow.md`.

## Test Locations

Tests for the current scripted module should live under:

```text
extensions/slicerSTRT/slicerSTRT/Testing/
```

Keep test files near the module they validate.

## What To Test First

Prioritize tests for:

1. Logic functions.
2. Data validation.
3. Coordinate conversions.
4. Input/output behavior.
5. Error handling.

Avoid testing only GUI clicks unless the task specifically concerns UI behavior.

## Fast Automated Checks

Fast checks should be repeatable and should not require private data, MCP, or a full Slicer rebuild.

Useful checks may include:

- Python syntax checks for edited module files.
- Focused unit-style tests for pure helper logic.
- Slicer scripted-module tests when Slicer is available and the active task calls for them.

## Slicer Tests

For Python scripted-module changes:

1. Edit code under `extensions/slicerSTRT/`.
2. Open Slicer.
3. Enable Developer Mode if needed.
4. Use Reload or Reload and Test.
5. Fix errors and repeat.

Only rebuild Slicer when C++, CMake, generated wrapping, or dependency changes require it.

### Automated slicerSTRT tests

The project-specific scripted-module tests can be run from any working directory with:

```powershell
.\scripts\development\run-slicer-tests.ps1
```

This command requires `config/local.json` with a non-empty `slicerExecutable` value. The
configured path may be absolute or relative to the repository root. The tests run in
Slicer's embedded Python runtime through the `slicerSTRTModuleTest` discovery adapter;
they use synthetic MRML data and require no private medical data.

The same test is registered with CTest as `py_slicerSTRTModuleTest`. After reconfiguring
the extension build so CMake sees the registration, run it with:

```powershell
ctest -C Release -R "^py_slicerSTRTModuleTest$" --output-on-failure
```

PowerShell/Slicer execution and CTest both execute the existing three module tests.
CTest registration provides build-integrated discovery, while Ruff and Pyright remain
separate Python quality checks. Reload and Reload and Test remain the interactive Slicer
development workflow and are not replaced by either automated path. A CMake change
requires extension-build reconfiguration before the new CTest test appears.

## Test Data

Use synthetic data, public Slicer sample data, anonymized test data, mock JSON/results, or explicitly approved public medical data.

Do not require private patient data for basic tests. Follow `.ai/policies/medical-data-policy.md` for the authoritative medical-data rules.

## Test Design

Tests should be:

- small;
- repeatable;
- independent;
- clear;
- focused on behavior that can regress;
- explicit about units and coordinate systems when those matter.
