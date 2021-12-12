# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return 
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        leftside = self.sortedArrayToBST(nums[0:mid])
        rightside = self.sortedArrayToBST(nums[mid+1:])
        
        root.left = leftside
        root.right = rightside
        
        return root
        