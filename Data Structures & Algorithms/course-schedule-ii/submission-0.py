class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visted, cycle = set(), set()
        
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visted:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            visted.add(crs)
            cycle.remove(crs)
            res.append(crs)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res