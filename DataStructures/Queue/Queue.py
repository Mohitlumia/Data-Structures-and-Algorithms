
class queue:
    def __int__(self,data):
        self.queue = [data]
    
    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        self.queue.pop(0)


q = queue(0)
q.enqueue(1)
q.dequeue()
