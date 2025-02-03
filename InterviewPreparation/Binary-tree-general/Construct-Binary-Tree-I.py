'''Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]'''

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # Store indices for quick lookup
        preorder_index = 0  # Keeps track of the root in preorder list
        
        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None  # No elements to construct the tree
            
            root_val = preorder[preorder_index]  # Pick root from preorder
            preorder_index += 1
            root = TreeNode(root_val)
            
            root.left = helper(left, inorder_map[root_val] - 1)  # Build left subtree
            root.right = helper(inorder_map[root_val] + 1, right)  # Build right subtree
            
            return root
        
        return helper(0, len(inorder) - 1)
