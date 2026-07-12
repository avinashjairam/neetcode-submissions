class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get board dimensions
        ROWS, COLS = len(board), len(board[0])
        
        # recursive DFS function to mark all Os connected to the border 
        def capture(r,c):
            # base case: out of bounds or not an 'O'
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != 'O':
                return 

            # temporarily mark safe 'O' as 'T'
            board[r][c] = 'T'

            # recurse in all four directions 
            capture(r + 1, c) # down
            capture(r - 1, c) # up
            capture(r, c + 1) # right
            capture(r, c - 1) # left

        # Step 1: Run DFS from all border '0's (top, bottom, left, right)
        for r in range(ROWS):
            if board[r][0] == 'O': # left column
                capture(r,0)

            if board[r][COLS -1] == 'O': # right column
                capture(r, COLS -1)

        for c in range(COLS):
            if board[0][c] == 'O': # top row
                capture(0, c)
            
            if board[ROWS-1][c] == 'O': # bottom row
                capture(ROWS-1, c)

        # Step 2: Flip surrounded 0's to X and restore 'T' back to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'