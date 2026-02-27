"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution :
    
    def __init__(self):
        pass

    def bruteForce(self, nums, target):

        traversed = set()
        p1 = None

        for i in range(len(nums)):
            curr_elem = nums[i]
            req_elem = target - curr_elem
            if req_elem in traversed :
                p1 = i
                break
                
            else:
                traversed.add(curr_elem)
        
        p2 = None
        for j in range(p1) :
            if nums[j] == target - nums[p1] :
                p2 = j
                break

        print([p2,p1])

    


    
if __name__ == "__main__" :
    nums = [3,3]
    target = 6
    solver = Solution()
    solver.solve(nums, target)