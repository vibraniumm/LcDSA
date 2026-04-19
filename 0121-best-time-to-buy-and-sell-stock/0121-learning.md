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



