# Dependency Policy

Do not add new dependencies unless the active task explicitly approves them.

## Rules

- Prefer Python standard library, Slicer-bundled modules, and existing project dependencies.
- Do not add a YAML parser for workflow metadata.
- Do not install Python packages, modify package manager files, or alter build dependency configuration without explicit approval.
- Document any approved dependency addition in the task card, including why existing tools were insufficient.
