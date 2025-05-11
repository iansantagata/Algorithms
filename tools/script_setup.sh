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

is_sourced() {
    if [ -n "$ZSH_VERSION" ]; then 
        case $ZSH_EVAL_CONTEXT in *:file:*) return 0;; esac  # sourced
    else  # Add additional POSIX-compatible shell names here, if needed
        case ${0##*/} in bash|-bash|sh|-sh) return 0;; esac  # sourced
    fi
    return 1  # NOT sourced
}

echo_err()
{
    echo "$@" 1>&2;
}

set_exit_mode()
{
    if is_sourced; then
        EXIT=return
    else
        EXIT=exit
    fi
}

# Environment Variables
PYTHON_VERSION=3.12.1
REPO_ROOT=$(get_repo_root)
VENV_NAME=venv.algorithms
VENV_PATH=$REPO_ROOT/.venv
TOOLS_PATH=$REPO_ROOT/Tools
