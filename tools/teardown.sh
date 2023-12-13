#!/bin/bash

# Acknowledgement
echo "Tearing down local development environment..."
echo ""

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Environment Teardown
if ! command -v pyenv &>/dev/null; then

	echo "pyenv command is not installed or is not discoverable in PATH and is required"
	echo ""
	echo "See here for more details on installing pyenv: https://github.com/pyenv/pyenv"
	echo "For Windows users, see the logically similar pyenv-win here: https://github.com/pyenv-win/pyenv-win"
	exit 1
fi

INSTALLED_VERSION=$(pyenv versions | grep "$PYTHON_VERSION")
case "$INSTALLED_VERSION" in

	*$PYTHON_VERSION*)
		echo "Uninstalling Python version: $PYTHON_VERSION"
        pyenv uninstall -f $PYTHON_VERSION
		;;

	*)
        echo "Python version is not installed: $PYTHON_VERSION"
        echo "Skipping uninstallation of Python version"
  		;;
esac

if [ -s "$REPO_ROOT/.python-version" ]; then

	echo "Removing .python-version file"
    rm -f "$REPO_ROOT/.python-version"
fi

if [ -n "$VIRTUAL_ENV" ]; then

    echo "Deactivating virtual environment: $VIRTUAL_ENV"
    deactivate
fi

if [ -d "$VENV_PATH" ]; then

	echo "Removing virtual environment: $VENV_PATH"
    rm -rf "$VENV_PATH"
fi

# Completion
echo "Completed teardown of local development environment!"
echo ""