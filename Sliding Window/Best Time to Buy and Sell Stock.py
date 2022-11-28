"""
leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given an array where the element at the index i represents the price of a stock on day i,
find the maximum profit that you can gain by buying the stock once and then selling it.

constraints:
- We can’t sell before buying a stock, that is, the array index at which stock is bought will always be less than the index at which the stock is sold.
- 1 <= array.length <= 10^5
- 0 <= array[i] <= 10^4

test case 1:
array = [10, 4, 11, 1, 5]
output: 7

test case 2:
array = [7, 7, 6, 6, 6]
output: 0

test case 3:
array = [4, 10, 5, 1, 6, 7]
output: 6
"""

from typing import List

def max_profit(stock_prices: List[int]) -> int | float:
    min_stock_price = float("inf")    
    max_profit_so_far = 0
    
    # we trying to find the minimum stock price and the maximum profit simultaneously
    for stock_price in stock_prices:
        min_stock_price = min(min_stock_price, stock_price)
        max_profit_so_far = max(max_profit_so_far, stock_price - min_stock_price)
        
    return max_profit_so_far

# test this code with the above test cases
print(max_profit([10, 4, 11, 1, 5]))
print(max_profit([7, 7, 6, 6, 6]))
print(max_profit([4, 10, 5, 1, 6, 7]))