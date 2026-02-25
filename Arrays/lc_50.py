"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start}s.")
        return result
    
    return wrapper


class Solution:

    def __init__(self):
        pass

    
    @timeit
    def brute_force(self,x, n):
        return x**n

    
    def pow(self, x: float, n:int):
        if n < 0 :
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1 :
                result *= x
            
            x *= x
            n //= 2

        return result 

if __name__ == "__main__" :
    x = 2.0
    n = -200000000
    solver = Solution()
    print("======== BRUTE FORCE =======")
    print(solver.brute_force(x,n))
    print()
    print("======== Optimized log(N) Approach =======")  
    print(solver.pow(x,n))