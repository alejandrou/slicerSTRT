## Slicer architecture summary

3D Slicer is built around:
- Slicer application core
- MRML scene
- modules
- extensions
- libraries such as Qt, VTK, ITK, CTK, Python and NumPy

Our project uses a Python scripted loadable module because it is the simplest way to extend Slicer with full access to the Slicer API.

## MRML scene

The MRML scene is the shared storage for Slicer data.

Modules should communicate mainly through MRML nodes, not by directly depending on each other.

Important ideas:
- Data is stored in MRML nodes.
- Display options belong in display nodes.
- Storage information belongs in storage nodes.
- Processing logic should read/write MRML nodes where needed.
- Do not store important state only in the UI.

## Scripted module structure

The module is split into:

- Module class
- Widget class
- Logic class

In this project:

- `Stratum.py` contains module metadata and module entry point.
- `StratumWidget.py` contains UI code only.
- `StratumLogic.py` contains processing/business logic.
- `StratumTest.py` contains tests.

## Module class rules

The module class should only define:
- title
- categories
- contributors
- help text
- acknowledgement text
- module-level setup if needed

Do not put feature logic here.

## Widget class rules

The Widget class is responsible for:
- building the UI
- connecting buttons and selectors
- reading values from UI controls
- calling methods from `StratumLogic`
- updating labels, tables, and visual UI output
- keeping UI synchronized with parameter nodes when used

The Widget must not contain processing algorithms.

Bad:
- calculating measurements directly in the button callback
- parsing AI JSON directly inside the UI
- modifying volumes directly from UI code

Good:
- button callback gets selected node
- button callback calls `self.logic.someMethod(...)`
- button callback displays returned result

## Logic class rules

The Logic class is responsible for:
- computation
- validation
- MRML node inspection
- measurements
- data conversion
- report generation helpers
- prototype workflow logic

The Logic class must not depend on the Widget.

Logic methods should be callable from:
- the UI
- tests
- another module
- the Python console

## Passive logic first

Use passive logic by default.

That means:
- the Widget creates/owns a logic instance
- the logic does work only when called
- no background scene observers unless needed later

Avoid active logic until the project really needs real-time background behavior.

## Parameter node policy

For early learning features, simple UI state is acceptable.

Use a parameter node when:
- settings must survive scene save/load
- the module has multiple linked inputs
- the UI must stay synchronized with MRML state
- workflows become more complex

Do not over-engineer parameter nodes too early.

## Common mistakes to avoid

1. Do not implement everything in the Widget.
2. Do not let Logic depend on Widget.
3. Do not store important state only in UI controls.
4. Do not modify MRML nodes without updating the UI when needed.
5. Do not add clinical/STRATUM production logic before the sandbox workflow is stable.
6. Do not add sample data, API calls, or AI workflows without a clear task.

## Current recommended feature order

1. Environment check
2. Volume metadata viewer
3. Markups distance calculator
4. Segmentation inspector
5. Mock AI JSON viewer
6. Markdown report generator
7. API integration placeholder

## Coding rules for AI

Before changing code:
- inspect current files
- explain planned changes
- keep changes small
- modify only files needed for the task
- update tests if logic changes
- update `context_handoff.md`
- provide manual Slicer test steps

Never:
- rewrite the whole module without asking
- add clinical claims
- add real STRATUM API integration without approval
- move logic into the UI