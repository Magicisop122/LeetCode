class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        mini = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - mini
            res = max(res, profit)
            mini = min(mini, prices[i])
        
        return res
        