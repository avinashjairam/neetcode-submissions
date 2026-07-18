from bisect import bisect_left 

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        n = len(nums)
        r = n 

        while l <= r:
            x = (l + r) // 2 

            pos = bisect_left(nums, x)

            count = n - pos 

            if count == x:
                return count 
            elif count > x:
                l = x + 1 
            else:
                r = x - 1

        return -1 