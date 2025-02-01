'''Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 '''

 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    if not head or k == 1:
        return head  # No need to reverse if k is 1

    # Step 1: Count the total number of nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    current = head

    # Step 2: Reverse in groups of k
    while count >= k:
        prev = None
        tail = current
        for _ in range(k):  # Reverse k nodes
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Connect the reversed group
        prev_group_end.next = prev
        tail.next = current
        prev_group_end = tail

        # Reduce count by k
        count -= k

    return dummy.next  # Return new head
