# Code Quality Policy

Code and documentation changes must be small, readable, and reviewable.

## Rules

- Keep responsibilities separated between UI, logic, I/O, tests, and reusable helpers.
- Prefer clear names over abbreviations. Include units or coordinate systems when they matter.
- Avoid unrelated refactors, broad formatting churn, and premature abstractions.
- Add comments only when they explain non-obvious intent, constraints, safety checks, or assumptions.
- Keep generated template behavior from becoming the source of project design.
- Do not hide validation failures or present mock results as real clinical output.

For Python scripted modules, keep module metadata, widget behavior, logic, tests, and helpers distinct whenever practical.
