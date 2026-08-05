class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #return 
        #Input: candidates = [9,2,2,4,6,1,5], target = 8

        res = []
        candidates = sorted(candidates)
        def helper(i,total, current_nums):
            if total == target:
                res.append(current_nums.copy())
                return
            if i >= len(candidates) or total > target:
                return


        
            current_nums.append(candidates[i])
            helper(i+1,total+candidates[i],current_nums)
            #do with current letter
            current_nums.pop()
            while (i <= (len(candidates)-2) and candidates[i+1] == candidates[i]):
                i+=1
            helper(i+1,total,current_nums)
            #do without current letter
        helper(0,0,[])
        return(res)