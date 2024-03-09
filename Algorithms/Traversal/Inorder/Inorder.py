
# inorder traversal takes root of a binary tree as an argument
# and print node values in inorder

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root is None:
        return []
    stack = []
    result = []
    current = root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            result.append(current.val)
            current = current.right
        else:
            break
    return result

# Example usage:
#     1
#    / \
#   2   3
#  / \
# 4   5
# Inorder traversal: [4, 2, 5, 1, 3]

# Constructing the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:", inorder_traversal(root))
