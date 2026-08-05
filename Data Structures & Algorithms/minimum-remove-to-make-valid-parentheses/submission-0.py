class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #lowercase 26
        #and ()

        #remove in num of parentehse so its valid
        #return resulting string

        if len(s)==0:
            return s
        open_stack = []
        s = list(s)
        #i is index
        for i,char in enumerate(s):
            if char == ")":
                if len(open_stack)==0:
                    s[i] = ''
                else:
                    open_stack.pop()
            elif char == "(":
                open_stack.append(i)
        #if len(stack)!= 0:
        #   return 
        while open_stack:
            s[open_stack.pop()]=''
        return "".join(s)