class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1

        r = n 

        ans = 1

        while l <= r:
            k = l + (r -l) // 2 

            coins_used = k * (k + 1) / 2

            if  coins_used < n:
                ans = k
                l = k + 1 
            else:
                r = k - 1 

        return ans