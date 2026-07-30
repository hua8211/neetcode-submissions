class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        mySet = set()
        result = 0
        while r <= len(s)-1:
            curr = s[r]
            while curr in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(curr)
            r+=1
            result = max(result, len(mySet))
        return result
            