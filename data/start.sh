#!/usr/bin/env bash
set -euo pipefail

LOCK_DIR="/shared-locks"
LOCK_FILE="$LOCK_DIR/data.lock"

mkdir -p "$LOCK_DIR"
exec 9>"$LOCK_FILE"
flock -n 9

uv run app.py
