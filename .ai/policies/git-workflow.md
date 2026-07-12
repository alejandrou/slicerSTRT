# Git Workflow Policy

Git actions require explicit user approval.

## Restricted Actions

Do not perform these actions unless the user explicitly requests them:

- `git commit`
- `git push`
- `git pull`
- creating, switching, deleting, or renaming branches
- merge
- rebase
- reset
- force operations
- deleting tracked files

Task cards may name a target branch, but Codex must not create that branch unless explicitly instructed.

## Local Changes

Assume existing local changes may belong to the user. Do not revert, overwrite, or clean them unless explicitly requested.
