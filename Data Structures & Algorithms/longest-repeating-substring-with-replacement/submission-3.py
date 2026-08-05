class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #slding windowm
        #s is uppercase
        # k - at most k replacement
        #return longestsub string with only1 charatcter
        L = 0
        res = 1
        k_counter = 0
        count = {}
        maxf = 0
        for R in range(len(s)):
            count[s[R]] = 1+count.get(s[R],0)
            maxf = max(maxf, count[s[R]])
            while (R-L+1-maxf>k):
                count[s[L]]-=1
                L+=1

            res= max(res, R-L+1)

        return res

