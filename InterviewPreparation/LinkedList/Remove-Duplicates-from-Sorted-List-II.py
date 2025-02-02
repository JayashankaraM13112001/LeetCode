'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy = ListNode(0)  # Dummy node before head
    dummy.next = head
    prev = dummy  # Pointer to track non-duplicate nodes
    
    while head:
        # If we find a duplicate sequence
        if head.next and head.val == head.next.val:
            # Skip all duplicates
            while head.next and head.val == head.next.val:
                head = head.next
            # Link prev to the next unique node
            prev.next = head.next
        else:
            prev = prev.next  # Move prev forward only if no duplicate

        head = head.next  # Move forward

    return dummy.next  # Return new head
