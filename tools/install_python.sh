#!/bin/bash

# Acknowledgement
echo "Installing Python $PYTHON_VERSION (if necessary)..."

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Python Version Installation
if ! command -v pyenv &>/dev/null; then

	echo "pyenv command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "See here for more details on installing pyenv: https://github.com/pyenv/pyenv"
	echo "For Windows users, see the logically similar pyenv-win here: https://github.com/pyenv-win/pyenv-win"
	exit 1
fi

if [ ! -s "$REPO_ROOT/.python-version" ]; then

	echo "Creating .python-version file using Python version: $PYTHON_VERSION"

    PREVIOUS_DIR=$(pwd)
	cd $REPO_ROOT
	pyenv local $PYTHON_VERSION
	cd $PREVIOUS_DIR
    unset $PREVIOUS_DIR
fi

INSTALLED_VERSION=$(pyenv versions | grep "$PYTHON_VERSION")
case "$INSTALLED_VERSION" in

	*$PYTHON_VERSION*)
		echo "Desired Python version already installed: $PYTHON_VERSION"
		;;

	*)
		echo "Desired Python version is not installed: $PYTHON_VERSION"
		echo "Installing desired Python version: $PYTHON_VERSION"

		pyenv install $PYTHON_VERSION
		PYENV_INSTALL_STATUS=$?

		if [ $PYENV_INSTALL_STATUS -ne 0 ]; then
			echo "ERROR: Unable to install desired Python version: $PYTHON_VERSION"
			exit 1
		fi
  		;;
esac

# Confirm Python Installation
if ! command -v python &>/dev/null; then

	echo "python command is not executable or is not discoverable in PATH and is required"
	exit 1

elif [ "$(python --version | awk '{print $2}')" != "$PYTHON_VERSION" ]; then
	
	echo "python command version $(python --version) does not match desired version: $PYTHON_VERSION"
	echo ""
	echo "There may be a problem with which Python version is being detected"
	echo "Try `which python` in this repository to determine if the python command being used is not using the correct path"
	exit 1
fi

# Completion
echo "Completed installation of Python!"
echo ""