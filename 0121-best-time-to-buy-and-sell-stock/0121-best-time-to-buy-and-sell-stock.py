class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]   # cheapest price seen so far
        maxProfit = 0          # best profit found so far

        for price in prices:
            # if current price is cheaper, update minPrice
            if price < minPrice:
                minPrice = price

            # calculate profit if we sell today
            profit = price - minPrice

            # keep the maximum profit
            if profit > maxProfit:
                maxProfit = profit

        return maxProfit