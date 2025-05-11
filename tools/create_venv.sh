#!/bin/bash

# Acknowledgement
echo "Creating virtual environment..."

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Create Virtual Environment
if [ -d "$VENV_PATH" ]; then
	echo "Detected existing virtual environment in: $VENV_PATH"
	echo "Note - this existing virtual environment will be cleared and re-created"
fi

if ! command -v python &>/dev/null; then

	echo_err "python command is not executable or is not discoverable in PATH and is required"
	exit 1
fi

echo "Creating virtual environment in: $VENV_PATH"
python -m venv $VENV_PATH --prompt $VENV_NAME --clear --upgrade-deps
VENV_CREATION_STATUS=$?

if [ $VENV_CREATION_STATUS -ne 0 ]; then
	echo_err "ERROR: Unable to create Python virtual env at: $VENV_PATH"
	exit 1
fi

# Completion
echo "Completed virtual environment creation!"
echo ""