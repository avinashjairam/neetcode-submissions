class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions =[[1,0],[-1,0],[0,1],[0, -1]]

        max_area = 0

        def bfs(r, c):
            area = 1 

            grid[r][c] = 0
         
            queue = deque([[r,c]])
            #print(queue.popleft(), queue.popleft())
         
            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc 

                    # check if out of bounds or we visited before 
                    if min(nr,nc) < 0  or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue 
                    
                    # enqueue valid neighbor land 
                    queue.append([nr, nc])
                    grid[nr][nc] = 0
                    area += 1
            print(area)
            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                   
                    max_area = max(max_area, bfs(r,c))

        
        return max_area

        