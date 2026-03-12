# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
      
        def findMin(node):
            while node.left:
                node = node.left
            return node
            
        def dfs(node, k):
            if not node:
                return None
            if k < node.val:
                node.left = dfs(node.left, k)
            elif k > node.val:
                node.right = dfs(node.right, k)
            else:
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                
                successor = findMin(node.right)
                node.val = successor.val

                node.right = dfs(node.right, successor.val)

            return node
        return dfs(root, key)
        