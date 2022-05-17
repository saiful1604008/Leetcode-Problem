# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(main_node, clone_node):
            if main_node == None:
                return
            elif main_node == target:
                return clone_node
            else:
                res = dfs(main_node.left, clone_node.left)
                res1 = dfs(main_node.right, clone_node.right)
                if res:
                    return res
                if res1:
                    return res1
        
        return dfs(original, cloned)
                
                