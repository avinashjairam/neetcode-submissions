class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # The answer must be between 0 and the largest existing gap
        left = 0
        right = 0

        # Find the largest gap between two existing neighboring stations
        for i in range(1, len(stations)):
            right = max(right, stations[i]-stations[i-1])

        # Helper function:
        # Given a possible maximum distance x, check whether we can make 
        # every gap <= x using at most k new stations 
        def can_make(x: float) -> bool:
            needed = 0

            for i in range(1, len(stations)):
                dist = stations[i] - stations[i-1]

                # If this gap has length dist, and each piece must be <= x,
                # then we need ceil(dist / x) pieces.
                # To create p pieces, we need p-1 new stations
                needed += math.ceil(dist/x) -1

                # If we already need too many stations
                # no need to continue counting
                if needed > k:
                    return False

            return needed <= k 


        # Binary search on the answer
        # We stop when left and right are extremely close 
        while right - left > 10e-9:
            mid = (left + right) / 2

            if can_make(mid):
                # mid is possible, so try an even smaller maximum distance
                right = mid 
            else:
                # mid is too small, so we need to allow larger gaps
                left = mid 

        return right 

        