class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) >= 2:
            stoneOne = -heapq.heappop(maxHeap)
            stoneTwo = -heapq.heappop(maxHeap)
            if stoneOne != stoneTwo:
                heapq.heappush(maxHeap, -abs(stoneOne - stoneTwo))

        if len(maxHeap) > 0:
            return -maxHeap[0]
        return 0