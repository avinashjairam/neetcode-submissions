class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        comb = []

        def helper(i, nums, target, results, comb):
            if sum(comb) == target:
                results.append(comb.copy())
                return 
            
            if i >= len(nums) or sum(comb) > target:
                return 

            comb.append(nums[i])
            helper(i, nums, target, results, comb)

            comb.pop()

            helper(i + 1, nums, target, results, comb)

        helper(0, nums, target, results, comb)

        return results
