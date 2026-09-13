class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}

        for s in strs:
            curr = [0] * 26

            for c in s:
                curr[ord(c) - ord("a")] += 1
            
            if tuple(curr) not in myMap:
                myMap[tuple(curr)] = []

            myMap[tuple(curr)].append(s)

        res = []

        for value in myMap.values():
            res.append(value)
        
        return res