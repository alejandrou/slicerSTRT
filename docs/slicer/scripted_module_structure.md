# Scripted Module Structure

This note summarizes the current `slicerSTRT` scripted module layout.

## Current Layout

The module entry point is:

```text
extensions/slicerSTRT/slicerSTRT/slicerSTRT.py
```

Supporting classes live in:

```text
extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/__init__.py
extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTLogic.py
extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py
extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py
```

The module UI file is:

```text
extensions/slicerSTRT/slicerSTRT/Resources/UI/slicerSTRT.ui
```

Test CMake files are under:

```text
extensions/slicerSTRT/slicerSTRT/Testing/
```

## Entry Point

`slicerSTRT.py` contains module metadata, startup setup, and public exports used by Slicer.

It should stay small. Keep helper implementation in `slicerSTRTLib/` so Slicer does not try to load helper files as standalone modules.

## Logic

`slicerSTRTLib/slicerSTRTLogic.py` contains:

- `registerSampleData()`;
- `slicerSTRTParameterNode`;
- `slicerSTRTLogic`.

The logic file owns reusable processing and validation behavior.

## Widget

`slicerSTRTLib/slicerSTRTWidget.py` contains `slicerSTRTWidget`.

The widget loads the `.ui` file, connects UI controls, synchronizes UI state, calls logic methods, and displays results.

## Tests

`slicerSTRTLib/slicerSTRTTest.py` contains `slicerSTRTTest`.

Tests should focus on logic and important Slicer integration behavior.

## Reload Guidance

For normal Python scripted-module changes, use Slicer Developer Mode and Reload or Reload and Test.

For `.ui` changes, Reload may be sufficient. Restart Slicer if the interface does not refresh cleanly.
