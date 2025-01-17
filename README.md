# Misoperate

> An x86-64 assembly correction puzzle

## Type

- [X] **OFF**line
- [ ] **ON**line

## Designer

- William Charron-Boyle

## Description

A Linux ABI-conforming executable seemingly printing the ASCII representation of a sequence of products. However, the executable uses eight-bit multiplication instead of its thirty-two-bit equivalent. The former operation causes integer overflows for the factors that the exectuble multiplies. Participants must increase the operand size of this operation to at least thirty-two-bits. This modification will cause the executable print out the flag when ran.

**IMPORTANT:** This description will **NOT** be shared with participants.

## Category

- `re`

---

# Project Structure

## 1. HACKME.md

- **[HACKME.md](HACKME.md)**: A teaser or description of the challenge to be shared with participants (in CTFd).

## 2. Source Code

- **[source/README.md](source/README.md)**: Sufficient instructions for building your offline artifacts from source
  code. If your project includes multiple subprojects, please consult us (Anis and Hugo).
- **[source/*](source/)**: Your source code.

## 3. Offline Artifacts

- **[offline-artifacts/*](offline-artifacts/)**: All files (properly named) intended for local download by
  participants (e.g., a binary executable for reverse engineering, a custom-encoded image, etc.). For large files (
  exceeding 100 MB), please consult us (Anis and Hugo).

## 4. Solution

- **[solution/README.md](solution/README.md)**: A detailed writeup of the working solution.
- **[solution/FLAGS.md](solution/FLAGS.md)**: A single markdown file listing all (up-to-date) flags.
- **[solution/*](solution/)**: Any additional files or code necessary for constructing a reproducible solution for the
  challenge (e.g., `PoC.py`, `requirement.txt`, etc.). 
