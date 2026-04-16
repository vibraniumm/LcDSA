# Problem: 3Sum

## Problem Overview
Tumhe ek array nums diya gaya hai. Tumhe aise triplets find karne hain jinke sum = 0 ho.

Condition:
- i, j, k sab different hone chahiye
- Duplicate triplets allowed nahi hain

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"3Sum → 2Sum ka extension hai"

Aur phir:

"Sorting + Two Pointer use karna padega"

## Key Observations
- Brute force O(n^3) hoga → too slow
- Sorting karne se:
  - Duplicates easily handle ho jaate hain
  - Two pointer apply kar sakte hain
- Har element ko fix karke baaki 2Sum solve kar sakte hain

## Approach (Step-by-step soch)
1. Array ko sort karo
2. Ek loop chalao (i = 0 to n-1)
3. Har i ke liye:
   - Agar duplicate hai → skip
4. Do pointers use karo:
   - left = i + 1
   - right = n - 1

5. Jab tak left < right:
   - sum = nums[i] + nums[left] + nums[right]

6. Agar sum == 0:
   - answer me add karo
   - duplicates skip karo
   - left++ aur right--

7. Agar sum < 0:
   → left++

8. Agar sum > 0:
   → right--

## Example (Important for memory)

Input:
nums = [-1,0,1,2,-1,-4]

After sorting:
[-4,-1,-1,0,1,2]

Step idea:

i = -1  
left = -1, right = 2  
sum = 0 → valid  

i = -1 (duplicate skip)  

i = 0  
left = 1, right = 2  
sum = 0 → valid  

Final Answer:
[[-1,-1,2], [-1,0,1]]

## Easy Memory Trick

"3Sum = fix one + solve 2Sum with two pointers"

## Pattern Recognition
- Sorting
- Two pointers
- Duplicate handling
- Reduction of problem (3Sum → 2Sum)

