class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # get grid dimensions
        ROWS, COLS = len(heights), len(heights[0])

        
        # sets to record cells that can flow to the pacific and atlantic oceans
        pac, atl = set(), set()

        # DFS function to mark reachable cells
        def dfs(r, c, visit, prevHeight):
            # if out of bounds, already visited, or can't flow (height dropped), stop
            if (r < 0 or c < 0 or ((r,c)) in visit or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return

            # mark the cell as visited 
            visit.add((r,c))

            # explore all 4 directions from the current cell
            dfs( r + 1, c, visit, heights[r][c])
            dfs( r - 1, c, visit, heights[r][c])
            dfs( r, c + 1, visit, heights[r][c])
            dfs( r, c - 1, visit, heights[r][c])

        # Step 1: Start DFS from all cells touching the Oceans (top and left) edges
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # top row (pacific)
            dfs(ROWS -1, c, atl, heights[ROWS-1][c]) # bottom row atlantic

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # left column (pacific)
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # right column (atlantic)

        # Step 2: Collect cells that are reacable from both areas 
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
        