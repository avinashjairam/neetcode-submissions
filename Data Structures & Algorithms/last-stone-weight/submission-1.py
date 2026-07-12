import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = []

        for x in stones:
            heapq.heappush(self.max_heap, -x)

        while len(self.max_heap) > 1:
            max1, max2 = abs(heapq.heappop(self.max_heap)), abs(heapq.heappop(self.max_heap))
            
            print(max1, max2, self.max_heap)
            diff = abs(max1 - max2)

            if diff != 0:
                heapq.heappush(self.max_heap, -diff)

        return 0 if len(self.max_heap) == 0 else abs(self.max_heap[0])
        