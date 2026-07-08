# STRATUM Slicer Context Handoff

## Current status

The local STRATUM/Slicer workspace is located at:

`C:\slicerSTRT`

The `Stratum` scripted module has been created and loads correctly in 3D Slicer.
Cleanup pass completed: removed generated `__pycache__` folders under `C:\slicerSTRT\extensions\SlicerStratum` and trimmed template boilerplate from `Stratum.py`, `StratumWidget.py`, `StratumLogic.py`, and `StratumTest.py` without changing the module split or adding STRATUM functionality.

## Main paths

- Project root: `C:\slicerSTRT`
- Codex instructions: `C:\slicerSTRT\AGENTS.md`
- Slicer source: `C:\slicerSTRT\source`
- Slicer build: `C:\slicerSTRT\apps\SR`
- Slicer executable: `C:\slicerSTRT\apps\SR\Slicer-build\Slicer.exe`
- STRATUM extension: `C:\slicerSTRT\extensions\SlicerStratum`
- STRATUM module: `C:\slicerSTRT\extensions\SlicerStratum\Stratum`
- Main module file: `C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py`
- Project docs: `C:\slicerSTRT\docs`
- Slicer skill: `C:\Users\AlejandroHerrera\.codex\skills\slicer-skill`

## Current project structure

The extension currently contains:

`C:\slicerSTRT\extensions\SlicerStratum`

with:

- `CMakeLists.txt`
- `SlicerStratum.png`
- `Stratum\Stratum.py`
- `Stratum\Resources`
- `Stratum\Testing`

## Rules

Before coding, Codex must read:

- `AGENTS.md`
- `docs/development/project_structure.md`
- `docs/development/coding_standards.md`
- `docs/development/testing_strategy.md`
- `docs/slicer/slicer_knowledge_index.md`
- `docs/codex/codex_workflow.md`

## Next technical goal

Verify the cleanup in Slicer with Reload / Reload and Test before any new STRATUM feature work.

Do not add real STRATUM medical functionality yet.

## Important

Do not edit:

- `C:\slicerSTRT\apps\SR`
- `C:\slicerSTRT\source`

unless explicitly requested.

Normal development goes under:

`C:\slicerSTRT\extensions\SlicerStratum`
