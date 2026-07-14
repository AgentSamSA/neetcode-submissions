class ListNode:
    
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        pos = 0

        if curr == None:
            return -1
        
        while curr:
            if pos == index:
                return curr.val
            pos += 1
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val)

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        

    def remove(self, index: int) -> bool:
        curr = self.head
        prev = self.head
        pos = 0

        if curr == None:
            return False

        while curr:
            if pos == index:
                if curr == self.head:
                    self.head = curr.next
                if curr == self.tail:
                    prev.tail = None
                if curr is not self.head and curr is not self.tail:
                    prev.next = curr.next
                return True
            pos += 1
            prev = curr
            curr = curr.next
        
        return False



    def getValues(self) -> List[int]:
        curr = self.head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
