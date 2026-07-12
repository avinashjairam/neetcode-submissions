class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    
        # single binary search that handles rotation during search process
        while l <= r:
            mid = (l + r) // 2
            # check if we found the target
            if target == nums[mid]:
                return mid

            # determine which half is properly sorted

            if nums[l] <= nums[mid]:
                # left half is sorted (no rotation in this half)
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 
                else:
                    r = mid - 1 
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1