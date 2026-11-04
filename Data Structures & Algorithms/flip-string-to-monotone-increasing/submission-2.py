class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        countOne = 0

        for c in s:
            if c == "1":
                countOne +=1
            else:
                res = min(res+1,countOne)
        return res
