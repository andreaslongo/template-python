#!/usr/bin/env bash

# Starts a new container based on the PROD image.
#
# Programs run as non-root-user inside the container for security reasons.
#
# The container uses a named volume for persisting AI models to speed up the
# startup process. Multiple containers can access the cache volumes
# simultaneously (`:z` lowercase).
#
# The named volume is not required. Without the volume, the container will
# download the required AI models during startup.

readonly local script_dir=$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" && pwd )
readonly local parent_dir=$(dirname ${script_dir})

# Container user: uid=1000(appuser) gid=1000(appuser) groups=1000(appuser)
readonly local uid=1000
readonly local gid=1000

# Use --publish <host_port>:<container_port> to enable networking.
# Use --rm to remove the container after exit.
# Use --env-file "${parent_dir}/.env" to read environment variables from a file.
podman container run \
    --detach \
    --env GRADIO_SERVER_NAME="0.0.0.0" \
    --name="$(basename ${parent_dir})_prod" \
    --publish 8000:7860 \
    --pull=newer \
    --rm \
    --user ${uid}:${gid} \
    --userns keep-id:uid=${uid},gid=${gid} \
    --volume "${HOME}/.cache/huggingface:/home/appuser/.cache/huggingface:z,rw" \
        localhost/"$(basename ${parent_dir})_prod":latest
