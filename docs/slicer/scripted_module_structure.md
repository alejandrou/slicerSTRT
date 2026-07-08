# Stratum Scripted Module Structure

This note summarizes the current structure of `C:\slicerSTRT\extensions\SlicerStratum\Stratum`.

## Module class: `Stratum`

Defines the module metadata shown in Slicer:

- title
- category
- dependencies
- contributors
- help text
- acknowledgement text

It also registers sample data after Slicer startup by connecting to `startupCompleted()`.

This file is now the thin entry point for the module and imports `StratumWidget` from the `StratumLib` package so Slicer can discover the widget class.

The packaged helper files live under `StratumLib/`. They are not top-level module entry points, so Slicer does not instantiate them as separate modules.

## Sample data helper: `registerSampleData()`

Registers the `Stratum` sample data category and the sample volumes that appear in the Sample Data module.

This helper keeps the sample-data setup separate from the widget and logic classes.

The helper lives in `StratumLib/StratumLogic.py` so the main file stays focused on module registration.

## Parameter node: `StratumParameterNode`

Defines the structured state that Slicer stores for the module.

In this module, it tracks:

- input volume
- threshold value
- invert flag
- output volume
- inverted output volume

The parameter node also lives in `StratumLib/StratumLogic.py` so the widget and logic share one definition.

## Widget class: `StratumWidget`

Implements the user interface and user interactions.

Responsibilities include:

- loading the `.ui` file
- connecting UI controls to the parameter node
- reacting to scene close events
- triggering the processing logic when the Apply button is clicked

The widget implementation lives in `StratumLib/StratumWidget.py`.

## Logic class: `StratumLogic`

Contains the processing code that can run without the GUI.

It calls the `Threshold Scalar Volume` CLI module, keeps sample-data registration separate, and handles the output volume update.

The logic implementation lives in `StratumLib/StratumLogic.py`.

## Test class: `StratumTest`

Provides the scripted module test.

The current test loads sample data, exercises the logic, and checks the resulting scalar range.

The scripted test lives in `Testing/Python/StratumTest.py` and is registered from `Testing/Python/CMakeLists.txt`.

## Development order

When developing this module, use this order:

1. Change `StratumLib/StratumWidget.py` for UI behavior.
2. Change `StratumLib/StratumLogic.py` for processing, parameter-node, or sample-data work.
3. Change `Testing/Python/StratumTest.py` for logic and regression tests.
4. Keep `Stratum.py` limited to module registration and top-level imports.

## Reload workflow

After edits, use Slicer Developer Mode and Reload / Reload and Test to confirm the module still loads and the test still runs.

## Phase 1 cleanup note

For Phase 1, keep the module behavior unchanged and limit edits to safe cleanup such as removing obvious template comments or placeholder text.
