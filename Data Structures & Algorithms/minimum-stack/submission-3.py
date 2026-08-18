class MinStack:

    def __init__(self):
        self.values = []
        self.mins = []
    

    def push(self, val: int) -> None:
        if len(self.values) > 0:
            self.values.append(val)
            self.mins.append(min(self.mins[-1], val))
        else:
            self.values.append(val)
            self.mins.append(val)
        

    def pop(self) -> None:
        self.values.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.values[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]