class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myMap = {}

        for i, num in enumerate(nums):
            if num in myMap and abs(i-myMap[num]) <= k:
                return True
            myMap[num] = i
        
        return False
