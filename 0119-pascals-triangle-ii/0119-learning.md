# Problem: Pascal's Triangle II

## Problem Overview
Tumhe ek integer rowIndex diya gaya hai.

Tumhe Pascal's Triangle ki sirf us row (0-indexed) return karni hai.

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe ek hi row build karni hai using previous values"

---

## Key Observations
- Row ka size = rowIndex + 1
- First aur last element hamesha 1 hota hai
- Middle elements:
  → previous values ka sum hote hain
- Previous row store karne ki zarurat nahi (optimize kar sakte hain)

---

## Approach (Step-by-step soch)
1. Ek array banao size = rowIndex + 1
2. Sab elements ko initially 1 se fill karo

3. Outer loop:
   - i = 2 to rowIndex

4. Inner loop (reverse me chalana hai):
   - j = i-1 to 1

5. Update:
   - row[j] = row[j] + row[j-1]

---

## Example (Important for memory)

Input:
rowIndex = 3

Step-by-step:

Start:
[1,1,1,1]

i = 2:
[1,2,1,1]

i = 3:
[1,3,3,1]

Final:
[1,3,3,1]

---

## Easy Memory Trick

"Reverse update karo taki previous values safe rahe"

---

## Pattern Recognition
- Dynamic Programming
- In-place update
- Reverse traversal

---

## Pattern Used
Dynamic Programming (Space Optimized)

---

## Why This Works
- Har value previous row par depend karti hai
- Reverse traversal se overwrite issue nahi hota
- Same array reuse hota hai → space efficient
- Incremental build hota hai

---

## When To Use This Pattern Again
- Jab previous state par depend ho
- Jab space optimize karna ho
- Jab in-place update possible ho
- Keywords: "DP", "in-place", "row build"

---

## Common Mistakes
- Forward loop chalana (values overwrite ho jayengi)
- Full triangle bana dena (unnecessary)
- Edge values ignore karna
- Wrong indices use karna

---

## Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(n)

---

## Interview Tip
- Start me bolo: "We use DP and build the row in-place"
- Reverse loop ka reason clearly explain karo
- Show karo kaise overwrite avoid hota hai
- Ek quick example run karo

Simple rule:
"Reverse loop = safe update"
