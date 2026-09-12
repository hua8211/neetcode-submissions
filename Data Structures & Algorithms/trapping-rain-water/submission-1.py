class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        maxHeight = 0
        for i in range(len(height)):
            maxHeight= max(height[i], maxHeight)
            prefix[i] = maxHeight

        suffix = [0] * len(height)
        maxHeight = 0
        for i in range(len(height)-1,-1,-1):
            maxHeight= max(height[i], maxHeight)
            suffix[i] = maxHeight

        res = 0
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i]
        return res