'''Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Get left and right subtree heights
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height == right_height:
            # Left subtree is perfect: 2^left_height - 1 nodes + root + right subtree count
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect: 2^right_height - 1 nodes + root + left subtree count
            return (1 << right_height) + self.countNodes(root.left)

    def getHeight(self, node):
        """Returns height of the leftmost path in the tree."""
        height = 0
        while node:
            height += 1
            node = node.left
        return height
