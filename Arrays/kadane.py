import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f" Time Taken by {func.__name__}: {end - start}")
        return result 

    return wrapper



class Kadane:

    nums = None
    subArrays = []
    allSums = []

    def __init__(self, nums:list):
        self.nums = nums
    
    def __genSubArrays(self):
        i = 0
        while i < len(self.nums) :
            for nelem in range(i, len(self.nums)):
                self.subArrays.append(list(self.nums[i:nelem]))

            i += 1

    def __getSum(self):
        for subarray in self.subArrays :
            self.allSums.append(sum(subarray))


    @timeit
    def bruteForce(self):
        """
        Time Taken is O(n^3)
        """

        self.__genSubArrays()
        self.__getSum()
        return max(self.allSums)


    @timeit
    def optimizedBruteForce(self):
        """
        Time Taken is O(n^2)
        """
        i = 0
        maxSum = 0
        while i < len(self.nums):
            for nelem in range(i, len(self.nums)):
                maxSum = sum(self.nums[i:nelem]) if sum(self.nums[i:nelem]) > maxSum else maxSum
            i += 1
        
        return maxSum


    @timeit
    def solve(self):
        curSum = 0
        maxSum = 0

        for elem in self.nums: 
            curSum += elem
            maxSum = maxSum if maxSum > curSum else curSum

            if curSum < 0 :
                curSum = 0
        
        return maxSum
    




if __name__ == "__main__":
    nums = [3,-4,5,4,-1,7,-8]
    kadane = Kadane(nums)

    
    print("====== Kadane ======")
    print(kadane.solve())
    print()
    print("====== Optimized Brute Force ======")
    print(kadane.optimizedBruteForce())
    print()
    print("====== BRUTE FORCE ======")
    print(kadane.bruteForce())
    