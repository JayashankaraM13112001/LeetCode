'''Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]'''

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # Store indices for quick lookup
        postorder_index = len(postorder) - 1  # Keeps track of the root in postorder list
        
        def helper(left, right):
            nonlocal postorder_index
            if left > right:
                return None  # No elements to construct the tree
            
            root_val = postorder[postorder_index]  # Pick root from postorder
            postorder_index -= 1
            root = TreeNode(root_val)
            
            # Build right subtree first (since postorder is Left-Right-Root)
            root.right = helper(inorder_map[root_val] + 1, right)
            root.left = helper(left, inorder_map[root_val] - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
