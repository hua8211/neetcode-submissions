class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        myMap = {}

        for s in strs:
            curr = ""
            for c in s:
                curr += c
                myMap[curr] = 1 + myMap.get(curr, 0)
        if myMap:
            maxValue = max(myMap.values())
   
        temp = []

        for key, value in myMap.items():
            if value == maxValue and value == len(strs):
                temp.append(key)

        res = ""
        longest = 0

        for t in temp:
            if len(t) > longest:
                res = t
                longest = len(t)

        return res
                