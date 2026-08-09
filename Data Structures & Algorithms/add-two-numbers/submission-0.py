# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head

        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            stringTotal = str(total)
            if len(stringTotal) > 1:
                carry = int(stringTotal[0])
                total = int(stringTotal[1])
            else:
                carry = 0
            
            tail.next = ListNode(total)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry != 0:
            tail.next = ListNode(carry)
        return dummy_head.next

        