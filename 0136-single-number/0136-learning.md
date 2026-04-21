# Problem: Single Number

## Problem Overview
Tumhe ek array nums diya gaya hai jisme har element 2 baar aata hai except ek element jo sirf 1 baar aata hai.

Tumhe wahi single element find karna hai.

Constraints:
- O(n) time
- O(1) extra space

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Duplicate cancel karne hain → XOR use karo"

## Key Observations
- Same number XOR kare → 0 (a ^ a = 0)
- 0 XOR a = a
- XOR commutative aur associative hota hai
- Sab duplicates cancel ho jayenge → sirf single number bachega

## Approach (Step-by-step soch)
1. result = 0
2. Har element ke liye:
   → result = result ^ num
3. End me result return karo

## Example (Important for memory)

Input:
nums = [4,1,2,1,2]

Step-by-step:

result = 0  
0 ^ 4 = 4  
4 ^ 1 = 5  
5 ^ 2 = 7  
7 ^ 1 = 6  
6 ^ 2 = 4  

Final:
4

## Easy Memory Trick

"Same number milte hi cancel ho jayega (XOR se)"

## Pattern Recognition
- Bit manipulation
- XOR properties
- Pair cancellation

## Pattern Used
XOR Trick (Duplicate Cancellation)

## Why This Works
- Har duplicate pair XOR hone par 0 ban jata hai
- Order matter nahi karta
- Last me sirf unique element bachta hai
- Extra space ki zarurat nahi hoti

## When To Use This Pattern Again
- Jab elements pairs me ho except ek
- Jab O(1) space constraint ho
- Jab duplicate cancel karna ho
- Keywords: "single number", "appear twice", "unique element"

## Common Mistakes
- Hashmap use karna (space waste)
- XOR concept samajh na paana
- Order ke baare me confusion
- Edge case ignore karna

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We use XOR because duplicates cancel out"
- XOR properties briefly explain karo
- Brute force ya hashmap approach mention karke optimize dikhao
- Ek quick dry run kar do

Simple rule:
"Same numbers cancel → XOR"

