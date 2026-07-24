# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            # Save next node
            temp = second.next

            # Swap
            second.next = first
            first.next = temp

            # Connect with previous part
            prev.next = second

            # Move prev
            prev = first

        return dummy.next