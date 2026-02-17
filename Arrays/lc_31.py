"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""

def solution(nums):
    break_point = 0
    n_elems = len(nums)
    ptr = n_elems - 1

    while ptr > 0:
        if nums[ptr] > nums[ptr - 1] :
            break_point = ptr
            
            if break_point != 0 :
                elem = nums[ptr - 1]
                min_ind = break_point
                for i in range(break_point, n_elems):
                    if (nums[i] < nums[min_ind]) and (nums[i] > elem) :
                        min_ind = i

                temp = nums[min_ind]
                nums[min_ind] = nums[break_point - 1]
                nums[break_point - 1] = temp

            break

        ptr -= 1


    if break_point == 0:
        nums.reverse()

    else :
        # Sort break_point :: 

        sort_pos = len(nums) - 1
        while sort_pos >= break_point:
            for i in range(break_point, sort_pos):
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
            sort_pos -= 1
        
if __name__ == "__main__" :
    nums = [2,2,1]
    solution(nums)
    print(nums)