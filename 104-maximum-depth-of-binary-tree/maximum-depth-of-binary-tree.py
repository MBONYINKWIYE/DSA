# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 1)]
        while root and stack:
            node, c = stack.pop()
            if node:
                stack.append((node.left, c+1))
                stack.append((node.right, c +1))

                max_depth = max(max_depth, c)
            # print(stack)
        return max_depth