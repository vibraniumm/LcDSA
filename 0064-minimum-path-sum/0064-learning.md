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


