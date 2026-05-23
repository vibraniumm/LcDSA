# Problem: Valid Palindrome

## Problem Overview
Tumhe ek string s diya gaya hai.

Tumhe check karna hai:
→ string palindrome hai ya nahi

Rules:
- Uppercase ko lowercase treat karo
- Non-alphanumeric characters ignore karo

Palindrome:
→ forward aur backward same read ho

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Two pointers from both ends"

---

## Key Observations
- Special characters ignore karne hain
- Case-insensitive comparison karna hai
- Left aur right se compare kar sakte hain
- Extra string banana optional hai

---

## Approach (Step-by-step soch)
1. Two pointers lo:
   - left = 0
   - right = len(s) - 1

2. Jab tak left < right:

3. Non-alphanumeric characters skip karo:
   - left++
   - right--

4. Characters lowercase me compare karo:
   - Agar mismatch:
     → return False

5. Match:
   - left++
   - right--

6. Loop complete:
   → return True

---

## Example (Important for memory)

Input:
"A man, a plan, a canal: Panama"

Processed comparison:

a == a  
m == m  
a == a  
...

Sab match hue

Final:
True

---

## Easy Memory Trick

"Ignore special chars, compare both ends"

---

## Pattern Recognition
- Two pointers
- String processing
- Palindrome check

---

## Pattern Used
Two Pointer Technique

---

## Why This Works
- Palindrome symmetric hota hai
- Two pointers efficiently symmetry check karte hain
- Invalid characters skip kar sakte hain
- O(n) me solution milta hai

---

## When To Use This Pattern Again
- Jab palindrome check karna ho
- Jab string symmetry ho
- Jab opposite-end comparison ho
- Keywords: "palindrome", "two ends", "mirror"

---


