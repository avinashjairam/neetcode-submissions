class Solution:
    def arrangeCoins(self, n: int) -> int:
        floors = 0 
        coins_used = 0
        coins_needed_next_floor = 1 

        while n - coins_needed_next_floor >= 0 :
            floors += 1 
            coins_needed_next_floor += floors + 1

        return floors 