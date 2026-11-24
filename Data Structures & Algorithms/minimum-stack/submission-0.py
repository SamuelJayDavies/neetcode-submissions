class MinStack:

    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.len += 1

    def pop(self) -> None:
        if self.len != 0:
            self.stack.pop()
            self.len -= 1

    def top(self) -> int:
        if self.len != 0:
            return self.stack[self.len-1]

    def getMin(self) -> int:
        if self.len != 0:
            return min(self.stack)
        
