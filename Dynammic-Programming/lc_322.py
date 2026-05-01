"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = int(1e9)

        dp = [[0] * (amount + 1) for _ in range(n)]

        # Base case
        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]
            else:
                dp[0][t] = INF

        # Fill table
        for idx in range(1, n):
            for t in range(amount + 1):
                not_take = dp[idx - 1][t]

                take = INF
                if coins[idx] <= t:
                    take = 1 + dp[idx][t - coins[idx]]

                dp[idx][t] = min(take, not_take)

        ans = dp[n - 1][amount]
        return ans if ans != INF else -1