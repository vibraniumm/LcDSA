# Problem: Best Time to Buy and Sell Stock

## Problem Overview
Tumhe ek array prices diya gaya hai jahan prices[i] stock ka price hai ith day par.

Tumhe ek hi baar buy aur ek hi baar sell karna hai (buy pehle, sell baad me).

Maximum profit return karo. Agar profit possible nahi hai → return 0.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe minimum price track karna hai aur max profit calculate karna hai"

## Key Observations
- Buy hamesha sell se pehle hona chahiye
- Profit = sell price - buy price
- Hume minimum buy price chahiye
- Har step pe best profit update karna hai

## Approach (Step-by-step soch)
1. min_price = infinity
2. max_profit = 0

3. Array traverse karo:
   - min_price = min(min_price, current price)
   - profit = current price - min_price
   - max_profit = max(max_profit, profit)

4. End me max_profit return karo

## Example (Important for memory)

Input:
prices = [7,1,5,3,6,4]

Step-by-step:

7 → min = 7  
1 → min = 1  
5 → profit = 4  
3 → profit = 2  
6 → profit = 5 (max)  
4 → profit = 3  

Final Answer:
5

## Easy Memory Trick

"Sabse sasta kharido, sabse mehenga baad me becho"

## Pattern Recognition
- Greedy
- Single pass optimization
- Min tracking

## Pattern Used
Greedy (Track Minimum + Max Profit)

## Why This Works
- Har step pe best buy price (minimum) maintain karte hain
- Future me agar better selling price mile to profit update karte hain
- Ek hi pass me optimal solution mil jata hai
- Brute force (O(n^2)) avoid ho jata hai

## When To Use This Pattern Again
- Jab max difference find karna ho
- Jab future value compare karni ho past minimum se
- Jab single transaction allowed ho
- Keywords: "max profit", "buy and sell", "difference"

## Common Mistakes
- Pehle sell kar dena (invalid case)
- Minimum track na karna
- Brute force use karna
- Negative profit allow karna

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We track the minimum price so far and calculate max profit in one pass"
- Brute force briefly mention karo
- Explain karo ki kyun greedy kaam karta hai
- Ek quick dry run kar do

Simple rule:
"Track min, update profit"



