class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:return True
        s = s.replace(" ","").lower()
        l,r  = 0, (len(s))-1
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        while l < r and l < len(s) and r > -1:
            while l< len(s) and s[l] not in alphabet and l < r:
                l+=1
            while  r >-1 and s[r] not in alphabet and l < r:
                r-=1
            if l>r or s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True