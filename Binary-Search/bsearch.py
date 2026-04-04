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




if __name__ == "__main__":
    arr = [1,2,3,4,5,8]
    target = 3

    solver = Search(arr, target)
    # print(solver.recursive_search(0, len(arr) - 1))
    print(solver.search())




