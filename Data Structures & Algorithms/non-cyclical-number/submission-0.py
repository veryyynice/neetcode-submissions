class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquares(num):
            sum = 0
            while num >0:
                curr = num%10
                sum+= (curr **2)
                num = num//10
            return sum
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sumSquares(n)
            if n==1:
                return True
            # if n in visited:
            #     return False
        return False
