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

echo "Creating virtual environment in: $VENV_PATH"
python -m venv $VENV_PATH --prompt $VENV_NAME --clear

[ $? -ne 0 ] && echo "ERROR: Unable to create Python virtual env at: $VENV_PATH" && exit 1

# Completion
echo "Completed virtual environment creation!"
echo ""