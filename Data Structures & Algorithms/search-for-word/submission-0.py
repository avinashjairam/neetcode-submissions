class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # get number of rows and columns in the board
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True 

            # boundary conditions or mismatch 
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or # out of bounds 
                    word[i] != board[r][c] or # current letter doesn't match 
                    board[r][c] == '#' # already visited cell 
                ):
                return False

            # mark the cell as visited by replacing it with a special character 
            temp = board[r][c]
            board[r][c] = '#'
            
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            board[r][c] = temp # backtrack: restore original value in the cell
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True 

        # if no path found after checking all cells, return False 
        return False 
  





        






