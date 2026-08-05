class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # result = 0
        # index = 0
        # for i range (len(digits)-1,-1,-1):
        #     result+= 10**i*digits[index]
        #     index+=1
        # result+=1
        index = len(digits)-1
        if digits[-1] == 9:
            while digits[index] ==9 and index >-1:
                digits[index]= 0
                index-=1
            if digits[index] ==0:
                digits.insert(0,1)
            else: digits[index]+=1
            return (digits)
        else:
            digits[-1]+=1
            return (digits)
