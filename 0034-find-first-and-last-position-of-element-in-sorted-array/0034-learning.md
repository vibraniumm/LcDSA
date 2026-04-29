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

## Approach (Step-by-step soch)
1. Binary search function use karo:
   - First occurrence ke liye
   - Last occurrence ke liye

2. First occurrence:
   - Agar nums[mid] == target:
     → result store karo
     → right = mid - 1 (left side me aur search karo)

3. Last occurrence:
   - Agar nums[mid] == target:
     → result store karo
     → left = mid + 1 (right side me aur search karo)

4. End me dono values return karo:
   → [first, last]

## Example (Important for memory)

Input:
nums = [5,7,7,8,8,10], target = 8

First occurrence:
→ index = 3  

Last occurrence:
→ index = 4  

Final:
[3,4]

## Easy Memory Trick

"Binary search ko left aur right side push karo"

## Pattern Recognition
- Binary search
- Bound finding
- Range queries

## Pattern Used
Binary Search (Lower Bound + Upper Bound)

## Why This Works
- Sorted array me binary search efficient hota hai
- Condition change karke leftmost aur rightmost find kar sakte hain
- Har search O(log n) hoti hai
- Total complexity O(log n) rehti hai

## When To Use This Pattern Again
- Jab first/last occurrence find karna ho
- Jab duplicates present ho
- Jab range find karna ho
- Keywords: "first occurrence", "last occurrence", "range"

## Common Mistakes
- Binary search ek hi baar use karna
- Condition galat likhna
- Result store na karna
- Final return likhna bhool jana
- Edge case ignore karna (empty array)

## Complexity Analysis
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We use binary search twice to find first and last occurrence"
- Clearly explain karo left aur right bias
- Edge cases mention karo
- Ensure final result return kar rahe ho

Simple rule:
"Find left bound + find right bound"

