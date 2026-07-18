class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # ensuring num1 is the larger array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        values = set(nums1)

        result = set()

        for x in nums2:
            if x in values:
                result.add(x)

        return list(result) 