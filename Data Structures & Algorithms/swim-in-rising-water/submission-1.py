class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Get the size of the grid(N x N)
        N = len(grid)

        # Set to keep track of visited cells 
        visit = set()

        # Min Heap to prioritize paths with minimum elevation 
        # Format: [max_height_so_far, row, column]
        # Start at top left cells with its height
        minH = [ [grid[0][0], 0, 0] ]

        # Possible movement directions: right, left, down, up 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Mark the starting cell as visited
        visit.add((0,0))

        while minH:
            # Pop the path with the lowest maximum height so far 
            t, r, c = heapq.heappop(minH)

            # If we've reached to bottom right cell, return the result 
            if r == N-1 and c == N-1:
                return t

            # Explore all 4 adjacent cells 
            for dr, dc in directions:
                neiR, neiC  = r + dr, c + dc 

                # Skip if out of bounds or already visited 
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue 

                # Mark the neighbor as visited 
                visit.add((neiR, neiC))

                # Add to heap with updated max height
                # The key insight: we need the max height encountered along the path
                # because the water level must be at least as high as the highest cell
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])



