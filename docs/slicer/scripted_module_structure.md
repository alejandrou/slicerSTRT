# slicerSTRT Scripted Module Structure

This note summarizes the current structure of the `slicerSTRT` scripted module.

## Current module layout

The module entry point stays at:

- `C:\stratum\extensions\slicerSTRT\slicerSTRT\slicerSTRT.py`

Supporting classes live in the package:

- `C:\stratum\extensions\slicerSTRT\slicerSTRT\slicerSTRTLib\__init__.py`
- `C:\stratum\extensions\slicerSTRT\slicerSTRT\slicerSTRTLib\slicerSTRTLogic.py`
- `C:\stratum\extensions\slicerSTRT\slicerSTRT\slicerSTRTLib\slicerSTRTWidget.py`
- `C:\stratum\extensions\slicerSTRT\slicerSTRT\slicerSTRTLib\slicerSTRTTest.py`

`slicerSTRT.py` exports:

- `slicerSTRT`
- `slicerSTRTWidget`
- `slicerSTRTLogic`
- `slicerSTRTTest`
- `slicerSTRTParameterNode`
- `registerSampleData()`

The module UI lives in:

- `C:\stratum\extensions\slicerSTRT\slicerSTRT\Resources\UI\slicerSTRT.ui`

## What each part does

### `slicerSTRT.py`

Module metadata, startup setup, and public exports:

- title
- categories
- contributors
- help text
- acknowledgement text
- sample data registration after startup

### `slicerSTRTLib/slicerSTRTLogic.py`

Contains:

- `registerSampleData()`
- `slicerSTRTParameterNode`
- `slicerSTRTLogic`

### `registerSampleData()`

Registers the sample data category and sample volumes shown in Slicer's Sample Data module.

### `slicerSTRTParameterNode`

Stores the module state that should survive scene save and reload:

- input volume
- threshold value
- invert flag
- thresholded output volume
- inverted output volume

### `slicerSTRTLib/slicerSTRTWidget.py`

Contains `slicerSTRTWidget`.

### `slicerSTRTWidget`

Handles the UI and user interaction:

- loads the `.ui` file
- connects selectors and buttons
- synchronizes the UI with the parameter node
- calls the logic when Apply is clicked

### `slicerSTRTLogic`

Contains the processing code:

- parameter-node access
- threshold processing
- CLI invocation
- output cleanup

### `slicerSTRTLib/slicerSTRTTest.py`

Contains `slicerSTRTTest`.

### `slicerSTRTTest`

Contains the scripted test that loads sample data and checks the logic.

## Development guidance

When editing this module:

1. Keep metadata and startup code in `slicerSTRT.py`.
2. Keep UI behavior in `slicerSTRTLib/slicerSTRTWidget.py`.
3. Keep processing in `slicerSTRTLib/slicerSTRTLogic.py`.
4. Keep regression checks in `slicerSTRTLib/slicerSTRTTest.py`.
5. Keep only `slicerSTRT.py` at the module root so Slicer does not try to load helper files as standalone modules.
6. Use Reload / Reload and Test after changes.


