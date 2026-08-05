class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            # if i ==len(temperatures)-1: 
            #     res.append(0)
            #     continue
            current = temperatures[i]
            if len(stack)==0:
                stack.append(i)
            else:
                if current<= temperatures[stack[-1]]: 
                    stack.append(i)
                else:
                    while stack and temperatures[stack[-1]]<current:
                        res[stack[-1]]=i-stack[-1]
                        stack.pop()
                    stack.append(i)
        
        return res
