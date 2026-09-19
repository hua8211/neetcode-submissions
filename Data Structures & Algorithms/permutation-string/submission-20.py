class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Map = defaultdict(int)
        s2Map = defaultdict(int)

        for c in s1:
            s1Map[c] += 1

        l, r = 0, 0

        while r < len(s2):
            if (r - l + 1) > len(s1):
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l += 1

            curr = s2[r]
            s2Map[curr] += 1

            if (r - l + 1) == len(s1):
                if s1Map == s2Map:
                    return True
                    
            r += 1

        return False
            