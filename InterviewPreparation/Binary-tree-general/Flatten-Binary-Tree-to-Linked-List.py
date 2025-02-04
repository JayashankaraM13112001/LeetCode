'''Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        self.prev = None  # Initialize a previous pointer
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)  # Process right subtree first
            dfs(node.left)   # Then left subtree
            
            node.right = self.prev  # Connect right pointer
            node.left = None        # Set left child to None
            self.prev = node        # Move prev pointer
        
        dfs(root)
