class Solution:
    def deleteDuplicates(self, head):

        count = {}

        temp = head

        # Count frequencies
        while temp:
            if temp.val in count:
                count[temp.val] += 1
            else:
                count[temp.val] = 1

            temp = temp.next

        dummy = ListNode(0)
        current = dummy

        temp = head

        # Add only unique values
        while temp:

            if count[temp.val] == 1:
                current.next = ListNode(temp.val)
                current = current.next

            temp = temp.next

        return dummy.next