
class binarySearchTree:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right
    
    def add_node(self,data):
        if self.val == data:
            return
        if data < self.val:
            if self.left:
                return self.left.add_node(data)
            else:
                self.left = binarySearchTree(data)
        else:
            if self.right:
                return self.right.add_node(data)
            else:
                self.right = binarySearchTree(data)

               
                
def get_bst(array):
    root = binarySearchTree(array[0])
    for element in array[1:]:
        root.add_node(element)
    return

nums = [9,12,3,4,6,5,7,78,34,34]

bst_root = get_bst(nums)