class Stack:
    def __init__(self):
        self.__top = -1
        self.__stack = []
        self.__mini = None
    
    def push(self, num):
        if self.__top == -1 :
            self.__mini = num
            self.__stack.append(num)
            self.__top += 1
            return
        
        if num > self.__mini:
            self.__stack.append(num)
            self.__top += 1
            return 
        
        self.__stack.append((2 * num) - self.__mini)
        self.__top += 1
        self.__mini = num
        return
    
    def pop(self):
        elem = self.__stack.pop()
        if elem < self.__mini :
            value = (2 * self.__mini - elem)
            self.__mini = value
            self.__top -= 1
            return value
        
        return elem

    def getMin(self):
        return self.__mini


if __name__ == "__main__" :
    nums = [12,10,15,16,18]
    mStack = Stack()
    
    for num in nums:
        mStack.push(num)
