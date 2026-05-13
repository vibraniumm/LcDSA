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


## Example (Important for memory)

Input:

1 2 3
4 5 6
7 8 9

Step 1: Transpose

1 4 7
2 5 8
3 6 9

Step 2: Reverse rows

7 4 1
8 5 2
9 6 3

Final:
[[7,4,1],[8,5,2],[9,6,3]]

---

## Easy Memory Trick

"Transpose karo, phir reverse"

---

## Pattern Recognition
- Matrix manipulation
- In-place transformation
- Symmetry operations

---

## Pattern Used
Matrix Transpose + Reverse

---

## Why This Works
- Transpose diagonal reflection karta hai
- Row reverse clockwise orientation deta hai
- Combined operation exact 90° rotation deta hai
- Extra space ki zarurat nahi hoti

---

## When To Use This Pattern Again
- Jab matrix rotation ho
- Jab in-place transformation ho
- Jab 2D matrix manipulation ho
- Keywords: "rotate matrix", "transpose", "in-place"

---



