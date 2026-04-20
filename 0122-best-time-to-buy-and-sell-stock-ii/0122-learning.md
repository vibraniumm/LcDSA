# Problem: Best Time to Buy and Sell Stock II

## Problem Overview
Tumhe ek array prices diya gaya hai jahan prices[i] stock ka price hai ith day par.

Tum multiple times buy aur sell kar sakte ho, lekin ek time par sirf ek stock hold kar sakte ho.

Maximum profit return karo.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Jab bhi price increase ho raha ho → profit le lo"

## Key Observations
- Multiple transactions allowed hain
- Har increasing pair se profit mil sakta hai
- Global max profit = sum of all positive differences
- Long hold karne ki zarurat nahi hai

## Approach (Step-by-step soch)
1. profit = 0
2. Array traverse karo (i = 1 to n-1)
3. Har step pe:
   - Agar prices[i] > prices[i-1]
     → profit += prices[i] - prices[i-1]

4. End me profit return karo

## Example (Important for memory)

Input:
prices = [7,1,5,3,6,4]

Step-by-step:

1 → 5 → profit = 4  
3 → 6 → profit = 3  

Total profit:
4 + 3 = 7

## Easy Memory Trick

"Har chhota profit le lo, sab add karo"

