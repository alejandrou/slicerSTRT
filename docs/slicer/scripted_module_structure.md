# slicerSTRT Scripted Module Structure

This note summarizes the current structure of the `slicerSTRT` scripted module.

## Current module layout

The module is implemented in a single Python file:

- `C:\slicerSTRT\extensions\slicerSTRT\slicerSTRT\slicerSTRT.py`

That file defines:

- `slicerSTRT`
- `registerSampleData()`
- `slicerSTRTParameterNode`
- `slicerSTRTWidget`
- `slicerSTRTLogic`
- `slicerSTRTTest`

The module UI lives in:

- `C:\slicerSTRT\extensions\slicerSTRT\slicerSTRT\Resources\UI\slicerSTRT.ui`

## What each part does

### `slicerSTRT`

Module metadata and startup setup:

- title
- categories
- contributors
- help text
- acknowledgement text
- sample data registration after startup

### `registerSampleData()`

Registers the sample data category and sample volumes shown in Slicer's Sample Data module.

### `slicerSTRTParameterNode`

Stores the module state that should survive scene save and reload:

- input volume
- threshold value
- invert flag
- thresholded output volume
- inverted output volume

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

### `slicerSTRTTest`

Contains the scripted test that loads sample data and checks the logic.

## Development guidance

When editing this module:

1. Keep metadata and startup code in `slicerSTRT.py`.
2. Keep UI behavior in `slicerSTRTWidget`.
3. Keep processing in `slicerSTRTLogic`.
4. Keep regression checks in `slicerSTRTTest`.
5. Use Reload / Reload and Test after changes.

