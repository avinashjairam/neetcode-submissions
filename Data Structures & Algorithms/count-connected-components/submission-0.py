class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list 
        adj = [[] for _ in range(n)]

        # keep track of whether a node has been visited 
        visit = [False] * n

        # build the adjacency list from the edges 
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        # dfs to visit all nodes in a connected component
        def dfs(n):
          
            for nei in adj[n]:
                if not visit[nei]:
                    visit[nei] = True # mark neighbor as visited                
                    dfs(nei) # recursively visit its neighbors 



        # count the number of connected components 
        res = 0

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1 


        return res 

        