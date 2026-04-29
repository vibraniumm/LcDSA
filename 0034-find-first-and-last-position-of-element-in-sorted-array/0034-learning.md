# Problem: Find First and Last Position of Element in Sorted Array

## Problem Overview
Tumhe ek sorted array nums aur ek target diya gaya hai.

Tumhe target ka starting aur ending index find karna hai.

Agar target present nahi hai → return [-1, -1]

Constraint:
- O(log n) time complexity

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Binary search 2 baar use karna hai (first occurrence + last occurrence)"

## Key Observations
- Array sorted hai → binary search apply hoga
- Target multiple times ho sakta hai
- Hume:
  - leftmost occurrence (first index)
  - rightmost occurrence (last index)
  find karna hai


