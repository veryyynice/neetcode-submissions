class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        #if (val<min_stack[len(min_stack)-1]):
        min_val = min(val, self.min_stack[len(self.min_stack)-1] if self.min_stack else val)
        self.min_stack.append(min_val)
        return None
    def pop(self) -> None:
        #if min_stack mepty........
        #if (min_stack[len(min_stack)-1]==stack[len(stack)-1]):
        self.min_stack.pop()
        self.stack.pop()
        return None
    def top(self) -> int:
        return(self.stack[len(self.stack)-1])
    def getMin(self) -> int:
        #if we run out we repopulate
        return(self.min_stack[len(self.min_stack)-1])