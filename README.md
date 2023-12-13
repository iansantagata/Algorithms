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
2. Run `source ./tools/bootstrap.sh` from the repository root to install everything you need and start up a virtual environment
3. Run any algorithm, test, or analysis you like on the code!

## Uninstallation

If you want to remove everything related to this repository from your computer, you can simply `rm -rf REPOSITORY/ROOT/PATH` wherever the repository is stored locally at `REPOSITORY/ROOT/PATH`.  All files and actions are self-contained to the repository, so removing the repository from your computer removes all files, configuration, and anything installed.

If you want to simply remove only the development environment that you spun up from the *Quick Start* guide, run `source ./tools/teardown.sh` from the repository root!  This deactivates, removes, and uninstalls all components installed for this repository, including virtual environments, Python installations, and the repository's package dependencies.