# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):

        def helper(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1

            left = float('inf')
            right = float('inf')

            if node.left:
                left = 1 + helper(node.left)

            if node.right:
                right = 1 + helper(node.right)

            return min(left, right)
        return helper(root)