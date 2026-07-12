class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Helper function:
        # Checks whether there exists a subarray of length at least K 
        # whose avg is >= avg

        def canFind(avg):
            curr = 0

            # Build the transformed sum of the first window of size k
            # If this sum is >= 0, then the first k elements have average >= avg
            for i in range(k):
                curr += nums[i] - avg

            # If the first window already works, avg is feasible
            if curr >= 0:
                return True

            # prev stores a transformed prefix sum that is BEFORE
            # the current window ending position 

            # min_prev stores the smallest prefix sum seen so far 

            # Why do we need min_prev? For subarrays longer than k, we want to 
            # subtract the smallest previous prefix to maximize the transformed subarray sum
            prev = 0 
            min_prev = 0 

            # Now we check subarrays of length greater than k 

            # curr will represent the transformed prefix sum from index 0 
            # up to the current index i 
            for i in range(k, len(nums)):

                # Add the current element to the running transformed sum 
                curr += nums[i] - avg

                # Add the element that is now far behind to be considered as a 
                # removeable prefix. 
                # nums[i - k] is exactly k positions behind i,
                # so removing a prefix up to this point still leaves 
                # a subarray of length at least k 
                prev += nums[i - k] - avg

                # Track the smallest prefix sum seen so far. 
                # Subtracting the smallest prefix gives the largest possible 
                # transformed subarray sum ending at i 
                min_prev = min(min_prev, prev)

                # curr - min_prev represents the best transformed sum
                # of any subarray ending at i with length at least k 

                # If it is >= 0, that means we found a subarray whose
                # average is at least avg
                if curr - min_prev >= 0:
                    return True 

            # No valid subarray was found for this average
            return False 

        # The maximum average must be between the smallest and largest values in the array
        left = min(nums)
        right = max(nums)

        # Binary Search over possible average values
        # We stop when the range is very small because the answer is accepted within 1e-5 error
        while right - left > 10e-6:
            mid = (left + right) / 2

            # If mid is feasible, then there exists a subarray with average at least mid
            # So we try a larger average
            if canFind(mid):
                left = mid 

            # If mid is not feasible, then mid is too large
            # Try a smaller average
            else:
                right = mid 

        # left is the largest feasible average we found 
        return left 