#!/bin/sh
# Example of a project-specific check (guard B). To use it, copy this file to
# .githooks/project-checks.sh, make it executable (chmod +x) and edit the paths.
# The pre-commit hook passes the staged file names on stdin, one per line.
# Exit 0 = fine. Exit 1 = stop the commit (print what to do instead).
#
# This example: a change to the database schema must come with a changelog line.

SCHEMA_PATTERN='^db/migrations/|^db/field_list\.json$'   # edit for your project
CHANGELOG='docs/reference/live-data-changelog.md'         # edit for your project

files=$(cat)
if printf '%s\n' "$files" | grep -q -E "$SCHEMA_PATTERN"; then
  if ! printf '%s\n' "$files" | grep -q -x "$CHANGELOG"; then
    echo "BLOCKED (guard B): the schema changed but $CHANGELOG is not part of this commit."
    echo "  Add one line to $CHANGELOG describing the change, then stage it."
    exit 1
  fi
fi
exit 0
