
# inorder traversal takes root of a binary tree as an argument
# and print node values in inorder

def inorder(root):
    if not root:
        return
    #left
    inorder(root.left)
    # mid
    print(root.val)
    # right
    inorder(root.right)

