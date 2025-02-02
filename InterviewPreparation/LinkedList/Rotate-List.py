'''Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head
    
    # Step 1: Calculate the length and form a circular list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    
    current.next = head  # Form a circular list
    
    # Step 2: Find the new tail (length - k % length - 1) and new head (next of new tail)
    k = k % length  # Handle cases where k >= length
    new_tail_position = length - k - 1
    new_tail = head
    
    for _ in range(new_tail_position):
        new_tail = new_tail.next
    
    new_head = new_tail.next
    new_tail.next = None  # Break the circle
    
    return new_head
