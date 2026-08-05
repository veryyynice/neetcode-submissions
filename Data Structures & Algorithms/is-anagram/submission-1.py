class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        freq_s, freq_t = {},{}
        for letter in s:
            if letter not in freq_s:
                freq_s[letter]=1
            else:
                freq_s[letter]+=1
        for letter in t:
            if letter not in freq_t:
                freq_t[letter]=1
            else:
                freq_t[letter]+=1
        for letter in freq_s.keys():
            if letter in freq_s and letter in freq_t:

                if freq_s[letter]!=freq_t[letter]:
                    return False
            else: return False
        return True
