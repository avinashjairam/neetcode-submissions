class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        answer = []

        for x in range(len(nums)):
            diff = target- nums[x]

            if diff in indexes:
                return [min(indexes[diff],x), max(indexes[diff],x)]

            if nums[x] not in indexes:
            
                indexes[nums[x]] = x
