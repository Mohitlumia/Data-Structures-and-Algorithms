from queue import Queue

# Create a queue
q = Queue()

# Enqueue elements
q.put(1)

# Dequeue elements
print(q.get())  # Output: 1

# Check if the queue is empty
print(q.empty())  # Output: True
