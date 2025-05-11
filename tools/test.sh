#!/bin/bash

# Acknowledgement
echo "Linting code in local development environment..."
echo ""

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Check Environment
if ! command -v pytest &>/dev/null; then

	echo_err "pytest command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "Local development environment should be installed and boostrapped to execute testing."
	exit 1
fi

# Move to Root Directory
PREVIOUS_DIR=$(pwd)
cd $REPO_ROOT

# Test Code
ERRORS_FOUND="false"

echo "Executing pytest..."
pytest -v
if [ "$?" != "0" ]; then
	echo_err "Errors found when executing pytest!"
	ERRORS_FOUND="true"
else
	echo "No errors found from pytest."
fi
echo ""

# Move Back to Previous Directory
cd $PREVIOUS_DIR
unset $PREVIOUS_DIR

# Report Completion
if [ $ERRORS_FOUND = "true" ]; then
	echo_err "Errors found when testing code in local development environment!"
	echo_err ""
	exit 1
fi

echo "No errors found when testing code in local development environment."
echo ""