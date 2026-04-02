class Recursion:

    def __init__(self):
        pass


    def log_1toN(self, n, reverse=False):
        if n == 1 :
            print(n)
            return

        else :
            if reverse:
                print(n)
                self.log_1toN(n - 1, reverse)
            else :
                self.log_1toN(n - 1, reverse)
                print(n)

    
    def factorial(self, n):
        if n == 1 or n == 0 :
            return 1
        
        else :
            return n * self.factorial(n - 1)
    

    def findSums(self,arr, index,current_sum,sums ):
        if index == len(arr):
            sums.append(current_sum)
            return 
        
        self.findSums(arr, index + 1, current_sum + arr[index],sums)
        self.findSums(arr, index + 1, current_sum,sums)


    def findSubsetSums(self, arr):
        sums = []
        self.findSums(arr, 0,0,sums)
        print(sums)

    def fibonaci(self, n):
        if n <= 1: 
            return n
        
        else :
            return self.fibonaci(n - 1) + self.fibonaci(n - 2) 
        
    def check_sorted(self, arr, idx):
        if idx == 1 :
            if arr[idx] >= arr[idx - 1]:
                return True

            return False
        
        else:
            return arr[idx] >= arr[idx - 1] and self.check_sorted(arr, idx - 1)


    def binary_search(self, arr, target, low, high):
        if low <= high :
            mid = int((low + high) / 2)
            if arr[mid] == target:
                return mid
            
            else :
                if arr[mid] > target:
                    return self.binary_search(arr, target, low, mid - 1)
                else :
                    return self.binary_search(arr, target, mid + 1, high)


        return -1


    def make_words(self, choices):
        result = []
        
        def explore(path):
            if len(path) == len(choices):
                result.append(path.copy())
                return 
            
            for choice in choices:
                if choice in path :
                    continue
                path.append(choice)
                explore(path)
                path.pop()

        explore([])
        return result
    
    def logNamesN(self,name, n, i=0):
        if i == n - 1:
            print(name)
            return
        else :
            print(name)
            self.logNamesN(name, n, i + 1)


    def sumNNumbers(self, n):
        if n == 0 :
            return 0
        
        return n + self.sumNNumbers(n - 1)
    

    def getSubsequences(self, arr):
        result = []

        def backtrack(i, subsequence):
            result.append(subsequence.copy())

            for j in range(i, len(arr)):
                subsequence.append(arr[j])
                backtrack( j + 1, subsequence)
                subsequence.pop()


        def backtrack1(idx, subsequence):
            if idx == len(arr) :
                result.append(subsequence.copy())
                return
            
            subsequence.append(arr[idx])
            backtrack1(idx + 1, subsequence)
            subsequence.pop()
            backtrack1(idx + 1, subsequence)

        backtrack(0,[])
        print(result)




if __name__ == "__main__" :
    executor = Recursion()
    arr = [3,1,2]

    # print(executor.findSubsetSums([1,2,3]))
    # print(executor.check_sorted(arr, len(arr) - 1))
    # print(executor.binary_search(arr, 1,0, len(arr) - 1))
    # print(executor.make_words(['k','u','s','h']))
    # print(len(executor.make_words(['k','u','s','h'])))

    # executor.logNamesN("Kush",10)

    # executor.log_1toN(10, True)
    # print(executor.sumNNumbers(3))

    executor.getSubsequences(arr)
