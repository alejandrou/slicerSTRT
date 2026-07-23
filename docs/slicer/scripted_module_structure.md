# Scripted Module Structure

This note summarizes the current `SLIAFlow` scripted module layout.

## Current Layout

The module entry point is:

```text
extensions/SLIAFlow/SLIAFlow/SLIAFlow.py
```

Supporting classes live in:

```text
extensions/SLIAFlow/SLIAFlow/SLIAFlowLib/__init__.py
extensions/SLIAFlow/SLIAFlow/SLIAFlowLib/SLIAFlowLogic.py
extensions/SLIAFlow/SLIAFlow/SLIAFlowLib/SLIAFlowWidget.py
extensions/SLIAFlow/SLIAFlow/SLIAFlowLib/SLIAFlowTest.py
```

The module UI file is:

```text
extensions/SLIAFlow/SLIAFlow/Resources/UI/SLIAFlow.ui
```

Test CMake files are under:

```text
extensions/SLIAFlow/SLIAFlow/Testing/
```

## Entry Point

`SLIAFlow.py` contains module metadata, startup setup, and public exports used by Slicer.

It should stay small. Keep helper implementation in `SLIAFlowLib/` so Slicer does not try to load helper files as standalone modules.

## Logic

`SLIAFlowLib/SLIAFlowLogic.py` currently defines `SLIAFlowLogic`.

The logic class owns reusable behavior for the module's current inspection tools:

- collecting a Slicer/Python environment report;
- checking core imports and optional packages;
- inspecting selected volume metadata, including dimensions, spacing, origin, IJK-to-RAS directions, scalar type, voxel count, and estimated voxel volume;
- formatting those reports for display by the widget and verification by tests.

The current production module does not define a parameter-node wrapper or sample-data registration function.

## Widget

`SLIAFlowLib/SLIAFlowWidget.py` contains `SLIAFlowWidget`.

The widget loads the `.ui` file, connects UI controls, synchronizes UI state, calls logic methods, and displays results.

## Tests

`SLIAFlowLib/SLIAFlowTest.py` contains `SLIAFlowTest`.

Tests should focus on logic and important Slicer integration behavior.

## Reload Guidance

For normal Python scripted-module changes, use Slicer Developer Mode and Reload or Reload and Test.

For `.ui` changes, Reload may be sufficient. Restart Slicer if the interface does not refresh cleanly.
