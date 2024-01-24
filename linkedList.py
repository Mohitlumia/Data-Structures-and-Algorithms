
class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, root) -> None:
        self.head = root
        self.next = None
        self.tail = None
    
    def add(self,data):
        ptr = self.next
        while ptr:
            ptr = ptr.next
        ptr = Node(data)


