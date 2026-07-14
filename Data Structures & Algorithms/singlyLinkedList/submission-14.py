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

        if curr == None:
            return -1
        
        for _ in range(index):
            print('iteration', _)
            print('curr', curr.val, 'curr.next', curr.next)
            if curr.next != None:
                curr = curr.next
            else:
                return -1
        
        return curr.val

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

        if curr == None:
            return False

        for _ in range(index):
            if curr.next != None:
                prev = curr
                curr = curr.next
            else:
                return False
            
        if curr == self.head:
            self.head = curr.next
        if curr == self.tail:
            prev.tail = None
        if curr is not self.head and curr is not self.tail:
            prev.next = curr.next
        return True



    def getValues(self) -> List[int]:
        curr = self.head
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
