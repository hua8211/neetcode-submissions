class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0

        l, r = 0, 0

        while r < len(s):
            curr = s[r]
            while curr in seen:
                seen.remove(s[l])
                l += 1
            seen.add(curr)
            res = max(res, r - l + 1)
            r += 1
        
        return res