class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) >= 2:
            stoneOne = -heapq.heappop(maxHeap)
            stoneTwo = -heapq.heappop(maxHeap)
            if stoneOne != stoneTwo:
                heapq.heappush(maxHeap, -abs(stoneOne - stoneTwo))

        return -maxHeap[0] if maxHeap else 0