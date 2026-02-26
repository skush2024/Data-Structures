"""
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
"""

class Solution:

    def __init__(self):
        pass

    def merge(self, nums, low, mid, high):
        count = 0
        j = mid + 1

        # Count reverse pairs
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))

        # Merge the two halves
        temp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= high:
            temp.append(nums[j])
            j += 1

        # Copy the sorted elements back into the original array
        for i in range(len(temp)):
            nums[low + i] = temp[i]

        return count

    def mergeSort(self, nums, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2
        count = self.mergeSort(nums, low, mid)
        count += self.mergeSort(nums, mid + 1, high)
        count += self.merge(nums, low, mid, high)

        return count


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    solver = Solution()
    print(solver.mergeSort(nums, 0, len(nums) - 1))  # Output: 4