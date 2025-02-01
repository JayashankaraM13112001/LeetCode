'''Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head  # No need to reverse if only one element

    dummy = ListNode(0)  # Dummy node to simplify edge cases
    dummy.next = head
    prev = dummy

    # Step 1: Move prev to node before left
    for _ in range(left - 1):
        prev = prev.next

    # Step 2: Reverse the sublist from left to right
    current = prev.next
    next_node = None
    for _ in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next  # Return the modified list
