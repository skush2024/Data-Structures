class Array:
    
    __array = []
    __size = None

    def __init__(self, arr:list):
        self.__array = arr
        self.__size = len(self.__array)

    def traverse(self):
        """
        Traversal in Arrays takes O(N) time.
        """
        for elem in self.__array :
            print(elem)

    def getElem(self, n:int):
        """
        Retrieving Element at a specific index takes O(1) time.
        """
        if abs(n) >= self.__size :
            raise OverflowError
        
        else :
            print(f"The element at index {n} is {self.__array[n]}")

    def insertElem(self, pos: int, elem:int):
        """
        Insertion takes O(N) time since we need to shift elements as well.
        """

        if (pos > len(self.__array)) or ( pos < 0 ) :
            raise IndexError

        else :
            temp = []
            new_arr_ptr = 0
            old_arr_ptr = 0
            
            while(new_arr_ptr <= self.__size):
                if new_arr_ptr == pos:
                    temp.insert(new_arr_ptr, elem)
                    new_arr_ptr += 1
                
                else :
                    temp.insert(new_arr_ptr,self.__array[old_arr_ptr])
                    new_arr_ptr += 1
                    old_arr_ptr += 1

            self.__array = temp
            self.__size = len(self.__array)

    def deleteElem(self, pos: int) :
        """
        Deletion takes O(N) time since we need to shift elements as well.
        """

        if (pos < 0 or pos >= self.__size):
            raise IndexError
        
        else :
            temp = []
            ptr = 0
            while(ptr < self.__size):
                if ptr != pos :
                    temp.append(self.__array[ptr])
                ptr += 1

            self.__array = temp
            self.__size = len(self.__array)

    def searchElem(self, elem_to_search:int):
        """
        Searching Takes O(N) times
        """
        for elem in self.__array : 
            if elem == elem_to_search :
                return True
            
        return False


if __name__ == "__main__":
    arr = Array([1,2,3,4])
