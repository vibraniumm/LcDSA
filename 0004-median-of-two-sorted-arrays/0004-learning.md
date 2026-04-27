Problem: Median of Two Sorted Arrays

## Problem Overview
Tumhe do sorted arrays nums1 aur nums2 diye gaye hain.

Tumhe in dono ko logically combine karke median find karna hai.

Constraint:
- Time complexity O(log(m+n)) honi chahiye

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Binary search on smaller array + partitioning"

## Key Observations
- Median middle element hota hai
- Even length → average of 2 middle elements
- Hume arrays ko merge nahi karna (warna O(n) ho jayega)
- Partition aise hona chahiye:
  - Left side me half elements
  - Right side me half elements

## Approach (Step-by-step soch)
1. Ensure nums1 smaller array ho (binary search easy hota hai)
2. Binary search apply karo nums1 par

3. Partition define karo:
   - partitionX = mid of nums1
   - partitionY = (m+n+1)//2 - partitionX

4. Left aur right elements identify karo:
   - maxLeftX, minRightX
   - maxLeftY, minRightY

5. Check condition:
   - maxLeftX <= minRightY
   - maxLeftY <= minRightX

6. Agar condition satisfy:
   - Agar total even:
     → median = (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
   - Agar odd:
     → median = max(maxLeftX, maxLeftY)

7. Agar condition fail:
   - maxLeftX > minRightY → move left
   - else → move right

## Example (Important for memory)

Input:
nums1 = [1,3], nums2 = [2]

Partition:

Left: [1,2]  
Right: [3]  

Median:
2

Example 2:

[1,2] + [3,4]

Left: [1,2]  
Right: [3,4]  

Median:
(2+3)/2 = 2.5

## Easy Memory Trick

"Partition karo taki left <= right ho aur size equal ho"

## Pattern Recognition
- Binary search
- Partitioning
- Divide arrays logically

## Pattern Used
Binary Search on Partition

## Why This Works
- Median ke liye hume sorted middle elements chahiye
- Binary search se correct partition fast milta hai
- Dono arrays ko merge ki zarurat nahi padti
- O(log(min(m,n))) me solution mil jata hai

## When To Use This Pattern Again
- Jab 2 sorted arrays ho
- Jab median ya kth element find karna ho
- Jab O(log n) constraint ho
- Keywords: "median", "kth element", "sorted arrays"

## Common Mistakes
- Arrays merge kar dena (wrong complexity)
- Partition logic galat samajhna
- Edge cases handle na karna (empty array)
- Infinite loop in binary search

## Complexity Analysis
- Time Complexity: O(log(min(m, n)))
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We use binary search on the smaller array and partition both arrays"
- Clearly explain karo partition concept
- Edge cases mention karo (empty arrays)
- Example ke saath explain karo (very important)


Simple rule:
"Binary search + correct partition"
