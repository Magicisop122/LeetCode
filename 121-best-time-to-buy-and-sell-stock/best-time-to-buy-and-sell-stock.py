class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) solution

        res = 0
        mini = prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - mini
            res = max(res, profit)
            mini = min(mini, prices[i])
        
        return res
        
        # 2 pointers solution
        
        res = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)

            else:
                l = r
            r += 1
        return res