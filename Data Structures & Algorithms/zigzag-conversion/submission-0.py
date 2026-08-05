class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #GOLIHRN
        #OGESIIG
        #n n-2, n
        #zigzags bottom up
        if numRows ==1:
            return s
        index = 0
        # curr = s[index]
        res = [[] for _ in range(numRows)]
        while index != len(s):
            for x in range(numRows):
                if index != len(s):
                    res[x].append(s[index])
                    index+=1
            for y in range(numRows-2):
                #len-1 = last index . -1
                if index != len(s):
                    res[numRows-2-y].append(s[index])
                    index+=1
        answer = ""
        for row in res:
            answer = answer+"".join(row)
        return answer
        
        