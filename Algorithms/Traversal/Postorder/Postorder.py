
# postorder traversal takes root of a binary tree as an argument
# and print node values in postorder

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def postorder_traversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        current = stack.pop()
        result.append(current.val)
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return result[::-1]

# Example usage:
#     1
#    / \
#   2   3
#  / \
# 4   5
# Postorder traversal: [4, 5, 2, 3, 1]

# Constructing the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Postorder Traversal:", postorder_traversal(root))
