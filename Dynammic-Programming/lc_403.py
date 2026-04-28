"""
A frog is crossing a river. 
The river is divided into some number of units, and at each unit, there may or may not exist a stone. 
The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.
"""

class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        target = stones[-1]
        memo = set()

        def dfs(pos, k):
            if (pos, k) in memo:
                return False
            
            if pos == target:
                return True
            
            for jump in [k-1, k, k+1]:
                if jump > 0 and pos + jump in stone_set:
                    if dfs(pos + jump, jump):
                        return True
            
            memo.add((pos, k))
            return False

        return dfs(0, 0)