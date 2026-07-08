# slicerSTRT Project Structure

Main workspace:

`C:\slicerSTRT`

Open this folder directly in VS Code when working with Codex.

## Folder responsibilities

### `apps`

Contains built or installed applications.

Current Slicer build:

`C:\slicerSTRT\apps\SR\Slicer-build\Slicer.exe`

Do not edit this folder unless explicitly requested.

### `source`

Contains the local Slicer source code.

Use it as reference for:

- Slicer APIs
- module examples
- MRML
- Qt
- VTK
- ITK
- CMake
- extension structure

Do not edit this folder unless explicitly requested.

### `extensions`

Contains slicerSTRT-specific Slicer extensions and modules.

Normal development goes here.

Current extension:

`C:\slicerSTRT\extensions\slicerSTRT`

Current module:

`C:\slicerSTRT\extensions\slicerSTRT\slicerSTRT`

### `docs`

Contains documentation for the developer and Codex.

Current sections:

- `docs/development`
- `docs/slicer`
- `docs/codex`
- `docs/knowledge`

### `knowledge`

Contains external references, PDFs, downloaded docs, notes, and extra material.

Use as reference only.

### `workspace`

Contains temporary work, scripts, experiments, and local-only material.

Do not put final module source code here.

## Current extension structure

`extensions\slicerSTRT`

Contains:

- `CMakeLists.txt`
- `slicerSTRT.png`
- `slicerSTRT\slicerSTRT.py`
- `slicerSTRT\Resources`
- `slicerSTRT\Testing`

## Edit permissions

Codex may normally edit:

- `C:\slicerSTRT\extensions`
- `C:\slicerSTRT\docs`
- `C:\slicerSTRT\workspace`

Codex must not edit unless explicitly requested:

- `C:\slicerSTRT\apps`
- `C:\slicerSTRT\source`

## Development rule

For now, slicerSTRT development should start as a Python scripted Slicer module.

Do not rebuild Slicer for normal Python changes.
Use Slicer Developer Mode and Reload / Reload and Test.

## Sandbox roadmap

The slicerSTRT learning sandbox is defined in:

`docs/development/sandbox_roadmap.md`

Sandbox code should live under:

`extensions/slicerSTRT`

Sandbox temporary/generated files should live under:

`workspace`

Suggested generated folders:

`workspace/sample_data`
`workspace/reports`
