class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        #0,1,1,2,4,7,13,24,44
        res = 1
        if n ==0:
            return 0
        if n ==1 or n==2:
            return 1
        for i in range (3, n+1):
            b_copy = b
            res = a+b+c
            
            b = c
            c = res 
            a = b_copy
        return res
            
