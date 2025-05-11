#!/bin/bash

# Setup Flags
[ ! -z $DEBUG ] && set -x

# Functions
get_repo_root()
{
    # Store the current working directory since we change directories to find the repo root
    local PREVIOUS_DIR=$(pwd)

    # Get directory where this setup file is stored, then move to the parent folder
    # We expect the parent folder to be repo root
    cd $(dirname "${BASH_SOURCE[0]}")/..
    local REPO_ROOT=$(pwd)

    # Restore our previous folder location before changing directories
    cd $PREVIOUS_DIR
    echo "$REPO_ROOT"
}

echo_err()
{
    echo "$@" 1>&2;
}

# Environment Variables
PYTHON_VERSION=3.12.1
REPO_ROOT=$(get_repo_root)
VENV_NAME=venv.algorithms
VENV_PATH=$REPO_ROOT/.venv
TOOLS_PATH=$REPO_ROOT/Tools
