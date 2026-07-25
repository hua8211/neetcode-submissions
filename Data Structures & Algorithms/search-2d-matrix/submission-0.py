class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            m = (l + r) // 2
            curr = matrix[m]

            l2, r2 = 0, len(curr)-1
            while l2 <= r2:
                print (l2, r2)
                m2 = (l2 + r2) // 2
                print(curr[m2])
                if curr[m2] < target:
                    l2 = m2 + 1
                elif curr[m2] > target:
                    r2 = m2 - 1
                else:
                    return True
            print(r2)
            if r2 < 0:
                r = m - 1
            else:
                l = m + 1
        return False