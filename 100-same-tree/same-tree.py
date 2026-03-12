# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(tr1, tr2):
            if not tr1 or not tr2:
                return tr1 == tr2
            left = helper(tr1.left, tr2.left)
            right = helper(tr1.right, tr2.right)
            return tr1.val == tr2.val and left and right 
        return helper(p,q)