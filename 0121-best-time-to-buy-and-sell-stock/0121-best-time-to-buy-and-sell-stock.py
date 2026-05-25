class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]             
                maxProfit = max(maxProfit, profit)
        return maxProfit
            