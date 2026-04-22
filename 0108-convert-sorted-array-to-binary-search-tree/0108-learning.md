# Problem: Convert Sorted Array to Binary Search Tree

## Problem Overview
Tumhe ek sorted array nums diya gaya hai (ascending order me).

Tumhe ise ek height-balanced Binary Search Tree (BST) me convert karna hai.

## Core Idea
Is problem ko dekhte hi yeh sochna chahiye:

"BST banani hai → middle element root hoga"

## Key Observations
- BST me:
  - left < root < right
- Sorted array already BST order follow karta hai
- Balanced tree ke liye:
  - middle element root hona chahiye
- Left part → left subtree
- Right part → right subtree

## Approach (Step-by-step soch)
1. Middle element find karo:
   - mid = (left + right) // 2

2. Root node banao using nums[mid]

3. Recursively:
   - left subtree = nums[left to mid-1]
   - right subtree = nums[mid+1 to right]

4. Base case:
   - Agar left > right → return None

## Example (Important for memory)

Input:
nums = [-10,-3,0,5,9]

Step-by-step:

mid = 0 → root  

Left:
[-10,-3] → mid = -3  

Right:
[5,9] → mid = 9  

Tree structure:

        0
      /   \
    -3     9
   /      /
 -10     5

## Easy Memory Trick

"Sorted array → middle ko root banao → divide & conquer"

## Pattern Recognition
- Recursion
- Divide and Conquer
- Tree construction

## Pattern Used
Divide and Conquer (Build Tree from Sorted Array)

## Why This Works
- Middle element lene se tree balanced rehta hai
- Left side automatically smaller values deta hai
- Right side larger values deta hai
- Recursion se pura tree build ho jata hai

## When To Use This Pattern Again
- Jab sorted data se tree banana ho
- Jab balanced BST banana ho
- Jab problem divide ho sakti ho subproblems me
- Keywords: "sorted array to BST", "balanced tree", "recursion"

## Common Mistakes
- Middle element na lena (tree unbalanced ho jayega)
- Base case miss karna
- Indices galat pass karna
- Infinite recursion

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(log n) (recursion stack)

## Interview Tip
- Start me bolo: "We use divide and conquer by picking middle element as root"
- Explain karo ki kyun middle se balanced tree banta hai
- Recursive breakdown clearly batao
- Ek small example dry run karo

Simple rule:
"Middle = root, left = left subtree, right = right subtree"
