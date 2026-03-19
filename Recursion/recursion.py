class Recursion:

    def __init__(self):
        pass


    def log_N(self, n):
        if n == 1 :
            print(n)

        else :
            print(n)
            self.log_N(n - 1)

    
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



if __name__ == "__main__" :
    executor = Recursion()

    print(executor.findSubsetSums([1,2,3]))