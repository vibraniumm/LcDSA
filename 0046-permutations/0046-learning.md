# Problem: Permutations

## Problem Overview
Tumhe ek array nums diya gaya hai jisme distinct integers hain.

Tumhe us array ke saare possible permutations return karne hain.

Permutation:
→ elements ka har possible arrangement

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Har position par har element try karo → Backtracking"

---

## Key Observations
- Har element ek baar use hona chahiye
- Har arrangement unique hoga (distinct numbers)
- Recursively permutations build kar sakte hain
- Backtracking perfect fit hai

---

## Approach (Step-by-step soch)
1. Ek result list banao

2. Recursive backtracking function:
   - current permutation path

3. Base case:
   - Agar path size == nums size
     → valid permutation mila
     → result me add karo

4. Loop chalao nums par:
   - Agar number already path me nahi hai:
     → add karo
     → recurse karo
     → remove karo (backtrack)

---

## Example (Important for memory)

Input:
nums = [1,2,3]

Step-by-step:

Start:
[]

Choose 1:
[1]

Choose 2:
[1,2]

Choose 3:
[1,2,3] → add

Backtrack:
[1,2]

Try other possibilities...

Final:
All permutations generated

---

## Easy Memory Trick

"Choose → Explore → Remove"

---

## Pattern Recognition
- Backtracking
- Recursion
- Permutation generation

---

## Pattern Used
Backtracking (Decision Tree)

---

## Why This Works
- Har step par ek choice lete hain
- Recursive exploration se saari possibilities cover hoti hain
- Backtracking state restore karta hai
- Complete search space explore hota hai

---

## When To Use This Pattern Again
- Jab all arrangements generate karne ho
- Jab ordering matter kare
- Jab recursive choices ho
- Keywords: "permutations", "arrangements", "all possibilities"

---

## Common Mistakes
- Backtrack karna bhool jana
- Duplicate elements reuse karna
- Base case galat likhna
- Path copy na karna before append

---

## Complexity Analysis
- Time Complexity: O(n!)
- Space Complexity: O(n)

---


## Interview Tip
- Start me bolo: "We use backtracking to generate all permutations"
- Explain recursion tree
- Show karo kaise choices banti hain
- Ek small dry run zaroor karo

Simple rule:
"Pick one → recurse → backtrack"
