class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []

        prev = []
        for i in range(len(intervals)):
            if i == 0:
                prev = intervals[0]
            currStart, currEnd = intervals[i][0], intervals[i][1]
            if currStart <= prev[1]:
                prev[1] = max(currEnd, prev[1])
            else:
                res.append(prev)
                prev = intervals[i]
        res.append(prev)

        return res