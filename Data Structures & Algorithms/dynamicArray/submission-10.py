class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        
        self.arr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        
        return val
 

    def resize(self) -> None:
        self.capacity *= 2

        new_arr = [None] * self.capacity

        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
