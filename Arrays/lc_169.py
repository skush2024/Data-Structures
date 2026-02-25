"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    
    def __init__(self):
        pass

    def solve(self, nums):
        record = {}

        for element in nums : 
            if element in record :
                record[element] += 1
            
            else :
                if len(record) >= 2 :
                    record = {key : value - 1 for key, value in record.items() if value - 1 > 0}
                    record[element] = 1

                else :
                    record[element] = 1
            

        max = None
        max_count = 0

        for key, value in record.items():
            if value >= max_count :
                max = key
                max_count = value
        
        return max

    def betterApproach(self, nums):
        count = 1
        element = nums[0]

        for i in range(1, len(nums)):
            curr_elem = nums[i]
            if count == 0 :
                count = 1
                element = curr_elem 
            else :
                if curr_elem == element :
                    count += 1
                else :
                    count -= 1
        
        return element



if __name__ == "__main__":
    nums = [1,2,3,2,2,4,2]
    solver = Solution()
    print(solver.solve(nums))
    print(solver.betterApproach(nums))