# slicerSTRT Coding Standards

These rules are based on the Perk Lab presentation "Writing correct and understandable code".

## Main priorities

Prioritize:

1. Readability
2. Maintainability
3. Robustness

Do not optimize for performance too early.

## Separate responsibilities

Do not mix everything in one file.

Separate:

- Algorithms
- Tests
- Input/output
- GUI code
- Utility code

For Slicer scripted modules:

- Widget class: UI and user interaction
- Logic class: processing and algorithmic logic
- Test class: automated checks

Avoid putting real algorithms directly inside button callbacks.

## Naming rules

Use clear names.

Bad:

- `tmp`
- `im`
- `BSh`
- `pos`
- `tt`
- `x1`

Better:

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

## Spatial naming

When working with medical images, transforms, points, or vectors, include the coordinate system when useful.

Examples:

- `entryPoint_RAS`
- `targetPoint_RAS`
- `needleTipPoint_RAS`
- `imagePlaneNormalVector_IJK`
- `imageToWorldTransform`
- `probeToReferenceTransform`

Avoid vague names such as:

- `ProbeTransform`
- `NeedleTrackerMatrix`
- `NeedleTipVector`

## Avoid magic numbers

Bad:

`if method == 1 or method == 3`

Better:

Use named constants, enums, or clear string values.

All non-obvious numeric values must have a name or explanation.

## Comments

Prefer self-documenting code.

Use comments to explain:

- Why something is done
- Medical/image-processing assumptions
- Coordinate system assumptions
- Non-obvious constraints
- Safety checks

Do not use comments for:

- Dead code
- Change logs
- Obvious syntax

Use TODO comments clearly:

`# TODO: Validate this threshold with slicerSTRT sample data.`

## Cohesion

Keep functions focused.

Rules of thumb:

- One function should do one thing.
- Avoid functions longer than 1–2 screens.
- Avoid huge files.
- Declare variables close to where they are used.
- Split unclear functions instead of creating vague names like `Manager` or `Controller`.
