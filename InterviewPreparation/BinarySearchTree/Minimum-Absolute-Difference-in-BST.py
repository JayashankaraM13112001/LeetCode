'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = None  # To store the previous node in inorder traversal
        self.min_diff = float('inf')  # Initialize minimum difference

        def inorder(node):
            if not node:
                return
            # Left subtree
            inorder(node.left)

            # Compute min difference with the previous node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update prev node
            
            # Right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff
