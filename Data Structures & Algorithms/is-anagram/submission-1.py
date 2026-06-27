class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        if(len(s) != len(t)):
            return False
        for r in range(len(s)):
            if s[r] != t[r]:
                return False
        return True
        