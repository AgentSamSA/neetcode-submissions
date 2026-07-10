class Node:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr_index = 0
        curr = self.head.next

        while curr:
            if curr_index == index:
                return curr.val
            curr_index += 1
            curr = curr.next
        
        return -1
        

    def insertHead(self, val: int) -> None:
        head = Node(val)
        head.next = self.head.next
        self.head.next = head

        if not head.next:
            self.tail = head
        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next


    def remove(self, index: int) -> bool:
        curr_index = 0
        curr = self.head

        while curr_index < index and curr:
            curr_index += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

            return True

        return False
        

    def getValues(self) -> List[int]:
        values = []

        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next
        
        return values
        
