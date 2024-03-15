class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        The asteroidCollision function takes a list of integers representing the initial positions of asteroids and 
        returns a list of integers representing the positions of surviving asteroids, ordered from left to right. 
        
        The function simulates the collision process by using a stack to keep track of the asteroids moving to the right and 
        checking the collision condition for each incoming asteroid moving to the left. 
        
        The collision occurs when the incoming asteroid moves to the left and collides with the top asteroid in the stack that moves to the right. 
        The function returns the stack after all incoming asteroids have been checked for collision.        
        
        
        :param asteroids: A list of integers representing asteroids.
        :type asteroids: List[int]
        :return: A list of integers representing the remaining asteroids after resolving collisions.
        :rtype: List[int]
        :except: This method does not raise any exceptions.
        
        Time Complexity : O(n) - n is number of elements in input array.
        Space Complexity : O(n)
        
        """
        
        
        stk = []
        for x in asteroids:
            if x > 0:
                stk.append(x)
            else:
                while stk and stk[-1] > 0 and stk[-1] < -x:
                    stk.pop()
                if stk and stk[-1] == -x:
                    stk.pop()
                elif not stk or stk[-1] < 0:
                    stk.append(x)
        return stk