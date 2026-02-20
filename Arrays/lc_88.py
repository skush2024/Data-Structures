"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
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
    nums1 = None
    nums2 = None
    m = None
    n = None

    def __init__(self, nums1:list, nums2:list, m:int, n:int):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n


    @timeit
    def solve(self):
        total = self.m + self.n - 1
        ptr_k = total

        ptr_m = self.m - 1
        ptr_n = self.n - 1

        while (ptr_m >= 0 and ptr_n >=0):
            if (self.nums1[ptr_m] >= self.nums2[ptr_n]):
                self.nums1[ptr_k], self.nums1[ptr_m] = self.nums1[ptr_m], self.nums1[ptr_k]
                ptr_m -= 1
            
            else :
                self.nums1[ptr_k] = self.nums2[ptr_n]
                ptr_n -= 1
            
            ptr_k -= 1

        
        while(ptr_m >= 0 and ptr_k >= 0):
            self.nums1[ptr_k], self.nums1[ptr_m] = self.nums1[ptr_m], self.nums1[ptr_k]
            ptr_k -= 1
            ptr_m -= 1

        while(ptr_n >= 0 and ptr_k >= 0):
            self.nums1[ptr_k] = self.nums2[ptr_n]
            ptr_n -= 1
            ptr_k -= 1





if __name__ == "__main__":
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    solver = Solution(nums1, nums2,m,n)
    print("===== Solution =====")
    print(solver.nums1)
    print()
    print(solver.nums2)
    print("Solving . . . . . ")
    solver.solve()
    print()
    print(solver.nums1)







