
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
    
    def getKthNode(self,k):
        if k > self.getLength():
            raise IndexError("k is greater than length of lindeList")
        
        ptr = self.head
        for i in range(k-1):
            ptr = ptr.next
        return ptr

lis = linkedList("one")
lis.add("two")
lis.add("three")
print(lis.getLength())
kthNode = lis.getKthNode(2)
print(kthNode.val)
anotherKthNode = lis.getKthNode(4)
print(anotherKthNode.val)

