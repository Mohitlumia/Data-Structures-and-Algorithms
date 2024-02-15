
class binaryTree:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right

    
root = binaryTree(0)

leftchild = binaryTree(1)
rightchild = binaryTree(2)

root.left = leftchild
root.right = rightchild
