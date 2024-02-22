
class linkedList:
    def __init__(self,data,next=None):
        self.val = data
        self.next = next
    
    def add(self,data):
        if self.next:
            self.next.add(data)
        else:
            self.next = linkedList(data)
    
    def length(self):
        if self.next:
            return 1 + self.next.length()
        else:
            return 1

    def getList(self):
        if self.next:
            return [self.val] + self.next.getList()
        else:
            return [self.val]
    
    def remove(self,index):
        if index in range(self.length()):
            if index == 0:
                return self.next
            else:
                self.next = self.next.remove(index-1)
                return self
        else:
            raise IndexError("Index out of range")



lis = linkedList(0)

for i in range(1,10):
    lis.add(i)

print(lis.getList()) # get linkedList as a list
print(lis.length()) # get length of linkedList
lis = lis.remove(10) # remove likedList node at index
print(lis.getList())
print(lis.length())
