class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set up binary search pointers
        l, r = 0, len(nums) - 1

        # continue until left and right pointers converge
        # use l < r (not l <=r ) because we want them to meet at the minimum 
        while l < r:
            # calculate the middle index
            # using l + (r - l) // 2
            m = l + (r - l) // 2

            # key comparison: comopare middle element with RIGHT element 
            if nums[m] < nums[r]:
                # middle < right means the right half of the array is sorted 
                # rotation point is could be at position m or in the left half 
                r = m # include m as it could be the minimum 
            else:
                # middle > right means: there's a rotation point between m and r
                # the minimum is definitely in the right half (after m)
                l = m + 1

        # when l == r, we've found the minimum element 
        return nums[l]
        