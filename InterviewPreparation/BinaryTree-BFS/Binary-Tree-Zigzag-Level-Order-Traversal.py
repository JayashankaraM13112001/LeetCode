'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        q = deque([root])
        reverse = True

        while q:
            new_q = deque()
            level = []
            for node in q:
                level.append(node.val)
                if reverse:
                    if node.left:
                        new_q.appendleft(node.left)
                    if node.right:
                        new_q.appendleft(node.right)
                else:
                    if node.right:
                        new_q.appendleft(node.right)
                    if node.left:
                        new_q.appendleft(node.left)
            
            res.append(level)
            q = new_q
            reverse = not reverse
        
        return res