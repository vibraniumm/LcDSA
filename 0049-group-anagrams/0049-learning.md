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

## Example (Important for memory)

Input:
["eat","tea","tan","ate","nat","bat"]

Step-by-step:

"eat" → "aet"  
"tea" → "aet"  
"ate" → "aet"

Group:
["eat","tea","ate"]

"tan" → "ant"  
"nat" → "ant"

Group:
["tan","nat"]

Final:
[["bat"],["nat","tan"],["ate","eat","tea"]]

---

## Easy Memory Trick

"Anagrams ka sorted version same hota hai"

---

## Pattern Recognition
- HashMap
- String transformation
- Grouping

---

## Pattern Used
HashMap + Sorted String Key

---

## Why This Works
- Sorting characters unique signature deta hai
- Same signature wale strings anagrams hote hain
- HashMap grouping easy bana deta hai
- Efficient categorization ho jata hai

---

## When To Use This Pattern Again
- Jab grouping based on character frequency ho
- Jab strings rearrangement related ho
- Jab same-pattern strings identify karne ho
- Keywords: "anagram", "group strings", "same characters"

---

## Common Mistakes
- List ko hashmap key banana (invalid)
- Sorting bhool jana
- String join na karna after sorting
- HashMap initialization issue

---


