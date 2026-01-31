class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0  
        b = int(c**0.5) # b pointer starts at the integer square root of c and i must be interger as we're dealing with integers
        
        while a <= b:
            curr_sum = a * a + b * b  
            if curr_sum == c:
                return True  
            elif curr_sum < c:
                a += 1 
            else:
                b -= 1  
        
        return False  