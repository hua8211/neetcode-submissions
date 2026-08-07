# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        l1, l2 = head, head

        while l2 and l2.next:
            print(l1.val, l2.val)
            l1 = l1.next
            l2 = l2.next
            l2 = l2.next
            if l1 == l2:
                return True               
        
        return False