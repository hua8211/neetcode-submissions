class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in myMap:
                return [myMap[comp], i]
            
            else:
                myMap[num] = i

        