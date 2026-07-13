---
id: BSSL-005
title: Introduce persistent module state
status: backlog
branch:
priority: high
depends_on: BSSL-004
required_skills: [slicer]
optional_tools: []
related_adrs: []
---

# BSSL-005 - Introduce persistent module state

## Goal

Represent module inputs and relevant UI state in MRML using the supported Slicer parameter-node pattern so state can survive scene save/load when appropriate.

## Context

The current module reads the selected volume directly from the widget and does not yet establish persistent parameter-node state. A stable state model is needed before processing boundaries are introduced.

## Requirements

- Assess the supported parameter-node wrapper approach for this module.
- Represent the input volume reference and approved relevant UI state.
- Define UI-to-MRML and MRML-to-UI synchronization.
- Define safe defaults and behavior across scene close/open.
- Add focused tests for state synchronization and safe empty-state behavior.

## Out of scope

- Algorithm providers, processing behavior, or result generation.
- Clinical data or clinical claims.
- Unrelated UI redesign or persistence of transient presentation details.

## Files allowed

Likely areas include the scripted module widget, logic/state support, tests, and narrowly scoped documentation. The exact allowlist requires inspection and approval during specification.

## Relevant skills and references

- Slicer skill for MRML scene and parameter-node patterns.
- Dependency: BSSL-004.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`

## Implementation plan

To be defined during specification after current module conventions and supported Slicer APIs are verified.

## Acceptance criteria

- The selected input volume is represented by approved persistent state.
- Synchronization is deterministic, defaults are safe, and scene transitions do not leave stale or invalid UI state.
- Automated tests cover synchronization and empty/default cases.

## Test plan

To be defined during specification; it must cover setting, clearing, saving, loading, and scene-close behavior using synthetic data.

## Manual verification

In Slicer, select and clear a synthetic volume, exercise scene close/open and save/load as specified, then use Reload and Reload and Test. Record observed state behavior.

## Risks

Persisting too much UI state or mishandling scene events could create stale references or surprising defaults. Exact wrapper and lifecycle choices require Slicer verification.

## Documentation impact

Update developer documentation only if the approved state contract introduces a reusable convention.

## Completion evidence

Reserved for implementation, automated-test, manual-verification, review, and approval evidence.

## Review findings

Reserved for later independent review.

## Human approval

Required before specification is activated and before implementation begins.
