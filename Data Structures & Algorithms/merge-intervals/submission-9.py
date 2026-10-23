class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            currEnd = res[-1][1]

            if start <= currEnd:
                res[-1][1] = max(currEnd, end)
            else:
                res.append([start, end])
        
        return res