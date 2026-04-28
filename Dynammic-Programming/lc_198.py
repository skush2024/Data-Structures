"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

"""

class Solution:
    def rob(self, nums) -> int:
        memo = {}

        def robMax(idx):
            if idx == 0:
                return nums[idx]
            
            if idx < 0:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            pick = nums[idx] + robMax(idx - 2)
            notPick = robMax(idx - 1)
            
            memo[idx] = max(pick, notPick)
            return memo[idx]
        
        return robMax(len(nums) - 1)

        