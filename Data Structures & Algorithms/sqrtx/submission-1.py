class Solution:
    def mySqrt(self, x: int) -> int:
        high = x // 2 + 2 

        ans = -1
        for i in range(high):
            if i * i <= x:
                ans = i 
            else:
                break

        return ans 
              