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

## Example (Important for memory)

Input:
haystack = "sadbutsad"  
needle = "sad"

Step-by-step:

i = 0 → "sad" → match → return 0  

Final:
0

---

## Easy Memory Trick

"Har position se check karo"

---

## Pattern Recognition
- String matching
- Sliding window
- Brute force substring

---

## Pattern Used
Sliding Window (Fixed Size)

---

## Why This Works
- Har possible starting index check karte hain
- Substring comparison simple aur direct hai
- First match milte hi stop karte hain
- Constraints allow O(n*m)

---

## When To Use This Pattern Again
- Jab substring search karna ho
- Jab exact match chahiye ho
- Jab constraints small ho
- Keywords: "find substring", "first occurrence"

---

## Common Mistakes
- Loop range galat lena (n-m+1 hona chahiye)
- Edge case ignore karna
- Early return na karna
- String slicing me mistake

---

## Complexity Analysis
- Time Complexity: O(n * m)
- Space Complexity: O(1)

---

## Interview Tip
- Start me bolo: "We check each possible starting index"
- Mention karo brute force acceptable hai
- Agar interviewer push kare → KMP mention karo
- Example dry run karo

Simple rule:
"Check all starting positions"
