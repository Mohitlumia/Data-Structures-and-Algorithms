
# dfs in a binary tree is identical to inorder traversal

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root):
    """
    DFS in binary tree has linear time and linear space complexity.
    
    Time Complexity:    O(n), where "n" is the number of nodes in the binary tree.
    Space Complexity:   O(h), where "h" is the height of the binary tree, and in the worst case "h = n" for a skewed binary tree..
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
        
        # Push the right child onto the stack first
        if node.right:
            stack.append(node.right)
        # Push the left child onto the stack
        if node.left:
            stack.append(node.left)

# Example usage:
# Constructing a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calling DFS on the tree
print("DFS traversal:")
dfs(root)
