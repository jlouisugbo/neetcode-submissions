class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                square = (r//3, c//3)
                if curr == ".":
                    continue
                if (curr in rows[r] or curr in cols[c] 
                    or curr in squares[square]):
                    return False

                cols[c].add(curr)
                rows[r].add(curr)
                squares[square].add(curr)

        return True