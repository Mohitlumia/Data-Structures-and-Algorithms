
class binarySearchTree:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right
        
    def add_child(self,data):
        if self.val == data:
            return
        
        if data < self.val:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binarySearchTree(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binarySearchTree(data)
                
    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        # visit base node
        elements.append(self.val)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def find_min(self):
        if self.left:
            min = self.left.find_min()
        else:
            min = self.val
        return min
    
    def find_max(self):
        if self.right:
            max = self.right.find_max()
        else:
            max = self.val
        return max


# helper function to build BST
def buld_BST(elements):
    root = binarySearchTree(elements[0])
    
    for element in elements:
        root.add_child(element)
    
    return root


# list of numbers
nums = [9,12,3,4,6,5,7,78,34,34]

# Build BST from list nums
root = buld_BST(nums)

# Output sorted list
print(root.in_order_traversal())

# Output the minimun and maximum values in BST
print(f"{root.find_min()} and {root.find_max()} is minimum and maximum value in the given BST respectively")
