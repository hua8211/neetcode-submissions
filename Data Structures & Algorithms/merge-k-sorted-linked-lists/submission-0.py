# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        minHeap = []
        for i, l in enumerate(lists):
            if l:
                minHeap.append((l.val, i, l))
        heapq.heapify(minHeap)

        while minHeap:
            currVal, index, currList = heapq.heappop(minHeap)
            curr.next = currList
            curr = curr.next
            if currList.next:
                heapq.heappush(minHeap, (currList.next.val, index, currList.next))
        return dummy.next