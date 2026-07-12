class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapq.heapify(min_heap)

        for x in nums:
            heapq.heappush(min_heap, x)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
            

