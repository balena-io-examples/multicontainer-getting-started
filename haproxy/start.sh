#!/usr/bin/env bash
set -euo pipefail

LOCK_DIR="/shared-locks"
FRONTEND_LOCK="$LOCK_DIR/frontend.lock"
PROXY_LOCK="$LOCK_DIR/proxy.lock"

mkdir -p "$LOCK_DIR"

wait_for_running_lock() {
  local lock_file="$1"
  until [[ -f "$lock_file" ]] && ! flock -n "$lock_file" -c true; do
    echo "Waiting for dependency lock: $lock_file"
    sleep 1
  done
}

wait_for_running_lock "$FRONTEND_LOCK"

exec 9>"$PROXY_LOCK"
flock -n 9

exec haproxy -f /usr/local/etc/haproxy/haproxy.cfg
