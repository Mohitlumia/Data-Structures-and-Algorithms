# BFS stands for breadth first search

class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right

# instanse of TreeNode
# defining a binary search tree [1,2,null,3,4,null,5] in Preorder
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.right = TreeNode(3)
root.right.right = TreeNode(5)

# BFS uses queue
class queue:
    def __init__(self,data):
        self.Queue = [data]
    
    def enqueue(self,input):
        self.Queue.append(input)
    
    def dequeue(self):
        output = self.Queue.pop(0)
        return output

# creating queue instance with root
bfs = queue(root)

values = [] # contains values

while bfs.Queue: # loop until it contains any node
    
    first = bfs.dequeue()
    values.append(first.val)

    if first.left:
        bfs.enqueue(first.left)
    if first.right:
        bfs.enqueue(first.right)

# [1,2,4,3,5] can be seen as it go for breadth first
print(values)

