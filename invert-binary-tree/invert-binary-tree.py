# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.left is None and root.right is None:
            return root
        else:
            right1 = self.invertTree(root.left)
            left1 = self.invertTree(root.right)
            root.left = left1
            root.right = right1
            
            return root
        