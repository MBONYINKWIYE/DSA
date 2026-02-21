class ListNode:
    def __init__(self, val):
        self.val = val  # FIXED: Assign the actual value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        cur = self.head
        cnt = 0
        while cur:
            if cnt == index:
                return cur.val
            cur = cur.next
            cnt += 1
        return -1 

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        
        new_node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next 
        cur.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return
        
        new_node = ListNode(val)
        cur = self.head
        cnt = 0
        while cur:
            if cnt == (index - 1):
                new_node.next = cur.next
                cur.next = new_node
            cur = cur.next
            cnt += 1
    def deleteAtIndex(self, index: int) -> None:
        if not self.head or index < 0:
            return
        
        if index == 0:
            self.head = self.head.next
            return
            
        cur = self.head
        cnt = 0
        while cur and cur.next:
            if cnt == (index - 1):
                cur.next = cur.next.next
            cur = cur.next
            cnt += 1
    
            