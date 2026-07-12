class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:


        def can_split(total):
            curr = 0 
            pieces = 1 

            for x in nums:
                curr += x 

                if curr > total:
                    pieces += 1
                    curr = x 

                if pieces > k:
                    return False 

            return True 


        # smallest possible subarray is min value of nums
        l = max(nums)

        # largest possible subarray sum is the sum of the entire sums 
        r = sum(nums)

        ans = r
        while l <= r:
            mid = (l + r) //2

            if can_split(mid):
                ans = mid 
                r = mid - 1 
            else:
                l = mid + 1 

        return ans 