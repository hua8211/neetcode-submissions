class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            miss = target - nums[i]
            if miss in seen:
                return [seen[miss], i]
            seen[num] = i