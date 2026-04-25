
# Problem: Next Permutation

## Problem Overview
Tumhe ek array nums diya gaya hai jo ek permutation represent karta hai.

Tumhe iska next lexicographically greater permutation find karna hai.

Agar possible nahi hai → smallest permutation (sorted ascending) return karo.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Mujhe right side se first decreasing point find karna hai"

## Key Observations
- Right side ka part usually descending hota hai
- Hume smallest bigger permutation banana hai
- Minimum change karna hai (just next permutation)
- End ka part reverse karna hota hai

## Approach (Step-by-step soch)
1. Right se first decreasing element find karo:
   - i aisa jahan nums[i] < nums[i+1]

2. Agar aisa i nahi mila:
   → pura array descending hai
   → reverse entire array

3. Right se element find karo jo nums[i] se bada ho:
   - j aisa jahan nums[j] > nums[i]

4. Swap nums[i] aur nums[j]

5. nums[i+1:] ko reverse karo

## Example (Important for memory)

Input:
nums = [1,2,3]

Step-by-step:

i = 1 (2 < 3)  
j = 2 (3 > 2)  

Swap:
[1,3,2]

Reverse after i:
(no change)

Final:
[1,3,2]

Example 2:

[3,2,1] → no i → reverse → [1,2,3]

## Easy Memory Trick

"Find dip → swap → reverse tail"

## Pattern Recognition
- Array manipulation
- Greedy
- Lexicographical ordering

## Pattern Used
Greedy + Reverse Suffix

## Why This Works
- Right side descending part sabse bada permutation hota hai
- Swap karke next greater permutation banate hain
- Reverse suffix se smallest arrangement ensure hota hai
- Minimum change me next permutation milta hai

## When To Use This Pattern Again
- Jab permutations ka next sequence chahiye ho
- Jab lexicographical order ka concept ho
- Jab minimal change required ho
- Keywords: "next permutation", "lexicographical order"

## Common Mistakes
- i galat find karna
- j galat choose karna
- suffix reverse na karna
- pura array sort kar dena (wrong)

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

## Interview Tip
- Start me bolo: "We find the first decreasing element from right"
- Clearly explain karo swap + reverse logic
- Mention karo descending case (reverse whole array)
- Ek dry run zaroor karo

Simple rule:
"Dip → Swap → Reverse"
