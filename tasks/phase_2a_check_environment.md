# Phase 2A - Check Environment

## Goal

Add a simple Check Environment button/panel to the STRATUM Slicer module.

## Allowed Files

- `extensions/slicerSTRT/**`
- Docs only if needed

## Do Not Edit

- `source/**`
- `apps/SR/**`
- Unrelated docs

## Feature Requirements

- Show Slicer version.
- Show Slicer revision/build info if safely available.
- Show Python version.
- Show Python executable/path.
- Show current module file path.
- Show current working directory.
- Check whether imports work: `slicer`, `vtk`, `qt`, `ctk`.
- Check whether useful packages are available: `numpy`, `SimpleITK`.
- Display readable PASS/WARN/FAIL style results in the module UI.

## Non-Goals

- No AI.
- No DICOM.
- No segmentation.
- No markups.
- No reports.
- No external dependencies.
- No full Slicer rebuild.

## Expected Final Report

- Files changed.
- What the new check does.
- Why the implementation is small/safe.
- How to test manually in Slicer.
- Whether Reload / Reload and Test should work.
- Any remaining generated-template code.
