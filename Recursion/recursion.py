class Recursion:

    def __init__(self):
        pass


    def log_N(self, n):
        if n == 1 :
            print(n)

        else :
            self.log_N(n - 1)
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


if __name__ == "__main__" :
    executor = Recursion()
    arr = [1,2,3,3,4]

    # print(executor.findSubsetSums([1,2,3]))
    # print(executor.check_sorted(arr, len(arr) - 1))
    # print(executor.binary_search(arr, 1,0, len(arr) - 1))
    print(executor.make_words(['k','u','s','h']))
    print(len(executor.make_words(['k','u','s','h'])))