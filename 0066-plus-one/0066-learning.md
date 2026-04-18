# Problem: Plus One

## Problem Overview
Tumhe ek array digits diya gaya hai jo ek number represent karta hai (most significant digit pehle).

Tumhe is number me +1 add karna hai aur updated digits return karne hain.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Addition with carry (right se start karke)"

## Key Observations
- Addition hamesha last digit se start hoti hai
- Agar digit < 9 hai → simple +1
- Agar digit = 9 hai → 0 banega aur carry aage jayega
- Agar sab digits 9 hain → new digit add karna padega

## Approach (Step-by-step soch)
1. Last index se start karo (right to left)
2. Har digit ke liye:
   - Agar digit < 9:
     → digits[i] += 1
     → return digits
   - Agar digit == 9:
     → digits[i] = 0
     → carry forward

3. Agar loop complete ho jaye:
   → sab digits 9 the
   → return [1] + digits

## Example (Important for memory)

Input:
digits = [1,2,9]

Step-by-step:

9 → becomes 0 (carry)  
2 → becomes 3 (stop)

Final:
[1,3,0]

Example 2:

digits = [9,9]

→ [0,0] → carry left  
→ return [1,0,0]

## Easy Memory Trick

"Right se start karo, 9 ko 0 banao, first non-9 ko +1 karo"

