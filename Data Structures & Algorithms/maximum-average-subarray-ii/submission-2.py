class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        # Returns True if there is a subarray of length at least k
        # whose average is at least avg. 
        def canFind(avg):
            current_sum = 0

            # Check the first subarray of length k 
            # We subtract avg from each number
            # If the transformed sum is >= 0,
            # then the original subarray average is >= avg
            for i in range(k):
                current_sum += nums[i] - avg

            if current_sum >= 0:
                return True

            # removable_prefix stores the sum of an earlier prefix
            # that we are allowed to remove while still leaving at least k elements
            removable_prefix_sum = 0

            # Keep track of the smallest removable prefix sum.
            # Subtracting the smallest prefix gives us the largest possible
            # subarray sum ending at the current index. 
            smallest_prefix_sum = 0

            # Extend the subarray one element at a time
            for i in range(k, len(nums)):

                # Add the current transformed value 
                current_sum += nums[i] - avg 

                # This earlier element can now become part of a removable prefix
                # Removing this prefix still leaves a subarray of length at least k
                removable_prefix_sum += nums[i - k] - avg

                # Save the smallest removeable prefix seen so far. 
                smallest_prefix_sum = min(smallest_prefix_sum, removable_prefix_sum)

                # current_sum is the transformed sum from index 0 to i 
                # Subtracting the smallest earlier prefix gives the best valid subarray ending at i
                if current_sum - smallest_prefix_sum >= 0:
                    return True

            return False  
        
        
        
        # Any subarray average must be between
        # the smallest and largest values in nums
        left = min(nums)
        right = max(nums)

        # Binary search for the largest average that is still possible
        while right - left > 1e-5:
            mid = (left + right) / 2

            if canFind(mid):
                # A subarray with average at least mid exists
                # so try a larger average
                left = mid 
            else:
                # mid is too large
                # so try a smaller average
                right = mid 

        return left 