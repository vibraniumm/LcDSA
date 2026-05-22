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


