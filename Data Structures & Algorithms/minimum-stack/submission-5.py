class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            self.min_val = val
            return
        self.min_val = min(self.stack[-1][1], val)
        self.stack.append((val, self.min_val))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
