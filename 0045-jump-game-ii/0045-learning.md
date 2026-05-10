# Problem: Jump Game II

## Problem Overview
Tumhe ek array nums diya gaya hai.

nums[i] batata hai ki current index se maximum kitna jump kar sakte ho.

Tumhe minimum jumps me last index tak pahunchna hai.

Guaranteed hai ki last index reachable hai.

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Minimum jumps → Greedy range expansion"

---

## Key Observations
- Har jump me hume maximum future reach choose karni hai
- BFS jaisa level traversal hota hai
- Current jump range track karna useful hai
- Jab current range end ho jaye:
  → jump increase karo

---

## Approach (Step-by-step soch)
1. Variables:
   - jumps = 0
   - current_end = 0
   - farthest = 0

2. Loop chalao till n-2:
   - farthest = max(farthest, i + nums[i])

3. Agar i == current_end:
   - jump lena padega
   - jumps++
   - current_end = farthest

4. End me jumps return karo

---

## Example (Important for memory)

Input:
nums = [2,3,1,1,4]

Step-by-step:

Index 0:
Reach = 2

Jump 1:
Range = [1,2]

From range:
Index 1 → reach = 4

Jump 2:
Reach end

Final:
2

---

## Easy Memory Trick

"Current range khatam → jump lo"

---

## Pattern Recognition
- Greedy
- Range expansion
- BFS-like traversal

---

## Pattern Used
Greedy (Farthest Reach)

---

## Why This Works
- Har jump me maximum reachable area expand karte hain
- Minimum jumps naturally ensure hote hain
- BFS levels ki tarah ranges process hoti hain
- Efficient O(n) solution milta hai

---

## When To Use This Pattern Again
- Jab minimum jumps/moves chahiye ho
- Jab range expansion ho raha ho
- Jab greedy optimal choice possible ho
- Keywords: "minimum jumps", "reach end", "farthest"

---

## Common Mistakes
- DP use karna unnecessarily
- current_end update galat karna
- Last index tak iterate karna
- Jump increment wrong place par karna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---



