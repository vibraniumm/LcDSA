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

