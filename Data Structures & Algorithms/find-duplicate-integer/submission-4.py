class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        
        prev = float("inf")

        for num in nums:
            if num == prev:
                return num
            prev = num

        return 1