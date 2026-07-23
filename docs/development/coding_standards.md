# Coding Standards

Mandatory code-quality policy lives in `.ai/policies/code-quality.md`. This document gives technical guidance for SLIAFlow Slicer development.

## Priorities

Prefer code that is:

1. Readable.
2. Maintainable.
3. Robust.

Do not optimize for performance before the behavior and boundaries are clear.

## Local Python Quality Checks

From the repository root, run:

```powershell
.\.venv\Scripts\Activate.ps1
.\scripts\development\run-python-quality.ps1
```

Create the ignored root `.venv` and install Ruff and Pyright there before the first run. Activate that environment in each new PowerShell session. The command runs Ruff and Pyright against project-owned Python under `extensions/SLIAFlow/`; they are development tools, not Slicer runtime dependencies, and the script does not install them.

Pyright uses `basic` checking. Missing imports from Slicer's runtime-provided modules are warnings because normal system Python does not provide the real `slicer`, `qt`, `ctk`, and Slicer-bundled `vtk` environment. `reportMissingModuleSource` is disabled because several of these modules are compiled or injected at runtime. Project files remain included, `SLIAFlowLib` is resolved through the repository configuration, and other basic diagnostics remain enabled.

## Separate Responsibilities

Keep UI, logic, I/O, tests, and reusable helpers separate when practical.

For Slicer scripted modules:

- Module entry point: metadata, startup setup, and public exports.
- Widget class: UI loading, user interaction, signal connections, and display updates.
- Logic class: computation, validation, MRML inspection, and reusable workflow logic.
- Test class: automated checks that exercise logic and important integration behavior.

Avoid putting algorithms directly in button callbacks.

## Naming

Use clear names instead of abbreviations.

Prefer:

- `inputVolumeNode`
- `segmentationNode`
- `targetPoint_RAS`
- `needleToTargetDistanceMm`
- `gaussianSigmaPixel`

Include units when relevant:

- `distanceMm`
- `angleDeg`
- `spacingMm`
- `timeSec`
- `indexPixel`

## Coordinate Systems

When working with medical images, transforms, points, or vectors, include the coordinate system when it matters.

Examples:

- `entryPoint_RAS`
- `targetPoint_RAS`
- `imagePlaneNormalVector_IJK`
- `imageToWorldTransform`
- `probeToReferenceTransform`

Avoid vague names such as `ProbeTransform`, `NeedleTrackerMatrix`, or `NeedleTipVector` when the coordinate system is significant.

## Avoid Magic Values

Use named constants, enums, or clear string values for non-obvious values.

All non-obvious numeric values should have a name or explanation, especially thresholds, units, coordinate-system assumptions, and image-processing parameters.

## Comments

Prefer self-documenting code. Use comments to explain:

- why something is done;
- medical-image or processing assumptions;
- coordinate-system assumptions;
- non-obvious constraints;
- safety checks.

Do not use comments as change logs or to restate obvious syntax.

Use TODO comments only when they are specific and actionable.

## Cohesion

Keep functions focused.

Rules of thumb:

- One function should do one thing.
- Avoid functions longer than one or two screens.
- Declare variables close to where they are used.
- Split unclear functions instead of creating vague containers such as `Manager` or `Controller`.
