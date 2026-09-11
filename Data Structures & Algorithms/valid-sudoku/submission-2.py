class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        squareMap = defaultdict(list)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr != ".":
                    sq = (r // 3, c // 3)
                    if curr in rowMap[r] or curr in colMap[c] or curr in squareMap[sq]:
                        return False
                    rowMap[r].append(curr)
                    colMap[c].append(curr)
                    squareMap[sq].append(curr)
        
        return True