# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maximum = float('inf')
        minimum = float('-inf')

        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            left = helper(node.left, low, node.val)
            right = helper(node.right, node.val, high)
            return right and left 

        return helper(root, minimum, maximum)
