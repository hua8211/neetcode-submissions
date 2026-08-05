class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        temp1 = [0]*26
        temp2 = [0]*26

        for c in s1:
            temp1[ord(c) - ord("a")] += 1

        l,r = 0,0
        while r <= len(s2)-1:
            temp2[ord(s2[r]) - ord("a")] +=1

            if (r-l+1) == len(s1):
                if temp1 == temp2:
                    return True
                else:
                    temp2[ord(s2[l]) - ord("a")] -=1
                    l += 1
            r += 1

        return False