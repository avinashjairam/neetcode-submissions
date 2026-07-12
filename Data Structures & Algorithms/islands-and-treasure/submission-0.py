from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])

        # set to keep track of visited cells
        visit = set()

        # queue for BFS
        q = deque()

        # helper function to safely add a cell to the queue
        def addCell(r,c):
            # skip if out of bounds, water, or already visited
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == -1):
                return 

            # mark the cell as visited
            visit.add((r,c))

            # enqueue for BFS
            q.append([r,c])

        # step 1. Add all treasure chest cells (value 0) to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        # step 2. Perform multi source BFS from all treasure chests 
        dist = 0 # distance from treasure 

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist # set the distance at the current cell 
                # try to add all 4 neighboring cells 
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            # increment distance after processing all nodes at the current level
            dist += 1
