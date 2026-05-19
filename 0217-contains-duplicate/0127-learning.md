# Problem: Contains Duplicate

## Problem Overview
Tumhe ek integer array nums diya gaya hai.

Tumhe check karna hai:
→ kya koi element array me at least 2 baar appear hota hai?

Return:
- True → agar duplicate exist karta hai
- False → agar saare elements unique hain

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Fast duplicate check → Hash Set"

---

## Key Observations
- Duplicate detect karna hai
- Fast lookup chahiye
- Set me unique elements hi store hote hain
- Agar element already set me hai:
  → duplicate mil gaya

---

## Approach (Step-by-step soch)
1. Ek empty set banao

2. Har number traverse karo:
   - Agar number already set me hai:
     → return True

3. Otherwise:
   - number ko set me add karo

4. Loop end ho gaya:
   → return False

---


