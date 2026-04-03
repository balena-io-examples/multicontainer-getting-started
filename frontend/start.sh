#!/usr/bin/env bash
set -euo pipefail

LOCK_DIR="/shared-locks"
DATA_LOCK="$LOCK_DIR/data.lock"
FRONTEND_LOCK="$LOCK_DIR/frontend.lock"

mkdir -p "$LOCK_DIR"

wait_for_running_lock() {
  local lock_file="$1"
  until [[ -f "$lock_file" ]] && ! flock -n "$lock_file" -c true; do
    echo "Waiting for dependency lock: $lock_file"
    sleep 1
  done
}

wait_for_running_lock "$DATA_LOCK"

exec 9>"$FRONTEND_LOCK"
flock -n 9

python -m streamlit run app.py --server.port 80 --server.address 0.0.0.0
