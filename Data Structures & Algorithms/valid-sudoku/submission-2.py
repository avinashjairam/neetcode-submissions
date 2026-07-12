class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all 9 rows for duplicates
        for row in range(9):
            seen = set() # track digits seen in this row

            for i in range(9):
                if board[row][i] == '.':
                    continue # skip empty cells

                if board[row][i] in seen:
                    return False

                seen.add(board[row][i])

        # check all 9 columns for duplicates 
        for col in range(9):
            seen = set() # track digits seen in this row

            for i in range(9):
                if board[i][col] == '.':
                    continue # skip empty cells

                if board[i][col] in seen:
                    return False

                seen.add(board[i][col])

        # check all 9 3 x 3 squares for duplicates 
        for square in range(9):
            seen = set() # track digits seen in this 3 x 3 square 

            for i in range(3):
                for j in range(3):
                    # calculate actual board coordinates
                    row = (square // 3) * 3 + i # starting row + offset
                    col = (square % 3) * 3 + j # starting col + offset

                    if board[row][col] == '.':
                        continue # skip empty cells 

                    if board[row][col] in seen:
                        return False # skip empty cells 

                    seen.add(board[row][col]) # mark this digit as seen

        return True # no duplicates found 

