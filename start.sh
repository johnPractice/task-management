#! /usr/bin/env bash

SERVER_PORT="${SERVER_PORT:?Variable not set or empty}"
WORKERS=$WORKERS
# start app
echo "Starting FASTAPI SERVER on 0.0.0.0:${SERVER_PORT} ..."
uvicorn app.main:app --host 0.0.0.0 --port "${SERVER_PORT}" --workers ${WORKERS}
