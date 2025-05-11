#!/bin/bash

# Acknowledgement
echo "Linting code in local development environment..."
echo ""

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Check Environment
if ! command -v black &>/dev/null; then

	echo_err "black command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "Local development environment should be installed and boostrapped to execute linting."
	set_exit_mode && $EXIT 1
fi

if ! command -v isort &>/dev/null; then

	echo_err "isort command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "Local development environment should be installed and boostrapped to execute linting."
	set_exit_mode && $EXIT 1
fi

if ! command -v mypy &>/dev/null; then

	echo_err "mypy command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "Local development environment should be installed and boostrapped to execute linting."
	set_exit_mode && $EXIT 1
fi

if ! command -v pylint &>/dev/null; then

	echo_err "pylint command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "Local development environment should be installed and boostrapped to execute linting."
	set_exit_mode && $EXIT 1
fi

# Move to Root Directory
PREVIOUS_DIR=$(pwd)
cd $REPO_ROOT

# Lint Code
ERRORS_FOUND="false"

echo "Executing black..."
black --check --diff $REPO_ROOT
if [ "$?" != "0" ]; then
	echo_err "Errors found when executing black!" 
	echo_err "Try running 'black .' in repository root to fix formatting issues."
	ERRORS_FOUND="true"
else
	echo "No errors found from black."
fi
echo ""

echo "Executing isort..."
isort --check-only --diff $REPO_ROOT
if [ "$?" != "0" ]; then
	echo_err "Errors found when executing isort!"
	echo_err "Try running 'isort .' in repository root to fix formatting issues."
	ERRORS_FOUND="true"
else
	echo "No errors found from isort."
fi
echo ""

echo "Executing mypy..."
mypy --pretty --strict $REPO_ROOT
if [ "$?" != "0" ]; then
	echo_err "Errors found when executing mypy!"
	ERRORS_FOUND="true"
else
	echo "No errors found from mypy."
fi
echo ""

echo "Executing pylint..."
pylint $(git ls-files '*.py')
if [ "$?" != "0" ]; then
	echo_err "Errors found when executing pylint!"
	ERRORS_FOUND="true"
else
	echo "No errors found from pylint."
fi
echo ""

# Move Back to Previous Directory
cd $PREVIOUS_DIR
unset $PREVIOUS_DIR

# Report Completion
if [ $ERRORS_FOUND = "true" ]; then
	echo_err "Errors found when linting code in local development environment!"
	echo_err ""
	set_exit_mode && $EXIT 1
fi

echo "No errors found when linting code in local development environment."
echo ""