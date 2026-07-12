class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers, l = buy, r = sell day
        l = 0
        r = 1

        # track the maximum profit found so far
        maxP = 0

        # move the sell day (right pointer) through all prices
        while r < len(prices):
            # check if current transaction is profitable (sell price > buy price)
            if prices[l] < prices[r]:
                # calculate profit for this buy-sell combination
                profit = prices[r] - prices[l]
                # update maximum profit if this transaction is better
                maxP = max(maxP, profit)

            else:
                # if sell price <= buy price, no profit possible
                # move buy day to current sell day
                l = r

            # always move to the next potential sell day
            r += 1 

        # return the maximum profit found 
        return maxP