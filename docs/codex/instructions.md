# slicerSTRT Codex Instructions

Personal workflow guide for using Codex efficiently in the slicerSTRT / 3D Slicer workspace.

This file is for the developer, not for the AI agent.

Recommended location:

```text
C:\slicerSTRT\docs\codex\instructions.md
```

---

## 1. Main idea

Use AI heavily, but do not give it the whole project every time.

The goal is not to reduce AI usage. The goal is to reduce wasted context.

Use:

- Small context for simple tasks.
- Larger context for Slicer-specific or architectural tasks.
- Stronger models only when the task actually needs deeper reasoning.

---

## 2. Default workflow

Always open VS Code at:

```text
C:\slicerSTRT
```

Before starting a Codex task, make sure the project has:

```text
C:\slicerSTRT\AGENTS.md
```

That file is the entry point for Codex.

For your own workflow, start each new Codex chat with a narrow task and a clear list of files to read.

---

## 3. Context strategy

### Good default

For most small tasks, ask Codex to read only:

```text
AGENTS.md
one relevant docs file
one relevant source file
```

Example:

```text
Read AGENTS.md and docs/development/coding_standards.md.

Then inspect only:
extensions/slicerSTRT/slicerSTRT/slicerSTRT.py

Task:
Explain the current module structure and suggest the smallest safe cleanup.

Do not inspect C:\slicerSTRT\source unless you need to verify a Slicer API.
Do not edit anything yet.
```

### Avoid

Avoid prompts like:

```text
Read all of C:\slicerSTRT and tell me what to do.
```

This wastes context and increases the chance of generic answers.

---

## 4. When to start a new chat

Start a new Codex chat when the task changes.

Good separation:

```text
Chat 1: project structure
Chat 2: clean slicerSTRT.py
Chat 3: add first test
Chat 4: understand MRML nodes
Chat 5: add UI controls
Chat 6: debug CMake/build issue
```

Do not keep one huge chat for everything.

Each new chat should start with:

```text
Read AGENTS.md first.
Then read only the files I mention.
Do not inspect the full project unless needed.
```

---

## 5. Model strategy

Use cheaper/faster models for:

- Documentation
- Markdown cleanup
- Folder organization
- Simple explanations
- Small Python edits
- Naming improvements
- Simple tests
- Reading generated template code

Use stronger reasoning models for:

- Slicer architecture decisions
- MRML logic
- VTK / ITK / SimpleITK issues
- C++ modules
- CLI modules
- CMake/build errors
- Medical-image processing logic
- Complex refactors
- Debugging errors that are not obvious
- Reviewing safety-sensitive code

Simple rule:

```text
Cheap/fast model = execution and cleanup
Strong model = planning, architecture, debugging, complex Slicer decisions
```

---

## 6. Prompt templates

### A. Documentation task

```text
Read AGENTS.md.

Then read:
docs/development/project_structure.md

Task:
Improve this document for clarity.

Rules:
- Do not inspect source code.
- Do not change project code.
- Keep it concise.
```

### B. Slicer API question

```text
Read AGENTS.md.

Task:
I need to understand how [SLICER CONCEPT] works.

Search order:
1. extensions/slicerSTRT
2. C:\slicerSTRT\source
3. C:\Users\AlejandroHerrera\.codex\skills\slicer-skill

Rules:
- Do not guess APIs.
- Mention exact local paths inspected.
- Do not edit files.
```

### C. Small code change

```text
Read AGENTS.md.

Then read:
docs/development/coding_standards.md
extensions/slicerSTRT/slicerSTRT/slicerSTRT.py

Task:
Make the smallest safe change to [GOAL].

Rules:
- Explain the plan before editing.
- Do not edit C:\slicerSTRT\source.
- Do not edit C:\slicerSTRT\apps\SR.
- Do not do Git operations.
- After editing, explain how to test with Slicer Reload / Reload and Test.
```

### D. Debugging task

```text
Read AGENTS.md.

Problem:
[PASTE ERROR]

Context:
[WHAT YOU WERE DOING]

Task:
Diagnose the likely cause.

Rules:
- First inspect the relevant project files.
- Search Slicer source only if needed.
- Give a minimal fix.
- Do not rewrite unrelated code.
```

### E. Architecture task

```text
Read AGENTS.md.

Then read:
docs/development/project_structure.md
docs/development/coding_standards.md
docs/development/testing_strategy.md
docs/slicer/slicer_knowledge_index.md

Task:
Propose the architecture for [FEATURE].

Rules:
- Do not code yet.
- Separate UI, logic, I/O, and tests.
- Prefer Python scripted module unless C++/CLI is clearly required.
- Mention which files would be changed or created.
```

---

## 7. Reusable knowledge strategy

When Codex gives an answer that will be useful again, save it into a local Markdown file.

Examples:

```text
docs/slicer/scripted_module_structure.md
docs/slicer/module_reload_workflow.md
docs/slicer/common_slicer_errors.md
docs/development/decisions.md
docs/codex/context_handoff.md
```

This acts like a manual cache.

If you solve a problem once, do not pay for the same reasoning again.

---

## 8. What to tag with @ in VS Code

For small tasks, tag only the exact files needed.

Good:

```text
@AGENTS.md
@docs/development/coding_standards.md
@extensions/slicerSTRT/slicerSTRT/slicerSTRT.py
```

For Slicer API tasks:

```text
@AGENTS.md
@docs/slicer/slicer_knowledge_index.md
@extensions/slicerSTRT/slicerSTRT/slicerSTRT.py
```

Only add source folders when needed:

```text
@source/Modules
@source/Libs
@source/Base
```

Avoid tagging:

```text
@C:\slicerSTRT
@source
@apps\SR
```

unless the task really needs that much context.

---

## 9. Safety rules

Do not let Codex edit these unless explicitly needed:

```text
C:\slicerSTRT\apps\SR
C:\slicerSTRT\source
```

Normal development goes under:

```text
C:\slicerSTRT\extensions\slicerSTRT
```

Documentation goes under:

```text
C:\slicerSTRT\docs
```

Temporary experiments go under:

```text
C:\slicerSTRT\workspace
```

---

## 10. Daily practical workflow

For a normal development session:

1. Open VS Code at `C:\slicerSTRT`.
2. Open Slicer from `C:\slicerSTRT\apps\SR\Slicer-build\Slicer.exe`.
3. Start a new Codex chat for the task.
4. Tell Codex to read `AGENTS.md`.
5. Give only the files needed.
6. Ask for a plan before edits.
7. Apply the smallest change.
8. Test in Slicer with Reload / Reload and Test.
9. Save useful conclusions into `docs`.
10. Start a new chat when switching task.

---

## 11. Quick decision table

| Task | Context | Model |
|---|---|---|
| Markdown/docs cleanup | AGENTS.md + one docs file | Cheap/fast |
| Explain slicerSTRT.py | AGENTS.md + slicerSTRT.py | Cheap/fast |
| Small Python change | AGENTS.md + coding standards + target file | Cheap/fast or medium |
| First test | AGENTS.md + testing strategy + target file | Medium |
| Slicer API question | AGENTS.md + slicer index + relevant source folder | Medium/strong |
| CMake/build problem | AGENTS.md + build docs + error log + relevant CMake files | Strong |
| VTK/ITK/MRML problem | AGENTS.md + relevant source + slicer-skill | Strong |
| Architecture/refactor | AGENTS.md + project docs + module files | Strong |

---

## 12. Golden rule

Do not ask Codex to know everything.

Ask it to inspect the right small part of the project, verify against local sources, and make the smallest safe next step.

## Working through the sandbox roadmap

Use the sandbox roadmap one phase at a time.

Location:

`docs/development/sandbox_roadmap.md`

Recommended approach:

1. Start a new Codex chat per phase.
2. Ask Codex to read `AGENTS.md` and `sandbox_roadmap.md`.
3. Mention the exact phase.
4. Ask for a plan before edits.
5. Test in Slicer.
6. Update `context_handoff.md`.
