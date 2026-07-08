# STRATUM Testing Strategy

This document defines how STRATUM Slicer code should be tested.

## Current phase

The current STRATUM module is a Python scripted Slicer module.

Testing should start simple.

## Test locations

Tests for the current module should live under:

`C:\slicerSTRT\extensions\SlicerStratum\Stratum\Testing`

## What to test first

Prioritize tests for:

1. Logic functions
2. Data validation
3. Coordinate conversions
4. Input/output behavior
5. Error handling

Avoid testing only GUI clicks unless necessary.

## Development workflow

For normal Python changes:

1. Edit code under `extensions\SlicerStratum`
2. Open Slicer
3. Use Developer Mode
4. Use Reload / Reload and Test
5. Fix errors
6. Only rebuild Slicer if C++ or CMake changes require it

## Test design rules

Tests should be:

- Small
- Repeatable
- Independent
- Clear
- Based on sample or synthetic data when possible

Do not require private patient data for basic tests.

## Medical data rule

Do not commit patient data, private DICOM files, or sensitive medical images.

Use anonymized, synthetic, or public sample data.