
# postorder traversal takes root of a binary tree as an argument
# and print node values in postorder

def postorder(root):
    if not root:
        return
    # right
    postorder(root.right)
    # mid
    print(root.val)
    #left
    postorder(root.left)

