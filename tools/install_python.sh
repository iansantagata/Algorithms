#!/bin/bash

# Acknowledgement
echo "Installing Python (if necessary)..."

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Python Version Installation
if ! command -v pyenv &>/dev/null; then

	echo_err "pyenv command is not installed or is not discoverable in PATH and is required"
	echo_err ""
	echo_err "See here for more details on installing pyenv: https://github.com/pyenv/pyenv"
	echo_err "For Windows users, see the logically similar pyenv-win here: https://github.com/pyenv-win/pyenv-win"
	set_exit_mode && $EXIT 1
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
			echo_err "ERROR: Unable to install desired Python version: $PYTHON_VERSION"
			set_exit_mode && $EXIT 1
		fi
  		;;
esac

if [ ! -s "$REPO_ROOT/.python-version" ]; then

	echo "Creating .python-version file using Python version: $PYTHON_VERSION"

    PREVIOUS_DIR=$(pwd)
	cd $REPO_ROOT
	pyenv local $PYTHON_VERSION
	cd $PREVIOUS_DIR
    unset $PREVIOUS_DIR
fi

# Confirm Python Installation
if ! command -v python &>/dev/null; then

	echo_err "python command is not executable or is not discoverable in PATH and is required"
	set_exit_mode && $EXIT 1

elif [ "$(python --version | awk '{print $2}')" != "$PYTHON_VERSION" ]; then
	
	echo_err "python command version $(python --version) does not match desired version: $PYTHON_VERSION"
	echo_err ""
	echo_err "There may be a problem with which Python version is being detected"
	echo_err "Try `which python` in this repository to determine if the python command being used is not using the correct path"
	set_exit_mode && $EXIT 1
fi

# Completion
echo "Completed installation of Python!"
echo ""