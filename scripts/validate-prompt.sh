#!/bin/bash
# Optional shell wrapper around the portable Python validator.

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
  exec python3 "$SCRIPT_DIR/validate_prompt.py" "$@"
elif command -v python >/dev/null 2>&1; then
  exec python "$SCRIPT_DIR/validate_prompt.py" "$@"
else
  echo "No Python runtime found; run scripts/validate_prompt.py with a supported Python interpreter." >&2
  exit 1
fi
