<!-- Badges -->
[![License](https://img.shields.io/github/license/iansantagata/algorithms?label=License&color=yellow)](LICENSE)

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
2. Run `source ./tools/bootstrap.sh` in your shell at the repository root to install and activate the virtual environment
3. Run any algorithm, test, or analysis you like using the code!

The [tools/bootstrap.sh](tools/bootstrap.sh) script is comprised of several parts that can be individually run if needed.

To exit the virtual environment once finished, run the command `deactivate` in your shell.

## Uninstallation

To delete everything related to this repository from your computer, run this command in a shell:

`rm -rf REPOSITORY/ROOT/PATH`

where `REPOSITORY/ROOT/PATH` is where you cloned or stored the repository locally.

To remove only the development environment that was created by running `source ./tools/bootstrap.sh`, run this command in your shell at repository root:

`source ./tools/teardown.sh`

This [tools/teardown.sh](tools/teardown.sh) script deactivates, removes, and uninstalls all components installed for this repository, including virtual environments, Python installations, and the repository's package dependencies.