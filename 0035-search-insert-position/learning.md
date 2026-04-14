# Problem: Search Insert Position

## Problem Overview
Tumhe ek sorted array nums aur ek target diya gaya hai. Agar target array me present hai to uska index return karo.

Agar present nahi hai, to batao ki wo kis index pe insert hoga sorted order maintain karne ke liye.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Sorted array + O(log n) = Binary Search use karna hai"

## Key Observations
- Array sorted hai
- Distinct elements hain
- O(log n) constraint diya hai → Binary Search confirm
- Answer always exist karega (either found or insert position)

## Approach (Step-by-step soch)
1. left = 0, right = len(nums) - 1
2. Jab tak left <= right:
   - mid = (left + right) // 2
3. Agar nums[mid] == target:
   → return mid
4. Agar nums[mid] < target:
   → left = mid + 1
5. Agar nums[mid] > target:
   → right = mid - 1
6. Loop ke baad:
   → left hi correct insert position hoga

## Example (Important for memory)

Input:
nums = [1,3,5,6], target = 2

Step-by-step:

left = 0, right = 3  
mid = 1 → nums[1] = 3 → target smaller → right = 0  

mid = 0 → nums[0] = 1 → target bigger → left = 1  

Loop end → left = 1  

Answer:
1

## Easy Memory Trick

"Binary search me agar element na mile, to left pointer hi answer hota hai"

## Pattern Recognition
- Binary search
- Sorted array
- Search or insert position

## Pattern Used
Binary Search (Lower Bound Concept)

## Why This Works
- Binary search search space ko half karta hai har step me
- Agar target mil jata hai → direct return
- Agar nahi milta → left pointer us position pe hota hai jahan insert karna chahiye
- Efficient O(log n) solution milta hai

## When To Use This Pattern Again
- Jab sorted array ho
- Jab O(log n) constraint diya ho
- Jab "search or insert position" type problem ho
- Keywords: "binary search", "insert position", "lower bound"

## Common Mistakes
- mid calculation galat karna
- infinite loop condition
- loop ke baad wrong value return karna (right instead of left)
- edge cases ignore karna

## Complexity Analysis
- Time Complexity: O(log n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "Since array sorted hai aur O(log n) required hai, we use binary search"
- Clearly explain karo ki left final answer kyun hota hai
- Edge cases mention karo (target smallest ya largest ho sakta hai)
- Ek quick dry run kar do

Simple rule:
"Binary search → not found → return left"
