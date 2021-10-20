class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        ans = 0
        # current price
        c_price = prices[0]
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                ans += prices[i] - c_price
                c_price = prices[i + 1]
        if prices[i] <= prices[-1]:
            ans += prices[-1] - c_price

        return ans

