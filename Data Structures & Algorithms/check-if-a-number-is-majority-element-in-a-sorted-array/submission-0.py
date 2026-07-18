class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        # use binary search to find the first index whose value
        # is greater than or equal to target. 

        l = 0
        r = n - 1 
        first= -1

        while l <= r: 
            mid = l + (r-l) // 2 

            if nums[mid] >= target:
                first = mid 
                r = mid - 1
            else:
                l = mid + 1 

        # A majority element must appear more than n//2 times 
        # Therefore, it must appear at least n//2 + 1 times
        check_index = first + n // 2

        return (
            # make sure binary search finds a valid index
            first < n
            # make sure the majority check position is inside the array
            and check_index < n 

            # confirm that the first value found is actually target
            # It could otherwise be the first value greater than target 
            and nums[first] == target

            # confirm that target extends far enough to occupy 
            # more than half the array 
            and nums[check_index] == target 


        )