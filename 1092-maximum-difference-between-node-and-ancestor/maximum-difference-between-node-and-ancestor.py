# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def helper(node, stack, diff):
            if not node:
                return diff

            stack.append(node.val)
            diff = helper(node.left, stack, diff)
            diff = helper(node.right, stack, diff)

            if not node.left and not node.right:
                diff = max(diff, max(stack) - min(stack))

            stack.pop()
            return diff

        return helper(root,[], 0)
       
    