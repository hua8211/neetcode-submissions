class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = defaultdict(list)

        for i, num in enumerate(nums):
            if num in myMap:
                for j in myMap[num]:
                    if abs(i-j) <= k:
                        return True
            myMap[num].append(i)
        
        return False
