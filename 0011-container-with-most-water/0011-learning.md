# Problem: Container With Most Water

## Problem Overview
Tumhe ek array height diya gaya hai jisme vertical lines ki heights di hui hain.

Tumhe do lines choose karni hain jo maximum water hold kar sake.

Return karo maximum area.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Width maximize karte hue height ka minimum maximize karna hai"

Aur phir next thought:

"Brute force O(n^2) hoga → optimize with two pointers"

## Key Observations
- Area = width × min(height[left], height[right])
- Width = (right - left)
- Water hamesha smaller height se limited hota hai
- Agar chhoti height wali side ko move nahi karoge → better result nahi milega

## Approach (Step-by-step soch)
1. Do pointers use karo:
   - left = 0
   - right = n - 1

2. Jab tak left < right:
   - width = right - left
   - height = min(height[left], height[right])
   - area = width × height
   - max area update karo

3. Pointer move rule:
   - Agar height[left] < height[right]
     → left++
   - else
     → right--

## Example (Important for memory)

Input:
height = [1,8,6,2,5,4,8,3,7]

Step-by-step (key idea):

Start:
left = 0, right = 8  
area = 8 × min(1,7) = 8  

Move left (kyunki 1 chhota hai)

left = 1, right = 8  
area = 7 × min(8,7) = 49 → max

Continue but 49 best rehta hai

Final Answer:
49

## Easy Memory Trick

"Chhoti wall hi water limit karti hai → usko hi move karo"

## Pattern Recognition
- Two pointers (opposite ends)
- Greedy decision making
- Optimization over brute force

## Pattern Used
Two Pointer (Greedy Optimization)

## Why This Works
- Maximum width start me hoti hai
- Area depend karta hai smaller height par
- Agar chhoti height ko replace nahi karoge → area improve nahi hoga
- Isliye hamesha chhoti side ko move karte hain better chance ke liye

## When To Use This Pattern Again
- Jab array me 2 ends se answer find karna ho
- Jab width/length reduce hoti hai aur optimize karna ho
- Jab greedy decision valid ho
- Keywords: "max area", "two ends", "optimize brute force"

## Common Mistakes
- Badi height wali pointer move kar dena (wrong logic)
- Area formula galat use karna
- Brute force use karna (TLE)
- min(height) ka concept ignore karna
                                                                                                                                                                                                                              
## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)
  
## Interview Tip
- Start me bolo: "Brute force O(n^2) hoga, so we optimize using two pointers"
- Explain karo ki kyun smaller height move karte hain
- Clearly bolo ki width decrease hoti hai but height improve ho sakti hai
- Ek dry run karke logic prove karo

Simple rule:
"Move the smaller height pointer"

