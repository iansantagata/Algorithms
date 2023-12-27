#!/bin/bash

# Acknowledgement
echo "Linting code in local development environment..."
echo ""

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Check Environment
if ! command -v pytest &>/dev/null; then

	echo "pytest command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "Local development environment should be installed and boostrapped to execute testing."
	exit 1
fi

# Move to Root Directory
PREVIOUS_DIR=$(pwd)
cd $REPO_ROOT

# Test Code
echo "Executing pytest..."
pytest
echo "Completed execution of pytest!"
echo ""

# Move Back to Previous Directory
cd $PREVIOUS_DIR
unset $PREVIOUS_DIR

# Completion
echo "Completed linting of code in local development environment!"
echo ""