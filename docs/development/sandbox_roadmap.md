# STRATUM Slicer Sandbox Roadmap

Personal learning roadmap for building a safe, local, STRATUM-inspired 3D Slicer sandbox.

Recommended location:

```text
C:\slicerSTRT\docs\development\sandbox_roadmap.md
```

This document is for learning and local development only. It is not the official STRATUM codebase and must not be treated as clinical software.

---

## 1. Purpose

The goal of this sandbox is to help the developer learn 3D Slicer development while preparing for future work on STRATUM.

The sandbox should simulate the type of workflow that may appear in a 3D decision-support tool:

- loading medical image data,
- inspecting volumes,
- using markups,
- working with segmentations,
- handling coordinate systems,
- displaying mock AI outputs,
- generating reports,
- writing tests,
- keeping code readable and maintainable.

The sandbox must avoid private patient data, real diagnostic claims, and any unvalidated clinical functionality.

---

## 2. Public STRATUM alignment

Public STRATUM information describes a 3D decision-support tool for brain surgery guidance and diagnostics based on multimodal data processing, AI algorithms, and point-of-care computing.

The sandbox is inspired by the public STRATUM work packages:

- WP2: intraoperative acquisition and data collection,
- WP3: diagnostic and integration algorithm development,
- WP4: HPC processing platform development,
- WP5: interactive 3D GUI and prototype integration,
- WP6: clinical demonstration and evaluation.

In the sandbox, these are represented only as safe mock workflows.

Sources:

- https://www.stratum-project.eu/
- https://www.stratum-project.eu/work-packages/
- https://www.stratum-project.eu/project-results/

---

## 3. Local project paths

Project root:

```text
C:\slicerSTRT
```

Main module:

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
```

Extension root:

```text
C:\slicerSTRT\extensions\SlicerStratum
```

Documentation:

```text
C:\slicerSTRT\docs
```

Temporary reports and generated files:

```text
C:\slicerSTRT\workspace
```

Built Slicer executable:

```text
C:\slicerSTRT\apps\SR\Slicer-build\Slicer.exe
```

Local Slicer source reference:

```text
C:\slicerSTRT\source
```

Slicer skill:

```text
C:\Users\AlejandroHerrera\.codex\skills\slicer-skill
```

---

## 4. Global development principles

Before coding, Codex should read:

```text
C:\slicerSTRT\AGENTS.md
C:\slicerSTRT\docs\development\project_structure.md
C:\slicerSTRT\docs\development\coding_standards.md
C:\slicerSTRT\docs\development\testing_strategy.md
C:\slicerSTRT\docs\slicer\slicer_knowledge_index.md
C:\slicerSTRT\docs\codex\codex_workflow.md
```

Core rules:

1. Do not edit `C:\slicerSTRT\apps\SR` unless explicitly requested.
2. Do not edit `C:\slicerSTRT\source` unless explicitly requested.
3. Normal sandbox development goes under `C:\slicerSTRT\extensions\SlicerStratum`.
4. Documentation goes under `C:\slicerSTRT\docs`.
5. Temporary generated files go under `C:\slicerSTRT\workspace`.
6. Start with Python scripted modules.
7. Do not start with C++ unless there is a clear reason.
8. Do not build real diagnostic logic.
9. Do not use private patient data.
10. Prefer small, testable, readable steps.

---

## 5. End goal

The final sandbox should provide a simple STRATUM-inspired workflow:

1. Check the Slicer environment.
2. Load or select a sample volume.
3. Display image metadata.
4. Place entry and target points.
5. Compute distance between points.
6. Create or select a segmentation.
7. Compute basic segmentation statistics.
8. Load a mock AI result from JSON.
9. Display mock AI output safely.
10. Generate a Markdown report.
11. Run basic tests.

This is a learning project. It does not diagnose, guide surgery, or make clinical decisions.

---

# Phase 0 — Confirm baseline environment

## Goal

Confirm that the local Slicer build and the `Stratum` module work.

## Skills learned

- Slicer startup
- scripted module discovery
- Developer Mode
- Reload / Reload and Test

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\docs\codex\context_handoff.md
```

## Tasks

1. Open Slicer:

```text
C:\slicerSTRT\apps\SR\Slicer-build\Slicer.exe
```

2. Confirm the `Stratum` module appears in Slicer.
3. Enable Developer Mode if not already enabled.
4. Test Reload / Reload and Test.
5. Record the status in `docs\codex\context_handoff.md`.

## Acceptance criteria

- Slicer opens.
- `Stratum` module loads.
- Reload works.
- No code changes required.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/codex/context_handoff.md.
The Stratum module loads correctly in Slicer.
Update context_handoff.md with this status only.
Do not edit source code.
```

---

# Phase 1 — Clean and understand the generated module

## Goal

Understand the generated `Stratum.py` structure and clean only what is safe.

## Skills learned

- scripted module template structure
- `ScriptedLoadableModule`
- `ScriptedLoadableModuleWidget`
- `ScriptedLoadableModuleLogic`
- `ScriptedLoadableModuleTest`

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\docs\slicer\scripted_module_structure.md
```

## Tasks

1. Inspect `Stratum.py`.
2. Identify generated classes.
3. Document what each class does.
4. Remove only obviously unused template comments if safe.
5. Keep functionality unchanged.
6. Create a short documentation file:

```text
C:\slicerSTRT\docs\slicer\scripted_module_structure.md
```

## Acceptance criteria

- Module still loads.
- Reload still works.
- No real feature added yet.
- Documentation explains the basic module structure.

## Suggested Codex prompt

```text
Read AGENTS.md, docs/development/coding_standards.md, and docs/slicer/slicer_knowledge_index.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py

Task:
Explain the generated scripted module structure and make only the smallest safe cleanup.

Rules:
- Do not add real STRATUM functionality.
- Do not edit C:\slicerSTRT\source.
- Do not edit C:\slicerSTRT\apps\SR.
- Explain how to test with Reload / Reload and Test.
```

---

# Phase 2 — Add an environment check panel

## Goal

Add a harmless first feature that confirms the environment is working.

## Skills learned

- UI button callbacks
- Slicer application information
- basic scene inspection
- separating UI from logic

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
```

Optional documentation:

```text
C:\slicerSTRT\docs\slicer\module_reload_workflow.md
```

## Feature

Add a button:

```text
Check Environment
```

When clicked, it should display:

- Slicer version,
- Python version,
- module path,
- number of MRML scene nodes,
- confirmation that the module is running.

## Acceptance criteria

- Button appears.
- Button does not require loaded data.
- Result is shown in the module UI or log.
- Logic is not hardcoded inside the button callback if avoidable.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/development/coding_standards.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py

Task:
Add a minimal "Check Environment" button.

Rules:
- Keep logic separate from UI where practical.
- Do not add external dependencies.
- Do not edit Slicer source.
- Explain how to test in Slicer.
```

---

# Phase 3 — Volume selector and metadata viewer

## Goal

Learn how to select a volume node and inspect basic image metadata.

## Skills learned

- MRML volume nodes
- node selectors
- image dimensions
- spacing
- origin
- scalar range
- scene interaction

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\docs\slicer\volume_nodes.md
```

## Feature

Add:

- input volume selector,
- metadata display area,
- button: `Inspect Volume`.

Display:

- volume name,
- dimensions,
- spacing in mm,
- origin,
- scalar range.

## Acceptance criteria

- Works with a selected scalar volume.
- Shows useful message if no volume is selected.
- Does not crash with invalid input.
- Uses clear variable names with units.

## Suggested Codex prompt

```text
Read AGENTS.md, docs/development/coding_standards.md, and docs/slicer/slicer_knowledge_index.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py

Search local Slicer source only if needed for volume node APIs.

Task:
Add a volume selector and an Inspect Volume button that displays basic metadata.

Rules:
- No clinical interpretation.
- Validate missing input.
- Keep the change small.
```

---

# Phase 4 — Markups distance tool

## Goal

Learn Slicer markups and coordinate systems.

## Skills learned

- markups fiducial nodes
- RAS coordinate system
- point extraction
- distance calculation in millimetres
- naming with coordinate systems and units

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\docs\slicer\markups_and_coordinates.md
```

## Feature

Allow the user to select or create a markups node with two points:

- entry point,
- target point.

Compute:

```text
entryToTargetDistanceMm
```

## Acceptance criteria

- Handles missing markups node.
- Handles fewer than two points.
- Computes distance in RAS space.
- Displays result in millimetres.
- Uses names such as `entryPoint_RAS`, `targetPoint_RAS`, `entryToTargetDistanceMm`.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/development/coding_standards.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py

Task:
Add a markups-based distance tool using two control points.

Rules:
- Use clear coordinate-system names.
- Validate that two points exist.
- Display distance in mm.
- Do not add medical decision logic.
```

---

# Phase 5 — Basic segmentation workflow

## Goal

Learn segmentation nodes and simple quantitative measurements.

## Skills learned

- segmentation nodes
- segment selection
- basic geometry/statistics
- safe display of derived measurements

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\docs\slicer\segmentation_nodes.md
```

## Feature

Add:

- segmentation selector,
- segment selector or first-segment fallback,
- button: `Inspect Segmentation`.

Display basic information:

- number of segments,
- selected segment name,
- approximate volume if available,
- center/bounding-box if easy to compute safely.

## Acceptance criteria

- Handles missing segmentation.
- Handles empty segmentation.
- Does not claim diagnosis.
- Documents any limitations.

## Suggested Codex prompt

```text
Read AGENTS.md, docs/development/coding_standards.md, and docs/slicer/slicer_knowledge_index.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py

Task:
Add a basic segmentation inspection feature.

Rules:
- Search local Slicer source or examples before using segmentation APIs.
- Do not guess APIs.
- Keep calculations simple and documented.
- Do not add clinical interpretation.
```

---

# Phase 6 — Mock multimodal data viewer

## Goal

Simulate STRATUM-style multimodal integration without using real project data.

## Skills learned

- coordinating multiple inputs
- fake auxiliary modality
- overlay/result display
- data validation

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\workspace\sample_data
C:\slicerSTRT\docs\slicer\multimodal_mock_workflow.md
```

## Feature

Create or load a fake auxiliary modality, such as:

- mock hyperspectral confidence map,
- mock probability map,
- mock point measurements.

The feature should clearly state:

```text
Mock data only. Not for clinical use.
```

## Acceptance criteria

- Does not require private data.
- Uses generated or public sample data only.
- Clearly labels outputs as mock/demo.
- Keeps I/O separate from algorithmic logic where practical.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/development/coding_standards.md.

Task:
Design, but do not implement yet, a mock multimodal data viewer for the sandbox.

Rules:
- Use generated or sample data only.
- No real diagnostic claims.
- Separate UI, I/O, and logic.
- Mention files to create.
```

---

# Phase 7 — Mock AI result JSON viewer

## Goal

Learn how to integrate AI outputs safely without building a real model.

## Skills learned

- JSON loading
- schema validation
- displaying AI-like outputs
- safety labels
- separating inference output from clinical claims

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\workspace\sample_data\mock_ai_result.json
C:\slicerSTRT\docs\slicer\mock_ai_result_schema.md
```

## Example mock JSON

```json
{
  "case_id": "demo_case_001",
  "model_name": "mock-stratum-demo-model",
  "model_version": "0.0.0-demo",
  "tumour_probability": 0.72,
  "confidence": "medium",
  "warning": "Mock result only. Not for clinical use."
}
```

## Feature

Add:

- JSON result loader,
- validation checks,
- display of mock AI result,
- visible safety warning.

## Acceptance criteria

- Invalid JSON is handled.
- Missing fields are reported.
- Output is clearly marked as mock/demo.
- No real diagnosis is implied.

## Suggested Codex prompt

```text
Read AGENTS.md, docs/development/coding_standards.md, and docs/development/testing_strategy.md.

Task:
Add a mock AI result JSON viewer.

Rules:
- Use a simple JSON schema.
- Validate required fields.
- Display "Mock result only. Not for clinical use."
- Do not add real model inference.
```

---

# Phase 8 — Markdown report generator

## Goal

Create a simple traceable output report from the sandbox workflow.

## Skills learned

- collecting module state
- report generation
- saving files
- timestamping
- traceability

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\workspace\reports
C:\slicerSTRT\docs\slicer\report_generation.md
```

## Feature

Generate a Markdown report containing:

- timestamp,
- selected volume,
- volume metadata,
- selected points,
- distance measurement,
- segmentation summary,
- mock AI result,
- safety warning.

## Acceptance criteria

- Report saves under `C:\slicerSTRT\workspace\reports`.
- Report is Markdown.
- Report clearly says it is a sandbox/demo output.
- No private patient data is included unless explicitly allowed.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/development/coding_standards.md.

Task:
Add a Markdown report generator for sandbox results.

Rules:
- Save to C:\slicerSTRT\workspace\reports.
- Include a clear demo warning.
- Do not include private patient data.
- Keep file writing code small and testable.
```

---

# Phase 9 — Basic tests

## Goal

Add automated checks for the most important logic.

## Skills learned

- Slicer scripted module tests
- logic testing
- test data setup
- input validation testing

## Files involved

```text
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Testing
C:\slicerSTRT\extensions\SlicerStratum\Stratum\Stratum.py
C:\slicerSTRT\docs\development\testing_strategy.md
```

## Tests to add

Start with:

1. environment check logic returns expected keys,
2. distance calculation works for known points,
3. volume metadata logic handles missing input,
4. mock AI JSON loader handles valid JSON,
5. mock AI JSON loader reports missing fields.

## Acceptance criteria

- Tests are small.
- Tests do not require private data.
- Tests focus on `Logic`, not only GUI.
- Reload and Test still works.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/development/testing_strategy.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py
extensions/SlicerStratum/Stratum/Testing

Task:
Add the first basic tests for logic-only functions.

Rules:
- Do not require private data.
- Keep tests small.
- Do not rewrite the whole module.
```

---

# Phase 10 — Refactor when the module grows

## Goal

Avoid letting `Stratum.py` become a large, unmaintainable file.

## Skills learned

- modular Python design
- separating UI, logic, I/O, utils
- maintaining Slicer compatibility
- project hygiene

## Trigger

Do this only when `Stratum.py` becomes difficult to read or grows too much.

## Possible structure

```text
Stratum
├── Stratum.py
├── lib
│   ├── logic
│   │   ├── environment.py
│   │   ├── volume_metadata.py
│   │   ├── markups.py
│   │   ├── segmentation.py
│   │   └── mock_ai_results.py
│   ├── io
│   │   ├── json_results.py
│   │   └── report_writer.py
│   └── utils
│       └── validation.py
├── Resources
└── Testing
```

## Acceptance criteria

- `Stratum.py` keeps Slicer module entry points and UI.
- Logic moves into focused files.
- Tests still run.
- Imports work inside Slicer.
- No unnecessary architecture is added too early.

## Suggested Codex prompt

```text
Read AGENTS.md, docs/development/project_structure.md, and docs/development/coding_standards.md.

Inspect:
extensions/SlicerStratum/Stratum/Stratum.py

Task:
Propose a refactor plan only.

Rules:
- Do not code yet.
- Keep Slicer compatibility.
- Split only if there is a clear benefit.
- Mention exact files to create.
```

---

# Phase 11 — Performance and processing simulation

## Goal

Prepare for more complex processing workflows without implementing real HPC.

## Skills learned

- long-running task structure
- progress reporting
- cancellation pattern
- timing
- avoiding UI freeze

## Feature

Add a mock processing step:

- input: selected volume,
- action: fake/safe computation,
- output: timing information and status,
- optional progress bar.

## Acceptance criteria

- UI remains usable.
- Processing status is visible.
- No real diagnosis.
- No real HPC dependency.

## Suggested Codex prompt

```text
Read AGENTS.md and docs/development/coding_standards.md.

Task:
Design a safe mock long-running processing workflow for the sandbox.

Rules:
- Do not implement real HPC.
- Do not block the UI unnecessarily.
- Include progress/cancel design.
- Keep it as a learning feature.
```

---

# Phase 12 — Final sandbox review

## Goal

Review the sandbox as a learning project and prepare for future real STRATUM onboarding.

## Tasks

1. Review documentation.
2. Review module structure.
3. Review tests.
4. List what was learned.
5. List gaps before working on real STRATUM code.
6. Create a final handoff:

```text
C:\slicerSTRT\docs\codex\context_handoff.md
```

## Final review questions

- Can I create and reload a Slicer scripted module?
- Can I inspect Slicer MRML nodes?
- Can I work with volumes?
- Can I work with markups?
- Can I work with segmentations?
- Can I load/display mock AI results safely?
- Can I generate a report?
- Can I test module logic?
- Can I use Codex with narrow local context?

## Acceptance criteria

- Sandbox is documented.
- Sandbox is safe.
- Sandbox is understandable.
- Sandbox prepares the developer for real STRATUM work.
