# Problem: Minimum Path Sum

## Problem Overview
Tumhe ek m x n grid diya gaya hai jisme non-negative numbers hain.

Tumhe top-left se bottom-right tak minimum path sum find karna hai.

Allowed moves:
- Right
- Down

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Current cell ka answer previous minimum path par depend karta hai → DP"

---

## Key Observations
- Har cell tak 2 directions se aa sakte hain:
  - top
  - left
- Minimum path choose karna hai
- Overlapping subproblems hain
- DP perfect fit hai

---

## Approach (Step-by-step soch)
1. First row update karo:
   - Sirf left se aa sakte hain

2. First column update karo:
   - Sirf top se aa sakte hain

3. Baaki cells ke liye:
   - grid[i][j] += min(grid[i-1][j], grid[i][j-1])

4. Final answer:
   - bottom-right cell

---

## Example (Important for memory)

Input:

1 3 1
1 5 1
4 2 1

Step-by-step:

First row:
1 4 5

First column:
1
2
6

Now update:

Cell(1,1):
5 + min(4,2) = 7

Cell(1,2):
1 + min(5,7) = 6

Cell(2,1):
2 + min(7,6) = 8

Cell(2,2):
1 + min(6,8) = 7

Final:
7

---

## Easy Memory Trick

"Current cell = value + min(top, left)"

---



