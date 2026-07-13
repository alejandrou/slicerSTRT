# Project Structure

This repository contains the STRATUM-related 3D Slicer development prototype. It is not production clinical software.

## Top-Level Areas

- `AGENTS.md`: Codex routing, repository source-of-truth order, and edit-scope rules.
- `.ai/`: authoritative policies, workflows, and templates for repository work.
- `tasks/`: active, review, backlog, and completed task cards.
- `docs/`: developer and technical documentation.
- `config/`: portable local configuration template and ignored local configuration.
- `extensions/`: STRATUM-specific Slicer extension and module source.
- `source/`: local upstream Slicer source reference.
- `apps/`: local Slicer application and build outputs.
- `workspace/`: temporary work, experiments, scripts, and local generated artifacts.
- `knowledge/`: ignored local reference material, downloaded files, and private working notes.

For exact edit permissions, follow `AGENTS.md` and the active task card.

## Development Code

STRATUM extension development occurs under:

```text
extensions/slicerSTRT/
```

The current scripted module lives under:

```text
extensions/slicerSTRT/slicerSTRT/
```

Keep final module source in `extensions/`, not in `workspace/`.

## Local Slicer Source And Build Outputs

The local Slicer source tree under `source/` is used as a reference for Slicer APIs, MRML, Qt, VTK, ITK, CMake, and extension examples.

The local build tree under `apps/` is generated output. The conventional build location for this workspace is `apps/SR/`, with the executable under `apps/SR/Slicer-build/`.

Machine-specific paths should be configured in `config/local.json`, using `config/local.example.json` as the template.

## Documentation

- `docs/development/`: project structure, coding standards, and testing strategy.
- `docs/slicer/`: reusable Slicer technical notes.
- `docs/architecture/decisions/`: accepted ADRs.
- `docs/knowledge/`: curated, non-sensitive, version-controlled reference notes useful to the project.

## Task And Workflow Files

Current work is tracked under `tasks/`.

Repository policies and workflows live under `.ai/`. Do not duplicate complete policies or workflows in development documentation; link to the authoritative file instead.
