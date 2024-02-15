
class node:
    def __init__(self,data,next=None):
        self.val = data
        self.next = next


class linkeList:
    def __init__(self,data):
        self.root = node(data)
        self.length = 1
    
    def add(self,data):
        ptr = self.root # initiating pointer
        while ptr.next: # loop until reach last node
            ptr = ptr.next
        ptr.next = node(data)

llist = linkeList(0)
llist.add(1)

print(llist.root.val)
print(llist.root.next.val)
