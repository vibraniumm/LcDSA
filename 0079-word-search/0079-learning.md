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

## Approach (Step-by-step soch)
1. Board ke har cell se DFS start karo

2. DFS function:
   - Current row
   - Current col
   - Word index

3. Base case:
   - Agar index == len(word)
     → pura word mil gaya → return True

4. Invalid conditions:
   - Out of bounds
   - Character mismatch
   - Already visited

5. Current cell mark karo visited

6. 4 directions me DFS:
   - up
   - down
   - left
   - right

7. Backtrack:
   - Cell restore karo

---

## Example (Important for memory)

Input:

A B C E
S F C S
A D E E

word = "ABCCED"

Path:
A → B → C → C → E → D

Final:
True

---

## Easy Memory Trick

"Match → Explore → Backtrack"

---



