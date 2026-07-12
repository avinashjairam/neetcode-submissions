class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Assign arrays to A and B for cleaner variable names
        A, B = nums1, nums2 

        # Calculate total length and half point (where median would be)
        total = len(nums1) + len(nums2)
        half = total // 2 

        # Ensure A is the smaller array to optimize binary search
        # Smaller array takes less time 
        if len(B) < len(A):
            A, B = B, A 

        # Binary Search bounds on array A 
        l, r = 0, len(A) - 1 

        while True:
            i = (l + r) // 2 # find partition index

            j = half -i - 2 # calculate corresponding partition in array B
            # we need exactly half elements in the left portion total.
            # we subtract 2 because i and j are 0 - indexed 

            # get boundary elements around partiion points 
            # use += infinity for out of bounds to handle edge cases 

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i + 1] if i + 1 < len(A) else float('infinity')
            Bleft = B[j] if j >= 0 else float('-infinity')
            Bright = B[j+1] if (j+1) < len(B) else float('infinity')

            # check if partition is correct, all left elements <= all right elements
            if Aleft <= Bright and Bleft <= Aright:
                # correct partition found! Calculate median based on total length
                if total % 2:
                    # odd total length: median is the smaller of the two leftmost right elements
                    return min(Aright, Bright)
                # even total length: median is average of maxleft and minright elements 
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2 
            
            elif Aleft > Bright:
                r = i - 1 # too many elements from A in left portion
            else:
                l = l + 1 # too few elements from A in the left porition