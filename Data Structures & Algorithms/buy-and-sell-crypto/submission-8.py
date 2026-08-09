class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0
        for end in range(1, len(prices)):
            
            profit = prices[end] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if prices[end] < prices[left]:
                left = end
        
        return max_profit