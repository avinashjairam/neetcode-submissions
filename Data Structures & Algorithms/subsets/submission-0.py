class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets_list , cur_list = [], []
        self.helper(0, nums, cur_list, subsets_list)
        return subsets_list 

    def helper(self, i, nums, cur_list, subsets_list):
        if i >= len(nums):
            subsets_list.append(cur_list.copy())
            return 

        # include the current number
        cur_list.append(nums[i])
        self.helper(i + 1, nums, cur_list, subsets_list)
        cur_list.pop()

        # exclude the current number
        self.helper(i+1, nums, cur_list, subsets_list)
