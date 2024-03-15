
# bfs in binary tree iterate level by level from left to right

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def bfs(root):
    """
    BFS in binary tree has linear time and linear space complexity.
    
    Time Complexity:    O(n), where "n" is the number of nodes in the binary tree.
    Space Complexity:   O(w), where "w" is the maximum width (maximum number of nodes at any level) of the binary tree.
    """
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Example usage:
# Constructing a sample binary tree
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#            \
#             8
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

print("BFS Traversal:", bfs(root))
