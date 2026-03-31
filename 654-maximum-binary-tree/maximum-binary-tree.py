# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(subarr):
            if not subarr:
                return 
            idx = subarr.index(max(subarr))    
            prefix = subarr[:idx]
            suffix = subarr[idx + 1:]

            node = TreeNode(val = max(subarr), left = helper(prefix), right = helper(suffix))
            
            return node
            
        return helper(nums)
