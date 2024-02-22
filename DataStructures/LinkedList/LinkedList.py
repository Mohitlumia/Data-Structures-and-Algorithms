
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



lis = linkedList(0)
lis.add(1)
print(lis.getList())
print(lis.length())
