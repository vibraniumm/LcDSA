class Solution:
    def partition(self, head, x):

        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        smaller = smaller_dummy
        greater = greater_dummy

        current = head

        while current:

            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                greater.next = current
                greater = greater.next

            current = current.next

        greater.next = None

        smaller.next = greater_dummy.next

        return smaller_dummy.next