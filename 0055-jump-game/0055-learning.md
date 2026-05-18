# Problem: Jump Game

## Problem Overview
Tumhe ek array nums diya gaya hai.

nums[i] batata hai ki current index se maximum kitna jump kar sakte ho.

Tumhe check karna hai ki:
→ kya tum last index tak pahunch sakte ho ya nahi.

Return:
- True → reachable
- False → not reachable

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Maximum reachable index track karo"

---


## Key Observations
- Har position se future reach calculate kar sakte hain
- Agar kisi point par current index reachable nahi hai:
  → answer False
- Hume sirf farthest reachable position maintain karni hai
- Greedy approach enough hai

---

## Approach (Step-by-step soch)
1. maxReach = 0

2. Array traverse karo:
   - Agar i > maxReach:
     → current index unreachable
     → return False

3. Update:
   - maxReach = max(maxReach, i + nums[i])

4. End tak safely traverse ho gaya:
   → return True

---

## Example (Important for memory)

Input:
nums = [2,3,1,1,4]

Step-by-step:

Index 0:
maxReach = 2

Index 1:
maxReach = 4

Ab last index reachable hai

Final:
True

Example 2:

nums = [3,2,1,0,4]

Index 3:
maxReach = 3

Index 4 unreachable

Final:
False

---

## Easy Memory Trick

"Check karo kitna aage tak pahunch sakte ho"

---

## Pattern Recognition
- Greedy
- Reachability
- Array traversal

---

## Pattern Used
Greedy (Farthest Reach)

---

## Why This Works
- Har step par best possible reach maintain karte hain
- Agar current index reachable nahi hai:
  → आगे जाना impossible hai
- Greedy locally optimal choice sufficient hai
- O(n) me efficient solution milta hai

---

## When To Use This Pattern Again
- Jab reachability check karni ho
- Jab maximum future reach important ho
- Jab jumps/moves allowed ho
- Keywords: "can reach", "maximum jump", "reachable"

---

## Common Mistakes
- DP unnecessarily use karna
- Reach update galat karna
- Early failure detect na karna
- Last index condition confuse karna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Interview Tip
- Start me bolo: "We greedily track the farthest reachable index"
- Explain karo unreachable condition
- Jump Game I vs II ka difference mention karo
- Dry run zaroor karo

Simple rule:
"Maintain farthest reachable index"
