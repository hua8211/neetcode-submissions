class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        myMap = defaultdict(int)
        for i in nums:
            myMap[i] += 1
        for key, value in sorted(myMap.items(), key=lambda x: x[1], reverse=True):
            result.append(key)
        return result[:k]