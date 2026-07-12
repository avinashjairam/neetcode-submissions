import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their left endpoint
        intervals.sort()

        # We must process queries in sorted order, but the final answers
        # must be returned in the original query order. 
        #
        # Each tuple contains: (query value, original index)
        sorted_queries = sorted( (query, index) for index, query in enumerate(queries))

        # Default answer is -1 in case no interval contains a query
        result = [-1] * len(queries)

        # Heap entries are:
        # (interval length, right endpoint)
        # 
        # The shortest interval will remain at heap[0].
        min_heap = []

        # Pointer to the next interval we have not processed.
        interval_index = 0

        for query, original_index in sorted_queries:
            # Add every interval that has started this query 
            #
            # Since intervals are sorted by left endpoint, once an
            # interval's left endpoint is greater than query, we stop 
            while (interval_index < len(intervals) and intervals[interval_index][0] <= query):
                left, right = intervals[interval_index]
                length = right - left + 1

                heapq.heappush(min_heap, (length, right))
                interval_index += 1 

            # Remove expired intervals
            #
            # An interval cannot contain query when
            # right < query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # After removing expired intervals, the interval at the top is the 
            # shortest interval containing the current query
            if min_heap:
                result[original_index] = min_heap[0][0]

        return result 
