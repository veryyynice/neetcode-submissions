class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0,0
        m,n = len(word1),len(word2)
        res =[]
        while l<m or r< n:
            if l<m:
                res.append(word1[l])
            if r<n:
                res.append(word2[r])
            l+=1
            r+=1
        # if l==m and r<n:
        #     while r<n:
        #         res += word2[r]
        #         r+=1
        # if r==n and l<m:
        #     while l<m:
        #         res += word1[l]
        #         l+=1
        return "".join(res)