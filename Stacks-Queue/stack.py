class Stack:

    def __init__(self, n):
        self.size = n
        self.stack = []
        self.top = -1

    def buildStack(self, nums):
        if len(nums) > self.size :
            raise OverflowError
        
        for num in nums:
            self.top += 1
            if self.top > self.size:
                self.stack = []
                self.top = -1
                raise OverflowError

            self.stack.insert(self.top, num)
            
    
    def push(self, num):
        if self.top + 1 > self.size :
            raise OverflowError
        
        self.top += 1
        self.stack.insert(self.top, num)
        
    
    def pop(self):
        if self.top < 0 :
            raise OverflowError
        
        self.top -= 1
        return self.stack.pop()
        
        
    
    def peek(self):
        if self.top < 0 :
            raise OverflowError
        
        return self.stack[self.top]





if __name__ == "__main__":

    nums = [12,13,11,10,8,15]
    stack = Stack(6)
    stack.buildStack(nums)
    print(stack.peek())