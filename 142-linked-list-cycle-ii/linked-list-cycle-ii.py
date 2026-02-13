# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = right = left = head 

        while right and right.next:
            prev = right.next
            right = right.next.next
            left = left. next

            if left == right:
                left = head
                break
        else:
            return
        while right != left:
            right = right.next
            left = left.next
        return left 



            

