# Slicer Knowledge Index

This file tells Codex where to look for Slicer information locally.

## Main local Slicer source

`C:\slicerSTRT\source`

Important folders:

- `C:\slicerSTRT\source\Modules`
- `C:\slicerSTRT\source\Libs`
- `C:\slicerSTRT\source\Base`
- `C:\slicerSTRT\source\Docs`
- `C:\slicerSTRT\source\Extensions`
- `C:\slicerSTRT\source\Utilities`

## Existing Slicer skill

`C:\Users\AlejandroHerrera\.codex\skills\slicer-skill`

Use this for:

- Slicer development patterns
- Example extensions
- Slicer source references
- Project Week material
- Slicer-specific AI guidance

## Search order

When answering a Slicer question:

1. Check the STRATUM extension first.
2. Check local Slicer source.
3. Check `slicer-skill`.
4. Only use web if local references are insufficient or the user asks for current/latest information.

## Important Slicer topics

Codex should search local sources before answering questions about:

- Scripted modules
- Loadable C++ modules
- CLI modules
- MRML nodes
- Scene management
- Segmentations
- Markups
- Transforms
- DICOM
- VTK
- ITK / SimpleITK
- Qt widgets
- CMake
- Extension packaging