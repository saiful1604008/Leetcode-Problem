# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    res = res + node.val
                    
                if low < node.val:
                    stack.append(node.left)
                    
                if high > node.val:
                    stack.append(node.right)
                    
        return res
                
            
            
         