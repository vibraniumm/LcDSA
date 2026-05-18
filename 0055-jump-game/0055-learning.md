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


