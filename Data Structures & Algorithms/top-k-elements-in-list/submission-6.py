class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # myMap = {}

        # for num in nums:
        #     myMap[num] = 1 + myMap.get(num, 0)

        # minHeap = []

        # for key, value in myMap.items():
        #     heapq.heappush(minHeap, [value, key])
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)

        # res = []
        # for value, key in minHeap:
        #     res.append(key)
        # return res

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for i in range(len(nums)+1)]

        for key, value in count.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res