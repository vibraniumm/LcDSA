# Problem: 4Sum

## Problem Overview
Tumhe ek array nums aur ek target diya gaya hai.

Tumhe aise unique quadruplets find karne hain jinka sum target ke equal ho.

Condition:
- All indices different hone chahiye
- Duplicate quadruplets allowed nahi hain

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"4Sum = 3Sum ka extension"

Aur phir:

"Sorting + nested loops + two pointer"

## Key Observations
- Brute force O(n^4) hoga → too slow
- Sorting se:
  - Duplicate handling easy ho jata hai
  - Two pointer apply kar sakte hain
- 2 elements fix karke baaki 2Sum solve kar sakte hain

## Approach (Step-by-step soch)
1. Array sort karo
2. Do loops chalao:
   - i = 0 to n-1
   - j = i+1 to n-1

3. Duplicate skip karo:
   - i aur j dono ke liye

4. Two pointers use karo:
   - left = j + 1
   - right = n - 1

5. Jab tak left < right:
   - sum = nums[i] + nums[j] + nums[left] + nums[right]

6. Agar sum == target:
   - result me add karo
   - duplicates skip karo
   - left++ aur right--

7. Agar sum < target:
   → left++
8. Agar sum > target:
   → right--

## Example (Important for memory)

Input:
nums = [1,0,-1,0,-2,2], target = 0

After sorting:
[-2,-1,0,0,1,2]

Try combinations:

[-2,-1,1,2]  
[-2,0,0,2]  
[-1,0,0,1]  

Final Answer:
All above unique quadruplets

## Pattern Recognition
- Sorting
- Two pointers
- Duplicate handling
- k-Sum reduction

## Pattern Used
Sorting + Two Pointer (k-Sum Pattern)

## Why This Works
- Sorting se structured traversal possible hota hai
- Problem reduce hoti hai 4Sum → 2Sum
- Two pointer efficiently pairs find karta hai
- Duplicate skipping ensures unique results

## When To Use This Pattern Again
- Jab 3Sum / 4Sum / kSum type problems aaye
- Jab combinations with target sum ho
- Jab duplicates avoid karne ho
- Keywords: "quadruplets", "k sum", "target combinations"

## Common Mistakes
- Duplicate skip na karna
- Sorting bhool jana
- Pointer movement galat karna
- Overflow ignore karna (large numbers)

## Complexity Analysis
- Time Complexity: O(n^3)
- Space Complexity: O(1) (excluding output)

## Interview Tip
- Start me bolo: "We sort the array and reduce 4Sum to 2Sum using two loops and two pointers"
- Brute force briefly mention karo
- Duplicate handling clearly explain karo
- Ek dry run karke approach prove karo

Simple rule:
"Sort + fix two + two pointer"

## Easy Memory Trick

"4Sum = fix two + solve 2Sum"


