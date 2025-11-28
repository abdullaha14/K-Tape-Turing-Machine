# MachineB

## 1. Problem Tackled

MachineB is a **two-tape Turing Machine** that copies an input string from tape 1 to tape 2 and verifies a condition for acceptance.

* **Type:** Computation problem (produces an output on the second tape while also deciding acceptance).
* **Function:** It reads input from tape 1, duplicates it onto tape 2, and accepts if the copied string matches certain criteria (e.g., exactly duplicates the input).

## 2. Reference

The problem is self-designed to illustrate multi-tape Turing Machine operations.

## 3. How the Machine Works

1. **Start state (`q0`)**: Reads symbols from tape 1 and writes them to tape 2 while moving both heads to the right.
2. **Copying state (`q_copy`)**: Continues copying until the blank symbol `_` is encountered on tape 1.
3. **Check state (`q_check`)**: Verifies if the string on tape 2 matches the input condition.
4. **Acceptance/Rejection**:

   * If the check passes, move to `q_accept`.
   * If the check fails, move to `q_reject`.

### Tape Example

| Tape 1 Input | Tape 2 Output | Result   |
| ------------ | ------------- | -------- |
| 01           | 01            | Accepted |
| 1100         | 1100          | Accepted |
| 10           | 11            | Rejected |

## 4. State Diagram

```
      ┌─────┐
      │ q0  │
      └─┬─┬─┘
        │ │
      Read symbol
        │
      ┌─▼─┐
      │q_copy│
      └─┬─┘
        │
      ┌─▼─┐
      │q_check│
    ┌───┴───┐
  Accept   Reject
```
## 5. Verification of Correct Operation

* Ran multiple test inputs on tape 1, ranging from single digits to multi-digit binary strings.
* Verified that tape 2 correctly mirrored tape 1 after computation.
* Checked that machine halted in `q_accept` for valid cases and `q_reject` for invalid cases.
* Cross-checked execution trace against expected step-by-step transitions.
* All were done to ensure correctness of MachineB.

