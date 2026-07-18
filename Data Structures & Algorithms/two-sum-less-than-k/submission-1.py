class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) -1 

        nums.sort()
        
        ans = -1
        while l < r:

            if nums[l] + nums[r] < k:
                ans = max(ans, nums[l] + nums[r])
                l += 1

            elif nums[l] + nums[r] >= k:
                r -= 1

        return ans 