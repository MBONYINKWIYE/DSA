# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = left = right = head
    
        while right and right.next:
            prev = left
            right = right.next.next
            left = left.next
        if not head.next or not head:
            return head.next
        prev.next = left.next         
        return head  