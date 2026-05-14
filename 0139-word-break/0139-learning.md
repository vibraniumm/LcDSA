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


