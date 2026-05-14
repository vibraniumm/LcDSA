# Problem: Word Break

## Problem Overview
Tumhe ek string s aur ek dictionary wordDict diya gaya hai.

Tumhe check karna hai ki string ko dictionary ke words me break kiya ja sakta hai ya nahi.

Words reuse ho sakte hain.

Return:
- True → agar valid segmentation possible hai
- False → otherwise

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Can we reach the end using valid words? → Dynamic Programming"

---

## Key Observations
- String ko multiple parts me todna hai
- Har substring dictionary me hona chahiye
- Same subproblem baar-baar repeat hoga
- DP perfect fit hai

---

## Approach (Step-by-step soch)
1. wordDict ko set me convert karo
   → fast lookup ke liye

2. DP array banao:
   - dp[i] = True
     → agar s[:i] valid break ho sakta hai

3. Initialize:
   - dp[0] = True
     → empty string valid hai

4. Har position i ke liye:
   - Previous positions j check karo

5. Agar:
   - dp[j] == True
   - aur s[j:i] wordDict me hai

   → dp[i] = True

6. Final answer:
   → dp[len(s)]

---

## Example (Important for memory)

Input:
s = "leetcode"  
wordDict = ["leet","code"]

Step-by-step:

"leet" → valid  
dp[4] = True

"code" → valid from dp[4]  
dp[8] = True

Final:
True

---

## Easy Memory Trick

"Previous valid point se next word check karo"

---

## Pattern Recognition
- Dynamic Programming
- String partitioning
- Prefix checking

---

## Pattern Used
Dynamic Programming (Prefix DP)

---

## Why This Works
- Har position previous valid states par depend karti hai
- DP repeated calculations avoid karta hai
- Prefix-based build efficient hota hai
- End tak reachable hua → valid segmentation

---

## When To Use This Pattern Again
- Jab string partition karni ho
- Jab dictionary-based matching ho
- Jab repeated subproblems ho
- Keywords: "word break", "segmentation", "dictionary"

---

## Common Mistakes
- List instead of set use karna
- dp[0] initialize na karna
- Wrong substring slicing
- Recursion bina memoization use karna

---

## Complexity Analysis
- Time Complexity: O(n²)
- Space Complexity: O(n)

---

## Interview Tip
- Start me bolo: "We use DP where dp[i] means string till i can be segmented"
- Prefix concept clearly explain karo
- Mention karo why set improves lookup
- Ek dry run zaroor karo

Simple rule:
"Valid prefix → extend further"

