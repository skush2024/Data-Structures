"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""



class Solution:

    def __init__(self, nums):
        self.nums = nums
    
    def bruteForce(self):
        output = set()
        
        for i in range(len(self.nums) - 2):
            elem = self.nums[i]
            target = 0 - elem
            
            traversed = {self.nums[i + 1]: i + 1}
            
            for j in range(i + 2, len(self.nums)):
                new_elem = self.nums[j]
                if target - new_elem in traversed :
                    output.add((elem, target - new_elem, new_elem))
                
                traversed[self.nums[j]] = j

        output = set((tuple(sorted(i)) for i in output))
        output = [list(i) for i in output]
        print(output)

    def solve(self, target=0):
        self.nums.sort()
        output = []


        for i in range(len(self.nums) - 2):
            
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue
            
            left, right = i + 1, len(self.nums) - 1

            while left < right :
                total = self.nums[i] + self.nums[left] + self.nums[right]

                if total == target :
                    output.append([self.nums[i], self.nums[left], self.nums[right]])
                    left += 1
                    right -= 1

                    while left < right and self.nums[left] == self.nums[left - 1]:
                        left += 1

                    while left < right and self.nums[right] == self.nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                
                else :
                    right -= 1

        return output

                    





if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    solver = Solution(nums)
    print(solver.solve())
