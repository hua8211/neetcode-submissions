class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            minHeap.append(stone * -1)
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            x, y = heapq.heappop(minHeap), heapq.heappop(minHeap)
            curr = (-1 * x) - (-1 *y)
            if curr > 0:
                heapq.heappush(minHeap, (-1 * curr))
        if minHeap:
            return (-1 * minHeap[0])
        return 0