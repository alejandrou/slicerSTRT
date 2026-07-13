---
id: BSSL-003
title: Align module identity and establish Python quality tooling
status: active
branch: feature/BSSL-003-module-identity-python-quality
required_skills:
  - slicer
optional_tools:
  - ruff
  - pyright
  - PowerShell
related_adrs: []
---

# BSSL-003 - Align module identity and establish Python quality tooling

## Goal

Complete one small, independently reviewable development-foundation task that aligns the remaining user-visible slicerSTRT module metadata with the active STRATUM project identity, establishes practical Ruff and Pyright baselines for project-owned Python, and provides one PowerShell command for running both tools locally.

## Context

BSSL-002 consolidated the repository documentation and is completed and merged into `main`. This task must not repeat or redesign that documentation work.

The current scripted module already provides Check Environment and Inspect Volume behavior. Its help and acknowledgement metadata still call the module a `learning sandbox`, which no longer matches the repository identity in `AGENTS.md`. The project-owned Python currently consists of the entry point and four files in `slicerSTRTLib`; there is no committed Ruff or Pyright configuration and no combined local Python-quality command.

The local Slicer runtime cannot be verified during specification because `config/local.json` is absent. Implementation must check the runtime configured by `config/local.json` when practical. If the embedded Python version cannot be verified, Ruff's `target-version` must be omitted rather than guessed.

This task does not require an ADR. The metadata correction and initial quality-tool settings are narrow, reversible development-foundation choices and do not establish a difficult or expensive-to-reverse architecture.

## Requirements

### Module identity

- Update only obsolete user-visible help and acknowledgement wording in `slicerSTRT.py`.
- Describe slicerSTRT accurately as:
  - part of the active STRATUM-related 3D Slicer prototype;
  - currently providing environment and volume-inspection tools;
  - not production clinical software;
  - not implementing validated clinical or STRATUM algorithms.
- Remove active module-metadata wording that presents the module as a `learning sandbox`, a disposable training module, or equivalent.
- Preserve the module title `slicerSTRT`, category `STRATUM`, contributors, dependencies, public Slicer class names, and all existing behavior.
- Do not change Check Environment, Inspect Volume, widget, logic, test, MRML, or UI behavior in this workstream.
- Keep user-visible strings translatable through the existing Slicer internationalization pattern.

### Ruff baseline

- Add a minimal `pyproject.toml` containing Ruff configuration only; do not add a build system, package metadata, runtime dependencies, or Slicer extension dependencies.
- Limit analysis to Python files under `extensions/slicerSTRT/slicerSTRT/`.
- Explicitly exclude `source/`, `apps/`, `knowledge/`, `workspace/`, local configuration, generated files, caches, virtual environments, and build outputs.
- Select the initial rule families `E4`, `E7`, `E9`, `F`, `I`, and `B`:
  - `E4`, `E7`, and `E9` for import, statement, and runtime/syntax-related pycodestyle errors;
  - `F` for Pyflakes import, undefined-name, and unused-import diagnostics;
  - `I` for import ordering;
  - `B` for low-risk flake8-bugbear correctness checks.
- Do not enable generic naming rules such as `N`; established public classes including `slicerSTRT`, `slicerSTRTWidget`, `slicerSTRTLogic`, and `slicerSTRTTest` must not be renamed.
- Do not enable Ruff formatting, repository-wide formatting rules, or broad style families that create large churn.
- The local quality script must run `ruff check` without `--fix` or unsafe fixes. Any fixes must be reviewed and applied explicitly.
- Verify the configured Slicer embedded Python version before setting Ruff `target-version`. Omit `target-version` if it cannot be verified from the configured runtime.

### Pyright baseline

- Add `pyrightconfig.json` with `typeCheckingMode` set to `basic`.
- Include only `extensions/slicerSTRT/` project-owned Python and exclude upstream, protected, generated, build, cache, virtual-environment, and local-only areas.
- Add `extensions/slicerSTRT/slicerSTRT` to `extraPaths` so imports of `slicerSTRTLib` resolve from the repository root.
- Keep syntax errors, undefined local symbols, local import diagnostics, and the ordinary obvious-type diagnostics from `basic` mode enabled.
- Treat missing imports from the external Slicer runtime as warnings rather than errors, and suppress `reportMissingModuleSource` noise caused by compiled or runtime-provided modules. This exception exists because normal system Python does not provide the real `slicer`, `qt`, `ctk`, and Slicer-bundled `vtk` runtime.
- Keep local import findings visible. Do not ignore the extension tree, disable all diagnostics, or use an `ignore` entry that hides project files.
- Prefer narrow per-import or per-diagnostic suppression only if the baseline still produces unusable false positives for runtime-provided Slicer APIs. Every such suppression must name the diagnostic and reason in `docs/development/coding_standards.md` and be listed individually in completion evidence.
- Do not add large fake Slicer, Qt, CTK, or VTK stubs.
- Do not commit machine-specific interpreter or search paths.

### Local quality command

- Add `scripts/development/run-python-quality.ps1`.
- Resolve the repository root from `$PSScriptRoot` so the script works from any current working directory.
- Check both `ruff` and `pyright` with clear preflight messages before running checks.
- If either tool is unavailable, identify the missing command, state that no installation was attempted, and exit non-zero.
- Print distinct Ruff and Pyright section headings.
- Run `ruff check extensions/slicerSTRT/slicerSTRT` from the repository root.
- Run `pyright --project pyrightconfig.json` from the repository root.
- Attempt both checks when both commands are available, even if Ruff fails, and return non-zero if either check fails.
- Restore the caller's location when the script exits.
- Do not install, update, or invoke a package manager, and do not use Slicer's embedded Python to install development tools.

### Documentation

- Add one concise `Local Python Quality Checks` section to `docs/development/coding_standards.md`.
- Document the repository-root command:

  ```powershell
  .\scripts\development\run-python-quality.ps1
  ```

- State that the command runs Ruff and Pyright against project-owned extension Python.
- State that Ruff and Pyright are local development prerequisites, not Slicer runtime dependencies, and may be installed in the developer's normal tooling environment before running the command.
- Briefly document the intentional Pyright treatment of unavailable Slicer runtime imports and the reason for each configured or inline suppression.
- Do not create a separate quality-tooling guide or repeat BSSL-002's documentation consolidation.

### Allowed source corrections

- After the configurations load and report findings, correct project-owned Python only when a finding is directly produced by the new baseline and the correction is behavior-preserving, mechanical, and easy to review.
- Permitted examples are unused-import removal, import ordering, a definite undefined-name correction, a narrow type annotation, or minor formatting required by an enabled Ruff rule.
- List every production Python correction individually in completion evidence with its originating diagnostic.
- If a finding would require behavioral judgment, architecture changes, a public-class rename, broad formatting, or more than a narrow mechanical correction, leave it unchanged and record it as a risk or follow-up instead of expanding this task.

## Out of scope

- New module functionality or UI behavior.
- Documentation consolidation or redesign.
- Automated Slicer test execution or CMake test registration.
- GitHub Actions, CI, or other automation services.
- Parameter nodes, algorithm providers, segmentation workflows, or datasets.
- Private or sensitive medical data.
- MCP.
- C++, CMake, production CMake, or Qt `.ui` changes.
- Runtime dependency or package-manager changes.
- Large Slicer API stubs.
- Project-wide formatting or automated rewrites.
- Changes under `source/`, `apps/`, `knowledge/`, or `workspace/`.
- Changes to external skills, build outputs, private local configuration, or generated files other than the explicitly approved ignored root `.venv/`.
- Creating or switching Git branches, installing tools, committing, pushing, or other unapproved Git mutations.

## Files allowed

Only these files may be created or modified during implementation:

- `extensions/slicerSTRT/slicerSTRT/slicerSTRT.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/__init__.py`, only for a directly reported quality finding
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTLogic.py`, only for a directly reported quality finding
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`, only for a directly reported quality finding
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`, only for a directly reported quality finding
- `pyproject.toml`
- `pyrightconfig.json`
- `scripts/development/run-python-quality.ps1`
- `.gitignore`, for the approved Ruff cache and root `.venv/` exclusions
- `.venv/**`, as an ignored local development environment containing only Ruff, Pyright, and their transitive dependencies
- `docs/development/coding_standards.md`
- `tasks/backlog/BSSL-003-module-identity-python-quality.md`, including lifecycle moves of this same task card

No other file is authorized. Update this task card and obtain human approval before changing the allowlist.

## Relevant skills and references

- Required: installed `slicer` skill for scripted-module metadata conventions, public Slicer class naming, and Reload / Reload and Test verification.
- Root `AGENTS.md`.
- `.ai/workflows/task-lifecycle.md`.
- `.ai/workflows/implementation-workflow.md`.
- `.ai/workflows/manual-verification-workflow.md`.
- `.ai/policies/code-quality.md`.
- `.ai/policies/dependency-policy.md`.
- `.ai/policies/git-workflow.md`.
- `.ai/policies/medical-data-policy.md`.
- `.ai/policies/algorithm-boundary-policy.md`.
- `config/local.example.json` for the portable local Slicer configuration shape.
- Current project-owned Python under `extensions/slicerSTRT/slicerSTRT/`.

## Implementation plan

1. Confirm this is the only task across `tasks/active/` and `tasks/review/`, obtain human approval, and move this same task card to `tasks/active/` before implementation.
2. Reinspect the allowed project-owned Python, current Git status, relevant policies, and configured local Slicer runtime without changing protected or local files.
3. Update only the obsolete module help and acknowledgement wording while preserving metadata and behavior.
4. Add the scoped Ruff configuration and verify whether a Ruff target Python can be supported by the configured Slicer runtime.
5. Add the scoped Pyright configuration with `basic` checking, local-package resolution, and documented Slicer-runtime import handling.
6. Add the PowerShell quality script and concise coding-standards section.
7. Run configuration and script validation without automatic fixes. Apply only permitted, directly reported mechanical source corrections and record each one.
8. Review the complete diff for scope, formatting churn, module logic changes, protected paths, generated files, and undocumented suppressions.
9. Ask the user to perform the required manual Slicer verification and record the results before review.

## Acceptance criteria

- Ruff configuration loads successfully.
- Pyright configuration loads successfully.
- The PowerShell command works from the repository root and from another working directory.
- The script runs Ruff and Pyright when both are available.
- The script reports each missing required command clearly, does not install anything, and exits non-zero when a required tool is unavailable.
- The script attempts both checks when available and exits non-zero if either check fails.
- Ruff checks only Python under `extensions/slicerSTRT/slicerSTRT/`.
- Pyright checks only project-owned Python under `extensions/slicerSTRT/` and resolves `slicerSTRTLib` through the configured `extraPaths`.
- Unavailable Slicer runtime imports do not create an unusable false-positive wall.
- Missing-import and missing-module-source treatment, plus any narrower suppressions, are documented with reasons.
- Useful syntax, undefined-symbol, local-import, and obvious-type diagnostics remain enabled.
- Ruff uses `E4`, `E7`, `E9`, `F`, `I`, and `B`; no generic naming rules or formatter are enabled.
- No Ruff target Python is guessed.
- No obsolete `learning sandbox` or disposable-training wording remains in active module metadata.
- Help and acknowledgement text accurately state the STRATUM prototype, current inspection tools, non-clinical status, and absence of validated clinical or STRATUM algorithms.
- Module title, category, contributors, dependencies, public Slicer class names, Check Environment, and Inspect Volume remain unchanged.
- No large fake stubs, runtime dependencies, broad automated rewrite, project-wide formatting, or unrelated cleanup is introduced.
- Every production Python correction is directly tied to a baseline diagnostic and listed individually in completion evidence.
- No upstream, protected, local, generated, build, production CMake, Qt `.ui`, dataset, or unlisted file changes.

## Test plan

Fast automated and command-line validation must include:

1. Run Ruff directly to prove `pyproject.toml` loads and inspect the reported file set.
2. Run Pyright directly with `--project pyrightconfig.json` to prove the configuration loads, the local package resolves, and the reported file set stays in scope.
3. Run `scripts/development/run-python-quality.ps1` from the repository root.
4. Run the same script by absolute or relative path from a different working directory.
5. Exercise the unavailable-tool preflight in a temporary child PowerShell environment with a deliberately restricted `PATH`; confirm a clear message and non-zero exit without installing or changing anything.
6. Exercise or inspect failure propagation so a Ruff or Pyright failure produces a non-zero script exit while the other available check is still attempted.
7. Search active module metadata for obsolete `learning sandbox`, disposable-training, or equivalent wording.
8. Review the before/after Python diff to confirm metadata-only identity changes and individually justified quality corrections.
9. Inspect tool output and configuration include/exclude settings to confirm no file outside the approved project-owned Python paths is analyzed.
10. Inspect Git status and diff to confirm only files in `Files allowed` changed and that protected, generated, build, CMake, UI, dataset, and local configuration areas remain untouched.

Do not run automated fixes across the repository. Automated Slicer test execution is outside this task; the user performs Slicer verification manually.

## Manual verification

Using the Slicer executable configured by `config/local.json`, the user must:

1. Open Slicer and load the slicerSTRT module.
2. Confirm the module title remains `slicerSTRT` and the category remains `STRATUM`.
3. Confirm the revised help and acknowledgement text displays correctly and communicates the prototype and non-clinical boundaries.
4. Run Check Environment and confirm it still works.
5. Select an allowed synthetic, public, anonymized, or mock volume and run Inspect Volume; confirm it still works.
6. Use Reload and confirm it succeeds.
7. Use Reload and Test and confirm it succeeds.
8. Confirm no new Python error appears in Slicer.
9. Record the Slicer version, embedded Python version, and observed results in completion evidence without adding machine-specific paths or private configuration.

## Risks

- Normal system Python does not expose the complete Slicer, Qt, CTK, and VTK runtime, so Pyright needs a documented compromise between useful project checks and external-import noise. The initial strategy downgrades missing runtime imports and suppresses missing-module-source noise without ignoring project files.
- A separately installed package named `slicer` may not represent 3D Slicer's runtime API. The configuration must not treat that package as authoritative or add machine-specific paths to make checks pass.
- The embedded Python version is currently unknown because `config/local.json` is absent. Ruff must omit `target-version` unless implementation can verify it from a configured Slicer runtime.
- Ruff `B` or Pyright `basic` may reveal a finding that is not safely mechanical. Such a finding must be documented and deferred rather than expanding the task.
- Import ordering or narrow suppression comments may touch several small Python files. The diff must remain behavior-preserving and every production correction must be itemized.
- Manual Slicer verification depends on the user's configured local runtime and cannot be replaced by system-Python checks.

## Documentation impact

Modify only the necessary portion of `docs/development/coding_standards.md` to add `Local Python Quality Checks`, the single PowerShell command, prerequisite status of Ruff and Pyright, and the documented reason for Slicer-runtime diagnostic handling. Do not create another Markdown guide or revisit BSSL-002's broader documentation organization.

## Completion evidence

Implementation evidence recorded on 2026-07-13. Ruff and Pyright validation is complete. The task remains active because manual Slicer verification is pending.

Activation:

- The user approved the specification and explicitly authorized activation, branch creation, and implementation on 2026-07-13.
- The user explicitly authorized replacing the external BSSL-003 environment with an ignored project-root `.venv` shared across branch switches in this working tree, installing the approved development tools there, and deleting the previous external environment on 2026-07-13.
- The task card was moved from `tasks/backlog/` to `tasks/active/` and its status was changed to `active`.
- `git switch -c feature/BSSL-003-module-identity-python-quality` created and switched to the approved branch.
- Active/review task enumeration reported exactly one task card: this file under `tasks/active/`.
- No commit or push was performed.

Files inspected:

- `AGENTS.md`
- This task card before and after activation
- `.ai/workflows/task-lifecycle.md`
- `.ai/workflows/implementation-workflow.md`
- `.ai/workflows/manual-verification-workflow.md`
- `.ai/policies/code-quality.md`
- `.ai/policies/dependency-policy.md`
- `.ai/policies/git-workflow.md`
- `.ai/policies/medical-data-policy.md`
- `.ai/policies/algorithm-boundary-policy.md`
- `config/local.example.json`
- Presence of ignored `config/local.json`, without modifying private configuration
- `.gitignore`
- `docs/development/coding_standards.md`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRT.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/__init__.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTLogic.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTTest.py`
- Installed Slicer skill, used only for public scripted-module class naming, metadata internationalization, and Reload / Reload and Test verification guidance

Files created:

- `pyproject.toml`
- `pyrightconfig.json`
- `scripts/development/run-python-quality.ps1`

Files modified:

- `.gitignore`: added `.ruff_cache/` and `/.venv/` so approved local quality artifacts and the project development environment remain untracked.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRT.py`: replaced obsolete learning-sandbox help and acknowledgement wording, removed one unused import, sorted imports, and made the three required public Slicer exports explicit. Title, category, contributors, dependencies, classes, widget/logic behavior, and tests were not changed.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/__init__.py`: made its three public package exports explicit for Ruff without changing exported names.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTLogic.py`: corrected standard-library import ordering only.
- `extensions/slicerSTRT/slicerSTRT/slicerSTRTLib/slicerSTRTWidget.py`: added narrow `typing.cast` calls for the initialized logic object at the two callback use sites; runtime values and behavior are unchanged.
- `docs/development/coding_standards.md`: added only the concise `Local Python Quality Checks` section.
- This task card: activation state and implementation evidence.

Configured Ruff baseline:

- Analysis include: `extensions/slicerSTRT/**/*.py`.
- Selected rules: `E4`, `E7`, `E9`, `F`, `I`, and `B`.
- No `N` naming rules, formatter, automatic fixes, unsafe fixes, build metadata, or runtime dependencies were added.
- Exclusions cover `apps`, `knowledge`, `source`, `workspace`, `config/local.json`, Git metadata, caches, virtual environments, `Build`/`build`, `__pycache__`, and generated directories.
- Ruff `target-version` is omitted. `config/local.json` is absent, so neither the configured Slicer version nor its embedded Python version could be verified without guessing.

Configured Pyright baseline:

- Analysis include: `extensions/slicerSTRT`.
- `typeCheckingMode` is `basic`.
- `extraPaths` contains `extensions/slicerSTRT/slicerSTRT` so `slicerSTRTLib` resolves locally.
- Exclusions cover `apps`, `knowledge`, `source`, `workspace`, `config/local.json`, Git metadata, caches, virtual environments, `Build`/`build`, `__pycache__`, and generated directories.
- No project path is ignored, no machine-specific interpreter path is committed, and no fake API stubs were added.

Suppressions and rationale:

- `reportMissingImports` is downgraded to `warning`, not disabled. Normal system Python does not contain the real Slicer runtime modules, but missing imports, including local-import mistakes, remain visible.
- `reportMissingModuleSource` is set to `none` because Slicer, Qt, CTK, and VTK include compiled or runtime-injected modules whose source is not available to ordinary system Python.
- No inline, per-file, `ignore`, attribute-access, undefined-symbol, syntax, or general type-diagnostic suppressions were added.

Commands and results:

- Initial `Get-Command ruff` and `Get-Command pyright` checks reported that neither command was available on `PATH`.
- Initial `./scripts/development/run-python-quality.ps1` runs from the repository root and another working directory printed clear errors for both missing commands, stated that no tools were installed or updated, and returned exit code `1`.
- In-memory mock commands, used only to validate script control flow, confirmed that the script resolves `C:\stratum` from its own location, invokes `ruff check extensions/slicerSTRT/slicerSTRT`, invokes `pyright --project pyrightconfig.json`, attempts Pyright after a mocked Ruff failure, returns `1` on a mocked check failure, and returns `0` when both mocks succeed. These mocks are not evidence that Ruff or Pyright passed.
- PowerShell's parser reported zero syntax errors for `scripts/development/run-python-quality.ps1`.
- `ConvertFrom-Json` parsed `pyrightconfig.json` successfully and confirmed `basic`, `warning`, and `none` for the configured checking and diagnostic levels.
- System Python is 3.10.11. It parsed all five project-owned Python files with `ast.parse` successfully without importing Slicer or generating cache files.
- At the user's explicit follow-up request, system Python 3.10.11 created the ignored project environment at `C:\stratum\.venv` with `python -m venv .venv` so it persists across branch switches in this working tree.
- After activating `.venv`, its pip was upgraded to 26.1.2, then `python -m pip install ruff pyright` installed Ruff 0.15.21, Pyright 1.1.411, and their declared transitive packages. No Slicer runtime dependency or tracked dependency manifest was added.
- Activation verification confirmed `VIRTUAL_ENV`, Python, Ruff, and Pyright all resolve inside `C:\stratum\.venv`.
- Pyright initialized its bundled Node runtime inside `.venv` on first use.
- After the root environment passed validation, the exact previous `%LOCALAPPDATA%\STRATUM\venvs\BSSL-003` directory was path-checked and recursively removed. The parent environment area and all other local paths were left untouched.
- Real initial analysis reported nine Ruff errors: two `I001` import-order findings and seven `F401` unused/import-export findings. Real initial Pyright analysis reported two `reportOptionalMemberAccess` errors and twelve expected `reportMissingImports` warnings.
- After approved mechanical corrections, an intermediate run reported one remaining Ruff `I001`, zero Pyright errors, and eleven expected runtime-import warnings.
- Final `./scripts/development/run-python-quality.ps1` runs with the root `.venv` active, from the repository root and from `%TEMP%`, both returned exit code `0`.
- Targeted `rg` search found no remaining `learning sandbox`, `disposable training`, or `training code` wording under the active module Python path.
- Git status and diff inspection found changes only in the approved allowlist. No CMake, `.ui`, dependency, protected-directory, workspace, generated, build-output, or private-configuration file changed.

Ruff result:

- Ruff 0.15.21 loaded `pyproject.toml` successfully.
- Final result: `All checks passed!`, exit code `0`.
- Analysis remained scoped to `extensions/slicerSTRT/slicerSTRT` with rules `E4`, `E7`, `E9`, `F`, `I`, and `B`.

Pyright result:

- Pyright 1.1.411 loaded `pyrightconfig.json` successfully.
- Final result: zero errors, eleven warnings, zero information diagnostics, exit code `0`.
- All eleven remaining warnings are `reportMissingImports` for external Slicer runtime imports from `slicer`, `slicer.i18n`, `slicer.ScriptedLoadableModule`, and `vtk`. They remain visible at warning level by design and do not hide local project diagnostics.

Behavior-preserving Python corrections:

- `slicerSTRT.py`: removed the unused `import slicer` reported by Ruff `F401`; no reference used it.
- `slicerSTRT.py`: ordered its import block as reported by Ruff `I001`.
- `slicerSTRT.py`: changed the `slicerSTRTLogic`, `slicerSTRTTest`, and `slicerSTRTWidget` imports to explicit same-name re-exports, preserving the public names required by Slicer while resolving Ruff `F401` and the final `I001` layout finding.
- `slicerSTRTLib/__init__.py`: changed each of the same three package imports to explicit same-name re-exports, preserving the public package API while resolving three Ruff `F401` findings.
- `slicerSTRTLogic.py`: moved `import importlib` before `import os`, resolving Ruff `I001` without runtime effect.
- `slicerSTRTWidget.py`: imported `typing.cast` and cast `self.logic` to `slicerSTRTLogic` locally before each of the two callback calls, resolving two Pyright `reportOptionalMemberAccess` errors. `cast` returns the original object unchanged at runtime.
- The `slicerSTRT.py` help and acknowledgement edit is the separately required metadata identity update, not a quality-tool correction. No application logic changed.

Remaining diagnostics and verification:

- Pyright intentionally retains eleven external Slicer/VTK `reportMissingImports` warnings. Removing or globally hiding them is not required and would weaken the documented baseline.
- Manual Slicer verification is pending because `config/local.json` is absent and no configured executable or runtime version is available.
- Required manual results for module load, title/category, help/acknowledgement, Check Environment, Inspect Volume, Reload, Reload and Test, and new Python errors must be recorded before review.

## Review findings

Pending independent AI review after implementation and manual verification.

## Human approval

Specification approved and task activation authorized by the user on 2026-07-13. Implementation review and final human approval remain pending.
