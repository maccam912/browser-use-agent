#!/bin/bash
# Start Xvfb on display :99 (matching the ENV DISPLAY in Dockerfile)
Xvfb :99 -screen 0 1280x1024x24 &
# Wait a moment for Xvfb to initialize
sleep 1
# Execute the main application
exec /root/.local/bin/uv run main.py "$@"