#!/bin/bash

echo "Setting UID and GID environment variables for database file permissions..."
export docker_uid=${UID}
export docker_gid=${GID}
