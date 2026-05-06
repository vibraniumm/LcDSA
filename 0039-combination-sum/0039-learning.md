# Problem: Combination Sum

## Problem Overview
Tumhe ek array candidates aur ek target diya gaya hai.

Tumhe aise unique combinations find karne hain jinka sum target ke equal ho.

Important:
- Same number multiple times use kar sakte ho
- Duplicate combinations allowed nahi hain

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"All possible combinations try karne hain → Backtracking"

---

## Key Observations
- Unlimited reuse allowed hai
- Combination order important nahi hai
- Sum track karna hoga
- Wrong path ko jaldi stop kar sakte hain

---

## Approach (Step-by-step soch)
1. Recursive backtracking function banao:
   - current combination
   - current sum
   - start index

2. Base cases:
   - Agar target == 0:
     → valid combination mila
   - Agar target < 0:
     → invalid path → stop

3. Loop chalao candidates par:
   - Current number add karo
   - Recursive call karo
   - Backtrack karo (remove last element)

4. Same index pass karo:
   → kyunki same element reuse allowed hai

---

## Example (Important for memory)

Input:
candidates = [2,3,6,7]  
target = 7

Step-by-step:

2 → 2 → 2 → target = 1 (fail)

2 → 2 → 3 → target = 0  
Valid:
[2,2,3]

7 → target = 0  
Valid:
[7]

Final:
[[2,2,3],[7]]

---

## Easy Memory Trick

"Choose → Explore → Backtrack"

---

## Pattern Recognition
- Backtracking
- Combination generation
- DFS recursion

---

## Pattern Used
Backtracking (Combination Building)

---

## Why This Works
- Har possible combination explore karte hain
- Invalid paths early stop ho jate hain
- Backtracking state ko restore karta hai
- All unique valid combinations mil jate hain

---

## When To Use This Pattern Again
- Jab all combinations generate karni ho
- Jab repeated choices allowed ho
- Jab target sum type problem ho
- Keywords: "combination", "target sum", "all possible"

---

## Common Mistakes
- Backtrack karna bhool jana
- Wrong index pass karna
- Duplicate combinations generate karna
- Base case galat likhna

---

## Complexity Analysis
- Time Complexity: Exponential (depends on combinations)
- Space Complexity: O(target) recursion stack

---

## Interview Tip
- Start me bolo: "We use backtracking to generate all valid combinations"
- Explain karo same index kyun pass karte hain
- Base cases clearly batao
- Ek recursion tree example dikhao

Simple rule:
"Choose → Recurse → Backtrack"

