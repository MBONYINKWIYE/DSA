# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def dfs(node):
            if not node:
                return (True, float("-inf"), float("inf"), 0)

            is_left_bst, left_max, left_min, left_sum = dfs(node.left)
            is_right_bst, right_max, right_min, right_sum = dfs(node.right)

            if (is_left_bst and is_right_bst and left_max < node.val < right_min):
                curr_sum = right_sum + left_sum + node.val
                self.max_sum = max(self.max_sum, curr_sum)

                return (
                    True,
                    max(right_max, node.val),
                    min(left_min, node.val),
                    curr_sum
                ) 
            else:
                return (False, 0, 0, 0)

        dfs(root)
        return self.max_sum