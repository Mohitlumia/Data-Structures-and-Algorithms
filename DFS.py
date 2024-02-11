# DFS stands for depth first search
# unlike it uses stack insted of a queue

class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.val = data
        self.left = left
        self.right = right

# instanse of TreeNode
# defining a binary search tree [1,2,null,3,4,null,5] in Preorder
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.right = TreeNode(3)
root.right.right = TreeNode(5)


dfs_values = []

def dfs(node):
    
    if not node:
        return
    dfs_values.append(node.val)
    if node.left:
        dfs(node.left)

    if node.right:
        dfs(node.right)

    return


dfs(root)

# [1,2,3,4,5]
print(dfs_values)


