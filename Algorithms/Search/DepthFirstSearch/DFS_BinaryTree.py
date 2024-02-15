
# dfs in binary tree is identical to inorder traversal

def DFS_binaryTree(root):
    if not root:
        return
    #left
    DFS_BinaryTree(root.left)
    # mid
    print(root.val)
    # right
    DFS_BinaryTree(root.right)