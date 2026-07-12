
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Step #1: Build the adjacency list with edge costs (Manhattan distances)
        # Each node (i) maps to a list of [distance, neighbor_index]

        adj = {i : [] for i in range(N) }

        for i in range(N):
            x1, y1 = points[i]

            for j in range(i+1, N):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2) # Manhattan distance

                # undirected edge: add distance both ways
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Step 2: initialize variables for Prim's algorithm 
        res = 0 # total cost of connection all points
        visit = set() # track nodes already in the MST 
        minH = [[0,0]] # MinHeap to pick the next edge with the smallest code (cost, node)

        # Step 3: Prim's algorithm -. grow MST one node at a time 
        while len(visit) < N:
            cost, i = heapq.heappop(minH) # Choose the edge with the smallest cost

            if i in visit:
                continue # skip the node if already in the MST 

            res += cost # add the cost of this edge to the result 
            visit.add(i) # mark the node as visited 

            # add all edges from the current node to the heap if the destination is unvisited
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        # Step 4: Return the total cost of the MST
        return res


