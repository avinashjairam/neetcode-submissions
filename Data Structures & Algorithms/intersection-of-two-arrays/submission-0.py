class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        nums2.sort()

        def binary_search(x):
            l = 0 
            r = len(nums2) - 1 

            while l <= r:
                mid = (l + r) // 2

                if nums2[mid] == x:
                    return True
                elif nums2[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1 

            return False 

        for x in nums1:
            if binary_search(x):
                if x not in result:
                    result.append(x)

        return result 