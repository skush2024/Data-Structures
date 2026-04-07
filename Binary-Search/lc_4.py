"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
"""

class Solution:

    def __init__(self):
        pass
    
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2) :
            nums1, nums2 = nums2, nums1
        
        low = 0
        high = len(nums1)
        half = ((low + high) // 2) + 1

        while True :
            i = (low + high) // 2
            j = half - i

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < len(nums1) else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < len(nums2) else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2:
                    return (min(right1, right2))
                return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2 :
                high = i - 1
            
            else :
                low = i + i

if __name__ == "__main__":
    nums1 = [1,3,5]
    nums2 = [2,4]

    solver = Solution()
    print(solver.findMedianSortedArrays(nums1, nums2))