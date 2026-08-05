class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #stack
        #when n=3, 3 parantheses 6 results
        #always closed parantheses = open 
        # open ,closed = 0,0
        # res = []
        # curr= ""
        # curr.append("(")

        # open+=1
        #     if open==n and closed==n:
        #now I know. backtrack == recursive
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN <openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
            
        backtrack(0,0)
        return res

 