"""
	문제    : 주식을 사고팔기 가장 좋은 시점2
    유형    : 그리디
	난이도  : 중
	시간    : 
	uri    : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    날짜    : 1x(21.6.25), 2o(21.6.28)
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1] - prices[i] , 0) for i in range(len(prices) - 1))

prices = [7,1,5,3,6,4]
