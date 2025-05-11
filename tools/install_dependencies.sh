#!/bin/bash

# Acknowledgement
echo "Installing Python dependencies..."

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Python Dependencies Installation
if ! command -v pip &>/dev/null; then

	echo_err "pip command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "Check your Python installation to see that pip is installed appropriately."
	set_exit_mode && $EXIT 1
fi

pip install -r $REPO_ROOT/requirements*.txt

# Completion
echo "Completed installation of Python dependencies!"
echo ""