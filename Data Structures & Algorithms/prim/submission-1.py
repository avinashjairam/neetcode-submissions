import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []

        for n1, n2, w in edges:
            adj[n1].append([n2, w])
            adj[n2].append([n1, w])

        visit = set()
        mst = []
        minHeap = []

        totalWeight = 0

        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])

        visit.add(0)

        while minHeap and len(visit) < n:
            w1, n1, n2 = heapq.heappop(minHeap)

            if n2 in visit:
                continue 

            mst.append([n1, n2])
            totalWeight += w1
            visit.add(n2)

            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])

        return totalWeight if len(visit) == n else -1 