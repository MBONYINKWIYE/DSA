# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val = val)
            return root
        def search(node, num):
            if not node:
                return 
            if num < node.val:
                if not node.left:
                    node.left = TreeNode(val = num)
        
                return search(node.left, num)
            if num > node.val:
                if not node.right:
                    node.right = TreeNode(val = num)
                return search(node.right, num) 
        search(root, val)
        return root