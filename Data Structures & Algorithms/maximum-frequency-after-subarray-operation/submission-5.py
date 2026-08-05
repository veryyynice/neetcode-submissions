class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #find subarray  (non empty) dand add x to those elements
        #find maximum  frequncy of value k after adding magic x value 

        #find duplicates or frequncy map
        #find most frequnt duplicate other than k
        
        #example: k is 10.     2,2,10,2,2

        #return frequency

        #check youtube
        max_gain = 0 #max profit
        frequency = defaultdict(int)
        for num in nums:
        #     # 1. Update the 'score' for the current number
        #     #[k] is our baseline
        #     frequency[num]=max(frequency.get(num,0),frequency.get(k,0))+1
        #     # 2. Update the max differences found so far
        #     max_freq = max(frequency[num]-frequency[k],max_freq)

        # return frequency.get(k,0)+max_freq
            #curr, reset to k (or 0) if bad
            frequency[num] = max(frequency[num],frequency[k]) +1

            max_gain = max(frequency[num]-frequency[k] , max_gain)
        return (frequency[k]+max_gain)