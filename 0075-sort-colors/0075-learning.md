# Problem: Sort Colors

## Problem Overview
Tumhe ek array nums diya gaya hai jisme:
- 0 → Red
- 1 → White
- 2 → Blue

Tumhe array ko in-place sort karna hai:
→ [0s, then 1s, then 2s]

Important:
- Built-in sort use nahi karna

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"3-way partitioning → Dutch National Flag Algorithm"

---

## Key Observations
- Sirf 3 unique values hain
- Hum pointers use karke partition kar sakte hain
- 0 left side me jayega
- 2 right side me jayega
- 1 middle me rahega

---

## Approach (Step-by-step soch)
1. 3 pointers lo:
   - low = 0
   - mid = 0
   - high = n - 1

2. Jab tak mid <= high:

   Case 1:
   - nums[mid] == 0
     → swap low aur mid
     → low++, mid++

   Case 2:
   - nums[mid] == 1
     → mid++

   Case 3:
   - nums[mid] == 2
     → swap mid aur high
     → high--

---

## Example (Important for memory)

Input:
nums = [2,0,2,1,1,0]

Step-by-step:

[2,0,2,1,1,0]

Swap 2 with high:
[0,0,2,1,1,2]

Move 0 left:
[0,0,2,1,1,2]

Continue...

Final:
[0,0,1,1,2,2]

---

## Easy Memory Trick

"0 left, 2 right, 1 middle"

---

## Pattern Recognition
- Two pointers
- Partitioning
- In-place sorting

---

## Pattern Used
Dutch National Flag Algorithm

---

## Why This Works
- Array ko 3 regions me divide karte hain
- Har step me ek element correct region me place hota hai
- One-pass sorting achieve hoti hai
- Extra space ki zarurat nahi hoti

---

## When To Use This Pattern Again
- Jab limited categories ho
- Jab partition-based sorting ho
- Jab in-place sorting required ho
- Keywords: "3 colors", "partition", "one pass"

---

## Common Mistakes
- Swap ke baad mid incorrectly move karna
- 2 swap case me mid increment kar dena
- Extra sorting use karna
- Pointer conditions galat likhna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Interview Tip
- Start me bolo: "We use Dutch National Flag Algorithm"
- Clearly explain 3 regions
- Mention karo why one-pass possible hai
- Dry run bahut important hai

Simple rule:
"0 left, 1 middle, 2 right"
