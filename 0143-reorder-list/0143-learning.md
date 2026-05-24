# Problem: Reorder List

## Problem Overview
Tumhe ek singly linked list di gayi hai:

L0 → L1 → L2 → ... → Ln

Tumhe list ko reorder karna hai:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...

Important:
- Node values change nahi kar sakte
- Sirf links modify karne hain

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Find middle → reverse second half → merge alternately"

---


## Key Observations
- List ko 2 halves me todna useful hai
- Second half reverse karna padega
- Alternate merge final pattern dega
- Linked list manipulation important hai

---

## Approach (Step-by-step soch)
1. Middle node find karo:
   - Slow & Fast pointer use karo

2. Second half reverse karo

3. Dono halves merge karo alternately:
   - first node
   - last node
   - second node
   - second last node

---

## Example (Important for memory)

Input:
1 → 2 → 3 → 4 → 5

Step 1:
Middle:
3

First half:
1 → 2 → 3

Second half:
4 → 5

Step 2:
Reverse second half:

5 → 4

Step 3:
Merge:

1 → 5 → 2 → 4 → 3

Final:
[1,5,2,4,3]

---

## Easy Memory Trick

"Middle → Reverse → Merge"

---

## Pattern Recognition
- Linked List
- Fast & Slow pointers
- Reverse linked list
- Merge two lists

---

## Pattern Used
Two Pointer + Reverse Linked List

---

## Why This Works
- Middle split balanced halves deta hai
- Reverse second half required order create karta hai
- Alternate merge final arrangement bana deta hai
- In-place efficient solution milta hai

---

## When To Use This Pattern Again
- Jab linked list reorder karni ho
- Jab end nodes ko front me lana ho
- Jab reverse + merge pattern ho
- Keywords: "reorder", "reverse second half", "linked list"

---

## Common Mistakes
- Middle split galat karna
- Reverse logic incorrect
- Merge me next pointers lose kar dena
- Infinite loop create kar dena

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Interview Tip
- Start me bolo:
  "We solve this in 3 steps:
   find middle, reverse second half, merge both halves"

- Clearly explain pointer changes
- Dry run linked list diagrams ke saath karo
- Reverse linked list confidently explain karo

Simple rule:
"Split → Reverse → Merge"
