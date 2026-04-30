# Problem: Valid Sudoku

## Problem Overview
Tumhe ek 9x9 Sudoku board diya gaya hai.

Tumhe check karna hai ki board valid hai ya nahi according to rules:
- Har row me duplicate nahi hona chahiye
- Har column me duplicate nahi hona chahiye
- Har 3x3 box me duplicate nahi hona chahiye

Note:
- Board fully filled hona zaroori nahi hai
- Sirf filled cells (digits) check karne hain

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe duplicates track karne hain (row, column, box wise)"

---

## Key Observations
- Board fixed size (9x9) hai
- '.' ko ignore karna hai
- Har number unique hona chahiye:
  - row me
  - column me
  - 3x3 box me
- Fast lookup ke liye set use karna best hai

---


