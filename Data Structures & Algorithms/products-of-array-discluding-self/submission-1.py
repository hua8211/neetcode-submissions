class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        

        i = 0
        curr = 1
        for i in range(len(nums)):
            prefix.append(curr)
            curr = curr * nums[i]
            i += 1
        # print(prefix)
        curr = 1
        for i in range(len(nums) -1, -1, -1):
            prefix[i] = prefix[i] * curr
            curr = curr * nums[i]
        return prefix
