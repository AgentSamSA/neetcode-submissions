class MinStack:

    def __init__(self):
        self.arr = []
        self.minimums = []
        

    def push(self, val: int) -> None:
        if len(self.arr) > 0:
            self.arr.append(val)
            self.minimums.append(min(val, self.minimums[-1]))
        else:
            self.arr.append(val)
            self.minimums.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.minimums.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
