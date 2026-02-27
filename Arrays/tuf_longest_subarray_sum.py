"""
Length of the longest subarray with zero Sum
Problem Statement: Given an array containing both positive and negative integers, 
we have to find the length of the longest subarray with the sum of all elements equal to zero.
"""

class Solution :

    def __init__(self):
        pass

    def solve(self, nums, k=0):
        
        prefix = 0
        traversed = {}
        maxi = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix == k :
                maxi = i + 1
            
            if prefix - k in traversed :
                maxi = max(maxi, i  - traversed[prefix - k])
                    
            if prefix not in traversed:
                traversed[prefix] = i

        print(maxi)


if __name__ == "__main__" :
    nums = [6, -2, 2, -8, 1, 7, 4, -10]
    solver = Solution()
    solver.solve(nums)