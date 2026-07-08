# STRATUM / slicerSTRT Codex Instructions

This repository is a Windows 11 3D Slicer development workspace for the STRATUM / slicerSTRT learning project.

Codex must treat this file as the entry point before making changes.

---

## 1. Project identity

This is not the upstream 3D Slicer repository.

This workspace contains:

* a local clone of upstream 3D Slicer for reference,
* a local Slicer build,
* a STRATUM-specific Slicer extension,
* project documentation,
* temporary workspace material,
* local knowledge and notes.

The current goal is to build a safe local Slicer scripted-module sandbox inspired by slicerSTRT concepts.

Do not implement clinical diagnosis, surgical guidance, real medical decision logic, or unvalidated STRATUM algorithms unless explicitly instructed.

---

## 2. Main paths

Project root:

```text
C:\stratum
```

Important paths:

```text
C:\stratum\source
C:\stratum\apps\SR
C:\stratum\apps\SR\Slicer-build\Slicer.exe
C:\stratum\extensions
C:\stratum\extensions\slicerSTRT
C:\stratum\extensions\slicerSTRT\slicerSTRT
C:\stratum\docs
C:\stratum\knowledge
C:\stratum\workspace
```

Slicer skill path:

```text
C:\Users\AlejandroHerrera\.codex\skills\slicer-skill
```

---

## 3. Folder responsibilities

### `source`

Local clone of upstream 3D Slicer.

Use only as reference for:

* Slicer APIs,
* scripted module examples,
* MRML,
* Qt,
* VTK,
* ITK,
* CMake,
* extension structure.

Do not edit this folder unless explicitly requested.

### `apps`

Local application/build area.

Current Slicer build:

```text
C:\stratum\apps\SR\Slicer-build\Slicer.exe
```

Do not edit this folder unless explicitly requested.

Do not commit generated build outputs.

### `extensions`

Main project code area.

Normal slicerSTRT development goes here.

Current extension:

```text
C:\stratum\extensions\slicerSTRT
```

Current module:

```text
C:\stratum\extensions\slicerSTRT\slicerSTRT
```

### `docs`

Project documentation, development notes, Codex workflow, Slicer notes, and planning files.

Use this as the main source of project intent.

### `knowledge`

External references, PDFs, downloaded docs, and supporting notes.

Use as read-only reference material unless explicitly asked to organize or update it.

### `workspace`

Temporary scripts, experiments, reports, generated data, and local-only material.

Do not put final module source code here.

---

## 4. Default edit permissions

Codex may normally edit:

```text
C:\stratum\extensions
C:\stratum\docs
C:\stratum\workspace
```

Codex must not edit unless explicitly requested:

```text
C:\stratum\source
C:\stratum\apps
C:\stratum\knowledge
```

Codex must ask before Git operations:

* commit,
* push,
* pull,
* branch,
* merge,
* rebase,
* reset,
* force operations,
* deleting tracked files.

---

## 5. Required reading order

Before changing project structure, read:

```text
docs\development\project_structure.md
```

Before writing or modifying code, read:

```text
docs\development\coding_standards.md
```

Before adding or changing tests, read:

```text
docs\development\testing_strategy.md
```

Before answering Slicer API/module questions, read:

```text
docs\slicer\slicer_knowledge_index.md
```

Before planning Codex workflow or context usage, read:

```text
docs\codex\codex_workflow.md
docs\codex\context_management.md
```

Before continuing project progress, read:

```text
docs\codex\context_handoff.md
```

Before implementing sandbox roadmap tasks, read:

```text
docs\development\sandbox_roadmap.md
```

---

## 6. Search order for Slicer questions

When answering Slicer-specific questions, do not invent APIs.

Search in this order:

1. Current project extension:

```text
C:\stratum\extensions\slicerSTRT
```

2. Local Slicer source:

```text
C:\stratum\source
```

3. Local Slicer skill:

```text
C:\Users\AlejandroHerrera\.codex\skills\slicer-skill
```

4. Web or external sources only if local references are insufficient or the user asks for current/latest information.

When giving an answer, mention which local paths were inspected.

---

## 7. Development rules

Use Python scripted modules by default.

Do not use C++ unless there is a clear reason.

Do not rebuild Slicer for normal Python changes.

For normal `.py` module changes:

1. edit files under `extensions\slicerSTRT`,
2. open Slicer,
3. enable Developer Mode,
4. use Reload or Reload and Test.

Only rebuild Slicer when changing C++, CMake, extension packaging, or build-level configuration.

Keep changes small, readable, and testable.

Avoid large multi-phase edits.

Do one roadmap phase at a time.

---

## 8. Code structure rules

Keep responsibilities separated.

For scripted modules:

* module entry file: metadata and registration only,
* widget class: UI, events, scene interaction,
* logic class: processing and algorithmic behavior,
* test class: automated checks,
* helper modules: reusable utilities when needed.

Do not put real logic directly inside button callbacks.

Avoid large files.

Avoid unclear names such as:

```text
tmp
data
manager
processor
x
pos
```

Prefer explicit names with units and coordinate systems where useful:

```text
inputVolumeNode
segmentationNode
entryPoint_RAS
targetPoint_RAS
distanceMm
angleDeg
spacingMm
```

---

## 9. Medical safety rules

This project is a learning sandbox.

Do not commit:

* private patient data,
* non-anonymized DICOM files,
* sensitive medical images,
* real clinical reports,
* private hospital data.

Use only:

* synthetic data,
* public Slicer sample data,
* anonymized test data,
* mock JSON/results.

Do not present mock AI output as real diagnosis.

Do not implement real surgical guidance or clinical decision-making.

---

## 10. Testing rules

Prefer tests for:

* logic functions,
* validation,
* coordinate conversions,
* input/output behavior,
* error handling.

Avoid testing only GUI clicks unless necessary.

Tests for the current module should live under:

```text
C:\stratum\extensions\slicerSTRT\slicerSTRT\Testing
```

For Python module changes, test with:

```text
Reload
Reload and Test
```

inside Slicer.

Use small, repeatable, independent tests.

---

## 11. Context and token management

Before starting a task, inspect only the files needed for that task.

Do not read the full Slicer source tree unless necessary.

Prefer targeted searches.

Use this order for task context:

1. `AGENTS.md`
2. relevant docs under `docs`
3. current extension files
4. local Slicer source only if API confirmation is needed
5. slicer-skill only if Slicer patterns are needed

For large tasks, first summarize:

* files inspected,
* current state,
* intended change,
* risks,
* test plan.

Then make the smallest safe change.

---

## 12. Expected Codex response format

For implementation tasks, respond with:

1. Direct answer.
2. Files inspected.
3. Changes made or proposed.
4. How to test in Slicer.
5. Any risks or follow-up tasks.

For review/planning tasks, respond with:

1. Current assessment.
2. Problems found.
3. Recommended next step.
4. Files or paths involved.

Do not over-explain unless the user asks.

---

## 13. Current working assumptions

The local Slicer build works.

The slicerSTRT module is a Python scripted module.

The active development location is:

```text
C:\stratum\extensions\slicerSTRT
```

The current project is still a safe sandbox and should not be treated as production clinical software.

Before adding new functionality, prefer cleaning generated template behavior and keeping the extension understandable.

---

## 14. Reusable Codex workflow

For future Codex tasks, prefer this pattern:

* Read `AGENTS.md`.
* Follow the relevant `.agents/*.md` files.
* Implement one specific `tasks/*.md` task card.
* Keep changes small and reviewable.
* Do not run Git commands unless explicitly asked.

Example 1:

```text
Read AGENTS.md. Follow .agents/task_protocol.md and .agents/slicer_workflow.md. Implement tasks/phase_2a_check_environment.md. Keep changes small. Do not run Git commands.
```

Example 2:

```text
Read AGENTS.md. Follow .agents/task_protocol.md and .agents/code_style.md. In extensions/slicerSTRT, make only the requested small change: <describe change>. Do not run Git commands.
```
