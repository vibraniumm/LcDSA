# Problem: Rotate Image

## Problem Overview
Tumhe ek n x n matrix diya gaya hai.

Tumhe matrix ko 90 degree clockwise rotate karna hai.

Important:
- In-place karna hai
- Extra matrix use nahi kar sakte

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Transpose + reverse"

---

## Key Observations
- 90° clockwise rotation ko 2 steps me tod sakte hain:
  1. Matrix transpose karo
  2. Har row reverse karo

- Transpose:
  → rows aur columns swap hote hain

- Reverse:
  → final clockwise rotation milta hai

---

## Approach (Step-by-step soch)
1. Matrix transpose karo:
   - matrix[i][j] ↔ matrix[j][i]

2. Har row reverse karo

3. Matrix automatically 90° clockwise rotate ho jayegi

---


