# Problem: Remove Nth Node From End of List

## Problem Overview
Tumhe ek linked list aur ek integer n diya gaya hai.

Tumhe end se nth node remove karna hai aur updated list return karni hai.

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Two pointers ke beech n distance maintain karo"

---

## Key Observations
- End se nth node directly access nahi kar sakte
- Two pointers use karke one-pass solution possible hai
- Dummy node edge cases simplify karta hai
- Fast pointer n steps ahead rahega

---

## Approach (Step-by-step soch)
1. Ek dummy node banao:
   - dummy.next = head

2. Fast aur slow pointers:
   - dono dummy se start karo

3. Fast ko n+1 steps move karo

4. Ab:
   - fast aur slow dono ek saath move karo
   - jab fast null ho jaye

5. Slow nth node ke previous node par hoga

6. Node remove karo:
   - slow.next = slow.next.next

7. Return:
   - dummy.next

---

## Example (Important for memory)

Input:
1 → 2 → 3 → 4 → 5  
n = 2

Step-by-step:

Fast pointer n+1 ahead

Jab fast end par:
slow = 3

Remove:
4

Final:
1 → 2 → 3 → 5

---

## Easy Memory Trick

"Keep gap of n nodes"

---

## Pattern Recognition
- Linked List
- Two pointers
- Fast & Slow pointer

---

## Pattern Used
Two Pointer Technique

---

## Why This Works
- Fast pointer gap maintain karta hai
- Jab fast end par hota hai:
  → slow correct previous node par hota hai
- One-pass efficient solution milta hai
- Dummy node edge cases simplify karta hai

---

## When To Use This Pattern Again
- Jab kth/nth node from end find karna ho
- Jab linked list one-pass solution chahiye ho
- Jab distance maintain karna ho
- Keywords: "from end", "two pointers", "linked list"

---

## Common Mistakes
- Dummy node use na karna
- Fast ko wrong steps move karna
- Head removal case miss karna
- Pointer updates galat karna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---


## Interview Tip
- Start me bolo:
  "We maintain a gap of n nodes between fast and slow pointers"

- Dummy node ka importance explain karo
- One-pass advantage mention karo
- Dry run definitely karo

Simple rule:
"Maintain gap of n"
