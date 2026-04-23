# Problem: Pascal's Triangle

## Problem Overview
Tumhe ek integer numRows diya gaya hai.

Tumhe Pascal's Triangle ke first numRows generate karne hain.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Har row previous row se banti hai"

## Key Observations
- Har row ka first aur last element hamesha 1 hota hai
- Beech ke elements:
  → previous row ke do adjacent elements ka sum hote hain
- Triangle incremental build hota hai

## Approach (Step-by-step soch)
1. Result list banao
2. Har row ke liye (0 to numRows-1):
   - Ek new row banao size = i + 1
   - First aur last element = 1
3. Beech ke elements ke liye:
   - row[j] = prev_row[j-1] + prev_row[j]
4. Row ko result me add karo

## Example (Important for memory)

Input:
numRows = 5

Step-by-step:

Row 1: [1]  
Row 2: [1,1]  
Row 3: [1,2,1]  
Row 4: [1,3,3,1]  
Row 5: [1,4,6,4,1]  

Final:
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

## Easy Memory Trick

"Edges always 1, middle = sum of above two"

## Pattern Recognition
- Dynamic Programming
- Build from previous state
- Triangle structure

## Pattern Used
Dynamic Programming (Row by Row Construction)

## Why This Works
- Har row previous row par depend karti hai
- Subproblem already solved hota hai (previous row)
- Incrementally solution build hota hai
- Efficient aur simple logic

## When To Use This Pattern Again
- Jab problem previous state par depend kare
- Jab pattern row-by-row build hota ho
- Jab overlapping subproblems ho
- Keywords: "triangle", "build rows", "previous row"

## Common Mistakes
- Edges me 1 set na karna
- Previous row index galat use karna
- Row size galat lena
- Direct formula try karna (unnecessary)

## Complexity Analysis
- Time Complexity: O(n^2)
- Space Complexity: O(n^2)

## Interview Tip
- Start me bolo: "Each row is built using the previous row"
- Clearly explain karo edge and middle logic
- Ek small triangle draw karke samjhao
- Dry run quickly

Simple rule:
"Edges 1, middle = sum"


