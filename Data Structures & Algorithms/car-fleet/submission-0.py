class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #brute force :
        #n^2 where we iterate and update each pos for every 1 sec, 
        #if a car touches the next one, we can remove from pool (stack) of cars that can join fleet
        stack = [] #each car's times
        
        #sort descending, leaders are bottlenecks
        # time = (target - position) / speed
        combo = list(zip(position, speed))
        combo.sort(reverse=True)
        for p,s in combo:
            time = (target-p)/s
            # time = time.roof()
            if len(stack)==0:
                stack.append(time)
            if stack[len(stack)-1] < time:
                stack.append(time)

        print(stack)
        return len(stack)

