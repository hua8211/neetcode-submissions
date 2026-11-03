class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * 1440

        for time in timePoints:
            h, m = time.split(":")
            minute = int(h) * 60 + int(m)
            if minutes[minute]:
                return 0
            minutes[minute] = True
        
        first, prev, last = float("inf"),float("inf"),float("inf")
        res = 1440
        for i in range(1440):
            if minutes[i]:
                if first == float("inf"):
                    first = i
                if prev != float("inf"):
                    res = min(res, i-prev)
                prev = i
                last = i
        return min(res, 1440-last+first)