'''Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    # Step 1: Move fast pointer `n+1` steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Step 2: Move both fast and slow until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Step 3: Remove the nth node
    slow.next = slow.next.next

    return dummy.next  # Return new head
