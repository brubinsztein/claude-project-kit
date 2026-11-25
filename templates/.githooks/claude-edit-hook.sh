#!/bin/sh
# Kit guard: Claude Code PostToolUse hook for Edit, Write and MultiEdit.
# After Claude changes a file it runs the guard on the lines changed in that
# file. If something is wrong, exit code 2 sends the message back to Claude so it
# fixes the problem while still editing. The git pre-commit hook is the backstop.

input=$(cat)
file=$(printf '%s' "$input" | python3 -c 'import sys, json
try:
    data = json.load(sys.stdin)
    print((data.get("tool_input") or {}).get("file_path", ""))
except Exception:
    print("")' 2>/dev/null)
[ -n "$file" ] || exit 0

ROOT=$(git -C "$(dirname "$file")" rev-parse --show-toplevel 2>/dev/null) || exit 0
[ -f "$ROOT/.githooks/guard.py" ] || exit 0
cd "$ROOT" || exit 0
[ -f .githooks/config.sh ] && . .githooks/config.sh

msg=$(python3 .githooks/guard.py file "$file" 2>&1)
status=$?
if [ "$status" -ne 0 ]; then
  printf '%s\n' "$msg" >&2
  exit 2
fi
exit 0
