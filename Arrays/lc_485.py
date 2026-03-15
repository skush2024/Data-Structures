"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:

    def __init__(self):
        pass

    def solve(self, nums):
        maxi = 0
        sum_temp = 0 
        
        for i in range(len(nums)):
            sum_temp += nums[i]
            if nums[i] == 0 :
                maxi = max(maxi, sum_temp)
                sum_temp = 0
        
        return (max(maxi, sum_temp))



if __name__ == "__main__":
    nums = [1,0,1,1,0,0,1,1,1,0]
    solver = Solution()
    solver.solve(nums)