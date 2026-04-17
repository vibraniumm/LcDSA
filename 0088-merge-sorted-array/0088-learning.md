# Problem: Merge Sorted Array

## Problem Overview
Tumhe do sorted arrays nums1 aur nums2 diye gaye hain.

nums1 ka size m + n hai jisme first m elements valid hain aur last n elements 0 hain (extra space).

Tumhe nums2 ke elements ko nums1 me merge karna hai in-place taki final array sorted rahe.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe reverse se merge karna hai taki existing elements overwrite na ho"

## Key Observations
- Dono arrays sorted hain
- nums1 me already extra space diya gaya hai
- Agar start se merge karenge → overwrite ho jayega
- Isliye end se fill karna best hai

## Approach (Step-by-step soch)
1. 3 pointers use karo:
   - i = m - 1 (nums1 ke last valid element)
   - j = n - 1 (nums2 ke last element)
   - k = m + n - 1 (final position)

2. Jab tak i >= 0 aur j >= 0:
   - Agar nums1[i] > nums2[j]
     → nums1[k] = nums1[i]
     → i--
   - else
     → nums1[k] = nums2[j]
     → j--
   - k--

3. Agar nums2 ke elements bache ho:
   → copy them into nums1

## Example (Important for memory)

Input:
nums1 = [1,2,3,0,0,0], m = 3  
nums2 = [2,5,6], n = 3  

Step-by-step:

Compare from end:

3 vs 6 → place 6  
3 vs 5 → place 5  
3 vs 2 → place 3  
2 vs 2 → place 2  
1 vs 2 → place 2  

Remaining:
1

Final array:
[1,2,2,3,5,6]

