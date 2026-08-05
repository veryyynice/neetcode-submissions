class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #dvdf
        res = 0
        curr = set()
        curr_start = 0
        for char in range(len(s)):
            curr.add(s[char])
            curr_start = char+1
            while curr_start < len(s) and[curr_start] != s[char] and s[curr_start] not in curr:
                curr.add(s[curr_start])
                curr_start+=1
            # if s[char] in curr:
            #     curr = set()
            #curr.add(s[char])
            print(curr)
            res = max(res,len(curr))
            curr =set()
        return res