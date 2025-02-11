'''Given the head of a linked list, return the list after sorting it in ascending order.
Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # Base case: empty list or single node is already sorted

        # Step 1: Split the list into two halves
        slow, fast = head, head.next  # Use slow & fast pointers to find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next  # Midpoint of the list
        slow.next = None  # Split the list into two halves

        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge two sorted halves
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the remaining nodes
        tail.next = l1 or l2
        return dummy.next
