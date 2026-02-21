# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        less, greater = left, right
        cur = head

        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next
        
        less.next = right.next
        greater.next = None

        return left.next

