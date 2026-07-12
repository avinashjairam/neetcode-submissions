class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        pieces_needed = k + 1

        max_sweetness = sum(sweetness) // pieces_needed 


        def is_possible(val):
            pieces = 0 
            current = 0 

            for x in sweetness:
                current += x 

                if current >= val:
                    pieces += 1 
                    current = 0 

            return pieces >= pieces_needed 


        # brute force 
        l = 1
        r = max_sweetness 
        ans = 0
        while l <= r:
            mid = (l + r) // 2

            if is_possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1 

        return ans 