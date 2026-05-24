# Problem: Valid Palindrome

## Problem Overview
Tumhe ek string s diya gaya hai.

Tumhe check karna hai:
→ string palindrome hai ya nahi

Rules:
- Uppercase ko lowercase treat karo
- Non-alphanumeric characters ignore karo

Palindrome:
→ forward aur backward same read ho

---

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"Two pointers from both ends"

---

## Key Observations
- Special characters ignore karne hain
- Case-insensitive comparison karna hai
- Left aur right se compare kar sakte hain
- Extra string banana optional hai

---

## Approach (Step-by-step soch)
1. Two pointers lo:
   - left = 0
   - right = len(s) - 1

2. Jab tak left < right:

3. Non-alphanumeric characters skip karo:
   - left++
   - right--

4. Characters lowercase me compare karo:
   - Agar mismatch:
     → return False

5. Match:
   - left++
   - right--

6. Loop complete:
   → return True

---

## Example (Important for memory)

Input:
"A man, a plan, a canal: Panama"

Processed comparison:

a == a  
m == m  
a == a  
...

Sab match hue

Final:
True

---

## Easy Memory Trick

"Ignore special chars, compare both ends"

---

## Pattern Recognition
- Two pointers
- String processing
- Palindrome check

---

## Pattern Used
Two Pointer Technique

---

## Why This Works
- Palindrome symmetric hota hai
- Two pointers efficiently symmetry check karte hain
- Invalid characters skip kar sakte hain
- O(n) me solution milta hai

---

## When To Use This Pattern Again
- Jab palindrome check karna ho
- Jab string symmetry ho
- Jab opposite-end comparison ho
- Keywords: "palindrome", "two ends", "mirror"

---

## Common Mistakes
- Special characters ignore na karna
- Lowercase conversion bhool jana
- Pointer update galat karna
- Empty string edge case miss karna

---

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Interview Tip
- Start me bolo: "We use two pointers from both ends"
- Explain karo invalid character skipping
- Mention karo in-place comparison ho raha hai
- Dry run quickly karo

Simple rule:
"Skip invalid, compare ends"

---

## Solution (Python)

```python
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
143. Reorder List
Medium
Topics
premium lock icon
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
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



