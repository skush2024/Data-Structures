"""
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteroid in the array represent their relative position in space.

For each asteroid, 
the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 

If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.
"""

class Solution:
    def asteroidCollision(self, asteroids) :
        stack = []
    
        for comet in asteroids:
            while stack and comet < 0 and stack[-1] > 0 :
                if stack[-1] < -comet:
                    stack.pop()
                    continue
        
                elif stack[-1] == -comet:
                    stack.pop() 
                
                break
            
            else:
                stack.append(comet)

        return stack

if __name__ == "__main__":
    solver = Solution()
    nums = [3,5,-6,2,-1,4]
    print(solver.asteroidCollision(nums))