class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            minHeap.append([-distance, [x, y]])
        
        heapq.heapify(minHeap)

        while k < len(minHeap):
            heapq.heappop(minHeap)
        
        res = []
        for point in minHeap:
            d, x = point
            res.append(x)
        
        return res