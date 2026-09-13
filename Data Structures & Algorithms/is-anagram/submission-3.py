class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = defaultdict(int)
        mapT = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            mapS[s[i]] +=1
            mapT[t[i]] +=1
        
        return mapS == mapT