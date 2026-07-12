class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # columns that already contain n queen (indexed by column number)
        col = set()

        # positive diagonals r + c ( top-left to bottom right)
        # that already contain a queen
        posDiag = set()

        # negative diagonals (r - c) (top -right to bottom left that already contain a queen)
        negDiag = set()

        res = [] # will hold all valid boards (each board is a list [str])
        # start with an empty n x n board filled with '.'
        board = [['.' for _ in range(n)] for _ in range(n)]


        def backtrack(r:int) -> None:
            # Base case: all rows are filled with valid queen placements
            if r == n:
                # convert each row list into a string and store a snapshot of the board
                res.append([''.join(row) for row in board])
                return 

            # try to place a queen in each column (of the current row)
            for c in range(n):
                # if placing at (r,c) conflicts with an existing queen, skip
                # conflict rules: 1) same column - > c in col
                # 2) same pos diag -> (r + c) in posDiag
                # 3) same neg diag -> (r - c) in negDiag

                if c in col or (r + c) in posDiag or (r-c) in negDiag:
                    continue
                # choose: place a queen at (r,c) and mark the column/diagonals as occupied
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
                # explore and move to the next row
                backtrack(r + 1)
                # un-choose (backtrack): remove the queen and free the column/diagonals
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        # start from first row
        backtrack(0)
        return res