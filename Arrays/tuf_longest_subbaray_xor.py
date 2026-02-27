"""
ount the number of subarrays with given xor K

Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.
"""


class Solution :
    def __init__(self):
        pass

    def solve(self, nums, k):
        traversed = {0:1}
        prefix = 0

        count = 0

        for i in range(len(nums)):
            prefix ^= nums[i]

            if prefix ^ k in traversed :
                count += traversed[prefix ^ k]
            
            traversed[prefix] = traversed.get(prefix, 0) + 1

        print(count)


if __name__ == "__main__" :
    nums = [5, 6, 7, 8, 9]
    k = 5
    solver = Solution()
    solver.solve(nums, k)