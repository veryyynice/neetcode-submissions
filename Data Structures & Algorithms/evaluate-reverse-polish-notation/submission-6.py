class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 3 2 2 2 + + + 
        number_stack = [int(tokens.pop(0))]
        temp =0
        while len(tokens)>0:
            next_token = tokens.pop(0)
            if next_token == "*":
                temp = int(number_stack.pop())
                number_stack[-1]*=temp
            elif next_token == "/":
                temp = int(number_stack.pop())
                number_stack[-1] = int(number_stack[-1]/temp)
            elif next_token == "+":
                temp = int(number_stack.pop())
                number_stack[-1]+=temp
            elif next_token == "-":
                temp = int(number_stack.pop())
                number_stack[-1]-=temp
            else:
                number_stack.append(int(next_token))
            print(number_stack)
        return number_stack.pop()