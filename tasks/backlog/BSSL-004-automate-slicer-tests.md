---
id: BSSL-004
title: Automate slicerSTRT test execution
status: backlog
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

Required before specification is activated and before implementation begins.
