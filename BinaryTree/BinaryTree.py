
class node:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right

class binaryTree:
    def __init__(self,root):
        self.root = root

    
root = node(0)
root.left = node(1)
root.right = node(2)

bt = binaryTree(root)
