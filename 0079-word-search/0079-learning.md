# Problem: Word Search

## Problem Overview
Tumhe ek m x n board aur ek string word diya gaya hai.

Tumhe check karna hai ki word board me exist karta hai ya nahi.

Rules:
- Adjacent cells horizontally ya vertically connected hone chahiye
- Same cell ek word me dobara use nahi kar sakte

Return:
- True → agar word mil jaye
- False → otherwise

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Grid traversal + backtracking"

---

## Key Observations
- Har character adjacent hona chahiye
- Same cell repeat nahi kar sakte
- Har starting point try karna padega
- DFS + Backtracking best fit hai

---



