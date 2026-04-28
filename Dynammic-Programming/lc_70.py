"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]

        return climb(0)
    
if __name__ == "__main__":
    solver = Solution()

    print(solver.climbStairs(3))