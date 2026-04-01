# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Merging two splited linked list to make it sorted in ascending order
    def merge(self, tortoise, rabbit):
        temp = ListNode()
        cur = temp 

        while rabbit and tortoise:
            if rabbit.val > tortoise.val:
                cur.next = tortoise
                tortoise =  tortoise.next
            else:
                cur.next = rabbit
                rabbit = rabbit.next
            cur = cur.next
        if rabbit:
            cur.next = rabbit
        elif tortoise:
            cur.next = tortoise
        
        return temp.next

    # Splitting the linked list in half to compare with it in the next function
    def sortList(self, head: Optional[ListNode])-> Optional[ListNode]: 
        if not head or not head.next:
            return head
            
        fast = slow = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None 

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right) 



          

