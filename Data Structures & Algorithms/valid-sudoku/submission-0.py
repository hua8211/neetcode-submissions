class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col = 0, 0
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        squareMap = defaultdict(list)

        while row < 9:
            currList = board[row]
            col = 0
            while col < 9:
                curr = currList[col]
                if curr != ".":
                    sq = (row // 3) * 3 + (col // 3)
                    if curr in rowMap[row] or curr in colMap[col] or  curr in squareMap[sq]:
                        return False
                    rowMap[row].append(curr)
                    colMap[col].append(curr)
                    squareMap[sq].append(curr)
                col += 1
            row += 1
        return True
        