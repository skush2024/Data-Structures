"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time Taken by {func.__name__}: {end - start}")
        return result 

    return wrapper


class Solution:

    prices = None

    def __init__(self, prices):
        self.prices = prices.copy()

    
    @timeit
    def solve(self):
        """
        Time Taken is O(n)
        """
        buyPrice = self.prices[0]
        profit = 0


        for price in self.prices:
            unrealizedProfit = price - buyPrice
            profit = max(profit, unrealizedProfit)
            buyPrice = min(buyPrice, price)

        return profit


if __name__ == "__main__":
    prices = [7,6,4,3,1]
    solver = Solution(prices=prices)
    print(solver.solve())