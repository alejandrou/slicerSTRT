# Manual Verification Workflow

Manual verification is required when a task affects Slicer behavior or user-visible workflow.

## Slicer Verification

For normal Python scripted-module changes:

1. Open `C:/stratum/apps/SR/Slicer-build/Slicer.exe`.
2. Enable Developer Mode if needed.
3. Open the relevant module.
4. Use Reload or Reload and Test.
5. Verify the task-specific acceptance criteria.
6. Record results in the task card.

## Documentation-Only Verification

For documentation-only changes, manual verification may be limited to checking links, paths, task status, and whether the written procedure is understandable.

MCP evidence may supplement this workflow only when allowed, but it never replaces manual user verification.
