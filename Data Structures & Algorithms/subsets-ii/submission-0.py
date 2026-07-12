class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, cur_list = [], []
        self.helper(0, nums, cur_list, subsets)

        return subsets 

    def helper(self, i, nums, cur_list, subsets):
        # base case 
        # when i matches length of nums, we have a full subset
        if i >= len(nums):
            subsets.append(cur_list.copy())
            return 

        # include num[i]
        cur_list.append(nums[i])
        self.helper(i + 1, nums, cur_list, subsets)
        cur_list.pop()

        # skip the duplicates
        while i + 1  < len(nums) and nums[i] == nums[i+1]:
            i = i + 1

        self.helper(i + 1, nums, cur_list, subsets) 