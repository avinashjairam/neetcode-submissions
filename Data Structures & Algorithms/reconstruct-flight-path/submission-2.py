class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build adjacency lists (graphs) from the list of tickets 

        # Each source maps to a list of destination airports 
        adj = {src: [] for src, dst in tickets}

        # sort tickets lexiographically to ensure lexiographical order is preserved in DFS traversal
        tickets.sort()

        # Populate the adjacency list
        for src, dst in tickets:
            adj[src].append(dst)

        # Result path - start from 'JFK' as per problem constraint 
        res = ['JFK']

        # DFS function to construct the valid itinerary
        def dfs(src):
            # Base case: if the itinerary includes all tickets + 1 stop
            if len(res) == len(tickets) + 1:
                return True 

            # If there are no outgoing flights from current airport
            if src not in adj:
                return False 

            # Make a copy of current destinations to try all options
            temp = list(adj[src])

            for i, v in enumerate(temp):
                # Remove the ticket being used (backtracking setup)
                adj[src].pop(i)
                res.append(v)

                # recur to next destination 
                if dfs(v):
                    return True 

                # Backtrack: undo the move
                adj[src].insert(i,v)
                res.pop()


            



        dfs('JFK')

        return res 

