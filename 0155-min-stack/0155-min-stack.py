class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if val is not None:
            if len(self.stack) == 0:
                self.stack.append((val, val))
                return None
            minimum = self.getMin()
            if val < minimum:
                self.stack.append((val, val))
            else:
                self.stack.append((val, minimum))
            return None

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        val = self.stack.pop()
        return val[0]

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()