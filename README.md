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
