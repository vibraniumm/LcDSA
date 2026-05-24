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

