class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a_set = set()
        b_set = set()
        b_set.add(trust[0][1])
        for i in range(1,n+1):
            a_set.add(i)
        #all the pairs of trust are unique
        for t in trust:
            if t[1] not in b_set:
                return -1
            
            if t[0] in a_set:
                a_set.remove(t[0])

        if len(a_set)==1:
            return (list(a_set)[0])
        else:
            return -1

