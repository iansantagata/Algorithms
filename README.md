<!-- General Badges -->
[![License](https://img.shields.io/github/license/iansantagata/algorithms?label=License&color=yellow)](LICENSE)
<!-- Developmental Badges -->
[![Lint](https://github.com/iansantagata/algorithms/actions/workflows/lint.yml/badge.svg)](https://github.com/iansantagata/algorithms/actions/workflows/lint.yml)
[![Tests](https://github.com/iansantagata/algorithms/actions/workflows/test.yml/badge.svg)](https://github.com/iansantagata/algorithms/actions/workflows/test.yml)
[![Code QL](https://github.com/iansantagata/algorithms/actions/workflows/codeql.yml/badge.svg)](https://github.com/iansantagata/algorithms/actions/workflows/codeql.yml)

# Algorithms

The purpose of this repository is to store various implementations of different types of algorithms, of varying goals and complexity.

Each implemented algorithm should be:
- Clear and concise
- Independently executable
- Rigorously tested
- Well documented
- Categorized with similar algorithms

In short, each algorithm should be implemented in a straight-forward enough way that a novice programmer could understand, replicate, and execute each algorithm as needed.

## Quick Start

To get started with running, analyzing, developing, and/or testing the code in this repository:

1. Run `git clone` on this repository to get the code locally
2. Run `source ./tools/bootstrap.sh` in your shell at the repository root
3. Run any algorithm, test, or analysis you like using the code!

The [bootstrap script](tools/bootstrap.sh) is a setup script that installs and activates a virtual environment.  The bootstrap script is comprised of several sub-scripts that can be individually run, if needed.

To exit the virtual environment once finished, run the command `deactivate` in your shell.

## Local Development

To lint the code in your local environment, run `source ./tools/lint.sh` in your shell at repository root.

To test the code in your local environment, run `source ./tools/test.sh` in your shell at repository root.

As a convenience, the [linting script](tools/lint.sh) and [testing script](tools/test.sh) can be executed locally in a virtual environment.  Both scripts require the virtual environment to be installed and bootstrapped.  

These scripts are meant to exactly mirror the automated linting and testing workflows on the `main` branch and used in pull requests.

## Uninstallation

To remove only the virtual environment but keep the code locally, run this command in your shell at repository root:

`source ./tools/teardown.sh`

This [teardown script](tools/teardown.sh) deactivates, removes, and uninstalls all components installed for this repository including virtual environments, Python installations, and the repository's package dependencies.

To delete everything related to this repository from your computer, simply delete your local copy of the repository in your file system.
