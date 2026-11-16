class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for j in range(len(prices)):
            min_price = min(prices[j], min_price)

            profit = prices[j] - min_price

            max_profit = max(profit, max_profit)

        return max_profit


        

        