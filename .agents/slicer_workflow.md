# Slicer Workflow

Use these rules for STRATUM Slicer work.

- Main extension code lives under `C:\stratum\extensions\slicerSTRT`.
- Upstream Slicer source is under `C:\stratum\source` and should be treated as read-only unless explicitly requested.
- Local Slicer SuperBuild/build tree is under `C:\stratum\apps\SR` and should not be edited or committed.
- Built Slicer executable is `C:\stratum\apps\SR\Slicer-build\Slicer.exe`.
- Python scripted module changes should usually be tested with Slicer Developer Mode using Reload / Reload and Test.
- A full Slicer rebuild should not be needed for normal Python-only module changes.
- Do not add external dependencies unless explicitly approved.
