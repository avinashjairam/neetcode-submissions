class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        mid = num // 2 + 1 

        for x in range(1, mid + 1):
            if x * x == num:
                return True 

        return False 