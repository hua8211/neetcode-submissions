class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {} # value : most recent index

        for i, num in enumerate(nums):
            if num in myMap and i - myMap[num] <= k:
                return True
            myMap[num] = i
        return False