# Problem: Find the Index of the First Occurrence in a String

## Problem Overview
Tumhe do strings diye gaye hain:
- haystack (main string)
- needle (search string)

Tumhe needle ka first occurrence haystack me find karna hai.

Agar present nahi hai → return -1

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Substring match karna hai → sliding window / direct compare"

---

## Key Observations
- Needle ka size important hai
- Har index se substring compare karna padega
- First match milte hi return karna hai
- Brute force acceptable hai (constraints small hain)

---

## Approach (Step-by-step soch)
1. n = len(haystack), m = len(needle)

2. Loop chalao i = 0 to n-m:
   - Substring = haystack[i:i+m]

3. Agar substring == needle:
   → return i

4. Loop end tak nahi mila:
   → return -1

---


