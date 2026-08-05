class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        #char ( ord(z) - ord(a) /8 +3  + ord (a))
        def helper(i,curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            #for i in range(3):
            digit = digits[i]
            for letter in digitToChar[digit]:
                helper(i+1,curr_str+letter)
        if digits:
            helper(0,"")

        return res

            