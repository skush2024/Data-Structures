"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""


class Solution:

    def __init__(self):
        pass

    def permute(self, nums):
        result = []
        nums.sort()

        def backtrack(idx, subset=[]):

            if idx == len(nums):
                result.append(subset.copy())
                return    
            
            for i in range(len(nums)):
                if nums[i] in subset :
                    continue

                subset.append(nums[i])
                backtrack(idx + 1, subset)
                subset.pop()


        backtrack(0)
        print(result)


if __name__ == "__main__" :
    solver = Solution()
    
    nums = [1,2,3]
    solver.permute(nums)



