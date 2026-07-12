class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
    
        # Helper function
        # Determines whether we can split the array into at most 'k' subarrays
        # such that no subarray has a sum greater than 'largest'
        def canSplit(largest):
            subarrays = 1 # start with one subarray
            currSum = 0 # running sum of the current subarray
            
            # Greedily build subarrays from left to right
            for num in nums:
                currSum += num

                # If adding num exceeds the allowed maximum sum
                # we must start a new subarray 
                if currSum > largest:
                    subarrays += 1 
                    currSum = num # start new subarray with current element

                    # If more than k subarrays are needed,
                    # this largest values is not feasible
                    if subarrays > k:
                        return False 
            return True


        # Binary Search Boundaries

        # Minimum possible largest sum is the maximum single element
        left = max(nums)

        # Maximum possible largest sum is teh sum of the entire array
        right = sum(nums)

        # Variable to store the best (minimum) feasible largest sum
        result = right 

        # Binary search to minimize the maximum subarray sum
        while left <= right:
            mid = left + (right - left) // 2 # candidate maximum subarray sum

            if canSplit(mid):
                # mid is feasible, so try to minimize further
                result = mid
                right = mid - 1
            else:
                # mid is too small; we need to allow larger subarray sums
                left = mid + 1 

        # result holds the smallest possible maximum subarray sum
        return result 