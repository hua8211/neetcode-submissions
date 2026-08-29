class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush(minHeap, (distance, point))

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res