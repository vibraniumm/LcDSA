# Problem: Gas Station

## Problem Overview
Tumhe 2 arrays diye gaye hain:
- gas[i] → ith station par available gas
- cost[i] → ith station se next station tak jane ka cost

Tumhe aisa starting index find karna hai jahan se poora circular route complete ho sake.

Agar possible nahi hai → return -1

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Greedy approach use karo → invalid start ko skip karo"

---

## Key Observations
- Agar total gas < total cost:
  → impossible hai

- Agar kisi point par tank negative ho gaya:
  → usse pehle ke kisi bhi station se start nahi kar sakte

- Isliye next station ko new start bana do

---

## Approach (Step-by-step soch)
1. Check karo:
   - sum(gas) < sum(cost)
   → return -1

2. Variables:
   - tank = current fuel
   - start = possible answer

3. Traverse all stations:
   - tank += gas[i] - cost[i]

4. Agar tank < 0:
   - current path fail
   - start = i + 1
   - tank = 0

5. End me:
   - start return karo

---

## Example (Important for memory)

Input:
gas  = [1,2,3,4,5]  
cost = [3,4,5,1,2]

Difference:
[-2,-2,-2,+3,+3]

Step-by-step:

Start = 0  
tank negative → fail

Start = 1  
tank negative → fail

Start = 2  
tank negative → fail

Start = 3  
tank stays positive till complete cycle

Final:
3

---

## Easy Memory Trick

"Negative tank means previous starts are impossible"

---

## Pattern Recognition
- Greedy
- Circular traversal
- Prefix sum logic

---

## Pattern Used
Greedy

---

## Why This Works
- Agar A se B tak nahi pahunch sakte:
  → A aur beech ke kisi station se bhi nahi pahunchoge
- Isliye directly next station try karte hain
- Single traversal me answer mil jata hai

---

## When To Use This Pattern Again
- Jab local failure future decisions affect kare
- Jab optimal choice greedily possible ho
- Circular route problems
- Keywords: "circular", "complete route", "gas", "minimum valid start"

---



