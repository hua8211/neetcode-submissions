# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        minHeap = []
        for i, l in enumerate(lists):
            if l:
                minHeap.append((l.val, i, l))
        heapq.heapify(minHeap)

        while minHeap:
            v, i, l = heapq.heappop(minHeap)
            curr.next = l
            curr = curr.next
            if l.next:
                heapq.heappush(minHeap, (l.next.val, i, l.next))
        
        return dummy.next