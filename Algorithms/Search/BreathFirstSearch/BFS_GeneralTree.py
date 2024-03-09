class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []

def bfs(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.val)
        queue.extend(node.children)

    return result

# Example usage:
# Constructing a sample general tree
#         1
#       / | \
#      2  3  4
#     / \   /|\
#    5   6 7 8 9
#               \
#                10
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
root.children[0].children = [TreeNode(5), TreeNode(6)]
root.children[2].children = [TreeNode(7), TreeNode(8), TreeNode(9)]
root.children[2].children[2].children = [TreeNode(10)]

print("BFS Traversal:", bfs(root))
