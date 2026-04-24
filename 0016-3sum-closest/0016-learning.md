# Problem: 3Sum Closest

## Problem Overview
Tumhe ek array nums aur ek target diya gaya hai.

Tumhe aise 3 elements find karne hain jinka sum target ke sabse closest ho.

Return karo woh sum.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"3Sum problem jaisa hai, bas exact match nahi, closest chahiye"

## Key Observations
- Brute force O(n^3) hoga → slow
- Sorting karne se two pointer use kar sakte hain
- Hume minimum difference track karna hai
- Exact match mil gaya → best possible answer

## Approach (Step-by-step soch)
1. Array sort karo
2. closest_sum = large value (ya first 3 elements ka sum)
3. Loop chalao (i = 0 to n-1)

4. Har i ke liye:
   - left = i + 1
   - right = n - 1

5. Jab tak left < right:
   - current_sum = nums[i] + nums[left] + nums[right]

6. Agar abs(current_sum - target) < abs(closest_sum - target):
   → closest_sum update karo

7. Agar current_sum < target:
   → left++
8. Agar current_sum > target:
   → right--
9. Agar equal ho:
   → return target

## Example (Important for memory)

Input:
nums = [-1,2,1,-4], target = 1

After sorting:
[-4,-1,1,2]

Try combinations:

-4 + -1 + 2 = -3  
-1 + 1 + 2 = 2 → closest  

Final Answer:
2

## Easy Memory Trick

"3Sum + closest → difference minimize karo"

## Pattern Recognition
- Sorting
- Two pointers
- Optimization problem

## Pattern Used
Sorting + Two Pointer (Closest Sum Variation)

