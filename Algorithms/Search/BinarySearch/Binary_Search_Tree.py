
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
                self.left.add_node(data)
            else:
                self.left = binarySearchTree(data)
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = binarySearchTree(data)
                
    def inorder(self):
        order = []
        if self.left:
            order += self.left.inorder()
        order.append(self.val)
        if self.right:
            order += self.right.inorder()
        return order


nums = [9,12,3,4,6,5,7,78,34,34]

root = binarySearchTree(nums[0])

for element in nums:
   root.add_node(element)

print(root.inorder())
