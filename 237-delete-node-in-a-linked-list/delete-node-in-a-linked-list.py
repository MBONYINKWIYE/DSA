# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # If we have to reamin with Memory by changing the val in-place to be equal to next val
        node.val = node.next.val
        #And then we reduce our node llist by one but remain in same order as before
        node.next = node.next.next
       
            
            

        