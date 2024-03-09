
# preorder traversal takes root of a binary tree as an argument
# and print node values in preorder

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return result

# Example usage:
#     1
#    / \
#   2   3
#  / \
# 4   5
# Preorder traversal: [1, 2, 4, 5, 3]

# Constructing the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder Traversal:", preorder_traversal(root))

