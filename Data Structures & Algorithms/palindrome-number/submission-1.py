import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        # Find the divisor to extract the leftmost digit
        left_divisor = 10 ** int(math.floor(math.log10(x)))
        right_divisor = 1

        while left_divisor > right_divisor:
            left_digit = (x // left_divisor) % 10
            right_digit = (x // right_divisor) % 10

            if left_digit != right_digit:
                return False

            left_divisor //= 10
            right_divisor *= 10

        return True
