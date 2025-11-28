# MachineA

## 1. Problem Tackled

MachineA is a **single-tape Turing Machine** that decides a simple binary language.

* **Type:** Decider.
* **Function:** It reads a string of 0s and 1s and determines whether the string belongs to the language defined by the transitions.

## 2. Reference

The problem was created an example of a decider TM.

## 3. How the Machine Works

1. **Start state (`q0`)**: Reads symbols from the tape and determines the next state based on input.
2. **Intermediate states (`q1`, `q2`)**: Mark processed symbols (e.g., replace 0 with X, 1 with Y) and navigate through the string according to the language rules.
3. **Acceptance/Rejection**:

   * If the input satisfies the language rules, machine transitions to `q_accept`.
   * If the input violates the rules, machine transitions to `q_reject`.

### Tape Example

| Tape Input | Result   | Steps | Final Tape |
| ---------- | -------- | ----- | ---------- |
| 01         | Accepted | 5     | XY         |
| 10         | Rejected | 0     | 10         |
| 0101       | Accepted | 9     | XYXY       |

## 4. State Diagram

```
      ┌─────┐
      │ q0  │
      └─┬─┬─┘
        │ │
      Read 0/1
        │
      ┌─▼─┐
      │ q1 │
      └─┬─┘
        │
      ┌─▼─┐
      │ q2 │
        │
   ┌────┴────┐
 q_accept   q_reject
```
## 5. Verification of Correct Operation
* Ran multiple binary input strings through the TM.
* Checked that accepted strings reached `q_accept` and rejected strings reached `q_reject`.
* Verified step-by-step execution traces matched expected behavior.
* Confirmed machine halts on all inputs within defined maximum steps.
