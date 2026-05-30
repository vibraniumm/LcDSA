class Solution:
    def sortList(self, head):

        values = []

        current = head

        # Store all node values in a list
        while current is not None:
            values.append(current.val)
            current = current.next

        # Sort the list
        values.sort()

        # Put sorted values back into the linked list
        current = head
        index = 0

        while current is not None:
            current.val = values[index]
            index += 1
            current = current.next

        return head