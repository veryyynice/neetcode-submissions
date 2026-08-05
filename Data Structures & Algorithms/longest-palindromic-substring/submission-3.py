class Solution:
    def longestPalindrome(self, s: str) -> str:
        #aabccbaa
        max_length = 1
        res = s[0]
        res_start_index = 0
        n = len(s)

        if n>1 and s[0]==s[1]:
            if 2> max_length:
                max_length = 2

        for i in range (len(s)):
            curr = s[i]

            if i != 0:
                l,r = i-1,i+1
                while l>=0 and r <= len(s)-1:
                    left_val = s[l]
                    right_val = s[r]
                    # print("big"+s[i])
                    # print("lr:"+left_val+","+right_val)
                    # print(max_length)
                    # print((r-l+1)>max_length)
                    if left_val == right_val and (r-l+1)>max_length:
                        max_length =(r-l+1)
                        res_start_index = l
                    if left_val != right_val:
                        break
                    l-=1
                    r+=1
        
            l,r = i,i+1
            while l >=0 and r <= len(s)-1:
                left_val = s[l]
                right_val = s[r]
                if left_val == right_val and (r-l+1)>max_length:
                    max_length =(r-l+1)
                    res_start_index = l

                if left_val != right_val:
                    break
                l-=1
                r+=1
        if max_length ==1:
            return res
        return s[res_start_index:res_start_index+max_length]