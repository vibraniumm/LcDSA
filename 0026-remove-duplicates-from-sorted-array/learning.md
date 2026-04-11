# Problem: Remove Duplicates from Sorted Array

## Problem Overview
Tumhe ek sorted array nums diya gaya hai. Tumhe duplicates remove karne hain in-place, taki har unique element sirf ek baar aaye.

Return karo k = number of unique elements.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Array sorted hai → duplicates side-by-side honge → mujhe unique elements ko aage shift karna hai"

## Key Observations
- Array already sorted hai
- Duplicate elements adjacent honge
- In-place modification karna hai (extra space allowed nahi hai)
- Relative order maintain karna hai

## Approach (Step-by-step soch)
1. Do pointers use karo:
   - i → slow pointer (unique elements ka position)
   - j → fast pointer (array traverse karega)

2. Initialize:
   - i = 0

3. j ko 1 se start karo

4. Har step pe:
   - Agar nums[j] != nums[i]
     → i++
     → nums[i] = nums[j]

5. End me return i + 1

## Example (Important for memory)

Input:
nums = [0,0,1,1,1,2,2,3,3,4]

Step-by-step:

i = 0

j = 1 → same → skip  
j = 2 → new → i = 1 → nums[1] = 1  
j = 3 → same → skip  
j = 5 → new → i = 2 → nums[2] = 2  
j = 7 → new → i = 3 → nums[3] = 3  
j = 9 → new → i = 4 → nums[4] = 4  

Final array:
[0,1,2,3,4,...]

Return:
5

## Easy Memory Trick

"Sorted array + duplicates = slow-fast pointer se unique values ko aage shift karo"

## Pattern Recognition
- Two pointers
- In-place array modification
- Sorted array optimization

## Pattern Used
Two Pointer Technique (Slow & Fast Pointer)

## Why This Works
- Sorted hone ki wajah se duplicates ek saath grouped hote hain
- Fast pointer naye elements detect karta hai
- Slow pointer unhe correct position par place karta hai
- Isse extra space use nahi hota aur efficient solution milta hai

## When To Use This Pattern Again
- Jab array sorted ho
- Jab duplicates remove/handle karne ho
- Jab in-place modification required ho
- Jab order maintain karna ho
- Keywords: "remove duplicates", "sorted array", "in-place"

## Common Mistakes
- New array bana lena (allowed nahi hai)
- i ko sahi update na karna
- Return value galat dena (i instead of i+1)
- j ko 1 se start na karna

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "Since array sorted hai, duplicates adjacent honge, so we use two pointers"
- Slow aur fast pointer ka role clearly explain karo
- In-place condition highlight karo
- Ek quick dry run karke apni logic validate karo

Simple rule:
"Sorted array + duplicates = two pointers"
