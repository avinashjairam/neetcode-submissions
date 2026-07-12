class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # queue for BFS - holds coordinates of rotten oranges
        q = collections.deque()

        # counter to track the number of fresh oranges
        fresh = 0

        # timer to track minutes passed during BFS
        time = 0

        # step 1: preprocess the grid to count fresh oranges
        # add all initially rotten oranges to the queue 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    # count of fresh oranges
                    fresh += 1
                if grid[r][c] == 2:
                    # enqueue rotten orange position
                    q.append((r,c))

        # step 2: define 4 directions - up, down, left, right
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        # step 3: perform multi-source BFS on all rotten oranges 
        while fresh > 0 and q:
            length = len(q) # process all rotten oranges at current time 

            for i in range(length):
                r, c = q.popleft() # get current rotten orange 
                # check all 4 neighbors
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    #if neighbor is within bounds and is a fresh fruit
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2 # rot it

                        # add newly rotted orange to queue
                        q.append([row,col])

                        # decrease fresh orange count
                        fresh -= 1  

            # one minute has passed (one BFS level done)
            time += 1 

        # step 4: return total time if all fresh oranges are rotted, else - 1
        return time if fresh == 0 else - 1

        