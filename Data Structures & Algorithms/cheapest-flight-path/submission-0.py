class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Using the BFS Approach

        # Step 1: Initialize the minimum prices to reach each node; set all to infinity except source
        prices = [ float('inf')] * n
        prices[src] = 0 

        # Step 2: Build the adjaceny list from the flights input 
        adj = [ [] for _ in range(n)]

        for u, v, cst in flights:
            # add (destination, cost) to the list for source node 'u'
            adj[u].append([v, cst])

        # Step 3: Use a queue to perform BFS 
        # Each item is (current total cost, current node, number of stops so far)

        q = deque([(0, src, 0)])

        while q:
            cst, node,stops = q.popleft()

            # if we've used more than k stops, skip this path
            if stops > k:
                continue 

            # Step 4 - explore neighbors of the current node
            for nei, w in adj[node]:
                nextCost = cst + w # cost to reach neighbor through this path

                # if the new cost is cheaper than any previously known cost
                # to reach this neighbor, update the price and enqueue the new path
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        # Step 5: if the destination is unreachable, return -1 
        return prices[dst] if prices[dst] != float('inf') else - 1
