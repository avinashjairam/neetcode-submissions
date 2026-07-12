class Solution:
    def compute_distance(self, coordinates):
        return math.sqrt((coordinates[1] - 0)**2 + (coordinates[0] - 0)**2)
   
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for x in range(len(points)):
            
            distance = self.compute_distance(points[x])
            heapq.heappush(min_heap, [-distance, x])

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        indexes = []
        print(min_heap)

        while min_heap:
            indexes.append(points[heapq.heappop(min_heap)[1]])

        return indexes
        


                


