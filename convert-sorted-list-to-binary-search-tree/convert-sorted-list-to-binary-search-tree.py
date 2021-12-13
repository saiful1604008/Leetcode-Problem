# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        list1 = [] 
        while(head):
            list1.append(head.val)
            head = head.next
        
        def solve(first,last):
            if first > last:
                return 
            
            mid = first + (last - first) // 2
            root = TreeNode(list1[mid])
            root.left = solve(first, mid -1)
            root.right = solve(mid+1,last)
            
            return root
        
        return solve(0, len(list1) -1)
        