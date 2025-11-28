#!/usr/bin/env python3
"""
k-tape Turing Machine simulator (Project 3-style).

Usage:
    python tm_netid.py <machine_file> <tape_file>
"""

import csv
import sys

BLANK = '_'  # underscore stands for blank

class TuringMachine:
    def __init__(self, name, k, max_tape_len, max_steps, sigma, states, start_state, accept_state, reject_state, gammas, transitions):
        self.name = name
        self.k = k
        self.max_tape_len = max_tape_len
        self.max_steps = max_steps
        self.sigma = sigma
        self.states = states
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.gammas = gammas
        self.transitions = transitions

def parse_csv_line(line):
    reader = csv.reader([line.rstrip("\r\n")])
    for row in reader:
        return [field.strip() for field in row]
    return []

def load_machine(filename):
    with open(filename, 'r', newline='') as f:
        raw_lines = [ln for ln in f.readlines() if ln.strip() != '']

    # Header
    header = parse_csv_line(raw_lines[0])
    name, k, max_tape_len, max_steps = header[0], int(header[1]), int(header[2]), int(header[3])

    sigma = set(parse_csv_line(raw_lines[1]))
    states = set(parse_csv_line(raw_lines[2]))
    start_state = parse_csv_line(raw_lines[3])[0]
    accrej = parse_csv_line(raw_lines[4])
    accept_state, reject_state = accrej[0], accrej[1]

    gammas = []
    for i in range(k):
        gamma = set(parse_csv_line(raw_lines[5 + i]))
        gamma.add(BLANK)
        gammas.append(gamma)

    transitions = {}
    rule_num = 0
    for line in raw_lines[5 + k:]:
        fields = parse_csv_line(line)
        if not fields: continue
        expected = 2 + 3*k
        if len(fields) != expected:
            raise ValueError("Incorrect number of fields in transition.")
        init_state = fields[0]
        read_syms = tuple(fields[1:1+k])
        new_state = fields[1+k]
        write_syms = tuple(fields[2+k:2+2*k])
        dirs = tuple(fields[2+2*k:2+3*k])
        rule_num += 1
        print(f"{rule_num}: {line.strip()}")
        trans = {
            "rule_num": rule_num,
            "init_state": init_state,
            "read": read_syms,
            "new_state": new_state,
            "write": write_syms,
            "dirs": dirs
        }
        transitions.setdefault(init_state, []).append(trans)

    return TuringMachine(name, k, max_tape_len, max_steps, sigma, states,
                        start_state, accept_state, reject_state, gammas, transitions)

def pattern_matches(pattern, symbols):
    return all(p=='*' or p==s for p,s in zip(pattern, symbols))

def find_transition(tm, state, symbols):
    rules = tm.transitions.get(state)
    if not rules: return None
    for t in rules:
        if pattern_matches(t["read"], symbols):
            return t
    return None

def init_tapes(tm, init_strings):
    tapes, heads = [], [0]*tm.k
    for i in range(tm.k):
        s = init_strings[i][:tm.max_tape_len]
        tape = list(s) + [BLANK]*(tm.max_tape_len - len(s))
        tapes.append(tape)
    return tapes, heads

def tape_to_str(tape):
    return ''.join(tape).rstrip(BLANK)

def run_problem(tm, init_strings, problem_idx):
    tapes, heads = init_tapes(tm, init_strings)
    state, step, status = tm.start_state, 0, None
    print(f"\nProblem {problem_idx}")
    for i in range(tm.k):
        print(f"Tape {i+1}: {tape_to_str(tapes[i])}")

    while True:
        if state==tm.accept_state: status="Accepted"; break
        if state==tm.reject_state: status="Rejected"; break
        if step>=tm.max_steps: print("Error: exceeded max steps"); status="Error"; break

        current_syms = tuple(tapes[i][heads[i]] for i in range(tm.k))
        for i,sym in enumerate(current_syms):
            if sym not in tm.gammas[i]: print(f"Error: invalid symbol '{sym}' on tape {i+1}"); status="Error"; break
        if status is not None: break

        trans = find_transition(tm, state, current_syms)
        if trans is None: print("Error: no transition defined"); status="Error"; break

        new_syms = [current_syms[i] if trans["write"][i]=='*' else trans["write"][i] for i in range(tm.k)]
        row = [str(step), str(trans["rule_num"])] + [str(h) for h in heads] + [state] + list(current_syms) + [trans["new_state"]] + new_syms + list(trans["dirs"])
        print(','.join(row))

        for i in range(tm.k): tapes[i][heads[i]] = new_syms[i]
        for i in range(tm.k):
            d = trans["dirs"][i]
            heads[i] += -1 if d=='L' else 1 if d=='R' else 0
            if heads[i]<0 or heads[i]>=tm.max_tape_len: print(f"Error: head off tape {i+1}"); status="Error"; break
        if status is not None: break
        state = trans["new_state"]
        step += 1

    print(status)
    print(f"Steps: {step}")
    for i in range(tm.k):
        print(f"Tape {i+1}: {tape_to_str(tapes[i])}")

def load_tape_file(tape_filename, k):
    problems = []
    with open(tape_filename,'r') as f:
        while True:
            block = []
            for _ in range(k):
                line = f.readline()
                if not line: return problems if not block else problems
                block.append(line.rstrip('\n'))
            problems.append(block)
    return problems

def main():
    if len(sys.argv)!=3: print("Usage: python tm_netid.py <machine_file> <tape_file>"); sys.exit(1)
    machine_file, tape_file = sys.argv[1], sys.argv[2]
    tm = load_machine(machine_file)
    print(f"Loaded machine: {tm.name}\nTape file: {tape_file}")
    problems = load_tape_file(tape_file, tm.k)
    for i,p in enumerate(problems, start=1):
        run_problem(tm,p,i)

if __name__=="__main__":
    main()
