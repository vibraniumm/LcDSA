# Problem: Remove Element

## Problem Overview
Tumhe ek array nums aur ek value val diya gaya hai. Tumhe array me se val ke sab occurrences remove karne hain in-place.

Return karo k = number of elements jo val ke equal nahi hain.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe unwanted value (val) ko skip karna hai aur baaki elements ko aage shift karna hai"

## Key Observations
- In-place modification karna hai
- Order maintain karna zaroori nahi hai
- Sirf valid elements ko front me lana hai
- Remaining elements important nahi hain

## Approach (Step-by-step soch)
1. Ek pointer i use karo (valid elements ka position)
2. Array traverse karo using j
3. Har step pe:
   - Agar nums[j] != val
     → nums[i] = nums[j]
     → i++
4. End me return i

## Example (Important for memory)

Input:
nums = [3,2,2,3], val = 3

Step-by-step:

i = 0

j = 0 → 3 → skip  
j = 1 → 2 → nums[0] = 2 → i = 1  
j = 2 → 2 → nums[1] = 2 → i = 2  
j = 3 → 3 → skip  

Final array:
[2,2,...]

Return:
2

## Easy Memory Trick

"Jo val ke equal hai use skip karo, baaki sab ko aage fill karo"

## Pattern Recognition
- Two pointers
- In-place filtering
- Array overwrite technique


