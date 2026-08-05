class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #permutation is differnet order but in a row
        #same length
        #return true or false
        #sliding window
        #start window if we have match
        #if no match shrnk it back
        #how we check if char in 

        alphabet1=[0]*26
        alphabet2=[0]*26
        frequency_matches = 0
        if len(s1)>len(s2):
            return False

        len_of_window = len(s1)

        for i in range(len(s1)):
            alphabet1[ord(s1[i])-ord('a')]+=1
            alphabet2[ord(s2[i])-ord('a')]+=1
        
        for i in range(26):
            frequency_matches += (1 if alphabet1[i]==alphabet2[i] else 0)

        l = 0
        for r in range(len(s1),len(s2)):
            if frequency_matches == 26: #all 26 frequencies the same
                return True

            index = ord(s2[r])-ord('a')

            #shift left and right pointers to the right
            
            alphabet2[index] +=1
            if alphabet1[index]== alphabet2[index]:
                frequency_matches +=1
            elif alphabet1[index]+1== alphabet2[index]:
                frequency_matches -=1

            index = ord(s2[l])-ord('a')

            #shift left and right pointers to the right
            
            alphabet2[index] -=1
            if alphabet1[index]== alphabet2[index]:
                frequency_matches +=1
            elif alphabet1[index]-1== alphabet2[index]:
                frequency_matches -=1
            l+=1

        if frequency_matches == 26:
            return True

        return False
        
