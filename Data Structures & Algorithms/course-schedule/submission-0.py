class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}

        for csr, pre in prerequisites:
            preMap[csr].append(pre)
        
        visted = set()

        def dfs(csr):
            if csr in visted:
                return False
            if preMap[csr] == []:
                return True
            
            visted.add(csr)

            for pre in preMap[csr]:
                if not dfs(pre):
                    return False
            
            visted.remove(csr)
            preMap[csr] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True