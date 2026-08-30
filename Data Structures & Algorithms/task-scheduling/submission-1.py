class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        myMap = defaultdict(int)

        for task in tasks:
            myMap[task] += 1
    
        maxHeap = []

        for value in myMap.values():
            maxHeap.append(-value)

        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])


        return time