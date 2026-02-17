# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, palind) -> ListNode:
        prev = None
        cur = right = palind
        while cur:
            new_node = cur.next
            cur.next = prev
            prev = cur
            cur = new_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = left = right = head
        while right and right.next:
            right = right.next.next
            left = left.next

        rev_cur = self.reverseList(left)
        
        while rev_cur:
            if cur.val != rev_cur.val:
                return False

            cur = cur.next
            rev_cur = rev_cur.next
            
        return True
       
