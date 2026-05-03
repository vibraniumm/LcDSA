# Problem: Majority Element

## Problem Overview
Tumhe ek array nums diya gaya hai.

Tumhe majority element find karna hai.

Majority element:
→ jo element ⌊n/2⌋ se zyada baar appear hota hai

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Majority element cancel nahi ho sakta → Boyer-Moore Voting use karo"

---

## Key Observations
- Majority element always exist karta hai
- Agar elements pair-wise cancel kare:
  → majority element bachega
- Count maintain karke candidate track kar sakte hain

---

## Approach (Step-by-step soch)
1. candidate = None
2. count = 0

3. Har element ke liye:
   - Agar count == 0:
     → candidate = num

   - Agar num == candidate:
     → count++

   - else:
     → count--

4. End me candidate return karo

---

## Example (Important for memory)

Input:
nums = [2,2,1,1,1,2,2]

Step-by-step:

2 → count = 1  
2 → count = 2  
1 → count = 1  
1 → count = 0  
1 → candidate = 1, count = 1  
2 → count = 0  
2 → candidate = 2, count = 1  

Final:
2

---

## Easy Memory Trick

"Same add, different cancel"

---

## Pattern Recognition
- Greedy
- Voting algorithm
- Cancellation logic

---

## Pattern Used
Boyer-Moore Voting Algorithm

---

## Why This Works
- Majority element count hamesha positive rehta hai
- Dusre elements cancel hote rehte hain
- Final me majority element hi bachta hai
- O(1) space me efficient solution milta hai

---

## When To Use This Pattern Again
- Jab majority (> n/2) guaranteed ho
- Jab space optimize karna ho
- Jab pair cancellation logic apply ho
- Keywords: "majority element", "more than half", "voting"

---

## Common Mistakes
- Count reset logic galat likhna
- Candidate update miss karna
- Hashmap use karna (extra space)
- Problem constraint ignore karna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Interview Tip
- Start me bolo: "We use Boyer-Moore Voting Algorithm"
- Explain karo cancellation logic
- Mention karo ki majority guaranteed hai
- Ek quick dry run dikhao

Simple rule:
"Majority survives cancellation"
