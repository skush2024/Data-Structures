"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

import heapq


class Solution:

    def __init__(self):
        pass

    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            print(heap)

            if len(heap) > k :
                heapq.heappop(heap)
                print(heap)
            
        
        
        return heap[0]
        
        
        
        
if __name__ == "__main__":
    solver = Solution()
    nums = [3,2,1,5,6]
    print(solver.findKthLargest(nums,2))