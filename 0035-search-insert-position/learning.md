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

