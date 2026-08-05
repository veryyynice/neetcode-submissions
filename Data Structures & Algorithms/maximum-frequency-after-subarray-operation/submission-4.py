class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #find subarray  (non empty) dand add x to those elements
        #find maximum  frequncy of value k after adding magic x value 

        #find duplicates or frequncy map
        #find most frequnt duplicate other than k
        
        #example: k is 10.     2,2,10,2,2

        #return frequency
        max_freq = 0
        frequency = defaultdict(int)
        for num in nums:
            frequency[num]=max(frequency.get(num,0),frequency.get(k,0))+1
            max_freq = max(frequency[num]-frequency[k],max_freq)

        return frequency.get(k,0)+max_freq