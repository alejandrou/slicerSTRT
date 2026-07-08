# slicerSTRT Slicer Context Handoff

## Current status

The local slicerSTRT/Slicer workspace is located at:

`C:\stratum`

The `slicerSTRT` scripted module has been created and loads correctly in 3D Slicer.
Cleanup pass completed: removed generated `__pycache__` folders under `C:\stratum\extensions\slicerSTRT` and trimmed template boilerplate from `slicerSTRT.py` without changing the module structure or adding slicerSTRT functionality.

## Main paths

- Project root: `C:\stratum`
- Codex instructions: `C:\stratum\AGENTS.md`
- Slicer source: `C:\stratum\source`
- Slicer build: `C:\stratum\apps\SR`
- Slicer executable: `C:\stratum\apps\SR\Slicer-build\Slicer.exe`
- slicerSTRT extension: `C:\stratum\extensions\slicerSTRT`
- slicerSTRT module: `C:\stratum\extensions\slicerSTRT\slicerSTRT`
- Main module file: `C:\stratum\extensions\slicerSTRT\slicerSTRT\slicerSTRT.py`
- Project docs: `C:\stratum\docs`
- Slicer skill: `C:\Users\AlejandroHerrera\.codex\skills\slicer-skill`

## Current project structure

The extension currently contains:

`C:\stratum\extensions\slicerSTRT`

with:

- `CMakeLists.txt`
- `slicerSTRT.png`
- `slicerSTRT\slicerSTRT.py`
- `slicerSTRT\Resources\UI\slicerSTRT.ui`
- `slicerSTRT\Resources\Icons\slicerSTRT.png`
- `slicerSTRT\Resources`
- `slicerSTRT\Testing`

## Rules

Before coding, Codex must read:

- `AGENTS.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/slicer/slicer_knowledge_index.md`
- `docs/codex/codex_workflow.md`

## Next technical goal

Verify the cleanup in Slicer with Reload / Reload and Test before any new slicerSTRT feature work.

Do not add real slicerSTRT medical functionality yet.

## Important

Do not edit:

- `C:\stratum\apps\SR`
- `C:\stratum\source`

unless explicitly requested.

Normal development goes under:

`C:\stratum\extensions\slicerSTRT`


