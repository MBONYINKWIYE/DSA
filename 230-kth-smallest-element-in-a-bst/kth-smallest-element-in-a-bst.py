# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.count = 0

        def helper(node, k):
            if not node or self.res:
                return 
            helper(node.left, k)
            self.count += 1
            if self.count == k:
                self.res = node
                return 
            helper(node.right, k)

        helper(root,k)
        return self.res.val