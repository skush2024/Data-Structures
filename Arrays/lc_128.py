"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def __init__(self):
        pass

    def solve(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set :
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set :
                    current += 1
                    length += 1
                
                longest = longest if length < longest else length
                
        print(longest)


if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    solver = Solution()
    solver.solve(nums)