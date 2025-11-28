# TM Project (k-Tape Turing Machine Simulator)

**Name:** Abdullah Altamir
**NetID:** 24418268
**Time Spent:** ~10 hours

## Project Overview
This project implements a k-tape Turing Machine (TM) simulator in Python.
The simulator:
* Reads a TM description file and a tape input file.
* Supports arbitrary number of tapes (`k`), maximum tape length, and maximum steps.
* Outputs CSV-compatible traces for each step.
* Supports wildcard `*` in reading/writing and head movement (`L`, `R`, `S`).

## Language and Libraries

* **Language:** Python 3
* **Libraries Used:** `sys`, `csv`

## Code Formatting
* **tm_netid.py:** Main simulator program.
* **Machines/**: Folder containing TM description files (MachineA.txt, MachineB.txt).
* **TestInputs/**: Input tape files for each machine.
* **Results/**: Stores results after files were executed.

## Testing
* Ran instructor-provided machines (MachineA and MachineB) with multiple input tapes.
* Verified correctness based on expected accept/reject outcomes.
* Tested edge cases: empty input, only blanks, maximum-length strings.