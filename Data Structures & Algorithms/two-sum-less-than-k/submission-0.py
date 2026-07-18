class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        ans = -1 

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k:
                    ans = max(ans, nums[i] + nums[j])

        return ans 