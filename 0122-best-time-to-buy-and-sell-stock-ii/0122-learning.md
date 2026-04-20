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

## Pattern Recognition
- Greedy
- Multiple transactions
- Peak-Valley concept

## Pattern Used
Greedy (Sum of Positive Differences)

## Why This Works
- Har increasing segment me profit milta hai
- Large profit ko small chunks me tod sakte hain
- Same result milta hai whether you hold long or sell multiple times
- Efficient O(n) solution milta hai

## When To Use This Pattern Again
- Jab multiple transactions allowed ho
- Jab profit maximize karna ho
- Jab adjacent differences ka use ho sakta ho
- Keywords: "multiple buy sell", "maximize profit", "unlimited transactions"

## Common Mistakes
- Sirf ek transaction solve karna (previous problem jaisa)
- Peak valley logic samajh na paana
- Negative differences add kar dena
- Overcomplicate karna

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We use greedy approach and take profit whenever price increases"
- Previous problem (single transaction) se difference explain karo
- Clearly batao ki kyun sab positive differences add karte hain
- Ek quick dry run kar do

Simple rule:
"Every rise is profit"



