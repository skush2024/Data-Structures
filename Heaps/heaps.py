class Solution:

    def __init__(self, nums):
        self.nums = nums

    def swap(self, nums, posA, posB):
        nums[posA], nums[posB] = nums[posB], nums[posA]

    
    def genMaxHeap(self):
        if len(self.nums) <= 1 :
            return self.nums

        
        result = [self.nums[0]]

        for i in range(1,len(self.nums)):
            result.append(self.nums[i])
            
            child_pos = len(result) - 1
            parent_pos = (child_pos - 1) // 2
            

            while result[child_pos] > result[parent_pos] and parent_pos >= 0:

                self.swap(result,child_pos, parent_pos)
                
                child_pos = parent_pos
                parent_pos = (child_pos - 1) // 2
            
        return result
    
    def genMinHeap(self):
        if len(self.nums) <= 1 :
            return self.nums
        
        result = [self.nums[0]]

        for i in range(1,len(self.nums)):
            result.append(self.nums[i])
            
            child_pos = i
            parent_pos = (i - 1) // 2

            while parent_pos >= 0 and result[child_pos] < result[parent_pos]:
                self.swap(result, child_pos, parent_pos)
                child_pos = parent_pos
                parent_pos = (child_pos - 1) // 2

        return result
    
    def heapify(self, nums, idx):
        if idx == - 1:
            return nums
        
        largest = idx
        left = (2 * idx) + 1
        right = (2 * idx) + 2

        if left < len(nums) and nums[left] > nums[largest]:
            largest = left 

        if right < len(nums) and nums[right] > nums[largest]:
            largest = right

        if largest != idx :
            nums[idx], nums[largest] = nums[largest], nums[idx]

        return self.heapify(nums, idx - 1)





if __name__ == "__main__":
    nums = [10,8,5,12]
    solver = Solution(nums)

    print("Max Heap . . . . ")
    print(solver.genMaxHeap())
    print()
    print("==================")
    print("Min Heap . . . . ")
    print(solver.genMinHeap())
    print(f"==========")
    nums = [10,8,5,12]
    solver = Solution(nums)
    print(solver.nums)
    print(solver.heapify(nums, (len(nums) - 1 ) // 2))



            

