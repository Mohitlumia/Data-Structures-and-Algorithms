class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(root):
    """
    DFS in general tree has linear time and linear space complexity.
    
    Time Complexity:    O(v + e), where "v" is the number of vertices and "e" is the number of edges in the tree.
    Space Complexity:   O(h), where "h" is the height of the tree.
    """
    if root is None:
        return
    
    # Initialize an empty stack for DFS traversal
    stack = []
    # Push the root node onto the stack
    stack.append(root)
    
    # Continue traversal until the stack is empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()
        # Visit the popped node
        print(node.value, end=' ')
        
        # Push children of the popped node onto the stack in reverse order
        for child in reversed(node.children):
            stack.append(child)

# Example usage:
# Constructing a general tree
#         1
#       / | \
#      2  3  4
#     / \
#    5   6

root = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)
child4 = TreeNode(4)
child5 = TreeNode(5)
child6 = TreeNode(6)

root.children = [child2, child3, child4]
child2.children = [child5, child6]

# Calling DFS on the tree
print("DFS traversal:")
dfs(root)
