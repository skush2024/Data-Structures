"""
Given two numbers N and M, find the Nth root of M. 
The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. 
If the Nth root is not an integer, return -1.
"""

class Solution:

    def __init__(self):
        pass

    def pow(self, x,n):
        if n < 0:
            x = 1 / x
            n = -n

        if n == 1: 
            return x
        if n == 2: 
            return x*x
        
        if n % 2 == 0:
            return self.pow(x,2) * self.pow(x, n - 2)
        
        else :
            return x * self.pow(x, n-1)
        
    def myPow(self, x, n):
        if n < 0 :
            x = 1 / x
            n = -N

        result = 1

        while n > 0:
            if n % 2 == 1 :
                result *= x

            x *= x
            n //= 2

        return result

    def nthRoot(self, m,n):
        if n == 2 :
            for i in range(int(m/2) + 1):
                if i * i == m :
                    return i
                
            return -1
        
        if n % 2 == 0:
            return self.nthRoot(self.nthRoot(m,2), int(n/2))
        
        else :
            if m % n != 0 :
                return -1
            return self.nthRoot(int(m // n), n - 1)



if __name__ == "__main__":
    N = 4
    M = 69
    
    solver = Solution()

    print(solver.nthRoot(M,N))


