class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Get length of mountainArr
        n = mountainArr.length()

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val = mountainArr.get(mid)
            left_val = mountainArr.get(mid -1)
            right_val = mountainArr.get(mid + 1)

            if mid_val > left_val and mid_val > right_val:
                peak = mid
                break
            
            elif mid_val > left_val:
                l = mid + 1

            else:
                r = mid - 1

        l = 0 
        r = peak
        
        while l <= r:
            mid = (l + r) // 2

            if mountainArr.get(mid) == target:
                return mid 

            elif mountainArr.get(mid) < target:
                l = mid + 1 
            else:
                r = mid - 1

        l = peak
        r = n - 1

        while l <= r:
            mid = (l + r) // 2

            if mountainArr.get(mid) == target:
                return mid 

            elif mountainArr.get(mid) < target:
                r = mid - 1
            
            else:
                l = mid + 1 

        return - 1 