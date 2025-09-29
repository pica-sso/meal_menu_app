#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $SCRIPT_DIR/server
echo "pwd: $(pwd)"
source ../.venv/bin/activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000
UVICORN_PID=$!
echo "uvicorn PID: $UVICORN_PID"

wait $UVICORN_PID