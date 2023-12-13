#!/bin/bash

# Acknowledgement
echo "Bootstrapping local development environment..."
echo ""

# Script Dependencies
source $(dirname "${BASH_SOURCE[0]}")/script_setup.sh

# Python Version Installation
source $TOOLS_PATH/install_python.sh

# Create Virtual Environment
source $TOOLS_PATH/create_venv.sh

# Activate Virtual Environment
source $TOOLS_PATH/activate_venv.sh

# Install Dependencies
source $TOOLS_PATH/install_dependencies.sh

# Completion
echo "Completed setup and activation of local development environment!"
echo ""