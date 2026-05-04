# Problem: Sudoku Solver

## Problem Overview
Tumhe ek 9x9 Sudoku board diya gaya hai jisme kuch cells empty hain ('.').

Tumhe board ko fill karna hai taki:
- Har row me digits 1-9 ek baar aaye
- Har column me digits 1-9 ek baar aaye
- Har 3x3 box me digits 1-9 ek baar aaye

Ek valid solution guaranteed hai.

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Backtracking + fast validation using sets"

---

## Key Observations
- Har step pe validity check fast hona chahiye
- Repeated scanning slow hota hai → optimize with sets
- 3 constraints track karne hain:
  - row
  - column
  - box
- Backtracking se solution explore karenge

---

## Approach (Step-by-step soch)
1. 3 data structures banao:
   - rows[9] → har row ke elements
   - cols[9] → har column ke elements
   - boxes[9] → har 3x3 box ke elements

2. Initial board scan karke sets fill karo

3. Recursive solve function:
   - Har empty cell ('.') ke liye:
     - Try digits '1' to '9'

4. Validity check:
   - num not in rows[r]
   - num not in cols[c]
   - num not in boxes[box_index]

5. Agar valid:
   - Place karo
   - Sets update karo
   - Recursively solve karo

6. Agar fail:
   - Backtrack (undo changes)

---

## Example (Important for memory)

Input:
Partially filled board

Process:
- Sets me already used numbers track hote hain
- Empty cell pe sirf valid options try hote hain
- Wrong path → backtrack

Final:
Fully solved Sudoku

---

## Easy Memory Trick

"Track → Try → Place → Backtrack"

---

## Pattern Recognition
- Backtracking
- Hashing (sets)
- Constraint optimization

---

## Pattern Used
Backtracking + Hash Set Optimization

---

## Why This Works
- Sets se validation O(1) me hota hai
- Har step me invalid choices skip ho jati hain
- Backtracking correct path find karta hai
- Optimization se performance improve hoti hai

---

## When To Use This Pattern Again
- Jab backtracking ho + frequent checks ho
- Jab constraints repeated check ho rahe ho
- Jab performance optimize karna ho
- Keywords: "backtracking optimization", "constraint tracking"

---

## Common Mistakes
- Sets update karna bhool jana
- Backtrack me remove na karna
- Box index galat calculate karna
- Infinite recursion

---

## Complexity Analysis
- Time Complexity: O(9^(n*n)) worst case
- Space Complexity: O(n*n)

---

## Interview Tip
- Start me bolo: "We use backtracking with sets for O(1) validation"
- Difference explain karo naive vs optimized approach
- Box indexing clearly batao
- Example dry run karo

Simple rule:
"Use sets to speed up backtracking"


---

