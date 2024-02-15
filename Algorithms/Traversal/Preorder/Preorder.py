
# preorder traversal takes root of a binary tree as an argument
# and print node values in preorder

def preorder(root):
    if not root:
        return
    # mid
    print(root.val)
    #left
    preorder(root.left)
    # right
    preorder(root.right)

