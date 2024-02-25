
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
    
    def addIndex(self,data,index=0):
        if index in range(self.length()):
            if index == 0:
                new = linkedList(data,self)
                return new
            else:
                self.next = self.next.addIndex(data,index-1)
                return self
        else:
            raise IndexError("Index out of range")



# Create linkedList object
lis = linkedList(0)

# add nodes to the object
for i in range(1,10):
    lis.add(i)


print(lis.getList())    # get linkedList as a list
print(lis.length())     # get length of linkedList
lis.remove(1)           # remove likedList node of the given index
lis.addIndex(100,1)     # add value at the given index
print(lis.getList())
print(lis.length())