# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        print(root)
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            # We need to go farthest node and get max-depth for each node from right and left 
            res = max(dfs(node.left),dfs(node.right)) 
           
            return  res + 1 #we Add one on max depth to include current node
        
        return dfs(root)