class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        if len(self.arr) > 0:
            self.arr.append(val)
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.arr.append(val)
            self.minimum.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minimum.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
