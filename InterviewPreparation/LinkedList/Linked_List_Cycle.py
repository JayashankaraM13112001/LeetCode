'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next        # Move slow pointer by 1 step
        fast = fast.next.next   # Move fast pointer by 2 steps
        if slow == fast:
            return True  # Cycle detected
    return False  # No cycle
