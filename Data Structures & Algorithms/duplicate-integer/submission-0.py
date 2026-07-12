class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set() 

        for x in nums:
            if x in duplicate:
                return True 
            duplicate.add(x)

        return False 
         