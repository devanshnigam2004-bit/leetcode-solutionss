1class Solution:
2    def maxProfit(self, prices):
3        min_price = float('inf')
4        max_profit = 0
5        
6        for price in prices:
7            if price < min_price:
8                min_price = price
9            else:
10                profit = price - min_price
11                max_profit = max(max_profit, profit)
12        
13        return max_profit