class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            minHeap.append(-stone)
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x, y = -heapq.heappop(minHeap), -heapq.heappop(minHeap)
            if x > y:
                heapq.heappush(minHeap, -(x-y))
        if minHeap:
            return (-minHeap[0])
        return 0