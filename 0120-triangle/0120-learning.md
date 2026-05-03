# Problem: Triangle

## Problem Overview
Tumhe ek triangle array diya gaya hai.

Tumhe top se bottom tak minimum path sum find karna hai.

Rule:
→ Har step par tum next row me index i ya i+1 par move kar sakte ho

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Bottom-up DP use karo (minimum path build karo)"

---

## Key Observations
- Har element depend karta hai next row ke 2 elements par
- Minimum path choose karna hai
- Top-down kar sakte hain, lekin bottom-up zyada efficient hai
- Last row already base case hai

---

## Approach (Step-by-step soch)
1. Last row ko base maan lo

2. Bottom se upar iterate karo:
   - Har element ke liye:
     → triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

3. End me top element hi answer hoga

---

## Example (Important for memory)

Input:
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

Step-by-step:

Start from bottom:

Row [4,1,8,3]

Move up:
[6,5,7] → [7,6,10]

Move up:
[3,4] → [9,10]

Move up:
[2] → [11]

Final:
11

---

## Easy Memory Trick

"Bottom se upar minimum add karo"

---

## Pattern Recognition
- Dynamic Programming
- Bottom-up
- Grid / triangle DP

---

## Pattern Used
Dynamic Programming (Bottom-Up)

---

## Why This Works
- Har step me best choice (minimum) choose karte hain
- Subproblem already solved hota hai (next row)
- Bottom-up se redundant computation avoid hota hai
- Efficient aur clean solution

---

## When To Use This Pattern Again
- Jab path minimum/maximum find karna ho
- Jab structure layered ho (triangle/grid)
- Jab overlapping subproblems ho
- Keywords: "minimum path", "triangle", "DP"

---

## Common Mistakes
- Top-down recursion bina memoization (slow)
- Adjacent condition ignore karna
- Wrong indices use karna
- Extra space unnecessarily use karna

---

## Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(1) (in-place)

---

## Interview Tip
- Start me bolo: "We use bottom-up DP to compute minimum path"
- Explain karo ki kyun bottom-up better hai
- Adjacent selection rule clearly batao
- Ek quick dry run zaroor karo

Simple rule:
"Take min from below"
