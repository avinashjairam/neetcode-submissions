class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Binary Search on the answer value x, for each x ask:
        # - how many products are <= x?
        # That count is monotonic in x (bigger x -> more products fit under it),
        # which is exactly what makes binary search legal

        # We want the smallest x where count (x) >= k. That x is the k-th smallest product
        # Same skeleton as koko / smallest divisor
        n2 = len(nums2)

        import bisect 

        def count_leq(x):
            total = 0

            for a in nums1:
                if a > 0: # a * b <= x
                    # b <= x/a, count elements <= floor(x/a)...but floats are unsafe
                    # use bisect on the boundary value
                    # largest b with a * b <= x -> b <= x/a
                    # bisect_right on x//a works if we're careful, but division sign issues remain
                    total += bisect.bisect_right(nums2, x / a)
                elif a < 0:
                    total += len(nums2) - bisect.bisect_left(nums2, x / a)

                else:
                    if x >= 0:
                        total += len(nums2)

            return total

        # Outer binary search on the answer value
        # Products range within [-1e10, 1e10] given the constraints
        # (values up to 1e5 in magnitude so |product| <= 1e10)
        # Standard 'smallest x where the feasibility count reaches k'
        lo, hi = -10**10, 10**10
        ans = hi

        while lo <= hi:
            mid = (lo + hi) // 2

            if count_leq(mid) >= k:
                ans = mid # enough products <= mid, try a smaller x
                hi = mid - 1
            else:
                lo = mid + 1 # too few products <= mid, need a bigger x

        return ans 