'''Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Create two dummy heads for two separate lists
    less_head = ListNode(0)
    greater_head = ListNode(0)
    
    less = less_head  # Pointer to track "less than x" list
    greater = greater_head  # Pointer to track "greater or equal to x" list
    
    # Traverse the linked list
    current = head
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next
    
    # Connect the two lists
    greater.next = None  # Ensure the last node of the greater list points to None
    less.next = greater_head.next  # Merge the two lists
    
    return less_head.next  # Return the head of the new partitioned list
