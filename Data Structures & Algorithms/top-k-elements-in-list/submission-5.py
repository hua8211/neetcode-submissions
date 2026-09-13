class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}

        for num in nums:
            myMap[num] = 1 + myMap.get(num, 0)

        minHeap = []

        for key, value in myMap.items():
            heapq.heappush(minHeap, [value, key])
            while len(minHeap) > k:
                heapq.heappop(minHeap)

        
        res = []
        print(minHeap)
        for value, key in minHeap:
            res.append(key)
        return res