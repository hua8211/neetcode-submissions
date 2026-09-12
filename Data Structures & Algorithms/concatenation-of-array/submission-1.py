class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * (length * 2)
        for i, num in enumerate(nums):
            res[i] = num
            res[i + length] = num
        return res
