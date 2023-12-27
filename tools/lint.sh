#!/bin/bash

# Acknowledgement
echo "Linting code in local development environment..."
echo ""

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Check Environment
if ! command -v black &>/dev/null; then

	echo "black command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "Local development environment should be installed and boostrapped to execute linting."
	exit 1
fi

if ! command -v isort &>/dev/null; then

	echo "isort command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "Local development environment should be installed and boostrapped to execute linting."
	exit 1
fi

if ! command -v mypy &>/dev/null; then

	echo "mypy command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "Local development environment should be installed and boostrapped to execute linting."
	exit 1
fi

if ! command -v pylint &>/dev/null; then

	echo "pylint command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "Local development environment should be installed and boostrapped to execute linting."
	exit 1
fi

# Move to Root Directory
PREVIOUS_DIR=$(pwd)
cd $REPO_ROOT

# Lint Code
echo "Executing black..."
black --check --diff $REPO_ROOT
echo "Completed execution of black!"
echo ""
echo "Executing isort..."
isort --check-only --diff $REPO_ROOT
echo "Completed execution of isort!"
echo ""
echo "Executing mypy..."
mypy --pretty --strict $REPO_ROOT
echo "Completed execution of mypy!"
echo ""
echo "Executing pylint..."
pylint $(git ls-files '*.py')
echo "Completed execution of pylint!"
echo ""

# Move Back to Previous Directory
cd $PREVIOUS_DIR
unset $PREVIOUS_DIR

# Completion
echo "Completed linting of code in local development environment!"
echo ""