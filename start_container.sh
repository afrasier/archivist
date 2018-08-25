#!/bin/bash

echo "Setting UID and GID environment variables for database file permissions..."
export UID=${UID}
export GID=${GID}

echo "Calling docker compose..."
docker-compose up -d --build
