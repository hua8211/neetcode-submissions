# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nexta

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, l in enumerate(lists):
            if l:
                minHeap.append((l.val, i, l))
        heapq.heapify(minHeap)

        curr = dummy = ListNode()

        while minHeap:
            v, i ,l  = heapq.heappop(minHeap)
            curr.next = ListNode(v)
            curr = curr.next
            if l.next:
                heapq.heappush(minHeap, (l.next.val,i,l.next))

        return dummy.next