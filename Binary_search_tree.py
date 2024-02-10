# binary search tree of BST contains values
# in assending order from its left to right

class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right

# instanse of TreeNode
# defining a binary search tree [5,3,null,4,6,null,7] in Preorder

#            5
#    3               6
#        4               7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
