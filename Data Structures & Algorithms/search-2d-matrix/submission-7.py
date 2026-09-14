class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l, r = 0, row * col - 1

        while l <=r :
            mid = (l+r)//2
            midRow = mid // col
            midCol = mid % col
            if matrix[midRow][midCol] < target:
                l = mid + 1
            elif matrix[midRow][midCol] > target:
                r = mid - 1
            elif matrix[midRow][midCol] == target:
                return True
        return False 