#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd $SCRIPT_DIR/frontend

if [ ! -d node_modules ]; then
    echo "Installing dependencies..."
    npm install
fi

echo "Starting frontend..."
npm run start
