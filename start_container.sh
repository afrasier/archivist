#!/bin/bash
source set_docker_id.sh

echo "Calling docker compose..."
docker-compose up -d --build
