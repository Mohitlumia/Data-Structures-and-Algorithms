
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
    
    def delete(self,node_val):
        if node_val < self.val:
            if self.left:
                self.left.delete(node_val)
        elif node_val > self.val:
            if self.right:
                self.right.delete(node_val)
        else:
            pass



nums = [9,12,3,4,6,5,7,78,34,34]

root = binarySearchTree(nums[0])

for element in nums:
   root.add_node(element)

print(root.inorder())
print(f"{root.find_min()} and {root.find_max()} is minimum and maximum value in the given BST respectively")

