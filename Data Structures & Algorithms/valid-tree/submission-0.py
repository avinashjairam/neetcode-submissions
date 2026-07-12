class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges 
        # If there are more than n-1 edges, then it must contain a cycle and not a tree
        if len(edges) > (n -1):
            return False 

        # Create an adjacency list 
        adj = [ [] for _  in range(n) ]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) # since the graph is undirected 

        # to keep track of the visited nodes 
        visit = set()

        def dfs(node, par):
            # if we've already visited this node, a cycle is detected 
            if node in visit:
                return False 

            visit.add(node)

            # visit all the neighbors
            for nei in adj[node]:
                # skip the parent to avoid false positive cycles in undirected graphs 
                if nei == par:
                    continue 

                # if DFS on neighbor fails, there's a cycle or disconnection 
                if not dfs(nei, node):
                    return False 
            
            return True # No cycles found for this path

        # check that the graph is fully connected (i.e. all nodes visited, and has no cycles)
        return dfs(0,-1) and len(visit) == n