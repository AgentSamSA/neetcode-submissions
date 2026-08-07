class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0

        for end in range(1, len(prices)):
            profit = prices[end] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[end] < prices[left]:
                left = end
        
        return max_profit