"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

class Solution():
    
    def __init__(self):
        pass

    def solve(self, nums):
        record = {}

        for element in nums :
            print(" =========== ")
            print(element)
            print(record)
            if element in record :
                record[element] += 1

            else :
                if len(record) >= 2 :
                    record = {key: value - 1 for key, value in record.items() if value - 1 > 0}
                else :
                    record[element] = 1
             
            print(" =========== ")
       
        mini = int(len(nums) / 3) + 1
        
        output = []
        for candidate in record :
            cnt = len([1 for elem in nums if elem == candidate])
            if cnt >= mini :
                output.append(candidate) 

        print(output)

if __name__ == "__main__" :
    nums = [4,2,1,1]
    solver = Solution()
    solver.solve(nums)


