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

## Example (Important for memory)

Input:
nums = [1,2,3,1]

Step-by-step:

1 → add  
2 → add  
3 → add  
1 → already exists

Final:
True

---

## Easy Memory Trick

"Seen before? → duplicate"

---

## Pattern Recognition
- Hashing
- Duplicate detection
- Set lookup

---

## Pattern Used
Hash Set

---

## Why This Works
- Set lookup O(1) hota hai
- Har element ek baar check hota hai
- Duplicate instantly detect ho jata hai
- Efficient linear solution milta hai

---

## When To Use This Pattern Again
- Jab duplicates detect karne ho
- Jab uniqueness check karna ho
- Jab fast lookup required ho
- Keywords: "duplicate", "distinct", "repeated"

---

## Common Mistakes
- List use karna instead of set
- Sorting unnecessarily karna
- Duplicate milne ke baad bhi continue karna
- Space complexity ignore karna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Interview Tip
- Start me bolo: "We use a hash set for O(1) duplicate checking"
- Mention karo why set is ideal
- Alternative sorting approach briefly bata sakte ho
- Quick dry run karo

Simple rule:
"Use set to track seen elements"

