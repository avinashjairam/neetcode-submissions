class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = len(nums)

        for x in range(len(nums)):
            if nums[x] >= target:
                ans = x
                break

        return ans