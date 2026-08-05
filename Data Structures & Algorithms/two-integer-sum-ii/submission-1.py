class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1,p2 = 0,len(numbers)-1
        
        # while numbers[p2] >= target:
        #     p2-=1
        while numbers[p2] > numbers[p1]:
            if numbers[p1] + numbers[p2] > target:
                p2-=1
                p1 =0
                continue
            if numbers[p1] == target-numbers[p2]:
                return [p1+1,p2+1]
            else:p1+=1
