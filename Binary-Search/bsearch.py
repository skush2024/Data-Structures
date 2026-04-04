class Search:

    def __init__(self, arr, target):
        arr.sort()
        self.arr = arr
        self.target = target
        pass

    def recursive_search(self, low, high):
        if low > high :
            return -1
        
        mid = int((low + high)/2)
        
        if self.arr[mid] == self.target:
            return mid
        
        if self.arr[mid] > target:
            return self.recursive_search(low, mid - 1)
        
        else :
            return self.recursive_search(mid + 1, high)
        
    def search(self):
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = int((low + high)/2)
            if self.arr[mid] == self.target:
                return mid
            
            if self.arr[mid] > target:
                high = mid - 1
            
            else :
                low = mid + 1
        
        return -1


    def lowerbound(self, n):
        ans = len(self.arr)

        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = int( (low + high) / 2)
            
            if self.arr[mid] >= n :
                ans = mid
                high = mid - 1
            
            else :
                low = mid + 1
        
        return(ans)

    def upperbound(self, n):
        ans = len(self.arr)

        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = int( (low + high) / 2)

            if self.arr[mid] > n :
                ans = mid
                high = mid - 1
            
            else :
                low = mid + 1

        return ans


if __name__ == "__main__":
    arr = [3,5,8,15,19,19,19]
    target = 3

    solver = Search(arr, target)
    # print(solver.recursive_search(0, len(arr) - 1))
    print(solver.lowerbound(19))
    print(solver.upperbound(19))




