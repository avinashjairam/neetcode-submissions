class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # step 1: initialize indegree array and adjacency list 
        indegree = [0] * (n + 1) # tracks number of edges for each node 

        # undirected graph representation 
        adj = [ [] for _ in range( n + 1 ) ]

        # step 2: build the graph and update degrees 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1 

        # step 3: queue for pruning leaf nodes (nodes with degree 1)
        q = deque()

        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        # step 4: prune leaves iteratively 
        while q:
            node = q.popleft()

            # mark node as removed 
            indegree[node] -= 1 

            for nei in adj[node]:
                # remove the connection
                indegree[nei] -= 1

                if indegree[nei] == 1:
                    # if the neighbor becomes a leaf, append it to the queue
                    q.append(nei) 

        # step 5: scan edges in reverse order to find the one that closes the cycle 
        for u, v in reversed(edges):
            if indegree[u] > 1 and indegree[v] > 0:
                return [u, v] # this edge forms a cycle and should be removed

        return []
        