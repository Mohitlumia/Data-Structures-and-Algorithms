# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        leftPtr = root
        rightPtr = root
        
        while True:
            if leftPtr.val < val:
                if not leftPtr.right:
                    leftPtr.right = TreeNode(val)
                    break
                else:
                    rightPtr = leftPtr.right
            elif leftPtr.val > val:
                rightPtr = leftPtr
                if not leftPtr.left:
                    leftPtr.left = TreeNode(val)
                    break
                else:
                    leftPtr = leftPtr.left
            if rightPtr.val > val:
                if not rightPtr.left:
                    rightPtr.left = TreeNode(val)
                    break
                else:
                    leftPtr = rightPtr.left
            elif rightPtr.val < val:
                leftPtr = rightPtr
                if not rightPtr.right:
                    rightPtr.right = TreeNode(val)
                    break
                else:
                    rightPtr = rightPtr.right
        
        return root
