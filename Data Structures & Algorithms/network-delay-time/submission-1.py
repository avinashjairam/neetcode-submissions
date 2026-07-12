class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        def dijkstra(k, times, n):
            # Initialize adjacency list for the graph
            adj = {}

            for i in range(n + 1):
                adj[i] = []

            # Populate the adjacency list with the edges 
            for ui, vi, ti in times:
                adj[ui].append([vi, ti])

            # Dictionary to store the shortest distance to each node
            shortest = {}

            # Min heap to keep track of the next node with the smallest distance
            min_heap = [[0, k]] # start with source node at distance 0 

            while min_heap:
                w1, n1 = heapq.heappop(min_heap)

                # if this node has already been visited (i.e.) shortest distance found, skip
                if n1 in shortest:
                    continue 

                # mark the node as visited 
                shortest[n1] = w1

                # explore all neighbors of the current node
                for n2, w2 in adj[n1]:
                    # only process unvisited nodes 
                    if n2 not in shortest:
                        # push updated distance
                        heapq.heappush(min_heap, [w1 + w2, n2])

            return shortest 

        shortest = dijkstra(k, times, n)

        return max(list(shortest.values())) if len(shortest) == n else - 1

