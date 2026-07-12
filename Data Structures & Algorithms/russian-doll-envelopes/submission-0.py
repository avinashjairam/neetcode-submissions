import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width increasing
        # If widths are equal, sort height decreasing
        envelopes.sort(key=lambda x:(x[0],-x[1]))

        # lis[i] will store the smallest possible ending height
        # of an increasing subsequence of length i + 1 
        lis = []

        for width, height in envelopes:
            # Find where this height should go in lis 

            # bisect_left gives the first index where height can be placed
            # while keeping lis sorted
            idx = bisect.bisect_left(lis, height)

            # if height is larger than everything in lis
            # extend the LIS
            if idx == len(lis):
                lis.append(height)

            # Otherwise, replace the existing value with height
            # This does not change the length of the LIS
            # but it gives us a smaller ending height
            # which is better for future envelopes 
            else:
                lis[idx] = height

        return len(lis)