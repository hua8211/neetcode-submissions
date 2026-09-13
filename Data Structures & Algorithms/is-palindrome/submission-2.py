class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1

        while l < r:
            while s[l].isalnum() == False and l < r:
                l += 1
            while s[r].isalnum() == False and l <r:
                r -= 1
            
            if ord(s[l]) != ord(s[r]):
                return False
            l += 1
            r -= 1

        return True