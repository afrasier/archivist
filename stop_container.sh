#!/bin/bash

source set_docker_id.sh

echo "Tearing down containers..."
docker-compose down
