
class stack:
    def __init__(self,data):
        self.stack = [data]
    
    def push(self,data):
        self.stack.append(data)
    
    def pull(self,data):
        self.stack.pop()

s = stack(0)
s.push(1)
s.pull()