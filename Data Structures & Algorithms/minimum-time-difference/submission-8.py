class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        pass
        minutes = [False] * 1440

        for time in timePoints:
            h,m = time.split(":")
            currMin = int(h) * 60 + int(m)
            if minutes[currMin]:
                return 0
            minutes[currMin] = True
        
        res = 1440
        first, last, prev = float("inf"),float("inf"),float("inf"),

        for i in range(1440):
            if minutes[i]:
                if first == float("inf"):
                    first = i
                if prev != float("inf"):
                    res = min(res, i-prev)
                prev = i
                last = i
        return min(res, 1440-last+first)