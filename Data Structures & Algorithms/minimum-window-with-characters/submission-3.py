class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tMap = {}
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        sMap = {}
        have, need = 0, len(tMap)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]

            if c in tMap:
                sMap[c] = 1 + sMap.get(c, 0)
                if sMap[c] == tMap[c]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                if s[l] in tMap:
                    sMap[s[l]] -= 1
                    if sMap[s[l]] < tMap[s[l]]:
                        have -=1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""