class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        pass

        times = []
        
        for time in timePoints:
            h, m = time.split(':')
            times.append(int(h)*60 + int(m))
        
        times.sort()

        res = 24 * 60 - times[-1] + times[0]

        for i in range(len(times)-1):
            res = min(times[i+1] - times[i], res)
        
        return res