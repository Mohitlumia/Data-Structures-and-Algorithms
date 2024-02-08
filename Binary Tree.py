class TreeNode:
  def __init__(self,val,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

  def get_height(self,node):
    if not node:
      return 0
    return 1 + get_height(node.left) + get_height(node.right)




