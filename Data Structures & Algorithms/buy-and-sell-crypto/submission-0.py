class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        n = len(prices)

        max_profit = 0

        while r < n:
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r]-prices[l])
            elif prices[l] > prices[r]:
                l = r
            r+=1

        return max_profit