#!/bin/bash

# Acknowledgement
echo "Activating virtual environment..."

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Activating Virtual Environment
if [ -s "$VENV_PATH/bin/activate" ]; then

	source $VENV_PATH/bin/activate

elif [ -s "$VENV_PATH/Scripts/activate" ]; then

	source $VENV_PATH/Scripts/activate

else

	echo "Unexpected venv directory structure - could not find activation command to automatically activate venv"
	echo ""
	echo "See this venv documentation for more details and possible manual activation paths: https://docs.python.org/3/library/venv.html#how-venvs-work"
    #exit 1
fi

# Completion
echo "Completed activating virtual environment!"
echo ""