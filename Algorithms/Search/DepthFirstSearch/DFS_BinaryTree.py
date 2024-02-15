
# dfs in binary tree is identical to inorder traversal

def DFS_binaryTree(root):
    if not root:
        return
    #left
    DFS_binaryTree(root.left)
    # mid
    print(root.val)
    # right
    DFS_binaryTree(root.right)