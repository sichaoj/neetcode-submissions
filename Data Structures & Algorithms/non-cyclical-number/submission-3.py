class Solution:
    def isHappy(self, n: int) -> bool:

        init = n
        hist = []

        if init == 1:
            return True
        else:
            while init != 1 and init not in hist:
                hist.append(init)
                digits = [int(digit) for digit in str(init)]
                init = sum(x**2 for x in digits)
                
                if init == 1:
                    return True 
                elif init !=1 and init in hist:
                    return False 

            
        
            
