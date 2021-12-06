# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.result = []
        
        def inorder_traverse(node):
            if not node:
                return
            else:
                inorder_traverse(node.left)
                self.result.append(node.val)
                inorder_traverse(node.right)
                
        inorder_traverse(root)
        minimum = [self.result[i] - self.result[i-1] for i in range (1, len(self.result))]
        return min(minimum)