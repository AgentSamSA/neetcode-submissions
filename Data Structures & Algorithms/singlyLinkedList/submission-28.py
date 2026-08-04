class ListNode:

    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        pos = 0

        while curr:
            if pos == index:
                return curr.val
            curr = curr.next
            pos += 1
        
        return -1
        

    def insertHead(self, val: int) -> None:
        head = ListNode(val)
        head.next = self.head.next
        self.head.next = head

        if not head.next:
            self.tail = head
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head

        for _ in range(index):
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
