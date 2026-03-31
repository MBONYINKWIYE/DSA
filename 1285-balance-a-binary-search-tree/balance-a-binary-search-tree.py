# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        listnode = []
        def dfs(node):
            if not node:
                return 
            listnode.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        listnode.sort()

        def helper(left, right):
            if left > right:
                return 
            mid = (left + right) // 2

            node = TreeNode(val = listnode[mid], left = helper(left, mid -1), right = helper(mid + 1, right))
            return node
        return helper(0, len(listnode) - 1)

