class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = prices[0]
        max_profit = 0
        for price in prices[1:]:
            profit = price - min_price_so_far
            max_profit = max(profit, max_profit)
            min_price_so_far = min(price,min_price_so_far)

        return max_profit