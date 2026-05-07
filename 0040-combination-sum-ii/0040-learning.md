# Problem: Combination Sum II

## Problem Overview
Tumhe ek array candidates aur ek target diya gaya hai.

Tumhe aise unique combinations find karne hain jinka sum target ke equal ho.

Important:
- Har element sirf ek baar use ho sakta hai
- Duplicate combinations allowed nahi hain

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Combination Sum + duplicates handle karne hain"

---

## Key Observations
- Same element reuse allowed nahi hai
- Duplicate numbers array me ho sakte hain
- Duplicate combinations avoid karne hain
- Sorting helpful rahegi

---

## Approach (Step-by-step soch)
1. Array sort karo
   → duplicates adjacent aa jayenge

2. Backtracking function banao:
   - current combination
   - remaining target
   - start index

3. Base cases:
   - target == 0:
     → valid combination mila
   - target < 0:
     → stop

4. Loop chalao from start index:
   - Duplicate skip karo:
     → if i > start and candidates[i] == candidates[i-1]
   - Current element add karo
   - Recursive call:
     → i + 1 pass karo (reuse allowed nahi)
   - Backtrack karo

---



