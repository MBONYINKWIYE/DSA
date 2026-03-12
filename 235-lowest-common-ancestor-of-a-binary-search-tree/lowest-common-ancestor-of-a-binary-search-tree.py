# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        def helper(node, des1, des2):
            if not node:
                return
            if min(des1.val, des2.val) > node.val:
                return helper(node.right, des1,des2)
            if max(des1.val, des2.val) < node.val:
                return helper(node.left, des1,des2)
            else:
                 return node
           
        return helper(root,p,q)