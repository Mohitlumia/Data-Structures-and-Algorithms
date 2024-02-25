from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


# Create a stack
s = Stack()

# Push elements
s.push(1)
s.push(2)

# Pop elements
print(s.pop())          # Output: 1

# Check if the stack is empty
print(s.is_empty())     # Output: False

# peek element
print(s.peek())         # Output: first element without removing
