"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:

    def __init__(self):
        pass

    

    def subsets(self, nums):
        nums.sort()
        result = []
        

        def explore(subsets, idx):
            result.append(subsets.copy())

            for i in range(idx, len(nums)):
                
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                
                subsets.append(nums[i])
                explore(subsets, i + 1)
                subsets.pop()
            
        explore([],0)
        return result 

if __name__ == "__main__":
    solver = Solution()

    nums = [1,2,2]
    # solver.subsets(nums)
    
    result = solver.subsets(nums)
    print(result)