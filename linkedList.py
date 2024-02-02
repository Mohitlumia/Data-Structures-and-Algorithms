
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class linkedList:
    def __init__(self, root) -> None:
        self.head = Node(root)
    
    def add(self,data):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(data)

    def getLength(self):
        length = 1
        ptr = self.head
        while ptr.next:
            length += 1
            ptr = ptr.next
        return length
    
    def getNode(self,k):
        if k > self.getLength() or k <= 0:
            raise IndexError("k is greater than length of lindeList")
        
        ptr = self.head
        for i in range(k-1):
            ptr = ptr.next
        return ptr
    
    def removeNode(self,k):
        if k > self.getLength() or k <= 0:
            raise IndexError("k is greater than length of lindeList")
        
        prev = None
        ptr = self.head
        for i in range(k-1):
            prev = ptr
            ptr = ptr.next
        
        if prev:
            prev.next = ptr.next
            return prev
        else:
            return ptr.next



lis = linkedList("one")
lis.add("two")
lis.add("three")

print(lis.getLength())

lis.removeNode(2)
print(lis.getLength())
print(lis.getNode(2).val)



