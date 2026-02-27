"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""

class Solution:

    def __init__(self):
        pass

    def bruteForce(self, nums, target):
        if len(nums) < 4 :
            return []
        
        output = []
        idx = len(nums) - 1
        while idx > 1 :
            for j in range(idx - 1, 1, -1):
                curr_sum = nums[idx] + nums[j]
                remaining_sum = target - curr_sum
                arr = sorted(nums[: j])
                left = 0
                right = j - 1
                while left < right :
                    curr_sum_arr = arr[left] + arr[right]
                    if curr_sum_arr == remaining_sum :
                        sorted_result = sorted([nums[idx], nums[j], arr[left], arr[right]])
                        if sorted_result not in output:
                            output.append(sorted_result)
                        left += 1
                        right -= 1
                    
                    elif curr_sum_arr < remaining_sum :
                        left += 1
                    
                    else : 
                        right -=1

            idx -= 1

        print(output)


    def solve(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        # The First Pointer that will iterate through a point after which we still have 3 values
        for i in range(n - 3):

            # We will skill duplicates so that we ensure distinct values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # We will skipp duplicates so that we ensure distinct values 
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1

                while left < right :
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left],nums[right]])
                        left += 1
                        right -= 1
                    
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        print(result)



if __name__ == "__main__" :
    nums = [-1,0,-5,-2,-2,-4,0,1,-2]
    target = -9
    solver = Solution()

    solver.solve(nums, target)