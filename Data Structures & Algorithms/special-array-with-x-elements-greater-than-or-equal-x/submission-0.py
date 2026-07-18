class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        def greater_than_x(x):
            count = 0
            for i in nums:
                if i >= x:
                    count += 1

            return count

       
        for x in range(len(nums) + 1):
            if greater_than_x(x) == x:
                return x

    
        return -1