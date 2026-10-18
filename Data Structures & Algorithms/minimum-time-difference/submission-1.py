class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        pass

        # times = []
        
        # for time in timePoints:
        #     h, m = time.split(':')
        #     times.append(int(h)*60 + int(m))
        
        # times.sort()

        # res = 24 * 60 - times[-1] + times[0]

        # for i in range(len(times)-1):
        #     res = min(times[i+1] - times[i], res)
        
        # return res

        times = [False] * (24 * 60)

        for time in timePoints:
            h, m = time.split(':')
            minute = int(h)*60 + int(m)
            if times[minute] == True:
                return 0
            else:
                times[minute] = True

        first, last, prev = float("inf"),float("inf"),float("inf")

        res = 24 * 60

        for i in range(24*60):
            if times[i]:
                if first == float("inf"):
                    first = i
                if prev != float("inf"):
                    res = min(res, i - prev)
                prev = i
                last = i
        
        return min(res, 24*60 - last + first)




