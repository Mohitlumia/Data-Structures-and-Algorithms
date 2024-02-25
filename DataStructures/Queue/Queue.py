
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None


# Create a queue
q = Queue()

# Enqueue elements
q.enqueue(1)
q.enqueue(2)

# Dequeue elements
print(q.dequeue())      # Output: 1

# Check if the queue is empty
print(q.is_empty())     # Output: False

# peek element
print(q.peek())         # Output: first element without removing