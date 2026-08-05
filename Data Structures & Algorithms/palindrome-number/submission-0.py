class Solution:
    def isPalindrome(self, x: int) -> bool:
        #string
        x_string = str(x)
        if x_string == x_string[::-1]:
            return True
        else:
            return False