## ⭐ Problem Overview

Tumhe ek sorted array diya gaya hai. Tumhe duplicates remove karne hain **in-place**, taki har unique element sirf ek baar aaye.

Return karo `k = number of unique elements`.

---

## 💡 Core Idea

Is problem ko dekhte hi yeh sochna chahiye:

> **"Sorted array hai → duplicates adjacent honge → mujhe unhe skip karna hai"**

---

## 🔍 Key Observations

- Array already sorted hai  
- Duplicate elements hamesha side-by-side honge  
- In-place modification karna hai (extra space nahi lena)

---

## ⚙️ Approach (Step-by-step soch)

1. Do pointers use karo:
   - `i` → slow pointer (unique elements ka position)
   - `j` → fast pointer (array traverse karega)

2. Start me:
   - `i = 0`

3. `j` ko `1` se start karo

4. Har step pe:
   - Agar `nums[j] != nums[i]`
     - `i++`
     - `nums[i] = nums[j]`

5. End me:
   - Return `i + 1` (unique elements count)

---

## 🧠 Example (Important for memory)

### Input

nums = [1,1,2,2,3]
Step-by-step
- Start: `i = 0`  
- `j = 1` → duplicate → skip  
- `j = 2` → new element → `i = 1` → `nums[1] = 2`  
- `j = 3` → duplicate → skip  
- `j = 4` → new element → `i = 2` → `nums[2] = 3`  

### Final array

[1,2,3,...]
Return 
3


---

## 🧩 Easy Memory Trick

> **"Sorted array + duplicates = two pointers se unique elements shift karo"**

---

## 🔄 Pattern Recognition

- Two pointers  
- In-place array modification  
- Sorted array optimization  

---

## 🧠 Pattern Used

**Two Pointer Technique (Slow & Fast Pointer)**

---

## ✅ Why This Works

- Sorted hone ki wajah se duplicates ek saath grouped hote hain  
- Fast pointer new elements find karta hai  
- Slow pointer unhe correct position par place karta hai  
- Isse extra space ki zarurat nahi padti  

---

## 📌 When To Use This Pattern Again

- Jab array sorted ho aur duplicates handle karne ho  
- Jab in-place modification required ho  
- Jab relative order maintain karna ho  

**Keywords:**  
`remove duplicates`, `sorted array`, `in-place`

---

## ⚠️ Common Mistakes

- ❌ New array banana (allowed nahi hai)  
- ❌ `i` pointer ko sahi update na karna  
- ❌ Return value galat dena (`i` instead of `i+1`)  

---

## 📊 Complexity Analysis

- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(1)`  

---

## 🎯 Interview Tip

- Start me bolo:
  > "Since array sorted hai, duplicates adjacent honge, so we use two pointers"

- Clearly explain karo slow-fast pointer ka role  
- In-place condition highlight karo  
- End me ek quick dry run kar do  

---

## 🔑 Simple Rule

> **"Sorted array + duplicates = two pointers"**
