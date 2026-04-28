# Problem: Search in Rotated Sorted Array

## Problem Overview
Tumhe ek sorted array diya gaya hai jo kisi unknown index par rotate hua hai.

Tumhe target element ka index find karna hai.

Agar element present nahi hai → return -1

Constraint:
- O(log n) time complexity

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Rotated array + O(log n) = Modified Binary Search"

## Key Observations
- Array do sorted parts me divided hota hai
- At least ek half hamesha sorted hota hai
- Binary search ka use kar sakte hain
- Hume identify karna hai kaunsa half sorted hai

## Approach (Step-by-step soch)
1. left = 0, right = n - 1

2. Jab tak left <= right:
   - mid = (left + right) // 2

3. Agar nums[mid] == target:
   → return mid

4. Check karo kaunsa half sorted hai:

   Case 1: Left half sorted
   - nums[left] <= nums[mid]

   → Check karo target is range me hai ya nahi:
     - nums[left] <= target < nums[mid]
       → right = mid - 1
     - else
       → left = mid + 1

   Case 2: Right half sorted
   - nums[mid] < nums[right]

   → Check karo target is range me hai ya nahi:
     - nums[mid] < target <= nums[right]
       → left = mid + 1
     - else
       → right = mid - 1

## Example (Important for memory)

Input:
nums = [4,5,6,7,0,1,2], target = 0

Step-by-step:

mid = 7 → left sorted  
target not in left → go right  

mid = 1 → right sorted  
target in right → go right  

mid = 0 → found  

Answer:
4

## Easy Memory Trick

"Check sorted half → decide direction"

## Pattern Recognition
- Binary search
- Rotated array
- Condition-based search

## Pattern Used
Modified Binary Search

## Why This Works
- Har step me ek half sorted hota hai
- Sorted half me easily check kar sakte hain target hai ya nahi
- Search space half hota rehta hai
- O(log n) complexity maintain hoti hai

## When To Use This Pattern Again
- Jab rotated sorted array ho
- Jab search karna ho with O(log n)
- Jab condition-based branching ho
- Keywords: "rotated", "search", "binary search"

## Common Mistakes
- Sorted half identify na kar paana
- Wrong comparison conditions
- Infinite loop
- Edge case miss karna (single element)

## Complexity Analysis
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We use modified binary search"
- Clearly explain karo kaise sorted half detect karte hain
- Condition explain karo step-by-step
- Ek dry run karke logic prove karo

Simple rule:
"Find sorted half → search there"
