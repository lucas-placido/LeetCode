class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:        
        self.stack.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)        
    
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
    
    def top(self) -> int:
        return self.stack[-1]    

    def getMin(self) -> int:
        return self.min[-1]

obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())