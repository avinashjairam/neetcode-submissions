class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        pieces_needed = k + 1

        max_sweetness = sum(sweetness) // pieces_needed

        def is_valid(val):
            pieces = 0
            count = 0
            for s in sweetness:
                count += s
                if count >= val:
                    pieces += 1 
                    count = 0

            return pieces >= pieces_needed


        low = 0

        high = max_sweetness

        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if is_valid(mid):
                ans = mid
                low = mid + 1 
            else:
                high = mid - 1 

        return ans 
        