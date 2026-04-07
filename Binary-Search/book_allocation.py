"""
Given an array nums of n integers, where 
nums[i] represents the number of pages in the i-th book, 
and an integer m representing the number of students, 

allocate all the books to the students so that 
each student gets at least one book, 
each book is allocated to only one student, 
and the allocation is contiguous.

Allocate the books to m students in such a way that 
the maximum number of pages assigned to a student is minimized. 

If the allocation of books is not possible, return -1.
"""

class Solution:

    def __init__(self):
        pass

    def nStudents(self, nums, max_pages):
        students = 1
        pages = 0

        for page in nums:
            if pages + page > max_pages :
                students += 1
                pages = page
            else :
                pages += page

        return students


    def findPages(self, nums, m):
        low = max(nums)
        high = sum(nums)

        while low <= high:
            max_pages_allowed = int((low + high) / 2)
            students_req = self.nStudents(nums, max_pages_allowed)
            if students_req > m :
                low = max_pages_allowed + 1
            
            else :
                high = max_pages_allowed - 1
                
        return low


if __name__ == "__main__":
    nums = [12,34,67,90]
    m = 2

    solver = Solution()
    print(solver.findPages(nums, m))