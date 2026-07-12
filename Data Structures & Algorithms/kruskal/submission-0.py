import heapq

class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i 
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p 

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False 

        if self.rank[p1] >= self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2 
        else:
            self.par[p1] = p2
            self.rank[p2] += 1 

        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minHeap = []
        totalWeight = 0 
        components = n

        unionFind = UnionFind(n)

        for u, v, w in edges:
            heapq.heappush(minHeap, [w, u, v])

        while components > 1 and  minHeap:
            w, n1, n2 = heapq.heappop(minHeap)

            if not unionFind.union(n1, n2):
                continue 

            totalWeight += w
            components -= 1

        return totalWeight if components == 1 else -1







        