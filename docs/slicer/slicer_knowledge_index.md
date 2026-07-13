# Slicer Knowledge Index

Use this index to find local Slicer information before relying on external examples.

Machine-specific source, build, executable, and skill paths belong in `config/local.json`.

## Search Order

For Slicer-specific questions, use this order:

1. Current project code under `extensions/`.
2. Local Slicer source configured by `config/local.json`.
3. The installed Slicer skill, following the skill-routing rules in `AGENTS.md`.
4. External sources only when local references are insufficient or current information is required.

Do not invent Slicer APIs. Inspect local project code and local Slicer sources when API details matter.

## Local Slicer Source Areas

When a local Slicer source tree is configured, useful areas commonly include:

- `Modules/`
- `Libs/`
- `Base/`
- `Docs/`
- `Extensions/`
- `Utilities/`

## Topics That Need Local Verification

Check local project code, Slicer source, or the installed Slicer skill before making claims about:

- scripted modules;
- loadable C++ modules;
- CLI modules;
- MRML nodes;
- scene management;
- segmentations;
- markups;
- transforms and coordinate systems;
- DICOM;
- VTK;
- ITK and SimpleITK;
- Qt widgets and `.ui` files;
- CMake;
- extension packaging;
- Slicer testing.
