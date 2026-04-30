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


## Approach (Step-by-step soch)
1. 3 sets maintain karo:
   - rows
   - columns
   - boxes

2. Har cell traverse karo:
   - Agar '.' hai → skip

3. Unique key banao:
   - row key → (row, value)
   - col key → (col, value)
   - box key → (row//3, col//3, value)

4. Check karo:
   - Agar kisi set me already present hai → return False

5. Otherwise:
   - sets me add karo

6. End tak koi issue nahi mila → return True

---

## Example (Important for memory)

Input:
Valid board

Check process:
- Har number ko row, column aur box me track kiya
- Koi duplicate nahi mila

Final:
True

Invalid case:
- Same number same 3x3 box me repeat → False

---

## Easy Memory Trick

"3 checks: row, column, box"

---

## Pattern Recognition
- Hashing (set)
- Matrix traversal
- Duplicate detection

---

## Pattern Used
Hash Set (Duplicate Tracking)

---

## Why This Works
- Set me lookup O(1) hota hai
- Har value ko uniquely track kar sakte hain
- Row, column aur box separately validate ho jate hain
- Efficient aur simple approach

---



