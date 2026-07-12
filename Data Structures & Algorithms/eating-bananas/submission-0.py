class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search bound
        # left bound - minimum possible speed is 1 banana per hour 
        # right bound - max needed speed is max(piles) - eating the largest pile 
        l, r = 1, max(piles)

        # initilize result to the max speed (worst case scenario)
        res = r 

        # binary search to find the minimum viable eating speed
        while l <= r:
            # calculate middle speed to test 
            k = (l + r) // 2

            # calculate total time needed to eat all piles at speed k
            totalTime = 0 

            for p in piles:
                totalTime += math.ceil(float(p) / k)

            # check if current speed allows finishing within h hours 
            if totalTime <= h:
                # speed k works, but we want the min speed so 
                # 1. update our result to this working speed
                res = k
                # 2. try to find an even smaller speed by searching the left half 
                r = k - 1
            else:
                # speed k is too slow (takes too much time)
                l = k + 1 

        # return the min speed that allows koko to finish within h hours
        return res 
        