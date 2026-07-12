class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort() # sort to enable two pointer technique and handle duplicates

        for i, a in enumerate(nums):
            # early termination: if smallest number > 0, sum can't be 0
            if a > 0:
                break 

            # skip duplicate values for first number, only check from second occurence onward
            if i > 0 and a == nums[i - 1]:
                continue

            # two pointer search for remaining pair that sums to -a
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1 # sum too large, need smaller number
                elif threeSum < 0:
                    l += 1 # sum too small, need larger number 
                else:
                    # found valid triplet
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1 # move both pointers to find other pairs 

                    # skip duplicate values for second number 
                    # keep moving left pointer while we see duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
        