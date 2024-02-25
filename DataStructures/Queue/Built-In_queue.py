from queue import Queue

# Inherit Queue and add peek method
class MyQueue(Queue):
    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.empty():
            return self.queue[0]
        else:
            print("Queue is empty")
            return None
          

# Create a queue
q = MyQueue()

# Enqueue elements
q.put(1)

# Dequeue elements
print(q.get())  # Output: 1

# Check if the queue is empty
print(q.empty())  # Output: True

# peek element
print(q.peek())
