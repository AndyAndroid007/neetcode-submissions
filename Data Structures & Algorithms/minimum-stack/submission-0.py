class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append((val,val if len(self.stack) == 0 else min(val,self.stack[-1][1])))
        return
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        return
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        
