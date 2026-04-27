# Problem: Longest Common Prefix

## Problem Overview
Tumhe ek array of strings diya gaya hai. Tumhe sabhi strings ka longest common prefix find karna hai.

Agar koi common prefix nahi hai, to empty string return karo.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Sabhi strings ko start se compare karo jab tak mismatch na mile"

## Key Observations
- Prefix hamesha string ke start se hota hai
- Jaise hi mismatch mile → stop
- Shortest string se zyada prefix possible nahi hai

## Approach (Step-by-step soch)
1. Pehli string ko prefix maan lo
2. Baaki sab strings ke saath compare karo
3. Jab tak current string prefix se match nahi karti:
   - prefix ko chhota karo (last character remove karo)
4. Agar prefix empty ho jaye → return ""
5. End me final prefix return karo

## Example (Important for memory)

Input:
strs = ["flower","flow","flight"]

Step-by-step:

Initial prefix = "flower"

Compare with "flow":
→ "flower" not match → reduce → "flow"

Compare with "flight":
→ "flow" not match → reduce → "flo" → "fl" (match)

Final Answer:
"fl"

## Easy Memory Trick

"Prefix ko chhota karte jao jab tak sab strings me fit na ho jaye"

## Pattern Recognition
- String comparison
- Prefix problems
- Iterative shrinking

## Pattern Used
Horizontal Scanning (Prefix Shrinking)

## Why This Works
- Hum ek initial prefix lete hain
- Har string ke saath validate karte hain
- Mismatch hone par prefix ko shrink karte hain
- Isse unnecessary comparisons avoid hote hain
- Efficient aur simple approach milti hai

## When To Use This Pattern Again
- Jab multiple strings ka common starting part find karna ho
- Jab prefix gradually reduce kar sakte ho
- Jab direct comparison simple ho
- Keywords: "common prefix", "shared start", "matching beginning"

## Common Mistakes
- Sirf first 2 strings compare kar lena
- Prefix ko shrink na karna
- Empty string case handle na karna

## Complexity Analysis
- Time Complexity: O(n * m)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We will take the first string as prefix and keep shrinking it until it matches all strings"
- Shortest string constraint mention karo
- Explain karo ki kyun shrinking approach efficient hai
- End me ek quick dry run kar do

Simple rule:
"Compare from start, shrink on mismatch"
