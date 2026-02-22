"""
Given an integer array nums. Return the number of inversions in the array.

Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

It indicates how close an array is to being sorted.

A sorted array has an inversion count of 0.

An array sorted in descending order has maximum inversion.
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time Taken by {func.__name__}: {end - start}")
        return result 

    return wrapper


class Solution:
    nums = None


    def __init__(self, nums):
        self.nums = nums

    
    def count_smaller_elements(self, pos):
        count = 0
        for i in range(pos + 1):
            if self.nums[i] > self.nums[pos]:
                count += 1
        
        return count
    
    @timeit
    def brute_force(self):
        count = 0
        for i in range(len(self.nums)) :
            count += self.count_smaller_elements(i)

        return count



    def merge(self, arr1, arr2):
        i = 0 
        j = 0
        count = 0
        arr = []

        while(i < len(arr1) and j < len(arr2)):
            if arr1[i] <= arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                count += len(arr1) - i
                arr.append(arr2[j])
                j += 1
        
        while(i < len(arr1)):
            arr.append(arr1[i])
            i += 1

        while(j < len(arr2)):
            arr.append(arr2[j])
            j += 1

        return arr, count

    def mergeSort(self, nums):
        if len(nums) <= 1 :
            return nums,0

        else :
            mid = int(len(nums) / 2)
            lpart, left_inv = self.mergeSort(nums[:mid])
            rpart, right_inv = self.mergeSort(nums[mid:])
            arr, cnt = self.merge(lpart, rpart)
            total_inv = left_inv + right_inv + cnt
            return arr, total_inv
    
if __name__ == "__main__":
    nums = [2, 4, 1, 3, 5]
    solver = Solution(nums)
    print(solver.mergeSort(solver.nums))
