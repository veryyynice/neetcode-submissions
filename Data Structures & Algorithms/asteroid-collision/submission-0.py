class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #size, and directoin , and position
        positive = []
        #1 1 1 5 -5 -5 5 -1 -1-1 => -5,-5,5
        #(a,i)
        #for every append then 
        for i in range(len(asteroids)):
            a = asteroids[i]
            alive = True

            while a <0 and len(positive)>0 and alive and positive[-1]>0:
                top = positive[-1]
                if abs(a)==top and top >0:
                    positive.pop()
                    alive = False
                    
                elif abs(a)>top and top >0 :
                    positive.pop()
                else:
                    alive = False
                    

            if alive:
                positive.append(a)
        return positive
        #at the end pop remaining
