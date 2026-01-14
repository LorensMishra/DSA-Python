class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    def peek(self):
        return self.stack[-1] if self.stack else None

