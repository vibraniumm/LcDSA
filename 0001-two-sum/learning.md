# Problem: Two Sum

## Problem Overview
Tumhe ek array nums aur ek target diya gaya hai. Tumhe aise do indices find karne hain jinke elements ka sum target ke equal ho.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe har element ke liye uska complement (target - current value) dhoondhna hai"

## Key Observations
- Har element ke liye ek complement exist karta hai
- Same element do baar use nahi kar sakte
- Exactly ek valid answer guaranteed hai

## Approach (Step-by-step soch)
1. Ek hashmap (dictionary) banao
2. Array traverse karo
3. Har element ke liye:
   - complement = target - nums[i]
   - Check karo kya complement hashmap me already hai
   - Agar hai → answer mil gaya
   - Agar nahi → current element ko hashmap me store karo

## Example (Important for memory)

Input:
nums = [2,7,11,15], target = 9

Step-by-step:

2 → complement = 7 → not found → store {2:0}  
7 → complement = 2 → found → answer = [0,1]

## Easy Memory Trick

"Har element ke liye poochho: mujhe kis number ki zarurat hai target banane ke liye?"

## Pattern Recognition
- Hashing
- Complement search
- One-pass lookup

## Pattern Used
HashMap (Value → Index Mapping)

## Why This Works
- Har element ka complement efficiently O(1) me check kar sakte hain
- Isse nested loop avoid hota hai (O(n^2) se O(n) ho jata hai)
- One-pass me hi answer mil jata hai

## When To Use This Pattern Again
- Jab "pair sum" ya "target sum" type ka question aaye
- Jab fast lookup required ho
- Jab order matter nahi karta
- Keywords: "two sum", "pair equals target", "find complement"

## Common Mistakes
- Same element reuse kar lena
- Complement check se pehle insert kar dena
- Index store na karna

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

## Interview Tip
- Start me bolo: "We will use a hashmap to store value-index pairs and check complements in one pass"
- Brute force (O(n^2)) briefly mention karke optimize explain karo
- Clearly bolo ki kyun hashmap use kar rahe ho
- End me ek quick dry run kar do

Simple rule:
"Target sum problems = complement + hashmap"
