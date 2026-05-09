# Problem: Group Anagrams

## Problem Overview
Tumhe ek array of strings strs diya gaya hai.

Tumhe anagrams ko ek saath group karna hai.

Anagrams:
→ words jinke characters same hote hain bas arrangement different hota hai

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Same characters → same key"

---

## Key Observations
- Anagrams ka sorted form same hota hai
- Example:
  - "eat" → "aet"
  - "tea" → "aet"
- Same sorted string ko hashmap key bana sakte hain

---

## Approach (Step-by-step soch)
1. Ek hashmap banao:
   - key → sorted string
   - value → list of anagrams

2. Har string ke liye:
   - sorted version nikalo
   - hashmap me append karo

3. End me hashmap values return karo

---


