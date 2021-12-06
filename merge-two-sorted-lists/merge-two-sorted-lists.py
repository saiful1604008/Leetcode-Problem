# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        current = head
        list1 = l1
        list2 = l2
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
                
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
                
        if list1:
            current.next = list1
                
        if list2:
            current.next = list2
            
        
        return head.next
                
            
                
            
            
            
        