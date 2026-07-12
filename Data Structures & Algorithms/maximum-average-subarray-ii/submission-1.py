class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')

        # start the for loop such that there are at least k elements available from the start
        for s in range(len(nums) - k + 1):
            curr_sum = 0
            sub_len = 0
            for s in range(s, len(nums)):
                sub_len += 1 
                curr_sum += nums[s]

                if sub_len >= k:
                    curr_avg = curr_sum / sub_len
                    max_avg = max(max_avg, curr_avg)

        return max_avg